from ..utils.color_analysis import HTML_CONTENT, extract_and_clean_colors
from collections import Counter
from statistics import variance
from ..model.color_analysis import Color
from fastapi import HTTPException, status
from ..schema.color_analysis import ColorRes, ColorFreq
from sqlmodel import select

async def analyse_store_color(session):
    try:
        ALL_STAFF_COLORS = await extract_and_clean_colors(HTML_CONTENT)
        COLOR_FREQUENCY = Counter(ALL_STAFF_COLORS)
        TOTAL_COLORS = len(ALL_STAFF_COLORS)
        if TOTAL_COLORS == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No color data was extracted from the source content or source content is empty."
            )
        UNIQUE_COLORS = sorted(COLOR_FREQUENCY.keys())
        COUNTS_ONLY = [COLOR_FREQUENCY[color] for color in UNIQUE_COLORS]

        #Question1: Which color of shirt is the mean color?
        #1. Count how many unique colors there are
        num_colors = len(UNIQUE_COLORS)
        if num_colors == 0:
            # Should not happen if TOTAL_COLORS > 0, but is a safe guard
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No unique colors found after counting."
            )

        #2. calculate the overall mean frequency
        mean_frequency = TOTAL_COLORS/num_colors

        #3. Find the minimum difference from the mean
        min_diff = min(abs(count - mean_frequency) for count in COUNTS_ONLY)

        #4. Get all colors with that minimum difference
        mean_colors = [color for color, count in COLOR_FREQUENCY.items() if abs(count - mean_frequency) == min_diff]

        #Question 2: Which color is mostly worn throughout the week?
        #1. find the mode of the colour frequency
        mode_color = COLOR_FREQUENCY.most_common(1)[0][0]

        #Question 3: Which color is the median?
        #sorting the list alphabetically to get a deterministic median position
        sorted_all_colors = sorted(ALL_STAFF_COLORS)
        #List Index start from zero, minus 1 to get actual index
        median_index = (TOTAL_COLORS - 1) // 2
        #select the median color using the index
        median_color = sorted_all_colors[median_index]

        #Question 4: BONUS Get the variance of the colors
        if len(COUNTS_ONLY) >= 2:
            freq_variance = variance(COUNTS_ONLY)
        else:
            freq_variance = 0.0 # Cannot calculate variance with less than 2 points

        #Question 5: BONUS if a colour is chosen at random, what is the probability that the color is red?
        red_count = COLOR_FREQUENCY.get('RED', 0)
        probability_red = red_count / TOTAL_COLORS if TOTAL_COLORS > 0 else 0.0

        #Question 6: Save the colours and their frequencies in postgresql database
        #check if this code have been run before
        all_result = await session.execute(select(Color))
        colors = all_result.scalars().first()
        if not colors:
            color_entries = []
            for color_name, freq_count in zip(UNIQUE_COLORS, COUNTS_ONLY):
            # Create one Color object for each pair
                entry = Color(color=color_name, frequency=freq_count)
                color_entries.append(entry)
            if not color_entries:
                raise(HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail = "no color and frequncies exist")
                )
            session.add_all(color_entries)
            await session.commit()

        result = await session.execute(select(Color))
        saved_colors = result.scalars().all()

        saved_freqs_pydantic = [
            entry.model_dump(exclude={'id'}) 
            for entry in saved_colors
        ]

        new_response = {
            "Which_color_of_shirt_is_the_mean_color":  mean_colors,
            "Which_color_is_mostly_worn_throughout_the_week": mode_color,
            "Which_color_is_the_median":  median_color,
            "Get_the_variance_of_the_colors": freq_variance,
            "what_is_the_probability_that_the_color_is_red": probability_red,
            "Saved_colours_and_their_frequencies": saved_freqs_pydantic
        }

        return new_response
    except HTTPException as Httpexc:
        await session.rollback()
        raise Httpexc
    except Exception as e:
        await session.rollback()
        raise(HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = str(e)
        ))
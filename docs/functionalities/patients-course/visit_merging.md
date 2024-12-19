## Merging visits into stays

!!! warning
     This feature is under review and should be used with caution.

### Presentation of the problem

In order to have a precise view of each patient's course of care, it can be useful to **merge together visit occurrences into stays.**

A crude way of doing so is by using the `preceding_visit_occurrence_id` column in the `visit_occurrence` table. However, this column isn't always filled, and a lot of visits would be missed by using only this method.

The method proposed here relies on **how close two visits are** in order to put them in the same stay. This is the role of the [`merge_visits()`][eds_scikit.period.stays.merge_visits] functions.

The figure below shows how the merging of visits into stays would occurs

<figure markdown>
  [![Image title](visit_merging.png)](#)
  <figcaption></figcaption>
</figure>

### The `merge_visits()` function

{{ load_data }}

```python
from eds_scikit.period.stays import merge_visits

visit_occurrence = merge_visits(visit_occurrence)
```

!!! warning
     The snippet above should run *as is*, however the `merge_visits()` function provides a lot of parameters that you **should** check in order to use it properly. Those parameters are described below or in [the corresponding code reference][eds_scikit.period.stays.merge_visits]

::: eds_scikit.period.stays.merge_visits
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true

## Computing stay duration

### Presentation of the problem

Once that visits are grouped into stays, you might want to compute stays duration.

### The `get_stays_duration()` function

```python
from eds_scikit.period.stays import get_stays_duration
```

This function should be used once you called the `merge_visits()` functions. It adds a `STAY_DURATION` column.

```python
vo = get_stays_duration(
    vo,
    algo="visits_date_difference",
    missing_end_date_handling="fill",
)
```

There are actually two ways to compute those stays durations. Pick the `"algo"` value that suits your needs.

!!! algos "Availables algorithms (values for `"algo"`)"

	=== "'visits_date_difference'"

        The stay duration corresponds to the difference between the **end datetime of the stay's last visit** and **the start datetime of the stay's first visit**.
    === "'sum_of_visits_duration'"

        The stay duration corresponds to the sum of the duration of all visits of the stay (and by handling overlapping)

Please check [the documentation][eds_scikit.period.stays.get_stays_duration] for additional parameters.

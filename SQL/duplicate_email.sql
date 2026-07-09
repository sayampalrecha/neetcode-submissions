-- using subarray

select email from (
    select email, count(email) as num
    from person
    group by email
) as statistic
where num>1;
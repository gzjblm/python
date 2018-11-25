declare @date_ DATE
begin
select    @date_ = getdate();
PRINT @date_
end;


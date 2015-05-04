use ResearchDocument
use CapitalIQ
use DocumentRepository
Declare @n INT = 6


--- part1. Contributors whose's documents got downloaded/viewed mostly in the last 6 months, get "these documents' contributors"
--- part2. Contributors total contributions in the last 6 months.

select contributors.researchContributorId, count(*) as totalDocs
from 
(select distinct rdt.researchContributorId
          from 
             (select top 10000 t.researchDocumentId,
                  (select count(r.researchActivityTypeId) 
                        from CapitalIQ.dbo.ResearchActivity_tbl r 
                        where r.researchActivityTypeId not in (2, 3) and r.researchDocumentId=t.researchDocumentId) download,
                  (select count(rr.researchActivityTypeId) 
                        from CapitalIQ.dbo.ResearchActivity_tbl rr 
                        where rr.researchActivityTypeId in (2, 3) and rr.researchDocumentId=t.researchDocumentId) viewd
              from CapitalIQ.dbo.ResearchActivity_tbl t
              where t.activityDateTime >= DATEADD(month, -6, GETDATE())
              group by t.researchDocumentId
              order by download DESC) recent
          join ResearchDocument.dbo.ResearchDocument_tbl rdt
          on recent.researchDocumentId = rdt.researchDocumentId ) as contributors
join ResearchDocument.dbo.ResearchDocument_tbl docs
on contributors.researchContributorId = docs.researchContributorId
group by contributors.researchContributorId


select comp.companyName
from ResearchDocument.dbo.ResearchContributor_tbl rct
join CapitalIQ.dbo.Company_tbl comp
on rct.companyId = comp.companyId
where rct.researchContributorId in (182, 650, 90, 2866)
              
              
  
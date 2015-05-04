use ResearchDocument
use CapitalIQ
use DocumentRepository
Declare @n INT = 6


select 
research_tbl.ResearchDocumentId,
research_tbl.DocumentHeadline,
research_tbl.GeographyName,
research_tbl.IndustryTypeName,
research_tbl.LanguageId, 
research_tbl.primaryCompanyName,
comp1.companyName as ContributorName,
category.researchCategoryName,
research_tbl.Downloads,
research_tbl.UserViews
from 
  (select 
     rdt.researchDocumentId as ResearchDocumentId,
     rdt.headline as DocumentHeadline,
     rdt.geoSubTypeValue as GeographyName,
     rdt.industrySubTypeValue IndustryTypeName,
     rdt.languageId as LanguageId,
     rdt.primaryCompanyId PrimaryCompanyId,
     comp.companyName as primaryCompanyName,
     rdt.researchContributorId as ContributorId,
     recent.download as Downloads,
     recent.viewd as UserViews
          from 
             (select top 100000 t.researchDocumentId,
                  (select count(r.researchActivityTypeId) 
                        from CapitalIQ.dbo.ResearchActivity_tbl r 
                        where r.researchActivityTypeId not in (2, 3) and r.researchDocumentId=t.researchDocumentId) download,
                  (select count(rr.researchActivityTypeId) 
                        from CapitalIQ.dbo.ResearchActivity_tbl rr 
                        where rr.researchActivityTypeId in (2, 3) and rr.researchDocumentId=t.researchDocumentId) viewd
              from CapitalIQ.dbo.ResearchActivity_tbl t
              where t.activityDateTime >= DATEADD(month, -@n, GETDATE())
              group by t.researchDocumentId
              order by download DESC) recent
         join ResearchDocument.dbo.ResearchDocument_tbl rdt
         on recent.researchDocumentId = rdt.researchDocumentId
         join CapitalIQ.dbo.Company_tbl comp
         on comp.companyId = rdt.primaryCompanyId) research_tbl
   join ResearchDocument.dbo.ResearchContributor_tbl rct 
   on research_tbl.ContributorId = rct.researchContributorId
   join CapitalIQ.dbo.Company_tbl comp1 
   on comp1.companyId = rct.companyId
   join 
   (select rtac.researchContributorId, rtac.researchCategoryId,rtac.researchCategoryName
     from CapitalIQ.dbo.ResearchTearsheet_AnalystsCategories_tbl rtac 
     group by rtac.researchContributorId, rtac.researchCategoryId,rtac.researchCategoryName) category
   on category.researchContributorId = research_tbl.ContributorId
   order by research_tbl.ResearchDocumentId
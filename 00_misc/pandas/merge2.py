import pandas as pd

# while reading larger csv files with size greater than 3GB, add usecols - to read only the required column to read and always use dtype=str to treat all the value of the df as strings


# columns_to_read = ["CompanyName"," CompanyNumber","CompanyCategory","CompanyStatus","CountryOfOrigin","DissolutionDate","IncorporationDate","SICCode.SicText_1","SICCode.SicText_2","SICCode.SicText_3","SICCode.SicText_4"]
# company_house_df = pd.read_csv("E:\\large_datasets\\BasicCompanyData.csv", usecols=columns_to_read)
# print(company_house_df.head())

columns_to_read = ["LEI","Entity.LegalName","Entity.RegistrationAuthority.RegistrationAuthorityID","Entity.RegistrationAuthority.OtherRegistrationAuthorityID","Entity.RegistrationAuthority.RegistrationAuthorityEntityID","Entity.LegalJurisdiction","Entity.EntityCategory","Entity.EntitySubCategory","Entity.LegalForm.EntityLegalFormCode","Entity.LegalForm.OtherLegalForm","Entity.AssociatedEntity.type","Entity.AssociatedEntity.AssociatedLEI","Entity.AssociatedEntity.AssociatedEntityName","Entity.EntityStatus","Entity.EntityCreationDate","Entity.EntityExpirationDate","Entity.EntityExpirationReason","Entity.SuccessorEntity.1.SuccessorLEI","Entity.SuccessorEntity.1.SuccessorEntityName","Entity.SuccessorEntity.1.SuccessorEntity.xmllang","Entity.SuccessorEntity.2.SuccessorLEI","Entity.SuccessorEntity.2.SuccessorEntityName","Entity.SuccessorEntity.2.SuccessorEntity.xmllang","Entity.SuccessorEntity.3.SuccessorLEI","Entity.SuccessorEntity.3.SuccessorEntityName","Entity.SuccessorEntity.3.SuccessorEntity.xmllang","Entity.SuccessorEntity.4.SuccessorLEI","Entity.SuccessorEntity.4.SuccessorEntityName","Entity.SuccessorEntity.4.SuccessorEntity.xmllang","Entity.SuccessorEntity.5.SuccessorLEI","Entity.SuccessorEntity.5.SuccessorEntityName","Entity.SuccessorEntity.5.SuccessorEntity.xmllang","Registration.InitialRegistrationDate","Registration.LastUpdateDate","Registration.RegistrationStatus","Registration.NextRenewalDate","Registration.ManagingLOU","Registration.ValidationSources","Registration.ValidationAuthority.ValidationAuthorityID","Registration.ValidationAuthority.OtherValidationAuthorityID","Registration.ValidationAuthority.ValidationAuthorityEntityID"]
gleif_df = pd.read_csv("E:\\large_datasets\\gleif-goldencopy.csv", usecols=columns_to_read, dtype=str)

print(gleif_df.head())
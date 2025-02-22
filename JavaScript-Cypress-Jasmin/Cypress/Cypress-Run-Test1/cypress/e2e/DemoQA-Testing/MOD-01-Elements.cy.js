/// <reference types = "cypress" />

import 'cypress-xpath';


describe("TS-001-Text Box", () => {

    beforeEach(() => {
        cy.visit("https://demoqa.com/")
        cy.intercept('GET', '*adtrafficquality*', { statusCode: 403 }).as('blockAds');
        cy.xpath("//h5[contains(text(),'Elements')]").click()
        cy.intercept('GET', '*adtrafficquality*', { statusCode: 403 }).as('blockAds');

    })

    it("TC001_01-Validate text input submission", () => {
        cy.intercept('GET', '*adtrafficquality*', { statusCode: 403 }).as('blockAds');
        cy.url().should("include", "/elements")
        cy.xpath("//span[contains(text(),'Text Box')]").click()
        cy.get("#userName").type("Haryish")
        cy.get("#userEmail").type("haryishkumaran16@gmail.com")
        cy.get("#currentAddress").type("23,XYZ,\n sdsd street \n City-YYUJSD")
        cy.xpath("//textarea[@id='permanentAddress']").type("23,XYZ,\n sdsd street \n City-YYUJSD")
        cy.xpath("//button[@id='submit']").click()
        
        // multiple web elemnt handling in cyoress
        cy.xpath("//div[@id='output']//p").each(($el, index) => {
            if (index === 0) {
              expect($el.text()).to.include("Haryish");
            } else if (index === 1) {
              expect($el.text()).to.include("@gmail.com");
            }
          });

        

    })

})
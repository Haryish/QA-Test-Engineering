/// <reference types = "cypress" />
import 'cypress-xpath';

describe("TS-001-Text Box", () => {
  
  beforeEach(() => {
    cy.visit("https://demoqa.com/");
    cy.intercept('GET', '*adtrafficquality*', { statusCode: 403 }).as('blockAds');

    cy.xpath("//h5[contains(text(),'Elements')]")
      .should("be.visible")
      .click();
    cy.xpath("//span[contains(text(),'Text Box')]").click();
    cy.url().should("include", "/text-box");

  });

  it("TC001_01 - Validate text input submission", () => {
    // cy.url().should("include", "/elements");
    cy.fixture('testdata-TS01').then((data) => {
      data.positiveCases.forEach((user) => {
        cy.get("#userName").clear().type(user.fullName);
        cy.get("#userEmail").clear().type(user.email);
        cy.get("#currentAddress").clear().type(user.currentAddress);
        cy.get("#permanentAddress").clear().type(user.permanentAddress);

        cy.xpath("//button[@id='submit']").click();
        
        cy.xpath("//div[@id='output']//p").should('exist').each(($el, index) => {
          if (index === 0) {
            expect($el.text()).to.include(user.fullName);
          } else if (index === 1) {
            expect($el.text()).to.include(user.email);
          } else if (index === 2) {
            expect($el.text()).to.include(user.currentAddress);
          } else if (index === 3) {
            expect($el.text()).to.include(user.permanentAddress);
          } 
        });
      });
    });
  });

  it("TC001_02 - Verify error message for invalid email", () => {
    // cy.url().should("include", "/elements");
    cy.fixture('testdata-TS01').then((data) => {
      data.negativeCases.forEach((user) => {
        cy.get("#userName").clear().type(user.fullName || " ");
        cy.get("#userEmail").clear().type(user.email || " ");
        cy.get("#currentAddress").clear().type(user.currentAddress || " ");
        cy.get("#permanentAddress").clear().type(user.permanentAddress || " ");
        
        cy.xpath("//button[@id='submit']").click();
        
        // ✅ Form should NOT submit, so `#output` should NOT exist
        cy.xpath("//div[@id='output']//p").should("not.exist");

        // // ✅ Optional: Check for expected error messages (if applicable)
        // cy.get("#userEmail").then(($el) => {
        //   const borderColor = $el.css("border-color");
        //   expect(borderColor).to.equal("rgb(255, 0, 0)"); // Red border for invalid email
        // });     
      });
    });
  });

  it("TC001_03 - Validate text input submission at edge level", () => {
    // cy.url().should("include", "/elements");
    cy.fixture('testdata-TS01').then((data) => {
      data.edgeCases.forEach((user) => {
        cy.get("#userName").type(user.fullName);
        cy.get("#userEmail").type(user.email);
        cy.get("#currentAddress").type(user.currentAddress);
        cy.get("#permanentAddress").type(user.permanentAddress);

        cy.xpath("//button[@id='submit']").click();
        
        cy.xpath("//div[@id='output']//p").should('exist').each(($el, index) => {
          if (index === 0) {
            expect($el.text()).to.include(user.fullName);
          } else if (index === 1) {
            expect($el.text()).to.include(user.email);
          } else if (index === 2) {
            expect($el.text()).to.include(user.currentAddress);
          } else if (index === 3) {
            expect($el.text()).to.include(user.permanentAddress);
          } 
        });
      });
    });
  });

});

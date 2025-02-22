/// <reference types = "cypress" />

describe('TS001 - Page Load Validation', () => {
  it('TS-001_TC-001 Verify the webpage loads successfully', () => {
      // Visit the URL
      cy.visit('https://rahulshettyacademy.com/AutomationPractice/');  

      // Verify the URL
      cy.url().should('eq', 'https://rahulshettyacademy.com/AutomationPractice/');  

      // Verify the page title
      cy.title().should('include', 'Practice Page');  

      // Verify visible elements (e.g., header, footer, main content)
      cy.get('header').should('be.visible');
      cy.get('body').should('be.visible');
      cy.get('footer').should('be.visible');
  });
});



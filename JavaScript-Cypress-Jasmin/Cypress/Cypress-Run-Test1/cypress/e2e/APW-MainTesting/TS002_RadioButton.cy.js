/// <reference types = "cypress" />

describe('TS-002 Radio Buttons', () => {
    it('TS-002_TC-001: Verify radio buttons are selectable', () =>{
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/'); 
        cy.get('[for="radio2"] > .radioButton').click()
        cy.get('[for="radio2"] > .radioButton').should('be.checked')
    });
    it('TS_002_TC-002: Verify only one radio button can be selected at a time', ()=> {
        cy.visit('https://rahulshettyacademy.com/AutomationPractice/'); 
        cy.get('[for="radio2"] > .radioButton').click()
        cy.get('[for="radio2"] > .radioButton').should('be.checked')
// input.radioButton 
    });
});
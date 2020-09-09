var tabButtons = document.querySelectorAll(
  ".tabContainer .buttonContainer button"
);
var tabPanels = document.querySelectorAll(".tabContainer  .tabPanel");

function showPanel(panelIndex, colorCode, bgCode) {
  tabButtons.forEach(function (node) {
    node.style.backgroundColor = "";
    node.style.color = "";
  });
  tabButtons[panelIndex].style.backgroundColor = colorCode;
  tabButtons[panelIndex].style.color = "white";
  tabPanels.forEach(function (node) {
    node.style.display = "none";
  });
  tabPanels[panelIndex].style.display = "block";
  tabPanels[panelIndex].style.backgroundColor = bgCode;
  tabPanels[panelIndex].style.backgroundOpacity = "0.9";
}
showPanel(0, "#f44336", "#f3a683");

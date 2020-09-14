var sideTabButtons = document.querySelectorAll(
  ".tabSideContainer .chart-btn .sideButtonContainer button"
);
var sideTabPanels = document.querySelectorAll(".tabSideContainer  .chartArea");

function showSidePanel(panelIndex) {
  // sideTabButtons.forEach(function (node) {
  //   node.style.backgroundColor = "";
  //   node.style.color = "";
  // });

  // sideTabButtons[panelIndex].style.backgroundColor = colorCode;
  // sideTabButtons[panelIndex].style.color = "white";
  sideTabPanels.forEach(function (node) {
    node.style.display = "none";
  });
  sideTabPanels[panelIndex].style.display = "block";
  // sideTabPanels[panelIndex].style.backgroundColor = colorCode;
}
showSidePanel(0);

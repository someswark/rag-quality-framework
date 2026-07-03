/*
====================================================
Dashboard Data Loader
====================================================
*/

console.log("dashboard.js loaded");

document.addEventListener("DOMContentLoaded", loadDashboard);




async function loadDashboard() {

    try {
		
        const response = await fetch(`assets/data/summary.json?t=${new Date().getTime()}`);

        const data = await response.json();

        console.log("JSON Loaded Successfully");

        console.log(data);
		console.log("Data Loaded Successfully");

        populateDashboard(data);

    }
    catch(error){

        console.error(error);

    }

}


function populateDashboard(data) {

    // Evaluation Context
	
	
    console.log("populateDashboard called");

    console.log(data.overall_quality.score);

    document.getElementById("application-type").textContent =
        data.application.type;

    document.getElementById("knowledge-source").textContent =
        data.application.knowledge_source;

    document.getElementById("framework-version").textContent =
        data.framework.version;

    document.getElementById("evaluation-date").textContent =
        data.framework.evaluation_date;

    document.getElementById("model-provider").textContent =
        data.application.model_provider;

    // Overall Score

    document.getElementById("quality-score").textContent =
        data.overall_quality.score + "%";

    document.getElementById("quality-rating").textContent =
        data.overall_quality.rating;

    // PASS REVIEW FAIL

    document.getElementById("pass-count").textContent =
        data.overall_quality.pass;

    document.getElementById("review-count").textContent =
        data.overall_quality.review;

    document.getElementById("fail-count").textContent =
        data.overall_quality.fail;

}
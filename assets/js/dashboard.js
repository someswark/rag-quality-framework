/*
====================================================
Dashboard Data Loader
====================================================
*/

console.log("dashboard.js loaded");

document.addEventListener("DOMContentLoaded", loadDashboard);




async function loadDashboard() {

    try {
		
        const response = await fetch(`assets/data/summary.json`);

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
		
		
		setMetric(
    "accuracy",
    data.metrics.accuracy
);

setMetric(
    "grounding",
    data.metrics.grounding
);

setMetric(
    "completeness",
    data.metrics.completeness
);

setMetric(
    "safety",
    data.metrics.safety
);

setMetric(
    "hallucination",
    data.metrics.hallucination
);

// Latest Evaluation

document.getElementById("latest-question").textContent =
    data.latest_evaluation.question;

document.getElementById("latest-status").textContent =
    data.latest_evaluation.status;

document.getElementById("latest-confidence").textContent =
    data.latest_evaluation.confidence + "%";
	
	
	
	
setText("quality-score", data.overall_quality.score + "%");
setText("latest-question", data.latest_evaluation.question);
setText("latest-confidence", data.latest_evaluation.confidence + "%");

}

function setMetric(name, value){

    document.getElementById(
        name + "-score"
    ).textContent = value + "%";

    document.getElementById(
        name + "-bar"
    ).style.width = value + "%";

}

function setText(id, value){

    const element = document.getElementById(id);

    if(element){

        element.textContent = value ?? "N/A";

    }

}

function setWidth(id, value){

    const element = document.getElementById(id);

    if(element){

        element.style.width = value + "%";

    }

}
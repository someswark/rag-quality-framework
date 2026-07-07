console.log("Dashboard Loaded");

async function loadSummary() {

    const response = await fetch(
        "assets/data/summary.json?t=" + new Date().getTime()
    );

    if (!response.ok) {
        throw new Error("Unable to load summary.json");
    }

    return await response.json();
}

async function loadEvaluationResults() {

    const response = await fetch(
        "assets/data/evaluation_results.json?t=" + new Date().getTime()
    );

    if (!response.ok) {
        throw new Error("Unable to load evaluation_results.json");
    }

    return await response.json();
}

function updateSummary(data) {

    const evaluation = data.evaluation;

    document.getElementById("overallScore").innerText =
        evaluation.overall_score + "%";

    document.getElementById("totalQuestions").innerText =
        evaluation.total_questions;

    document.getElementById("passCount").innerText =
        evaluation.pass_count;

    document.getElementById("reviewCount").innerText =
        evaluation.review_count;

    document.getElementById("failCount").innerText =
        evaluation.fail_count;

    document.getElementById("confidence").innerText =
        evaluation.average_confidence + "%";

    document.getElementById("latency").innerText =
        evaluation.average_latency + " ms";
}

function updateEvaluationResults(results) {
	
	evaluationResults = results;

    const tbody = document.getElementById("resultsBody");

    tbody.innerHTML = "";

    results.forEach((result, index) => {

        const row = document.createElement("tr");

row.innerHTML = `
			<td>${index + 1}</td>
			<td>${result.category}</td>
			<td>${result.question}</td>
			<td class="${result.status.toLowerCase()}">${result.status}</td>
			<td>${result.confidence}%</td>
			<td>${result.latency_ms} ms</td>

			<td>
				<button onclick="viewQuestion(${index})">
					View
				</button>
			</td>
`;	

        tbody.appendChild(row);

    });

}

document.addEventListener("DOMContentLoaded", async () => {

    try {

        const summary = await loadSummary();

        updateSummary(summary);

        const results = await loadEvaluationResults();

        updateEvaluationResults(results);

        console.log("Dashboard Updated Successfully");

    }
    catch (error) {

        console.error(error);

    }

});

let evaluationResults = [];

function viewQuestion(index){

    const result = evaluationResults[index];

    document.getElementById("mCategory").textContent =
        result.category;

    document.getElementById("mQuestion").textContent =
        result.question;

    document.getElementById("mExpected").textContent =
        result.expected_answer;

    document.getElementById("mGenerated").textContent =
        result.generated_answer;

    document.getElementById("mStatus").textContent =
        result.status;

    document.getElementById("mConfidence").textContent =
        result.confidence + "%";

    document.getElementById("mLatency").textContent =
        result.latency_ms + " ms";

    document.getElementById("questionModal").style.display = "block";

}

function closeModal(){

    document.getElementById("questionModal").style.display = "none";

}
async function getStrategy() {
    let inputData = document.getElementById("lap_data").value.trim();

    if (!inputData) {
        document.getElementById("result").innerText = "Please enter lap data.";
        return;
    }

    try {
        let response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ input_text: inputData })
        });

        if (!response.ok) throw new Error("Server error: " + response.status);

        let data = await response.json();

        // Use strategy suggestions
        let strategySuggestions = {
            "Pit Now": "Consider changing tires & refueling.",
            "Hold Position": "Maintain pace, avoid unnecessary pit stops."
        };

        document.getElementById("result").innerHTML = `
            Recommended Strategy: ${data.strategy} <br>
            <span style="color: gray;">${strategySuggestions[data.strategy]}</span>
        `;
    } catch (error) {
        document.getElementById("result").innerText = "Error: " + error.message;
    }
}

// Function to auto-fill example lap data
function fillExample() {
    document.getElementById("lap_data").value = "Lap Delta: 600, Lap Number: 20, Position: 4, Tire Condition: Worn, Weather: Dry";
}

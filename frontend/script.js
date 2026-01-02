document.getElementById("predictBtn").addEventListener("click", predict);

const API_BASE = "https://student-pass-backend.onrender.com"; 

function predict() {
    const model = document.getElementById("model").value;

    const data = {
        school: document.getElementById("school").value,
        sex: document.getElementById("sex").value,
        age: Number(document.getElementById("age").value),
        address: "U",
        famsize: "GT3",
        Pstatus: "A",
        Medu: 4,
        Fedu: 4,
        Mjob: "teacher",
        Fjob: "services",
        reason: "course",
        guardian: "mother",
        traveltime: 2,
        studytime: Number(document.getElementById("studytime").value),
        failures: Number(document.getElementById("failures").value),
        schoolsup: "no",
        famsup: "yes",
        paid: "no",
        activities: "yes",
        nursery: "yes",
        higher: "yes",
        internet: "yes",
        romantic: "no",
        famrel: 4,
        freetime: 3,
        goout: 3,
        Dalc: 1,
        Walc: 2,
        health: 5,
        absences: Number(document.getElementById("absences").value),
        G1: Number(document.getElementById("G1").value),
        G2: Number(document.getElementById("G2").value)
    };

    fetch(`${API_BASE}/predict/${model}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("result").innerText =
            `Model: ${result.model} → Prediction: ${result.prediction}`;
    })
    .catch(() => {
        document.getElementById("result").innerText =
            "❌ Unable to connect to backend";
    });
}

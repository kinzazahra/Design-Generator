function generate() {
    const area = document.getElementById("area").value;
    const bhk = document.getElementById("bhk").value;
    const floors = document.getElementById("floors").value;
    const style = document.getElementById("style").value;

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ area, bhk, floors, style })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data); // debug

        if (data.result) {
            document.getElementById("output").innerHTML = marked.parse(data.result);
        } else {
            document.getElementById("output").innerText =
                data.error || "No response from server";
        }
    })
    .catch(err => {
        console.error("Fetch error:", err);
    });
}

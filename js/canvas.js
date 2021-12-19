function scatterPlot(canvas, xArray, yArray, color="blue") {
    const ctx = canvas.getContext("2d");
    canvas.height = canvas.width;
    ctx.transform(1, 0, 0, -1, 0, canvas.height);
    ctx.fillStyle = color;
    for (let i = 0; i < xArray.length - 1; i++) {
        let x, y = xArray[i] * 400 / 150, yArray[i] * 400 / 15;
        ctx.beginPath();
        ctx.ellipse(x, y, 3, 3, 0, 0, Math.PI * 2);
        ctx.fill();
    }
}

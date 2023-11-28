function preprocessCsvData(data) {
  data.forEach((row) => {
    // // Replace all '年' with ''
    // if (row["學年度別"]) {
    //   row["學年度別"] = row["學年度別"].replace(/年/g, "");
    // }

    // Replace all '-' with 0
    for (const key in row) {
      if (Object.prototype.hasOwnProperty.call(row, key)) {
        row[key] = row[key].replace(/-/g, "0");
      }
    }
  });

  return data;
}

function createLineChart(data) {
  const categories = [...new Set(data.map((row) => row["學制別"]))];

  // Create traces
  const traces = [];
  categories.forEach((category) => {
    const categoryData = data.filter((row) => row["學制別"] === category);
    const years = categoryData.map((row) => row["學年度別"]);
    const totals = categoryData.map((row) => parseInt(row["總計"]));

    const trace = {
      x: years,
      y: totals,
      type: "scatter",
      mode: "lines+markers+text",
      text: totals,
      testposition: "bottom center",

      name: `${category}`,
    };

    traces.push(trace);
  });

  const layout = {
    title: "各學年度畢業生人數統計",
    xaxis: {
      title: "學年度",
    },
    yaxis: {
      title: "畢業生人數",
    },
  };

  Plotly.newPlot("line-chart", traces, layout);
}

d3.csv("Graduate_Outcomes_of_Taipei_City_Secondary_Schools.csv")
  .then((data) => {
    data = preprocessCsvData(data);
    createLineChart(data);
  })
  .catch((error) => console.error("Error fetching or parsing CSV:", error));

// function drawLineChart(res) {
//   let myGraph = document.getElementById("myGraph");

//   let trace1 = {};
//   trace1.mode = "lines+markers";
//   trace1.type = "scatter";
//   trace1.name = "Revenue";
//   trace1.marker = {
//     size: 10,
//   };
//   trace1.x = [];
//   trace1.y = [];
//   trace1.text = [];
//   trace1.textposition = "bottom center";
//   trace1.textfont = {
//     family: "Raleway, sans-serif",
//     size: 15,
//     color: "blue",
//   };

//   for (let i = 0; i < res.length; i++) {
//     trace1.x[i] = res[i]["release_year"];
//     trace1.y[i] = res[i]["revenue"];
//     trace1.text[i] = res[i]["title"];
//   }

//   let trace2 = {};
//   trace2.mode = "lines+markers";
//   trace2.type = "scatter";
//   trace2.name = "Budget";
//   trace2.marker = {
//     size: 10,
//   };
//   trace2.x = [];
//   trace2.y = [];
//   trace2.text = [];
//   trace2.textposition = "bottom center";
//   trace2.textfont = {
//     family: "Raleway, sans-serif",
//     size: 15,
//     color: "blue",
//   };

//   for (let i = 0; i < res.length; i++) {
//     trace2.x[i] = res[i]["release_year"];
//     trace2.y[i] = res[i]["budget"];
//     trace2.text[i] = res[i]["title"];
//   }

//   let data = [];
//   data.push(trace1);
//   data.push(trace2);

//   let layout = {
//     margin: {
//       t: 80,
//     },
//     title: "Harry Potter 2001 ~ 2011",
//     // xaxis: {
//     //     range: [0, 6]
//     // },
//     // yaxis: {
//     //     range: [0, 25]
//     // }
//   };

//   Plotly.newPlot(myGraph, data, layout);
// }
// let myGraph = document.getElementById("myGraph");

// let trace1 = {};
// trace1.mode = "markers";
// trace1.type = "scatter";
// trace1.x = [];
// trace1.y = [];

// let trace2 = {};
// trace2.mode = "lines+markers";
// trace2.type = "scatter";
// trace2.x = [];
// trace2.y = [];

// for (let i = 0; i < set1.length; i++) {
//   trace1.x[i] = set1[i][0];
//   trace1.y[i] = set1[i][1];
// }

// for (let i = 0; i < set2.length; i++) {
//   trace2.x[i] = set2[i][0];
//   trace2.y[i] = set2[i][1];
// }

// let data = [];
// data.push(trace1);
// data.push(trace2);

// let layout = {};

// Plotly.newPlot(myGraph, data, layout);

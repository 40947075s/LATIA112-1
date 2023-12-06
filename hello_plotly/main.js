function preprocessCsvData(data) {
  data.forEach((row) => {
    // if (row["學年度別"]) {
    //   // Replace all '年' with ''
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
      textposition: "bottom center",

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

function createPieChart(data) {
  // setup years and type
  const years = [...new Set(data.map((row) => row["學年度別"]))];
  const types = ["高中", "高職"];

  // Create a subplot with a grid layout
  const layout = {
    title: "畢業生出路分佈圖",
    grid: {
      rows: types.length,
      columns: years.length,
    },
  };
  // Initialize an array to store traces
  const traces = [];

  types.forEach((type, row) => {
    years.forEach((year, col) => {
      // Filter data by year and type
      const yearData = data.filter(
        (row) => row["學年度別"] === year && row["學制別"] === type,
      );

      // Get values
      const categories = ["升學/合計", "就業/合計", "閒居", "其他"];
      const values = categories.map((category) => {
        return yearData[0][category];
      });
      console.log(values);

      // Create a trace for the current subplot
      const trace = {
        title: { text: `${year} ${type}`, font: { size: 14, weight: "bold" } },
        hole: 0.5,
        labels: categories,
        values: values,
        type: "pie",
        textinfo: "percent",
        textposition: "outside",
        outsidetextfont: { size: 12 },
        pull: 0.03,
        domain: { row: row, column: col },
        rotation: 0,
        hoverinfo: "label+percent+value",
      };

      // Add the trace to the array
      traces.push(trace);
    });
  });

  Plotly.newPlot("pie-chart", traces, layout);
}

function createBarChart1(data, year) {
  // Filter data by year and types
  const highSchoolData = data.filter(
    (row) => row["學年度別"] === year && row["學制別"] === "高中",
  );
  const vocationalData = data.filter(
    (row) => row["學年度別"] === year && row["學制別"] === "高職",
  );

  // Get values for each category
  const categories = [
    "升學/大學校院",
    "升學/專科學校",
    "升學/高中或高職",
    "升學/師專師院",
    "升學/軍警學校",
    "升學/其他",
  ];
  const highSchoolValues = categories.map((category) => {
    return parseInt(highSchoolData[0][category]);
  });
  const vocationalValues = categories.map((category) => {
    return parseInt(vocationalData[0][category]);
  });

  // Create traces for the bar chart
  const trace1 = {
    x: categories.map((category) => category.replace("升學/", "")),
    y: highSchoolValues,
    type: "bar",
    name: "高中",
    text: highSchoolValues.map(String),
    textposition: "outside",
    hoverinfo: "name",
    marker: {
      color: "rgba(55,128,191,0.7)",
    },
    width: 0.4,
  };

  const trace2 = {
    x: categories.map((category) => category.replace("升學/", "")),
    y: vocationalValues,
    type: "bar",
    name: "高職",
    text: vocationalValues.map(String),
    textposition: "outside",
    hoverinfo: "name",
    marker: {
      color: "rgba(219, 64, 82, 0.7)",
    },
    width: 0.4,
  };

  // Create a layout
  const layout = {
    title: `${year} 升學分佈`,
    xaxis: {
      title: "升學類別",
    },
    yaxis: {
      title: "人數",
    },
    barmode: "group",
    bargap: 0.2,
    height: 500,
  };

  // Plot the combined bar chart
  Plotly.newPlot("bar-chart-1", [trace1, trace2], layout);
}

function createBarChart2(data, year) {
  // Filter data by year and types
  const highSchoolData = data.filter(
    (row) => row["學年度別"] === year && row["學制別"] === "高中",
  );
  const vocationalData = data.filter(
    (row) => row["學年度別"] === year && row["學制別"] === "高職",
  );

  // Get values for each category
  const categories = [
    "就業/農林漁牧業",
    "就業/礦業及土石採取業",
    "就業/製造業營建工程業",
    "就業/用水電力燃氣供應及污染整治業",
    "就業/批發零售住宿及餐飲業",
    "就業/金融保險及不動產業",
    "就業/運輸倉儲資訊及通訊業",
    "就業/公共行政及國防",
    "就業/其他",
  ];

  const highSchoolValues = categories.map((category) => {
    return parseInt(highSchoolData[0][category]);
  });
  const vocationalValues = categories.map((category) => {
    return parseInt(vocationalData[0][category]);
  });

  // Create traces for the bar chart
  const trace1 = {
    x: categories.map((category) => category.replace("就業/", "")),
    y: highSchoolValues,
    type: "bar",
    name: "高中",
    text: highSchoolValues.map(String),
    textposition: "outside",
    hoverinfo: "name",
    marker: {
      color: "rgba(55,128,191,0.7)",
    },
    width: 0.4,
  };

  const trace2 = {
    x: categories.map((category) => category.replace("就業/", "")),
    y: vocationalValues,
    type: "bar",
    name: "高職",
    text: vocationalValues.map(String),
    textposition: "outside",
    hoverinfo: "name",
    marker: {
      color: "rgba(219, 64, 82, 0.7)",
    },
    width: 0.4,
  };

  // Create a layout
  const layout = {
    title: `${year} 就業分佈`,
    xaxis: {
      title: "就業類別",
    },
    yaxis: {
      title: "人數",
    },
    barmode: "group",
    bargap: 0.2,
    height: 600,
    margin: { b: 150 },
  };

  // Plot the combined bar chart
  Plotly.newPlot("bar-chart-2", [trace1, trace2], layout);
}

// 載入CSV數據
d3.csv("Graduate_Outcomes_of_Taipei_City_Secondary_Schools.csv")
  .then((data) => {
    data = preprocessCsvData(data);
    createLineChart(data);
    createPieChart(data);
    createBarChart1(data, "109年");
    createBarChart2(data, "109年");
  })
  .catch((error) => console.error("Error fetching or parsing CSV:", error));

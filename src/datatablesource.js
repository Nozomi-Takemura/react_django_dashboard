export const userColumnsPerProject = [
    { field: "id", headerName: "ID", width:20}, 
    { field: "model", headerName: "Model", width: 140}, 
    { field: "metric", headerName: "Metric", width:200},
    { field: "testid", headerName: "Test set Id", width:140},
    { field: "testresult", headerName: "Test result", width:140},
    { field: "preprocessing", headerName: "Preprocessing methods", width: 140},
    { field: "features", headerName: "Key features", width: 140},
    { field: "status", headerName: "Status", width: 140},
    // { field: "bestvalresult", headerName: "Best validation result", width:140},

]

export const userRowsPerProject = [
    { 
        id: 1,
        model: "Xgboost",
        metric: "MSE",
        testid: "xnejduejg",
        testresult:"0.0003",
        preprocessing: "outlier removal, wavelet, standardization",
        features: "O, NO, NO2",
        status: "Approved",
    },
    { 
        id: 2,
        model: "Ridge regression",
        metric: "MAE",
        testid: "xyyyyyy",
        testresult:"0.01",
        preprocessing: "normalization",
        features: "O, NO, NO2",
        status: "Pending",
    },
]

export const userColumns = [
    { field: "id", headerName: "ID", width:20},
    { field: "project", headerName: "Project", width:250},
    { field: "bestmodel", headerName: "Best Model", width: 140}, 
    // { field: "model", headerName: "Model", width: 140}, 
    { field: "metric", headerName: "Metric", width:200},
    { field: "kpi", headerName: "KPI", width:200},
    // { field: "testid", headerName: "Test set Id", width:140},
    // { field: "valid", headerName: "Validation set Id", width:140},
    { field: "besttestresult", headerName: "Best test result", width:140},
    { field: "datasize", headerName: "Data size", width: 140},
    // { field: "bestvalresult", headerName: "Best validation result", width:140},

]
// export const userColumns = [
//     { field: "id", headerName: "ID", width: 70 },
//     {
//         field: "user",
//         headerName: "User",
//         width: 230,
//         renderCell: (params) => {
//             return (
//                 <div className="cellWithImg">
//                     <img className="cellImg" src={params.row.img} alt="avatar" />
//                     {params.row.username}
//                 </div>
//             );
//         },
//     },
//     {
//         field: "email",
//         headerName: "Email",
//         width: 230,
//     },

//     {
//         field: "age",
//         headerName: "Age",
//         width: 100,
//     },
//     {
//         field: "status",
//         headerName: "Status",
//         width: 160,
//         renderCell: (params) => {
//             return (
//                 <div className={`cellWithStatus ${params.row.status}`}>
//                     {params.row.status}
//                 </div>
//             );
//         }, 
//     },
// ];

//temporary data
export const userRows = [
    {
        id: 1,
        project: "Boiler tuning prediction",
        // model: "Xgboost",
        bestmodel: "Xgboost",
        metric: "MSE",
        kpi: "Prediction accuracy",
//        testid: "xxsgdfsge123456",
        besttestresult: "0.0005",
        datasize: "999876654222",
    },
    {
        id: 2,
        project: "Awar Awar 1",
        bestmodel: "Xgboost",
        metric: "MAE",
        kpi: "Prediction accuracy",
        besttestresult: "0.0001",
        datasize: "1000000000",
    },
    {
        id: 3,
        project: "Awar Awar 2",
        bestmodel: "Ridge Reg.",
        metric: "E(y - yhat)/n(n-1)",
        kpi: "Prediction accuracy",
        besttestresult: "50.5",
        datasize: "50000",
    }

]

//temporary data
// export const    userRows = [
//     {
//         id: 1,
//         username: "Snow",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         status: "active",
//         email: "1snow@gmail.com",
//         age: 35,
//     },
//     {
//         id: 2,
//         username: "Jamie Lannister",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "2snow@gmail.com",
//         status: "passive",
//         age: 42,
//     },
//     {
//         id: 3,
//         username: "Lannister",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "3snow@gmail.com",
//         status: "pending",
//         age: 45,
//     },
//     {
//         id: 4,
//         username: "Stark",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "4snow@gmail.com",
//         status: "active",
//         age: 16,
//     },
//     {
//         id: 5,
//         username: "Targaryen",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "5snow@gmail.com",
//         status: "passive",
//         age: 22,
//     },
//     {
//         id: 6,
//         username: "Melisandre",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "6snow@gmail.com",
//         status: "active",
//         age: 15,
//     },
//     {
//         id: 7,
//         username: "Clifford",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "7snow@gmail.com",
//         status: "passive",
//         age: 44,
//     },
//     {
//         id: 8,
//         username: "Frances",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "8snow@gmail.com",
//         status: "active",
//         age: 36,
//     },
//     {
//         id: 9,
//         username: "Roxie",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "snow@gmail.com",
//         status: "pending",
//         age: 65,
//     },
//     {
//         id: 10,
//         username: "Roxie",
//         img: "https://images.pexels.com/photos/1820770/pexels-photo-1820770.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500",
//         email: "snow@gmail.com",
//         status: "active",
//         age: 65,
//     },
// ];

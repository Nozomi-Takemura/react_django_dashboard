import Home from "./pages/home/Home"
import Login from "./pages/login/Login"
import Single from "./pages/single/Single"
import New from "./pages/new/New"
import List from "./pages/list/List"
import "./style/dark.scss"
import {
  BrowserRouter as Router,
//  Switch,
  Routes,
  Route,
//  Link
} from "react-router-dom";
import { productInputs, userInputs, projectInputs, applicationAccounts } from "./formSource"
import { useContext } from "react"
import { DarkModeContext } from "./components/context/darkModeContext"

function App() {
  const {darkMode} = useContext(DarkModeContext)
  return (
    <div className= { darkMode ? "app dark" : "app"}>
      <Router>
        <Routes>
          <Route path="/">
            <Route index element={<Home/>} />
            <Route path="login" element={<Login/>} />
            <Route path="users">
              <Route index element={<List/>}/>
              <Route path=":userId" element={<Single/>}/>
              <Route path="new" element={<New inputs={userInputs} title="Add New User" />}/>
            </Route>
            <Route path="products">
              <Route index element={<List/>}/>
              <Route path=":productId" element={<Single/>}/>
              <Route path="new" element={<New inputs={productInputs} title="Add New Product" />}/>
            </Route>
            <Route path="projects">
              <Route index element={<List/>}/>
              <Route path=":projectId" element={<Single/>}/>
              <Route path="new" element={<New inputs={projectInputs} title="Add New Project" />}/>
            </Route>
            <Route path="ApplicationAccount">
              <Route index element={<List/>}/>
              <Route path=":applicationAccountId" element={<Single/>}/>
              <Route path="new" element={<New inputs={ applicationAccounts } title="Add New ApplicationAccount"/>}/>
            </Route>
          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;

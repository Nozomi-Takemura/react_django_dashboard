import "./scheme.scss"
import Sidebar from "../../components/sidebar/Sidebar"
import Navbar from "../../components/navbar/Navbar"
// import Datatable from "../../components/datatable/Datatable"
import BasicEditingGrid from "../../components/basiceditinggrid/BasicEditingGrid"

const Scheme = ({inputs,title}) => {
    return (
        <div className="scheme">
            <Sidebar/>
            <div className="schemeContainer">
                <Navbar/>
                <BasicEditingGrid />
            </div>
        </div>
    )
}

export default Scheme
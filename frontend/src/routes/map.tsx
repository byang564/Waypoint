import 'leaflet/dist/leaflet.css'
import * as React from 'react'
import {usePath} from '@/contexts/pathcontext'
import {MapContainer, TileLayer, Polyline, Marker} from 'react-leaflet'
import Waypoint from '@/assets/waypoint.svg?react'
import {Link} from 'react-router-dom'

const Map = () => {
    const {path} = usePath()

    const start = [path[0][0], path[0][1]]
    const end = [path[path.length - 1][0], path[path.length - 1][1]]

    return (
        <div>
            <Link to="/" className="flex flex-col items-center">
                <Waypoint className="w-20 h-20 rounded-full"/>
            </Link>
            <MapContainer center={start} zoom={13} scrollWheelZoom={true} style={{ height: '80vh', width: '100%' }}>
                <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                <Marker position={start} />
                <Polyline positions={path} />
                <Marker position={end} />
            </MapContainer>
        </div>
    )
}

export default Map
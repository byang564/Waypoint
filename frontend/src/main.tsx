import * as React from "react"
import {createRoot} from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom"
import App from '@/App'
import '@/index.css'
import {PathProvider} from '@/contexts/pathcontext'
import Map from '@/routes/map'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/map",
    element: <Map />,
  },
])

createRoot(document.getElementById('root')!).render(
  <PathProvider>
    <RouterProvider router={router} />
  </PathProvider>
)
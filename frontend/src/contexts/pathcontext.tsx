import {createContext, useContext, useState} from 'react';
import * as React from 'react'

const PathContext = createContext(null)

export const PathProvider = ({children}) => {
  const [path, setPath] = useState(null)

  return (
    <PathContext.Provider value={{path, setPath}}>
      {children}
    </PathContext.Provider>
  )
}

export const usePath = () => useContext(PathContext)
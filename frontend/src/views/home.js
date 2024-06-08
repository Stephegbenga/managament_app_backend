import React, {useEffect, useState} from 'react'

import { Helmet } from 'react-helmet'

const Home = (props) => {
  const [botName, setBotName] = useState('')
  const [botImage, setBotImage] = useState('https://upalertz.steksolutions.net/playground_assets/logo-200h.png')

  useEffect(() => {
    const onLoad = async () => {
    }
    onLoad()
  }, [])


  return (
    <div>
    </div>
  )
}

export default Home

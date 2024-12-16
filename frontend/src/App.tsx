import * as React from 'react'
import {Button} from '@/components/ui/button'
import {Input} from '@/components/ui/input'
import Waypoint from '@/assets/waypoint.svg?react'
import {usePath} from '@/contexts/pathcontext'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import {Progress} from '@/components/ui/progress'
import {Link} from 'react-router-dom'

function App() {
  const [start, setStart] = React.useState("")
  const [end, setEnd] = React.useState("")
  const [data, setData] = React.useState("")
  const [loading, setLoading] = React.useState(false)
  const [link, setLink] = React.useState(false)
  const [progress, setProgress] = React.useState(0)
  const {setPath} = usePath()

  const handleStartChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setStart(event.target.value)
  }

  const handleEndChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEnd(event.target.value)
  }

  const handleSelectChange = (value: string) => {
    setData(value)
  }

  const handleSubmit = async () => {
    const coords = {
      start: start,
      end: end,
      data_structure: data,
    }

    setLoading(true)
    setProgress(0)

    const interval = setInterval(() => {
      setProgress((prev) => (prev < 100 ? prev + 0.5 : prev))
    }, 50)

    try {
      const response = await fetch("http://127.0.0.1:8000/path/", {
        method: "POST",
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify(coords),
      })

      if (!response.ok) {
        throw new Error('No Response')
      }
      const data = await response.json()
      setPath(data)

    }
    catch (error) {
      console.error('Error type:', error)
    }
    finally {
      clearInterval(interval)
      setProgress(100)
      setTimeout(() => {
        setLoading(false)
      }, 500)
      setStart("")
      setEnd("")
      setLink(true)
    }
  }

  return (
      <div className="flex flex-col h-screen w-screen justify-center items-center bg-black gap-8">
        <Waypoint className="w-48 h-48 rounded-full"/>
        <div className="flex flex-row gap-6">
          <Input
            type="start"
            placeholder="Start"
            value={start}
            onChange={handleStartChange}
          />
          <Input
            type="end"
            placeholder="End"
            value={end}
            onChange={handleEndChange}
          />
        </div>
        <div>
          <Select onValueChange={handleSelectChange}>
            <SelectTrigger>
              <SelectValue placeholder="Select a data structure" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="fibheap">Fibonacci Heap</SelectItem>
              <SelectItem value="minheap">Min-Heap</SelectItem>
            </SelectContent>
          </Select>
        </div>
        <Button
          variant="ghost"
          size="sm"
          className="bg-slate-500"
          onClick={handleSubmit}
        >
          {loading ? "Loading..." : "Submit"}
        </Button>
        <span className="w-1/2 h-4">{loading && <Progress value={progress} />}</span>
        <div className="h-4">
        {!loading && link &&
          <Button>
            <Link to="/map">
              Go to Map
            </Link>
          </Button>
        }
        </div>
      </div>
  )
}

export default App

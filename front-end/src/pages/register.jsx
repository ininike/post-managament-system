import { useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
const registrationInputData = {
    username: '',
    password: ''
}

const Register = () => {
    const [registrationInput, setRegistrationInput] = useState(registrationInputData)
    const handleInputChange = (e) => {
        setRegistrationInput({
            ...registrationInput,
            [e.target.name]: e.target.value})
    }
    
    const handleRegistration = async () => {
        const{username, password} = registrationInput
        const response =await axios.post('http://127.0.0.1:8000/user/register', {
            username: username,
            password: password
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        if (response.status === 200) {
            console.log('yes')
        }
    }

  return (
   
    <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div className="sm:mx-auto sm:w-full sm:max-w-sm">
      <img
        alt="Your Company"
        src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=600"
        className="mx-auto h-10 w-auto"
      />
      <Link to={'/'}>register</Link>
      <h2 className="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">
        Sign in to your account
      </h2>
    </div>

    <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form className="space-y-6">
        <div>
          <label htmlFor="username" className="block text-sm/6 font-medium text-gray-900">
            Username
          </label>
          <div className="mt-2">
            <input
              id="username"
              name="username"
              type="text"
              required
              autoComplete="username"
              onChange={handleInputChange}
              className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
            />
          </div>
        </div>

        <div>
          <div className="flex items-center justify-between">
            <label htmlFor="password" className="block text-sm/6 font-medium text-gray-900">
              Password
            </label>
            <div className="text-sm">
              <a href="#" className="font-semibold text-indigo-600 hover:text-indigo-500">
                Forgot password?
              </a>
            </div>
          </div>
          <div className="mt-2">
            <input
              id="password"
              name="password"
              type="password"
              required
              autoComplete="current-password"
              onChange={handleInputChange}
              className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
            />
          </div>
        </div>

        <div>
          <button
            type="button"
            onClick={handleRegistration}
            className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Sign in
          </button>
        </div>
      </form>

      <p className="mt-10 text-center text-sm/6 text-gray-500">
        Not a member?{' '}
        <a href="#" className="font-semibold text-indigo-600 hover:text-indigo-500">
          Start a 14 day free trial
        </a>
      </p>
    </div>
  </div>
  )
}

export default Register
import { useState } from 'react'

function App() {
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [downloadUrl, setDownloadUrl] = useState(null)
  const [error, setError] = useState(null)
  const [showHostingMessage, setShowHostingMessage] = useState(false)

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0]
    if (selectedFile) {
      const fileExt = selectedFile.name.split('.').pop().toLowerCase()
      if (fileExt !== 'pdf' && fileExt !== 'docx') {
        setError('Please upload a PDF or DOCX file')
        setFile(null)
        return
      }
      setFile(selectedFile)
      setError(null)
      setDownloadUrl(null)
      setShowHostingMessage(false)
    }
  }

  const handleGenerate = async () => {
    if (!file) {
      setError('Please select a file first')
      return
    }

    setLoading(true)
    setError(null)
    setDownloadUrl(null)
    setShowHostingMessage(false)

    try {
      const formData = new FormData()
      formData.append('file', file)

      const response = await fetch('http://localhost:8000/upload-resume', {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ detail: 'Failed to process resume' }))
        throw new Error(errorData.detail || 'Failed to generate portfolio')
      }

      // Create blob from response
      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      setDownloadUrl(url)
      setShowHostingMessage(true)
    } catch (err) {
      setError(err.message || 'An error occurred while generating the portfolio')
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = () => {
    if (downloadUrl) {
      const link = document.createElement('a')
      link.href = downloadUrl
      link.download = 'portfolio.zip'
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
  }

  return (
    <div className="min-h-screen bg-white flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-lg shadow-lg p-8 border border-gray-200">
          <h1 className="text-3xl font-bold text-center text-black mb-8">
            Resume → Portfolio Converter
          </h1>

          <div className="space-y-6">
            {/* File Upload */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Upload Resume
              </label>
              <input
                type="file"
                accept=".pdf,.docx"
                onChange={handleFileChange}
                className="block w-full text-sm text-gray-500
                  file:mr-4 file:py-2 file:px-4
                  file:rounded-md file:border-0
                  file:text-sm file:font-semibold
                  file:bg-gray-100 file:text-gray-700
                  hover:file:bg-gray-200
                  cursor-pointer"
                disabled={loading}
              />
              {file && (
                <p className="mt-2 text-sm text-gray-600">
                  Selected: {file.name}
                </p>
              )}
            </div>

            {/* Error Message */}
            {error && (
              <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-md text-sm">
                {error}
              </div>
            )}

            {/* Generate Button */}
            <button
              onClick={handleGenerate}
              disabled={!file || loading}
              className="w-full bg-black text-white py-3 px-4 rounded-md font-medium
                hover:bg-gray-800 disabled:bg-gray-400 disabled:cursor-not-allowed
                transition-colors duration-200 flex items-center justify-center gap-2"
            >
              {loading ? (
                <>
                  <svg
                    className="animate-spin h-5 w-5 text-white"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      className="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      strokeWidth="4"
                    ></circle>
                    <path
                      className="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    ></path>
                  </svg>
                  <span>Generating Portfolio...</span>
                </>
              ) : (
                'Generate Portfolio'
              )}
            </button>

            {/* Download Button */}
            {downloadUrl && (
              <button
                onClick={handleDownload}
                className="w-full bg-gray-800 text-white py-3 px-4 rounded-md font-medium
                  hover:bg-gray-700 transition-colors duration-200"
              >
                Download Portfolio
              </button>
            )}

            {/* Hosting Instructions */}
            {showHostingMessage && (
              <div className="bg-blue-50 border border-blue-200 text-blue-800 px-4 py-3 rounded-md text-sm">
                <p className="font-medium mb-1">Portfolio Generated Successfully!</p>
                <p>
                  Upload the extracted <code className="bg-blue-100 px-1 rounded">portfolio</code> folder to{' '}
                  <a
                    href="https://pages.github.com"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="underline hover:text-blue-900"
                  >
                    GitHub Pages
                  </a>
                  ,{' '}
                  <a
                    href="https://www.netlify.com"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="underline hover:text-blue-900"
                  >
                    Netlify
                  </a>
                  , or{' '}
                  <a
                    href="https://vercel.com"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="underline hover:text-blue-900"
                  >
                    Vercel
                  </a>{' '}
                  to host your portfolio.
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App


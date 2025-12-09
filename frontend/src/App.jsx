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
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-2xl shadow-2xl p-8 border border-blue-100 backdrop-blur-lg bg-opacity-95">
          <div className="text-center mb-8">
            <div className="inline-block p-3 bg-gradient-to-br from-blue-100 to-blue-50 rounded-full mb-4">
              <svg className="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h1 className="text-3xl font-bold text-center bg-gradient-to-r from-blue-600 to-blue-800 bg-clip-text text-transparent mb-2">
              Resume → Portfolio Converter
            </h1>
            <p className="text-blue-500 text-sm font-medium">Transform your resume into a stunning portfolio website</p>
          </div>

          <div className="space-y-6">
            {/* File Upload */}
            <div>
              <label className="block text-sm font-semibold text-blue-700 mb-3">
                Upload Your Resume
              </label>
              <div className="relative group">
                <input
                  type="file"
                  accept=".pdf,.docx"
                  onChange={handleFileChange}
                  className="block w-full text-sm text-gray-500
                    file:mr-4 file:py-2 file:px-4
                    file:rounded-lg file:border-0
                    file:text-sm file:font-semibold
                    file:bg-gradient-to-r file:from-blue-500 file:to-blue-600 file:text-white
                    hover:file:from-blue-600 hover:file:to-blue-700
                    cursor-pointer border-2 border-dashed border-blue-200 rounded-lg p-3
                    hover:border-blue-400 transition-colors"
                  disabled={loading}
                />
              </div>
              {file && (
                <p className="mt-3 text-sm font-medium text-blue-600 bg-blue-50 p-2 rounded-lg">
                  ✓ Selected: {file.name}
                </p>
              )}
            </div>

            {/* Error Message */}
            {error && (
              <div className="bg-red-50 border-l-4 border-red-500 text-red-700 px-4 py-3 rounded-lg text-sm shadow-sm flex items-start gap-3">
                <svg className="w-5 h-5 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
                <span>{error}</span>
              </div>
            )}

            {/* Generate Button */}
            <button
              onClick={handleGenerate}
              disabled={!file || loading}
              className="w-full bg-gradient-to-r from-blue-600 to-blue-700 text-white py-3 px-4 rounded-lg font-semibold
                hover:from-blue-700 hover:to-blue-800 disabled:from-gray-400 disabled:to-gray-400 disabled:cursor-not-allowed
                transition-all duration-200 flex items-center justify-center gap-2 shadow-lg hover:shadow-xl disabled:shadow-none"
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
                className="w-full bg-gradient-to-r from-blue-500 to-blue-600 text-white py-3 px-4 rounded-lg font-semibold
                  hover:from-blue-600 hover:to-blue-700 transition-all duration-200 shadow-lg hover:shadow-xl flex items-center justify-center gap-2"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
                Download Portfolio
              </button>
            )}

            {/* Hosting Instructions */}
            {showHostingMessage && (
              <div className="bg-gradient-to-br from-blue-50 to-blue-100 border-l-4 border-blue-500 px-4 py-4 rounded-lg text-blue-900 text-sm shadow-md">
                <div className="flex items-start gap-3">
                  <svg className="w-6 h-6 text-blue-600 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  <div>
                    <p className="font-bold mb-2">✨ Portfolio Generated Successfully!</p>
                    <p className="text-blue-800 leading-relaxed">
                      Extract and upload the <code className="bg-white bg-opacity-60 px-2 py-1 rounded font-mono text-blue-700">portfolio</code> folder to{' '}
                      <a
                        href="https://pages.github.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="font-semibold hover:text-blue-700 transition-colors underline underline-offset-2"
                      >
                        GitHub Pages
                      </a>
                      , <a
                        href="https://www.netlify.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="font-semibold hover:text-blue-700 transition-colors underline underline-offset-2"
                      >
                        Netlify
                      </a>
                      , or{' '}
                      <a
                        href="https://vercel.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="font-semibold hover:text-blue-700 transition-colors underline underline-offset-2"
                      >
                        Vercel
                      </a>
                      {' '}to launch your portfolio online.
                    </p>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App


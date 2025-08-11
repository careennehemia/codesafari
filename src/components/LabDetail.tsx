import React, { useState, useEffect } from 'react';
import { ArrowLeft, BookOpen, Code, Target, MessageCircle, X, ChevronDown, ChevronUp } from 'lucide-react';
import ChatBot from './ChatBot';

interface Lab {
  id: string;
  title: string;
  description: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  duration: string;
}

interface LabDetailProps {
  lab: Lab;
  skill: string;
  onBack: () => void;
}

const LabDetail: React.FC<LabDetailProps> = ({ lab, skill, onBack }) => {
  const [labContent, setLabContent] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [isChatbotOpen, setIsChatbotOpen] = useState(false);

  useEffect(() => {
    const fetchLabContent = async () => {
      try {
        const response = await fetch(`http://localhost:8000/labs/${skill.toLowerCase()}/${lab.id}`);
        const data = await response.json();
        setLabContent(data);
      } catch (error) {
        console.error('Failed to fetch lab content:', error);
        // Fallback to basic content if API fails
        setLabContent({
          reading: `# ${lab.title}\n\nContent is loading...`,
          exercises: ['Loading exercises...']
        });
      } finally {
        setLoading(false);
      }
    };

    fetchLabContent();
  }, [skill, lab.id, lab.title]);

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'Beginner': return 'difficulty-beginner';
      case 'Intermediate': return 'difficulty-intermediate';
      case 'Advanced': return 'difficulty-advanced';
      default: return 'text-gray-600 bg-gray-100';
    }
  };

  const getLabContent = () => {
    // Return content fetched from backend API
    if (labContent) {
      return {
        reading: labContent.reading || `# ${lab.title}\n\nContent loading...`,
        exercises: labContent.exercises || ['Loading exercises...']
      };
    }
    
    // Fallback content while loading
    return {
      reading: `# ${lab.title}\n\nLoading comprehensive course content...`,
      exercises: ['Loading exercises...']
    };
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-white">
        <div className="bg-white shadow-sm border-b border-blue-200">
          <div className="max-w-full mx-auto px-6 py-4">
            <div className="flex items-center space-x-4">
              <div className="bg-blue-600 text-white px-4 py-2 rounded-lg font-bold text-lg">
                CodeSafari
              </div>
              <button onClick={onBack} className="flex items-center space-x-2 text-blue-600 hover:text-blue-800 transition-colors font-medium">
                <ArrowLeft className="w-5 h-5" />
                <span>Back to Labs</span>
              </button>
            </div>
          </div>
        </div>
        <div className="max-w-4xl mx-auto px-6 py-16 text-center">
          <div className="bg-white rounded-xl shadow-lg p-12 border border-blue-200">
            <div className="animate-spin w-12 h-12 border-4 border-blue-600 border-t-transparent rounded-full mx-auto mb-6"></div>
            <h1 className="text-3xl font-bold text-blue-800 mb-4">Loading {lab.title}...</h1>
            <p className="text-blue-600 text-lg">Fetching comprehensive course content from backend...</p>
          </div>
        </div>
      </div>
    );
  }

  const content = getLabContent();

  const oldGetLabContent = () => {
    // This is now unused - content comes from API
    return {
      reading: `# ${lab.title}\n\nContent coming soon...`,
      exercises: ['Practice exercises will be added soon.']
    };
  };

  return (
    <div className="min-h-screen bg-white">
      {/* Header with Logo and Navigation */}
      <div className="bg-white shadow-sm border-b border-blue-200">
        <div className="max-w-full mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              {/* Logo Placeholder */}
              <div className="bg-blue-600 text-white px-4 py-2 rounded-lg font-bold text-lg">
                CodeSafari
              </div>
              <button 
                onClick={onBack}
                className="flex items-center space-x-2 text-white px-6 py-3 rounded-xl font-semibold text-lg hover:shadow-lg transition-all duration-200"
                style={{ backgroundColor: '#2F4156' }}
              >
                <ArrowLeft className="w-5 h-5" />
                <span>Back to Labs</span>
              </button>
            </div>
            
            {/* Ask AI Button */}
            <button
              onClick={() => setIsChatbotOpen(!isChatbotOpen)}
              className="flex items-center space-x-2 text-white px-6 py-3 rounded-xl font-semibold text-lg hover:shadow-lg transition-all duration-200"
              style={{ backgroundColor: '#2F4156' }}
            >
              <MessageCircle className="w-5 h-5" />
              <span>{isChatbotOpen ? 'Close Rafiki' : 'Ask Rafiki'}</span>
              {isChatbotOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
            </button>
          </div>
        </div>
      </div>

      <div className="max-w-full mx-auto px-4 py-4">
        {/* Full-width Lab Content */}
        <div className={`transition-all duration-300 ${
          isChatbotOpen ? 'grid grid-cols-1 lg:grid-cols-3 gap-8' : 'max-w-6xl mx-auto'
        }`}>
          <div className={isChatbotOpen ? 'lg:col-span-2' : 'w-full'}>
            <div className="bg-white rounded-xl shadow-lg border border-blue-200 overflow-hidden">
              {/* Lab Header */}
              <div className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-8">
                <h1 className="text-4xl font-bold mb-3">{lab.title}</h1>
                <p className="text-blue-100 mb-4 text-lg">{lab.description}</p>
                <div className="flex items-center space-x-4">
                  <span className={`px-4 py-2 rounded-full text-sm font-medium bg-white text-blue-600`}>
                    {lab.difficulty}
                  </span>
                  <span className="text-blue-100 flex items-center">
                    <Target className="w-4 h-4 mr-1" />
                    {lab.duration}
                  </span>
                </div>
              </div>

              {/* Lab Content */}
              <div className="p-6">

                {/* Reading Material */}
                <div className="mb-6">
                  <div className="flex items-center space-x-2 mb-4">
                    <BookOpen className="w-6 h-6 text-blue-600" />
                    <h2 className="text-2xl font-bold text-blue-800">Reading Material</h2>
                  </div>
                  <div className="rounded-xl p-8 border border-blue-100" style={{ backgroundColor: '#f8fafc' }}>
                    <div className="prose prose-lg max-w-none">
                      <div 
                        className="markdown-content text-gray-800 leading-relaxed"
                        dangerouslySetInnerHTML={{
                          __html: content.reading
                            .replace(/\*\*(.*?)\*\*/g, '<strong class="text-blue-700 font-bold">$1</strong>')
                            .replace(/\*(.*?)\*/g, '<em class="text-blue-600">$1</em>')
                            .replace(/^### (.*$)/gm, '<h3 class="text-xl font-bold text-blue-800 mt-6 mb-3">$1</h3>')
                            .replace(/^## (.*$)/gm, '<h2 class="text-2xl font-bold text-blue-900 mt-8 mb-4">$1</h2>')
                            .replace(/^# (.*$)/gm, '<h1 class="text-3xl font-bold text-blue-900 mt-8 mb-6">$1</h1>')
                            .replace(/```python([\s\S]*?)```/g, '<pre class="bg-gray-800 text-green-400 p-4 rounded-lg overflow-x-auto my-4 font-mono text-sm"><code>$1</code></pre>')
                            .replace(/```javascript([\s\S]*?)```/g, '<pre class="bg-gray-800 text-yellow-400 p-4 rounded-lg overflow-x-auto my-4 font-mono text-sm"><code>$1</code></pre>')
                            .replace(/```([\s\S]*?)```/g, '<pre class="bg-gray-800 text-gray-100 p-4 rounded-lg overflow-x-auto my-4 font-mono text-sm"><code>$1</code></pre>')
                            .replace(/`([^`]+)`/g, '<code class="bg-blue-100 text-blue-800 px-2 py-1 rounded font-mono text-sm">$1</code>')
                            .replace(/\n/g, '<br>')
                        }}
                      />
                    </div>
                  </div>
                </div>

                {/* Practice Exercises */}
                <div className="mb-8">
                  <div className="flex items-center space-x-2 mb-6">
                    <Code className="w-6 h-6 text-blue-600" />
                    <h2 className="text-2xl font-bold text-blue-800">Practice Exercises</h2>
                  </div>
                  <div className="space-y-4">
                    {(content.exercises || []).map((exercise: string, index: number) => (
                      <div key={index} className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200 hover:shadow-md transition-shadow">
                        <div className="flex items-start space-x-4">
                          <span className="bg-blue-600 text-white text-lg font-bold px-4 py-2 rounded-full min-w-[3rem] text-center">
                            {index + 1}
                          </span>
                          <p className="text-gray-800 text-lg leading-relaxed flex-1">{exercise}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Lab Project */}
                <div>
                  <div className="flex items-center space-x-2 mb-6">
                    <Target className="w-6 h-6 text-blue-600" />
                    <h2 className="text-2xl font-bold text-blue-800">Lab Project</h2>
                  </div>
                  <div className="bg-gradient-to-r from-blue-100 to-indigo-100 rounded-xl p-8 border border-blue-300">
                    <p className="text-gray-800 mb-6 text-lg leading-relaxed">{(labContent && labContent.lab_description) || lab.description}</p>
                    <button 
                      className="text-white px-8 py-4 rounded-lg transition-all font-bold text-lg shadow-lg hover:shadow-xl transform hover:-translate-y-1"
                      style={{ backgroundColor: '#2F4156' }}
                    >
                      🚀 Start Implementation
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Collapsible AI Tutor Sidebar */}
          {isChatbotOpen && (
            <div className="lg:col-span-1">
              <div className="bg-white rounded-xl shadow-lg border border-blue-200 overflow-hidden sticky top-8">
                <div className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-4">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                      <div className="w-10 h-10 bg-white bg-opacity-20 rounded-full flex items-center justify-center">
                        <MessageCircle className="w-5 h-5" />
                      </div>
                      <div>
                        <h3 className="text-lg font-bold">Rafiki AI Tutor</h3>
                        <p className="text-blue-100 text-sm">Your coding companion</p>
                      </div>
                    </div>
                    <button
                      onClick={() => setIsChatbotOpen(false)}
                      className="text-white hover:bg-white hover:bg-opacity-20 p-2 rounded-lg transition-colors"
                    >
                      <X className="w-5 h-5" />
                    </button>
                  </div>
                </div>
                <div className="p-4">
                  <ChatBot 
                    labId={lab.id}
                    skill={skill}
                    labTitle={lab.title}
                  />
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default LabDetail;

import React, { useState } from 'react';
import { ChevronRight, Play, Users, Code, ArrowLeft, BookOpen, Zap, Star } from 'lucide-react';
import './App.css';
import LabDetail from './components/LabDetail';

interface Lab {
  id: string;
  title: string;
  description: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  duration: string;
}

interface Skill {
  name: string;
  icon: string;
  color: string;
  labs: Lab[];
}

const skillsData: Skill[] = [
  {
    name: 'Python',
    icon: '',
    color: 'from-green-500 to-blue-600',
    labs: [
      {
        id: 'python-basics',
        title: 'Python Fundamentals & Data Structures',
        description: 'Master lists, dictionaries, and basic algorithms with hands-on exercises',
        difficulty: 'Beginner',
        duration: '2-3 hours'
      },
      {
        id: 'python-algorithms',
        title: 'Graph Algorithms & BFS/DFS',
        description: 'Implement breadth-first search, depth-first search, and solve graph problems',
        difficulty: 'Intermediate',
        duration: '3-4 hours'
      },
      {
        id: 'python-advanced',
        title: 'Object-Oriented Design Patterns',
        description: 'Build complex systems using classes, inheritance, and design patterns',
        difficulty: 'Advanced',
        duration: '4-5 hours'
      }
    ]
  },
  {
    name: 'JavaScript',
    icon: '',
    color: 'from-yellow-500 to-orange-600',
    labs: [
      {
        id: 'js-fundamentals',
        title: 'Modern JavaScript & DOM Manipulation',
        description: 'Learn ES6+ features, async/await, and interactive web elements',
        difficulty: 'Beginner',
        duration: '2-3 hours'
      },
      {
        id: 'js-algorithms',
        title: 'Data Structures in JavaScript',
        description: 'Implement stacks, queues, trees, and sorting algorithms in JS',
        difficulty: 'Intermediate',
        duration: '3-4 hours'
      },
      {
        id: 'js-react',
        title: 'React Components & State Management',
        description: 'Build dynamic UIs with React hooks, context, and component patterns',
        difficulty: 'Advanced',
        duration: '4-5 hours'
      }
    ]
  },
  {
    name: 'C Programming',
    icon: '',
    color: 'from-gray-600 to-gray-800',
    labs: [
      {
        id: 'c-basics',
        title: 'Memory Management & Pointers',
        description: 'Master malloc, free, pointer arithmetic, and memory debugging',
        difficulty: 'Beginner',
        duration: '3-4 hours'
      },
      {
        id: 'c-systems',
        title: 'System Programming & File I/O',
        description: 'Work with files, processes, and system calls in C',
        difficulty: 'Intermediate',
        duration: '4-5 hours'
      },
      {
        id: 'c-advanced',
        title: 'Data Structures & Performance',
        description: 'Implement linked lists, hash tables, and optimize for speed',
        difficulty: 'Advanced',
        duration: '5-6 hours'
      }
    ]
  },
  {
    name: 'Web Development',
    icon: '',
    color: 'from-purple-500 to-pink-600',
    labs: [
      {
        id: 'web-html-css',
        title: 'Responsive Design & CSS Grid',
        description: 'Create beautiful, mobile-first layouts with modern CSS',
        difficulty: 'Beginner',
        duration: '2-3 hours'
      },
      {
        id: 'web-fullstack',
        title: 'Full-Stack Web Application',
        description: 'Build a complete app with frontend, backend, and database',
        difficulty: 'Intermediate',
        duration: '4-5 hours'
      },
      {
        id: 'web-deployment',
        title: 'Cloud Deployment & DevOps',
        description: 'Deploy applications with Docker, CI/CD, and cloud platforms',
        difficulty: 'Advanced',
        duration: '3-4 hours'
      }
    ]
  }
];

function App() {
  const [selectedSkill, setSelectedSkill] = useState<string | null>(null);
  const [selectedLab, setSelectedLab] = useState<{ lab: Lab; skill: string } | null>(null);

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'Beginner': return 'text-green-600 bg-green-100';
      case 'Intermediate': return 'text-yellow-600 bg-yellow-100';
      case 'Advanced': return 'text-red-600 bg-red-100';
      default: return 'text-gray-600 bg-gray-100';
    }
  };

  // Show lab detail if a lab is selected
  if (selectedLab) {
    return (
      <LabDetail 
        lab={selectedLab.lab}
        skill={selectedLab.skill}
        onBack={() => setSelectedLab(null)}
      />
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
  <img
    src="/logo.png"
    alt="CodeSafari"
    className="w-10 h-10 rounded-lg"  // 48px — smaller than w-16
  />
  <h1 className="text-2xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
    CodeSafari
  </h1>
</div>
            
            <div className="flex items-center space-x-2 text-sm text-gray-600">
              <Users className="w-4 h-4" />
              <span>Join thousands of learners</span>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative py-20 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <div className="mb-8">
            <h2 className="text-5xl font-bold text-gray-900 mb-6">
              Your One-Stop
              <span className="bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent"> Coding Adventure</span>
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
              Master programming fundamentals through hands-on labs inspired by MIT's rigorous curriculum. 
              Get stuck? Our AI tutor is ready to guide you through any challenge.
            </p>
          </div>
          
          <div className="flex justify-center space-x-8 mb-12">
            <div className="flex items-center space-x-2 text-gray-700">
              <BookOpen className="w-5 h-5 text-blue-600" />
              <span>Interactive Labs</span>
            </div>
            <div className="flex items-center space-x-2 text-gray-700">
              <Zap className="w-5 h-5 text-yellow-600" />
              <span>AI-Powered Help</span>
            </div>
          
          </div>

          <button 
            onClick={() => {
              setSelectedSkill('Python');
              document.getElementById('labs')?.scrollIntoView({ behavior: 'smooth' });
            }}
            className="text-white px-8 py-4 rounded-lg font-semibold text-lg hover:shadow-lg transform hover:scale-105 transition-all duration-200 flex items-center space-x-2 mx-auto"
            style={{ backgroundColor: '#2F4156' }}
          >
            <Play className="w-5 h-5" />
            <span>Start Your Journey</span>
          </button>
        </div>
      </section>

      {/* Skills & Labs Section */}
      <section id="labs" className="py-16 px-4 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-12">
            <h3 className="text-3xl font-bold text-gray-900 mb-4">Choose Your Skill Track</h3>
            <p className="text-gray-600 max-w-2xl mx-auto">
              Each skill track contains carefully crafted labs that build upon each other, 
              taking you from fundamentals to advanced concepts.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
            {skillsData.map((skill) => (
              <div
                key={skill.name}
                onClick={() => setSelectedSkill(selectedSkill === skill.name ? null : skill.name)}
                className={`cursor-pointer transform transition-all duration-200 hover:scale-105 ${
                  selectedSkill === skill.name ? 'scale-105' : ''
                }`}
              >
                <div className={`bg-gradient-to-r ${skill.color} rounded-xl p-6 text-white shadow-lg hover:shadow-xl`}>
                  <div className="text-center mb-4">
                    <div className="text-4xl mb-2">{skill.icon}</div>
                    <h4 className="text-xl font-bold mb-1">{skill.name}</h4>
                  </div>
                  <p className="text-sm opacity-90 mb-4 text-center">{skill.labs.length} Labs Available</p>
                  <div className="flex items-center justify-center text-sm font-medium">
                    <span>Explore Labs</span>
                    <ChevronRight className="w-4 h-4 ml-1" />
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Labs Display */}
          {selectedSkill && (
            <div className="bg-gradient-to-br from-blue-50 to-indigo-100 rounded-xl p-8 animate-fadeIn border border-blue-200 shadow-lg">
              <div className="flex items-center mb-6">
                <span className="text-3xl mr-3">
                  {skillsData.find(s => s.name === selectedSkill)?.icon}
                </span>
                <h4 className="text-2xl font-bold text-gray-900">
                  {selectedSkill} Labs
                </h4>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {skillsData
                  .find(s => s.name === selectedSkill)
                  ?.labs.map((lab, index) => (
                    <div
                      key={lab.id}
                      className="bg-white rounded-lg p-6 shadow-md hover:shadow-lg transition-shadow duration-200 border border-gray-200"
                    >
                      <div className="flex items-start justify-between mb-3">
                        <span className="text-2xl font-bold text-gray-400">
                          {String(index + 1).padStart(2, '0')}
                        </span>
                        <span className={`px-2 py-1 rounded-full text-xs font-medium ${getDifficultyColor(lab.difficulty)}`}>
                          {lab.difficulty}
                        </span>
                      </div>
                      
                      <h5 className="text-lg font-bold text-gray-900 mb-2">
                        {lab.title}
                      </h5>
                      
                      <p className="text-gray-600 text-sm mb-4 leading-relaxed">
                        {lab.description}
                      </p>
                      
                      <div className="flex items-center justify-between">
                        <span className="text-xs text-gray-500">
                          ⏱️ {lab.duration}
                        </span>
                        <button 
                          onClick={() => setSelectedLab({ lab, skill: selectedSkill })}
                          className="text-white px-4 py-2 rounded-lg text-sm font-medium hover:shadow-md transition-all duration-200 flex items-center space-x-1"
                          style={{ backgroundColor: '#2F4156' }}
                        >
                          <span>Start Lab</span>
                          <ChevronRight className="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                  ))}
              </div>
            </div>
          )}
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 text-center">
            <div className="flex items-center space-x-3 mb-4 md:mb-0">
              {/* Footer Logo - Replace this div with <img src="/logo.png" alt="CodeSafari" className="w-8 h-8" /> when you have your logo */}
              <div className="w-8 h-8 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg flex items-center justify-center">
                <Code className="w-5 h-5 text-white" />
              </div>
              <span className="text-xl font-bold">CodeSafari</span>
            </div>
          <p className="text-gray-400">
            Architecting self-guided coding excellence, one lab at a time.
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;

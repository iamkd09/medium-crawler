# 📰 Medium.com Crawler – Django + React Assignment

## Overview
A web application that crawls the latest 10 Medium blogs for any tag and displays them in real-time on a React frontend.  
Built using **Django (backend)**, **MySQL (database)**, and **React.js (frontend)**.

## 🧱 Tech Stack
- **Backend:** Django, Django REST Framework  
- **Frontend:** React.js + Bootstrap  
- **Database:** MySQL  
- **Crawling:** Requests + BeautifulSoup  

## ⚙️ Features
✅ Crawl latest 10 Medium blogs for a given tag  
✅ Real-time crawl updates (polling)  
✅ Search history tracking  
✅ Tag suggestions for typos  
✅ Admin panel for managing blogs & tags  
✅ Attractive Bootstrap + React UI  

## 🧩 API Endpoints
| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/api/crawl/<tag>/` | POST | Crawl latest Medium blogs |
| `/api/blogs/?tag=<tag>` | GET | Fetch crawled blogs for tag |
| `/api/history/` | GET | Get search history |

## 🗄️ Database Models
- **Tag:** stores unique tag names  
- **Blog:** stores title, creator, details, URL, and tag relations  
- **Response:** optional comments  
- **SearchHistory:** stores all searched tags  

## 🧪 Test Cases
Basic Django unit tests in `blogs/tests.py`.

## 🗓️ Timeline
| Phase | Description | Duration |
|--------|--------------|----------|
| Phase 1 | Django + MySQL + project setup | 1 day |
| Phase 2 | Crawler logic + API creation | 1 day |
| Phase 3 | React integration + display | 1.5 days |
| Phase 4 | Real-time updates + suggestions | 1 day |
| Phase 5 | Testing + documentation | 0.5 day |

## 🚀 How to Run
### Backend
```bash
python manage.py runserver

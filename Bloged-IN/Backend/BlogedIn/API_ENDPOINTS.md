# Bloged-IN API Documentation

## Base URL: `http://localhost:8000/api/`

---

## 1. AUTHENTICATION & USERS

### Get All Users
**Request:**
```
GET /api/users/
```

**Response:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "admin",
            "email": "admin@example.com",
            "first_name": "Admin",
            "last_name": "User",
            "date_joined": "2024-01-01T00:00:00Z"
        },
        {
            "id": 2,
            "username": "john_doe",
            "email": "john@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "date_joined": "2024-01-02T00:00:00Z"
        }
    ]
}
```

### Get User by ID
**Request:**
```
GET /api/users/1/
```

**Response:**
```json
{
    "id": 1,
    "username": "admin",
    "email": "admin@example.com",
    "first_name": "Admin",
    "last_name": "User",
    "date_joined": "2024-01-01T00:00:00Z"
}
```

---

## 2. CATEGORIES

### Get All Categories
**Request:**
```
GET /api/categories/
```

**Response:**
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Technology",
            "description": "Tech-related posts",
            "post_count": 5,
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 2,
            "name": "Travel",
            "description": "Travel and adventure posts",
            "post_count": 3,
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        }
    ]
}
```

### Create Category
**Request:**
```
POST /api/categories/
Content-Type: application/json
Authorization: Token your_token_here

{
    "name": "Programming",
    "description": "Programming and coding posts"
}
```

**Response:**
```json
{
    "id": 3,
    "name": "Programming",
    "description": "Programming and coding posts",
    "post_count": 0,
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
}
```

### Update Category
**Request:**
```
PUT /api/categories/1/
Content-Type: application/json
Authorization: Token your_token_here

{
    "name": "Technology Updated",
    "description": "Updated tech description"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Technology Updated",
    "description": "Updated tech description",
    "post_count": 5,
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
}
```

### Delete Category
**Request:**
```
DELETE /api/categories/1/
Authorization: Token your_token_here
```

**Response:**
```
204 No Content
```

---

## 3. USER PROFILES

### Get All Profiles
**Request:**
```
GET /api/profiles/
```

**Response:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "first_name": "Admin",
                "last_name": "User",
                "date_joined": "2024-01-01T00:00:00Z"
            },
            "username": "admin",
            "bio": "Admin user bio",
            "profile_picture": null,
            "website": "https://example.com",
            "location": "New York",
            "date_of_birth": null,
            "is_verified": true,
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        }
    ]
}
```

### Get Profile by User ID
**Request:**
```
GET /api/profiles/?user=1
```

**Response:**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "first_name": "Admin",
                "last_name": "User",
                "date_joined": "2024-01-01T00:00:00Z"
            },
            "username": "admin",
            "bio": "Admin user bio",
            "profile_picture": null,
            "website": "https://example.com",
            "location": "New York",
            "date_of_birth": null,
            "is_verified": true,
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        }
    ]
}
```

---

## 4. POSTS

### Get All Posts
**Request:**
```
GET /api/posts/
```

**Response:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Getting Started with Django",
            "slug": "getting-started-with-django",
            "author": {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "first_name": "Admin",
                "last_name": "User",
                "date_joined": "2024-01-01T00:00:00Z"
            },
            "category": {
                "id": 1,
                "name": "Technology",
                "description": "Tech-related posts",
                "post_count": 5,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z"
            },
            "excerpt": "Learn how to build web applications with Django...",
            "featured_image": null,
            "status": "published",
            "is_featured": true,
            "view_count": 150,
            "comment_count": 5,
            "like_count": 12,
            "tags": [
                {
                    "id": 1,
                    "name": "django",
                    "created_at": "2024-01-01T00:00:00Z"
                },
                {
                    "id": 2,
                    "name": "python",
                    "created_at": "2024-01-01T00:00:00Z"
                }
            ],
            "created_at": "2024-01-01T00:00:00Z",
            "published_at": "2024-01-01T00:00:00Z"
        }
    ]
}
```

### Get Posts with Filters
**Request:**
```
GET /api/posts/?status=published&category=1&featured=true&search=django&ordering=-created_at
```

**Response:**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Getting Started with Django",
            "slug": "getting-started-with-django",
            "author": {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "first_name": "Admin",
                "last_name": "User",
                "date_joined": "2024-01-01T00:00:00Z"
            },
            "category": {
                "id": 1,
                "name": "Technology",
                "description": "Tech-related posts",
                "post_count": 5,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z"
            },
            "excerpt": "Learn how to build web applications with Django...",
            "featured_image": null,
            "status": "published",
            "is_featured": true,
            "view_count": 150,
            "comment_count": 5,
            "like_count": 12,
            "tags": [
                {
                    "id": 1,
                    "name": "django",
                    "created_at": "2024-01-01T00:00:00Z"
                }
            ],
            "created_at": "2024-01-01T00:00:00Z",
            "published_at": "2024-01-01T00:00:00Z"
        }
    ]
}
```

### Get Single Post (Detailed)
**Request:**
```
GET /api/posts/1/
```

**Response:**
```json
{
    "id": 1,
    "title": "Getting Started with Django",
    "slug": "getting-started-with-django",
    "author": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "date_joined": "2024-01-01T00:00:00Z"
    },
    "category": {
        "id": 1,
        "name": "Technology",
        "description": "Tech-related posts",
        "post_count": 5,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    },
    "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design...",
    "excerpt": "Learn how to build web applications with Django...",
    "featured_image": null,
    "status": "published",
    "is_featured": true,
    "allow_comments": true,
    "view_count": 150,
    "comment_count": 5,
    "like_count": 12,
    "tags": [
        {
            "id": 1,
            "name": "django",
            "created_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 2,
            "name": "python",
            "created_at": "2024-01-01T00:00:00Z"
        }
    ],
    "comments": [
        {
            "id": 1,
            "post": 1,
            "author": {
                "id": 2,
                "username": "john_doe",
                "email": "john@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "date_joined": "2024-01-02T00:00:00Z"
            },
            "username": "john_doe",
            "parent": null,
            "content": "Great tutorial! Very helpful.",
            "is_approved": true,
            "replies": [],
            "reply_count": 0,
            "created_at": "2024-01-02T00:00:00Z",
            "updated_at": "2024-01-02T00:00:00Z"
        }
    ],
    "likes": [
        {
            "id": 1,
            "user": {
                "id": 2,
                "username": "john_doe",
                "email": "john@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "date_joined": "2024-01-02T00:00:00Z"
            },
            "username": "john_doe",
            "post": 1,
            "like_type": "like",
            "created_at": "2024-01-02T00:00:00Z"
        }
    ],
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "published_at": "2024-01-01T00:00:00Z"
}
```

### Create Post
**Request:**
```
POST /api/posts/
Content-Type: application/json
Authorization: Token your_token_here

{
    "title": "My First Blog Post",
    "content": "This is the content of my blog post. It can be very long and contain multiple paragraphs...",
    "excerpt": "A brief summary of the post",
    "category": 1,
    "status": "published",
    "is_featured": false,
    "allow_comments": true
}
```

**Response:**
```json
{
    "id": 2,
    "title": "My First Blog Post",
    "slug": "my-first-blog-post",
    "author": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "date_joined": "2024-01-01T00:00:00Z"
    },
    "category": {
        "id": 1,
        "name": "Technology",
        "description": "Tech-related posts",
        "post_count": 6,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    },
    "content": "This is the content of my blog post. It can be very long and contain multiple paragraphs...",
    "excerpt": "A brief summary of the post",
    "featured_image": null,
    "status": "published",
    "is_featured": false,
    "allow_comments": true,
    "view_count": 0,
    "comment_count": 0,
    "like_count": 0,
    "tags": [],
    "comments": [],
    "likes": [],
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "published_at": "2024-01-01T00:00:00Z"
}
```

### Update Post
**Request:**
```
PUT /api/posts/1/
Content-Type: application/json
Authorization: Token your_token_here

{
    "title": "Updated Title",
    "content": "Updated content...",
    "status": "published"
}
```

**Response:**
```json
{
    "id": 1,
    "title": "Updated Title",
    "slug": "getting-started-with-django",
    "author": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "date_joined": "2024-01-01T00:00:00Z"
    },
    "category": {
        "id": 1,
        "name": "Technology",
        "description": "Tech-related posts",
        "post_count": 5,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    },
    "content": "Updated content...",
    "excerpt": "Learn how to build web applications with Django...",
    "featured_image": null,
    "status": "published",
    "is_featured": true,
    "allow_comments": true,
    "view_count": 150,
    "comment_count": 5,
    "like_count": 12,
    "tags": [
        {
            "id": 1,
            "name": "django",
            "created_at": "2024-01-01T00:00:00Z"
        }
    ],
    "comments": [],
    "likes": [],
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z",
    "published_at": "2024-01-01T00:00:00Z"
}
```

### Delete Post
**Request:**
```
DELETE /api/posts/1/
Authorization: Token your_token_here
```

**Response:**
```
204 No Content
```

### Increment Post View Count
**Request:**
```
POST /api/posts/1/increment_view/
```

**Response:**
```json
{
    "status": "view count incremented"
}
```

### Get Post Comments
**Request:**
```
GET /api/posts/1/comments/
```

**Response:**
```json
[
    {
        "id": 1,
        "post": 1,
        "author": {
            "id": 2,
            "username": "john_doe",
            "email": "john@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "date_joined": "2024-01-02T00:00:00Z"
        },
        "username": "john_doe",
        "parent": null,
        "content": "Great tutorial! Very helpful.",
        "is_approved": true,
        "replies": [],
        "reply_count": 0,
        "created_at": "2024-01-02T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }
]
```

### Get Post Likes
**Request:**
```
GET /api/posts/1/likes/
```

**Response:**
```json
[
    {
        "id": 1,
        "user": {
            "id": 2,
            "username": "john_doe",
            "email": "john@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "date_joined": "2024-01-02T00:00:00Z"
        },
        "username": "john_doe",
        "post": 1,
        "like_type": "like",
        "created_at": "2024-01-02T00:00:00Z"
    }
]
```

---

## 5. COMMENTS

### Get All Comments
**Request:**
```
GET /api/comments/
GET /api/comments/?post=1
GET /api/comments/?author=1
```

**Response:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "post": 1,
            "author": {
                "id": 2,
                "username": "john_doe",
                "email": "john@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "date_joined": "2024-01-02T00:00:00Z"
            },
            "username": "john_doe",
            "parent": null,
            "content": "Great tutorial! Very helpful.",
            "is_approved": true,
            "replies": [
                {
                    "id": 2,
                    "post": 1,
                    "author": {
                        "id": 1,
                        "username": "admin",
                        "email": "admin@example.com",
                        "first_name": "Admin",
                        "last_name": "User",
                        "date_joined": "2024-01-01T00:00:00Z"
                    },
                    "username": "admin",
                    "parent": 1,
                    "content": "Thank you!",
                    "is_approved": true,
                    "replies": [],
                    "reply_count": 0,
                    "created_at": "2024-01-02T00:00:00Z",
                    "updated_at": "2024-01-02T00:00:00Z"
                }
            ],
            "reply_count": 1,
            "created_at": "2024-01-02T00:00:00Z",
            "updated_at": "2024-01-02T00:00:00Z"
        }
    ]
}
```

### Create Comment
**Request:**
```
POST /api/comments/create/
Content-Type: application/json
Authorization: Token your_token_here

{
    "post": 1,
    "content": "Great post! Thanks for sharing.",
    "parent": null
}
```

**Response:**
```json
{
    "id": 3,
    "post": 1,
    "author": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "date_joined": "2024-01-01T00:00:00Z"
    },
    "username": "admin",
    "parent": null,
    "content": "Great post! Thanks for sharing.",
    "is_approved": false,
    "replies": [],
    "reply_count": 0,
    "created_at": "2024-01-02T00:00:00Z",
    "updated_at": "2024-01-02T00:00:00Z"
}
```

### Create Reply to Comment
**Request:**
```
POST /api/comments/create/
Content-Type: application/json
Authorization: Token your_token_here

{
    "post": 1,
    "content": "This is a reply to the comment",
    "parent": 1
}
```

**Response:**
```json
{
    "id": 4,
    "post": 1,
    "author": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "date_joined": "2024-01-01T00:00:00Z"
    },
    "username": "admin",
    "parent": 1,
    "content": "This is a reply to the comment",
    "is_approved": false,
    "replies": [],
    "reply_count": 0,
    "created_at": "2024-01-02T00:00:00Z",
    "updated_at": "2024-01-02T00:00:00Z"
}
```

### Get Comment Replies
**Request:**
```
GET /api/comments/1/replies/
```

**Response:**
```json
[
    {
        "id": 2,
        "post": 1,
        "author": {
            "id": 1,
            "username": "admin",
            "email": "admin@example.com",
            "first_name": "Admin",
            "last_name": "User",
            "date_joined": "2024-01-01T00:00:00Z"
        },
        "username": "admin",
        "parent": 1,
        "content": "Thank you!",
        "is_approved": true,
        "replies": [],
        "reply_count": 0,
        "created_at": "2024-01-02T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }
]
```

---

## 6. LIKES

### Get All Likes
**Request:**
```
GET /api/likes/
GET /api/likes/?post=1
GET /api/likes/?user=1
```

**Response:**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": {
                "id": 2,
                "username": "john_doe",
                "email": "john@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "date_joined": "2024-01-02T00:00:00Z"
            },
            "username": "john_doe",
            "post": 1,
            "like_type": "like",
            "created_at": "2024-01-02T00:00:00Z"
        },
        {
            "id": 2,
            "user": {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "first_name": "Admin",
                "last_name": "User",
                "date_joined": "2024-01-01T00:00:00Z"
            },
            "username": "admin",
            "post": 1,
            "like_type": "love",
            "created_at": "2024-01-02T00:00:00Z"
        }
    ]
}
```

### Create/Update Like
**Request:**
```
POST /api/likes/create/
Content-Type: application/json
Authorization: Token your_token_here

{
    "post": 1,
    "like_type": "like"
}
```

**Available Like Types:**
- `like`
- `love`
- `laugh`
- `wow`
- `sad`
- `angry`

**Response:**
```json
{
    "id": 3,
    "user": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "date_joined": "2024-01-01T00:00:00Z"
    },
    "username": "admin",
    "post": 1,
    "like_type": "like",
    "created_at": "2024-01-02T00:00:00Z"
}
```

---

## 7. TAGS

### Get All Tags
**Request:**
```
GET /api/tags/
```

**Response:**
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "django",
            "created_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 2,
            "name": "python",
            "created_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 3,
            "name": "web-development",
            "created_at": "2024-01-01T00:00:00Z"
        }
    ]
}
```

### Create Tag
**Request:**
```
POST /api/tags/
Content-Type: application/json
Authorization: Token your_token_here

{
    "name": "javascript"
}
```

**Response:**
```json
{
    "id": 4,
    "name": "javascript",
    "created_at": "2024-01-01T00:00:00Z"
}
```

---

## 8. SEARCH

### Search Across Posts, Categories, and Tags
**Request:**
```
GET /api/search/?q=django
```

**Response:**
```json
{
    "posts": [
        {
            "id": 1,
            "title": "Getting Started with Django",
            "slug": "getting-started-with-django",
            "author": {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "first_name": "Admin",
                "last_name": "User",
                "date_joined": "2024-01-01T00:00:00Z"
            },
            "category": {
                "id": 1,
                "name": "Technology",
                "description": "Tech-related posts",
                "post_count": 5,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z"
            },
            "excerpt": "Learn how to build web applications with Django...",
            "featured_image": null,
            "status": "published",
            "is_featured": true,
            "view_count": 150,
            "comment_count": 5,
            "like_count": 12,
            "tags": [
                {
                    "id": 1,
                    "name": "django",
                    "created_at": "2024-01-01T00:00:00Z"
                }
            ],
            "created_at": "2024-01-01T00:00:00Z",
            "published_at": "2024-01-01T00:00:00Z"
        }
    ],
    "categories": [],
    "tags": [
        {
            "id": 1,
            "name": "django",
            "created_at": "2024-01-01T00:00:00Z"
        }
    ],
    "query": "django"
}
```

---

## 9. PAGINATION

### Example with Pagination
**Request:**
```
GET /api/posts/?page=1&page_size=5
```

**Response:**
```json
{
    "count": 25,
    "next": "http://localhost:8000/api/posts/?page=2&page_size=5",
    "previous": null,
    "results": [
        // 5 posts here
    ]
}
```

**Next Page:**
```
GET /api/posts/?page=2&page_size=5
```

**Response:**
```json
{
    "count": 25,
    "next": "http://localhost:8000/api/posts/?page=3&page_size=5",
    "previous": "http://localhost:8000/api/posts/?page=1&page_size=5",
    "results": [
        // 5 more posts here
    ]
}
```

---

## 10. ERROR RESPONSES

### 400 Bad Request
```json
{
    "field_name": [
        "This field is required."
    ]
}
```

### 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
    "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
    "detail": "Not found."
}
```

### 500 Internal Server Error
```json
{
    "detail": "Internal server error."
}
```

---

## 11. FILTERING AND SEARCHING

### Available Query Parameters

**Posts:**
- `status`: Filter by post status (draft, published, archived)
- `category`: Filter by category ID
- `author`: Filter by author ID
- `featured`: Filter featured posts (true/false)
- `tags`: Filter by tags (comma-separated)
- `search`: Search in title, content, excerpt, author username
- `ordering`: Order by field (-field for descending)

**Comments:**
- `post`: Filter by post ID
- `author`: Filter by author ID
- `ordering`: Order by created_at

**Likes:**
- `post`: Filter by post ID
- `user`: Filter by user ID
- `ordering`: Order by created_at

**Profiles:**
- `user`: Filter by user ID
- `search`: Search in username, bio, location
- `ordering`: Order by created_at, username

**Categories:**
- `search`: Search in name, description
- `ordering`: Order by name, created_at, post_count

**Tags:**
- `search`: Search in name
- `ordering`: Order by name, created_at, post_count

---

## 12. AUTHENTICATION

### Token Authentication
Add this header to authenticated requests:
```
Authorization: Token your_token_here
```

### Session Authentication
Login through Django admin or use session cookies.

---

## 13. FILE UPLOADS

### Upload Profile Picture
**Request:**
```
POST /api/profiles/
Content-Type: multipart/form-data
Authorization: Token your_token_here

Form Data:
- profile_picture: [file]
- bio: "My bio"
- website: "https://example.com"
- location: "New York"
```

### Upload Post Featured Image
**Request:**
```
POST /api/posts/
Content-Type: multipart/form-data
Authorization: Token your_token_here

Form Data:
- title: "My Post"
- content: "Post content"
- featured_image: [file]
- category: 1
- status: "published"
```

---

## 14. TESTING TIPS

1. **Start with GET requests** (no authentication needed for public data)
2. **Use Django Admin** to create initial test data
3. **Test pagination** with large datasets
4. **Test filtering** with different query parameters
5. **Test search** functionality
6. **Test nested relationships** (comments with replies, posts with tags)
7. **Test file uploads** for images
8. **Test error handling** with invalid data

---

## 15. COMMON USE CASES

### Create a Complete Blog Post
1. Create category: `POST /api/categories/`
2. Create tags: `POST /api/tags/`
3. Create post: `POST /api/posts/`
4. Add comments: `POST /api/comments/create/`
5. Add likes: `POST /api/likes/create/`

### Get User's Blog Activity
1. Get user posts: `GET /api/posts/?author=1`
2. Get user comments: `GET /api/comments/?author=1`
3. Get user likes: `GET /api/likes/?user=1`
4. Get user profile: `GET /api/profiles/?user=1`

### Search and Filter Posts
1. Search posts: `GET /api/search/?q=keyword`
2. Filter by category: `GET /api/posts/?category=1`
3. Filter by tags: `GET /api/posts/?tags=django,python`
4. Get featured posts: `GET /api/posts/?featured=true`
5. Sort by popularity: `GET /api/posts/?ordering=-view_count` 
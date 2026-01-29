<template>
    <section class="blog-view-section">
      <div class="container">
        <!-- Loading State -->
        <div v-if="isLoading" class="loading">
          <p>Loading blog post...</p>
        </div>
  
        <!-- in case the page does not load -->
        <div v-else-if="errorMessage" class="error">
          <p>{{ errorMessage }}</p>
          <router-link to="/blog" class="back-link">
            Back to Blogs
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
          </router-link>
        </div>
  
        <!-- Blog Content -->
        <div v-else-if="blogPost" class="blog-content">
          <!-- Back Link -->
          <router-link to="/blog" class="back-link">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Back to Blogs
          </router-link>

          <div class="tags">
            <span class="category-tag">{{ blogPost.category }}</span>
            <span class="location-tag">{{ blogPost.location }}</span>
          </div>

          <div class="meta">
            <span>{{ blogPost.date }}</span>
            <span>{{ blogPost.readTime }} min read</span>
          </div>
  
          <h1>{{ blogPost.title }}</h1>
  
          <div class="author">
            <span>By {{ blogPost.author }}</span>
          </div>
  
          <div class="content" v-html="blogPost.content"></div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import axios from 'axios';
  
  const route = useRoute();
  const blogPost = ref(null);
  const isLoading = ref(false);
  const errorMessage = ref('');
  
  const fetchBlogPost = async () => {
    isLoading.value = true;
    const blogID = route.params.blogid
    try {
      const response = await axios.get(`https://apibooksal.getintoto.com/api/v1/blog/retrieve-blog/${blogID}/`);
      const post = response.data;
  
      blogPost.value = {
        id: post.id,
        title: post.title,
        content: post.content || '<p>No content available.</p>',
        author: post.author || 'Unknown',
        date: new Date(post.created_at).toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'long',
          day: 'numeric'
        }),
        category: post.category?.name || 'Uncategorized',
        location: post.meta_tags?.split(',')[1]?.trim() || 'Unknown',
        readTime: calculateReadTime(post.content || ''),
      };
    } catch (error) {
      console.error('Failed to fetch blog post:', error);
      errorMessage.value = 'Could not load blog post. Please try again later.';
    } finally {
      isLoading.value = false;
    }
  };

  const calculateReadTime = (content) => {
  const wordsPerMinute = 200;
  const wordCount = content.split(/\s+/).length;
  const readTime = Math.ceil(wordCount / wordsPerMinute);
  return readTime < 1 ? 1 : readTime;
};
  
  onMounted(() => {
    console.log('Route Params:', route.params);
    fetchBlogPost();
  });

  console.log('Route Params:', route.params.blogid);
  </script>
  
  <style scoped>
  .blog-view-section {
    background-color: #f8f9fa;
    padding: 48px 16px;
    min-height: 100vh;
  }
  
  .container {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .loading, .error {
    text-align: center;
    padding: 48px;
  }
  
  .loading p, .error p {
    color: #374151;
    font-size: 18px;
    margin-bottom: 16px;
  }
  
  .back-link {
    display: inline-flex;
    align-items: center;
    color: #15803d;
    font-weight: 500;
    font-size: 16px;
    margin-bottom: 24px;
    text-decoration: none;
  }
  
  .back-link:hover {
    text-decoration: underline;
  }
  
  .back-link svg {
    width: 16px;
    height: 16px;
    margin-right: 8px;
  }
  
  .blog-content {
    background-color: #fff;
    border-radius: 8px;
    padding: 32px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 16px;
  }
  
  .category-tag {
    background-color: #15803d;
    color: #fff;
    font-size: 12px;
    font-weight: bold;
    padding: 4px 12px;
    border-radius: 9999px;
  }
  
  .location-tag {
    background-color: #f3f4f6;
    color: #4b5563;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 9999px;
  }
  
  .meta {
    display: flex;
    align-items: center;
    color: #6b7280;
    font-size: 14px;
    margin-bottom: 16px;
  }
  
  .meta span:first-child {
    margin-right: 12px;
  }
  
  .author {
    color: #6b7280;
    font-size: 14px;
    margin-bottom: 16px;
  }
  
  h1 {
    font-size: 32px;
    font-weight: bold;
    color: #15803d;
    margin-bottom: 16px;
  }
  
  .content {
    color: #374151;
    font-size: 16px;
    line-height: 1.6;
  }
  
  .content :deep(p) {
    margin-bottom: 16px;
  }
  
  .content :deep(h2) {
    font-size: 24px;
    font-weight: bold;
    color: #15803d;
    margin: 24px 0 16px;
  }
  
  .content :deep(h3) {
    font-size: 20px;
    font-weight: bold;
    color: #374151;
    margin: 20px 0 12px;
  }
  
  .content :deep(ul), .content :deep(ol) {
    margin-bottom: 16px;
    padding-left: 24px;
  }
  
  .content :deep(li) {
    margin-bottom: 8px;
  }
  
  @media (min-width: 768px) {
    .blog-view-section {
      padding: 48px 32px;
    }
  
    .blog-content {
      padding: 48px;
    }
  
    h1 {
      font-size: 40px;
    }
  }
  
  @media (min-width: 1024px) {
    .blog-view-section {
      padding: 48px 48px;
    }
  }
  </style>
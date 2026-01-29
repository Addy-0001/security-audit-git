import { writeFile } from 'fs/promises';
import { format } from 'date-fns';
import axios from 'axios';

// Configure axios instance
const apiClient = axios.create({
    baseURL: 'https://apibooksal.getintoto.com/api/v1/',
    headers: {
        'Content-Type': 'application/json'
    }
});

const staticRoutes = [
    { path: '/', priority: 1.0, changefreq: 'daily' },
    { path: '/about', priority: 0.8, changefreq: 'monthly' },
    { path: '/futsals', priority: 0.9, changefreq: 'daily' },
    { path: '/login', priority: 0.6, changefreq: 'monthly' },
    { path: '/register', priority: 0.6, changefreq: 'monthly' },
    { path: '/terms', priority: 0.5, changefreq: 'yearly' },
    { path: '/privacy-policy', priority: 0.5, changefreq: 'yearly' },
    { path: '/blog', priority: 0.8, changefreq: 'weekly' }
];

async function generateSitemap() {
    const baseUrl = 'https://booksall.app';
    const currentDate = format(new Date(), 'yyyy-MM-dd');
    let sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n';
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';

    // Static routes
    staticRoutes.forEach(route => {
        sitemap += '  <url>\n';
        sitemap += `    <loc>${baseUrl}${route.path}</loc>\n`;
        sitemap += `    <lastmod>${currentDate}</lastmod>\n`;
        sitemap += `    <changefreq>${route.changefreq}</changefreq>\n`;
        sitemap += `    <priority>${route.priority}</priority>\n`;
        sitemap += '  </url>\n';
    });

    // Dynamic routes: futsals
    try {
        const { data: futsals } = await apiClient.get('futsal/list-futsals/');
        for (const futsal of futsals) {
            sitemap += '  <url>\n';
            sitemap += `    <loc>${baseUrl}/futsals/${futsal.id}</loc>\n`;
            sitemap += `    <lastmod>${currentDate}</lastmod>\n`;
            sitemap += '    <changefreq>weekly</changefreq>\n';
            sitemap += '    <priority>0.9</priority>\n';
            sitemap += '  </url>\n';

            sitemap += '  <url>\n';
            sitemap += `    <loc>${baseUrl}/futsals/${futsal.id}/book</loc>\n`;
            sitemap += `    <lastmod>${currentDate}</lastmod>\n`;
            sitemap += '    <changefreq>daily</changefreq>\n';
            sitemap += '    <priority>0.8</priority>\n';
            sitemap += '  </url>\n';
        }
    } catch (error) {
        console.error('Failed to fetch futsals:', error.message);
    }

    // Dynamic routes: blogs
    try {
        const { data: blogs } = await apiClient.get('blog/list-blogs/');
        for (const blog of blogs) {
            sitemap += '  <url>\n';
            sitemap += `    <loc>${baseUrl}/blog/${blog.id}</loc>\n`;
            sitemap += `    <lastmod>${blog.updated_at || currentDate}</lastmod>\n`;
            sitemap += '    <changefreq>weekly</changefreq>\n';
            sitemap += '    <priority>0.7</priority>\n';
            sitemap += '  </url>\n';
        }
    } catch (error) {
        console.error('Failed to fetch blogs:', error.message);
    }

    sitemap += '</urlset>';

    try {
        await writeFile('./public/sitemap.xml', sitemap, { encoding: 'utf8', flag: 'w' });
        console.log('Sitemap generated at ./public/sitemap.xml');
    } catch (error) {
        console.error('Error saving sitemap:', error.message);
    }
}

generateSitemap().catch(err => console.error('Sitemap generation failed:', err));
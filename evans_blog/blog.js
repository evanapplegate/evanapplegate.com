document.addEventListener('DOMContentLoaded', async () => {
  // List of posts (will be auto-generated or manually updated)
  const posts = [
    { title: 'ML has killed “looks okay from arm’s length” cartography', file: 'posts/ML_killed_carto.md' },
    { title: 'When Danielle Baskin took a romanesco broccoli to the 3D printing conf...', file: 'posts/baskin.md' },
    { title: 'The soft end of something sharp', file: 'posts/bedside_nursing.md' },
    { title: 'The Best Maps Lie Ahead', file: 'posts/best_maps_lie_ahead.md' },
    { title: 'Computer-mediated cartographer bestiary', file: 'posts/bestiary_part_1.md' },
    { title: 'Get me some computer rurality', file: 'posts/computer_rurality.md' },
    { title: '“COVID response” was the nuttiest event of my lifetime and I’m going to die mad about it', file: 'posts/covid.md' },
    { title: 'My least favorite ten thousand words', file: 'posts/evans_thesis_notes.md' },
    { title: 'Have you heard about our painfully loud speaker as a service?', file: 'posts/genasys.md' },
    { title: 'Cartographic graduate education at the University of Wisconsin–Madison, 2014–2017', file: 'posts/grad_school.md' },
    { title: '365 days of great ideas for your map business', file: 'posts/great_map_ideas.md' },
    { title: 'What I’ve learned during 14 years of mapmaking', file: 'posts/map_tips.md' },
    { title: 'The mapmaker’s terrible hand', file: 'posts/mapmakers_terrible_hand.md' },
    { title: 'More men eases eldercare', file: 'posts/men_eldercare.md' },
    { title: '2060: 62 million old, lonely, broke millennials', file: 'posts/millenials_old.md' },
    { title: 'Podcasting tips', file: 'posts/podcast_tips.md' },
    { title: 'Making a public lands explorer map', file: 'posts/public_lands_map.md' },
    { title: 'Shoutout machine learning', file: 'posts/shoutout_ML.md' },
    { title: 'Low-pressure sodium lamp salvage', file: 'posts/sodium.md' },
    { title: 'The American Hospital: Trying to Heal in Someone’s Workplace', file: 'posts/trying_to_heal_in_a_workplace.md' }
  ];
  
  // Track current post index
  let currentPostIndex = 0;
  
  // Populate sidebar navigation
  const postList = document.getElementById('post-list');
  posts.forEach(post => {
    const listItem = document.createElement('li');
    listItem.style.listStyleType = 'none';
    const link = document.createElement('a');
    link.href = '#';
    link.textContent = post.title;
    link.addEventListener('click', (e) => {
      e.preventDefault();
      loadPost(post.file);
    });
    listItem.appendChild(link);
    postList.appendChild(listItem);
  });
  
  // Set up navigation buttons
  const prevButton = document.getElementById('prev-post');
  const nextButton = document.getElementById('next-post');
  
  prevButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (currentPostIndex > 0) {
      loadPost(posts[currentPostIndex - 1].file);
    }
  });
  
  nextButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (currentPostIndex < posts.length - 1) {
      loadPost(posts[currentPostIndex + 1].file);
    }
  });
  
  // Update navigation buttons based on current post
  function updateNavigation() {
    prevButton.style.visibility = currentPostIndex > 0 ? 'visible' : 'hidden';
    nextButton.style.visibility = currentPostIndex < posts.length - 1 ? 'visible' : 'hidden';
  }

  // Load a post
  async function loadPost(file) {
    try {
      // Scroll to top of the page when loading a new post
      window.scrollTo(0, 0);
      
      const response = await fetch(file);
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      const markdown = await response.text();
      
      // Convert markdown to HTML. Posts reference media as /images/... or ../images/...;
      // point those at this folder's images/ so the blog works from whatever path it is served at.
      const html = marked.parse(markdown).replace(/(src|href)="(?:\.\.\/|\/)(images\/)/g, '$1="$2');
      document.getElementById('post-content').innerHTML = html;
      
      // Update URL hash
      window.location.hash = file;
      
      // Handle images
      document.querySelectorAll('#post-content img').forEach(img => {
        if (!img.src.startsWith('http')) {
          const postDir = file.substring(0, file.lastIndexOf('/'));
          img.src = `${postDir}/${img.getAttribute('src')}`;
        }
      });
      
      // Update current post index
      currentPostIndex = posts.findIndex(post => post.file === file);
      updateNavigation();
    } catch (error) {
      console.error('Error loading post:', error);
      document.getElementById('post-content').innerHTML = `<h1>Error</h1><p>Failed to load post: ${error.message}</p>`;
    }
  }
  
  // Load post from URL hash on page load
  if (window.location.hash) {
    const postFile = window.location.hash.substring(1);
    loadPost(postFile);
  } else if (posts.length > 0) {
    // Load the first post by default
    loadPost(posts[0].file);
  }
});
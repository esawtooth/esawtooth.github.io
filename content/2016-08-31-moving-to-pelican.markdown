Title: Moving to Pelican
Slug: blog-v3
Date: 2016-08-31 11:44
Category: tech
Tags: blog tech
Author: Rohit Jain

Sadly, I seem to be blogging more about how I've been shifting the shape of my blog than on anything else. Anyhow, this change seems significant enough, so I guess I might as well continue in the same vein and make a mention of it. I got bored with the [Jekyll](https://jekyllrb.com/) thing I had been doing in the past. Besides I much prefer python to ruby. So I ended up moving the whole thing over to [pelican](blog.getpelican.com). More interestingly, I was able to hook up the excellent [pelican-ipynb](https://github.com/danielfrg/pelican-ipynb) plugin to compile my Jupyter IPython notebooks to blog posts. It should give me more avenues to write since jupyter notebooks are things I create fairly often. 

Another interesting thing I did was to hook up the entire blog generation logic in [travis-ci](https://travis-ci.org/), so I don't need to install or maintain the generation environment. A simple git push of my notebooks or blog posts will eventually end up on the blog, which is pretty neat. The only thing that irritates me a bit about this is the ~3minute lag in publishing as travis regenerates the entire build environment over and over again. Cacheing the pip packages required speeded up the build a bit, but even so, that can get annoying if one is fixing something small and wants instant gratification. I really should fix that up with some post commit hooks on my local machine where I blog from, and keep the travis thing going for a rainy day if I mess up my environment.

On another note, the container thing the folks at travis are doing is pretty neat. The techology is finding more takers and it is good to see that what a product person might naively call a "better virtual machine", has had considerable impact on the business of software development and deployment. I really ought to check out [kubernetes](kubernetes.io/) one of these days and see what Google has been up to with its [container engine](https://cloud.google.com/container-engine/). The last time I looked at it was when it was in beta and lots of things did not simply join up cleanly. It really seems to have matured in the past year.

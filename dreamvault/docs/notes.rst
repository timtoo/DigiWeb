Dream Vaults
============

Design Principles:
------------------

- Easy recording of dreams (obviously)
- Detailed classification mechanisms available
- Various levels of anonymity when desired for privacy
    - partial anonymity masks names of people and places (and
      relationship)
    - full anonymity masks names of people and places and does not
      identify dream with author's account
- Social network elements (follow, friend)
- Social login (facebook/google, etc)
- Dream comments
- integration with other social networks (for login & sharing)
- API so apps can be created for other platforms
- Analysis features
    - dream search engine
    - tag/mood/reaction analysis
    - similar dreams
- General discussion threads (probably third party hosted)

Data Design
-----------



Dream:
    - date entered
    - date of dream
    - anonymous (not attached to account)

Characters:
    - name
    - gender
    - birth date / age
    - bio
    - always anonymous (even in non-anonymous posts)
    - anonymouse name (optional, else randomly chosen)

dream vividness: scale
dream author rating: scale (how much dream was liked)
dream reader rating: scale

reaction/reception: negative-positive scale

emotion classification: (negative_positive)
    - possitive
    - negative
    - neutral

dream type tags:
    - anxiety
    - erotic
    - observatory
    - memory
    - lesson

dream mood tags:
    - happy
    - sad
    - excited
    - loved
    - terror
    - neutral

Future Ideas
------------
- dream art (attach media)
- facebook integration
- other social media integration
- native mobile apps and/or mobile specific web interface



Dream Vaults
============

Design Goals:
------------------

- Easy recording of dreams (obviously)
- Detailed classification mechanisms available (via tags & ratings)
- Various **levels of anonymity** when desired for privacy
    - private: content can not be seen by anyone except user
    - full: content can be seen/searched (with text substitutions) but is not linked to any user
    - alias: content can be seen/searched (with text substitutions), is linked to a persona
    - public: content can be seen/searched (no text subtitutions), and is linked to main user persona
- Social login (facebook/google, etc)
- Dream commentary
- Social network elements (follow, friend)
- Integration with other social networks (for login & sharing)
- (internal) API so apps can be created for other platforms
- Text analysis features
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

dream vividness: scale
dream author rating: scale (how much dream was liked)
dream reader rating: scale

reaction/perception: negative-positive scale

emotion classification: (negative_positive)
    - positive
    - negative
    - neutral

dream type tags:
    - anxiety
    - erotic
    - observing
    - memory
    - lesson
    - precient

dream mood tags:
    - happy
    - sad
    - excited
    - loved
    - terror
    - neutral

Original Overly Complciated Design
----------------------------------

When first concieved, there was the idea that a user could define a lot of very
specific information, such as lists of locations, names, relationships and so on.
The idea was that the anonymizing system could use this information to intelligently
make substituations where necessary. For example, if a location is identified then
an anonymized version of the location would be used. These sorts of classifed tags
could also be used for organization and data mining purposes.

Coming back to this after a long absense, this scheme seems insanely complicated.
So a new scheme of simple optional generic alias lists will be used instead.

A global alias list which can be applied to all text marked anonymous can be defined,
as well as a local alias list which can be appended to each individual dream. Local,
of course, overrides any matching global aliases.



Future Ideas
------------
- dream art (attach media)
- facebook integration
- other social media integration
- native mobile apps and/or mobile specific web interface
- anonymity level: friends. Friends are able to see all non-private dreams linked to user




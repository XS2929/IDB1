// Overwatchdb Class Diagram

[Hero|id: int; description:text; name: text; affiliation: text; age: text],
[Reward|id: int; name: text; quality: text; cost: text],
[Achievement|id: int; name: text; description: text ; cost: text],
[Player|id: int; name: text; server: text; level: text],

[Player]1..*-1[Hero], 
[Achievement]0..*-0..*[Player], 
[Achievement]0..*-1[Hero],
[Achievement]0..1-1[Reward],
[Reward]0..*-0..*[Player],
[Reward]1..*-0..1[Hero]
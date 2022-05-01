# A lightweight text editor for daily use.
## An essential program that'll insert itself into your routine seamlessly.
>latest: v\_Alpha\_0.1

> still in early stages of development. This will be first written using Python and then ported to C++ for final use.
---
### description
---
### Version naming
All versions are named with this scheme:
>"v"+"\_"+type+"\_"+numbers

"v" stands for "version" here.

type is a way of separating finished products from the versions that still need debugging. It can be either "Alpha" (used only before 1.0),"Canary"(slight tweaks needed but still usable),"Goose"(both) or "Release"(finished)

numbers is the version numbers. according to the size of the changes you increment a different number.
valid increment examples include:  
"0.2.3"->"0.3" (major changes made),  
"0.9"->"0.10" (),  
"0.18"->"1",  
"1"->"1.0.1"

When asking to merge your changes, make sure to change the version name to your liking, for example:

it's a finished version:    
v\_Canary\_2.3.3 --> v\_Release\_2.3.3

most of the changes you need for the next version are there, but there's still some bugs to iron out:    
v\_Release\_2.3.2 --> v\_Canary\_2.3.3,  
v\_Release\_2.3.2 --> v\_Canary\_2.3.2.1

for releases before v\_Release\_1:    
v\_Alpha\_0.6.4 --> v\_Alpha\_0.7,  
v\_Alpha\_0.9.2 --> v\_Goose\_0.10,  
v\_Alpha\_0.12.0--> v\_Canary\_1

note: you can also include the previous version in parentheses for clarity:    
v\_Canary\_1.2.1 (previous: v\_Release\_1.2)

All versions (**including Canary**) have to be properly tested, reviewed and the version label must be accordingly changed before being added to the version history

---
### Development notes, don't copy
#### Alpha 0.1 checklist
##### expected date of release: end may 2022
>working prototype that can read and write to files seamlessly through its GUI

>rough plan of infrastructure

**started in late April 2022. finished in the future**
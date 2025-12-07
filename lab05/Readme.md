
## What I did
- Created a test group `students`. 
- Created user `student2` with home directory. 
- Added `student2` to `students`. 
- Verified group membership with `id` and `groups`.
- Tested login with `su - student2`. 
- Removed user `student2`. 

## Commands used
- `sudo groupadd students` 
- `sudo adduser student2` 
- `sudo usermod -aG students student2` 
- `id student2`, `groups student2` 
- `su - student2` 


EOF 





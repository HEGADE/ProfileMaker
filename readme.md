# Profile maker

## it takes a github use name as argument and generate a pdf profile from it 

## Running the app
```bash
cd profile
python main.py github_username

```
### profile pdf will be saved in profile directory it self

## Note : I'm not using github api for extracting data,I'm using bs4 for doing that,and if your profile contains some emoji ,that time ,created pdf will get some garbage text(it's problem of pdf formatter). Fix for these things will be provided very soon



# Sea For Haifa
## Before deploy
1) Run:
- `pip install -r requirements`
- `npm i`
- `npm run buildcss`
- `pybabel compile -d src/translations`
2) Create *.env*
## Restarting
1) Rebuild frontend:
`npm run buildcss`
2) Restart backend:
`systemctl restart sea.service`

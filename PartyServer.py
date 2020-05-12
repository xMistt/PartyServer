import sanic

app = sanic.Sanic(name="PartyServer")


@app.route("/account/api/oauth/token", methods=["POST", ])
async def token(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    return sanic.response.json(
        {
            "access_token": "eg1~ACCESS_TOKEN",
            "expires_in": 28800,
            "expires_at": "9999-12-31T23:59:59.999Z",
            "token_type": "bearer",
            "refresh_token": "REFRESH_TOKEN",
            "refresh_expires": 28800,
            "refresh_expires_at": "9999-12-31T23:59:59.999Z",
            "account_id": "ACCOUNT_ID",
            "client_id": "CLIENT_ID",
            "internal_client": True,
            "client_service": "fortnite",
            "app": "fortnite",
            "in_app_id": "ACCOUNT_ID"
        },
        status=200
    )


@app.route("/waitingroom/api/waitingroom")
async def waiting_room(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    return sanic.response.text(
        "",
        status=204
    )


@app.route("account/api/oauth/sessions/kill", methods=["DELETE", ])
async def kill_token(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    return sanic.response.text(
        "",
        status=204
    )


@app.route("/account/api/public/account/<account_id>")
async def account_lookup(request: sanic.request.Request, account_id) -> sanic.response.HTTPResponse:
    return sanic.response.json(
        {
            "id": account_id,
            "displayName": "PARTYSERVER",
            "name": "PARTYSERVER",
            "email": "PARTYSERVER@gmail.com",
            "failedLoginAttempts": 0,
            "lastLogin": "2020-05-11T21:14:12.698Z",
            "numberOfDisplayNameChanges": 0,
            "ageGroup": "UNKNOWN",
            "headless": False,
            "country": "GB",
            "lastName": "PARTYSERVER",
            "preferredLanguage": "en",
            "canUpdateDisplayName": True,
            "tfaEnabled": False,
            "emailVerified": True,
            "minorVerified": False,
            "minorExpected": False,
            "minorStatus": "UNKNOWN"
        },
        status=200
    )


@app.route("/account/api/public/account/<account_id>/externalAuths")
async def external_auths(request: sanic.request.Request, account_id) -> sanic.response.HTTPResponse:
    return sanic.response.json(
        [],
        status=200
    )


@app.route("/fortnite/api/game/v2/tryPlayOnPlatform/account/<account_id>", methods=["POST", ])
async def platform_check(request: sanic.request.Request, account_id: str) -> sanic.response.HTTPResponse:
    return sanic.response.text(
        True,
        status=200
    )


@app.route("lightswitch/api/service/bulk/status")
async def server_status(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    return sanic.response.json(
        [
            {
                "serviceInstanceId": "fortnite",
                "status": "UP",
                "message": "Up",
                "maintenanceUri": None,
                "overrideCatalogIds": [
                    "a7f138b2e51945ffbfdacc1af0541053"
                ],
                "allowedActions": [
                    "PLAY",
                    "DOWNLOAD"
                ],
                "banned": False,
                "launcherInfoDTO": {
                    "appName": "Fortnite",
                    "catalogItemId": "4fe75bbc5a674f4f9b356b5c90567da5",
                    "namespace": "fn"
                }
            }
        ],
        status=200
    )


@app.route("/fortnite/api/game/v2/enabled_features")
async def enabled_features(request: sanic.request.Request) -> sanic.response.HTTPResponse:
    return sanic.response.json(
        [],
        status=200
    )


@app.route("fortnite/api/cloudstorage/user/<account_id>")
async def cloudstorage(request: sanic.request.Request, account_id) -> sanic.response.HTTPResponse:
    return sanic.response.json(
        [],
        status=200
    )


app.run(host="0.0.0.0", port="80")

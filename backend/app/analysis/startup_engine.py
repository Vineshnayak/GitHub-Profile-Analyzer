def startup_readiness_analysis(repositories):

    deployment_detected = False

    ci_cd_detected = False

    for repo in repositories:

        repo_text = str(repo)

        if "vercel" in repo_text.lower():
            deployment_detected = True

        if "github actions" in repo_text.lower():
            ci_cd_detected = True

    score = 50

    if deployment_detected:
        score += 25

    if ci_cd_detected:
        score += 25

    return {
        "startup_readiness_score": score,

        "deployment_detected":
            deployment_detected,

        "ci_cd_detected":
            ci_cd_detected
    }

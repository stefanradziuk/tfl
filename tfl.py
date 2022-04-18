import json
import sys
import urllib.request
import urllib.parse


SEVERITY_GOOD_SERVICE = 10
STATUS_URL = "https://tfl.gov.uk/tube-dlr-overground/status/"


def main():
    lines = ["circle", "district"]
    lines_enc = urllib.parse.quote(",".join(lines))
    with urllib.request.urlopen(
        f"https://push-api.tfl.gov.uk/Line/{lines_enc}/Status?detail=true"
    ) as resp_raw:
        resp = json.load(resp_raw)

        all_good = True

        for line in resp:
            for status in line["lineStatuses"]:
                severity = status["statusSeverity"]
                all_good &= severity == SEVERITY_GOOD_SERVICE

                print(f"{line['name']}: {status['statusSeverityDescription']}")

                if (disruption := status.get("disruption")) is not None:
                    if (description := disruption.get("description")) is not None:
                        print(description)

        print(f"More information at {STATUS_URL}")

        return all_good


if __name__ == "__main__":
    all_good = main()
    sys.exit(0 if all_good else 1)

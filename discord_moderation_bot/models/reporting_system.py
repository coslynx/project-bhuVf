# reporting_system.py (Python)

class ReportingSystem:
    def __init__(self):
        self.reports = []

    def add_report(self, report):
        self.reports.append(report)
        print(f"Report added: {report}")

    def remove_report(self, report_id):
        for report in self.reports:
            if report["id"] == report_id:
                self.reports.remove(report)
                print(f"Report removed: {report_id}")
                return
        print(f"Report with id {report_id} not found")

    def get_reports(self):
        return self.reports

    def clear_reports(self):
        self.reports = []
        print("All reports cleared")


# End of reporting_system.py
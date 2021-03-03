from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs


def get_jobs(word):
    indeed_jobs = get_indeed_jobs(word)
    so_jobs = get_so_jobs(word)
    jobs = so_jobs + indeed_jobs
    return jobs

# UI English to Somali Translation Guide

This document contains all user-visible English text from the Exam System, organized by module, with suggested Somali translations for internationalization.

---

## Table of Contents

- [Dashboard Module](#dashboard-module)
- [Students Module](#students-module)
- [Teachers Module](#teachers-module)
- [Invigilators Module](#invigilators-module)
- [Classes Module](#classes-module)
- [Subjects Module](#subjects-module)
- [Exams Module](#exams-module)
- [Results Module](#results-module)
- [Attendance Module](#attendance-module)
- [Settings Module](#settings-module)
- [ID Cards Module](#id-cards-module)
- [Incidents Module](#incidents-module)
- [Public Pages Module](#public-pages-module)
- [Audit Module](#audit-module)
- [Analytics Module](#analytics-module)
- [Academic Structure Module](#academic-structure-module)
- [Login & Authentication Module](#login--authentication-module)

---

## Dashboard Module

### Admin Dashboard

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Dashboard | Dhismaha | app/templates/admin/base.html | 24 | Sidebar menu item |
| Academic & Results | Akademics & Natiijooyin | app/templates/admin/base.html | 25 | Sidebar menu item |
| Results | Natiijooyin | app/templates/admin/base.html | 26 | Sidebar menu item |
| Teacher Department | Waaxda Macalimiinta | app/templates/admin/base.html | 27 | Sidebar menu item |
| Attendance | Dhexdhexaad | app/templates/admin/base.html | 28 | Sidebar menu item |
| ID Cards | Baasaboorta | app/templates/admin/base.html | 29 | Sidebar menu item |
| Exam Invigilators | Rukhsadaha Imtixaanka | app/templates/admin/base.html | 30 | Sidebar menu item |
| Incident Reports | Warbixininta Dhacdada | app/templates/admin/base.html | 31 | Sidebar menu item |
| Incident Settings | Dejinta Dhacdada | app/templates/admin/base.html | 32 | Sidebar menu item |
| Users | Isticmaalayaasha | app/templates/admin/base.html | 33 | Sidebar menu item |
| Settings | Dejinta | app/templates/admin/base.html | 34 | Sidebar menu item |
| Audit Log | Qoraalka Baaritaanka | app/templates/admin/base.html | 35 | Sidebar menu item |
| Logout | Ka bax | app/templates/admin/base.html | 50 | Logout button |
| Somali | Soomaali | app/templates/admin/base.html | 44 | Language option |
| English | English | app/templates/admin/base.html | 45 | Language option |
| Arabic | Carabi | app/templates/admin/base.html | 46 | Language option |
| Turkish | Turkish | app/templates/admin/base.html | 47 | Language option |
| Secure Admin Workspace | Goob Admin oo Nadiif ah | app/templates/admin/base.html | 48 | Page header |
| Dashboard | Dhismaha | app/templates/admin/dashboard.html | 2 | Page title |
| Total Students | Wadarta Ardayda | app/templates/admin/dashboard.html | 8 | Dashboard card label |
| Total Classes | Wadarta Fasallada | app/templates/admin/dashboard.html | 9 | Dashboard card label |
| Total Exams | Wadarta Imtixaanka | app/templates/admin/dashboard.html | 10 | Dashboard card label |
| Published | La daah-furay | app/templates/admin/dashboard.html | 11 | Dashboard card label |
| Subjects | Maadooyinka | app/templates/admin/dashboard.html | 12 | Dashboard card label |
| Locked Results | Natiijooyin la xiray | app/templates/admin/dashboard.html | 13 | Dashboard card label |
| Statistics | Xisaab-yada | app/templates/admin/dashboard.html | 15 | Section heading |
| Activity Timeline | Waqtiga Dhaqanka | app/templates/admin/dashboard.html | 16 | Section heading |
| Recent Results | Natiijooyin Dhow | app/templates/admin/dashboard.html | 17 | Section heading |
| Student | Arday | app/templates/admin/dashboard.html | 39 | Table header |
| Exam | Imtixaan | app/templates/admin/dashboard.html | 39 | Table header |
| Subject | Maado | app/templates/admin/dashboard.html | 39 | Table header |
| Score | Dhibcaha | app/templates/admin/dashboard.html | 39 | Table header |
| Status | Xaalada | app/templates/admin/dashboard.html | 39 | Table header |
| Published | La daah-furay | app/templates/admin/dashboard.html | 41 | Status label |
| Hidden | Loo qarxay | app/templates/admin/dashboard.html | 42 | Status label |
| No recent activity yet. | Weli dhaqan dhow ah ma jiro. | app/templates/admin/dashboard.html | 43 | Empty state message |
| No results yet. | Weli natiijo ma jiro. | app/templates/admin/dashboard.html | 44 | Empty state message |

### Results Dashboard

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Results Dashboard | Dhismaha Natiijooyinka | app/templates/admin/results_dashboard.html | 3, 4, 13 | Page title and heading |
| Guudmarka | Guudmarka | app/templates/admin/results_dashboard.html | 12 | Eyebrow label |
| Sanad Dugsiyeedka | Sanadka Dugsiga | app/templates/admin/results_dashboard.html | 18 | Selector label |
| Auto | Otomaatig | app/templates/admin/results_dashboard.html | 18 | Auto pill label |
| Active | Firfircoon | app/templates/admin/results_dashboard.html | 23 | Status pill |
| Archived | Kaydsan | app/templates/admin/results_dashboard.html | 23 | Status pill |
| Exam Type | Nooca Imtixaanka | app/templates/admin/results_dashboard.html | 29 | Selector label |
| Dooro imtixaan | Dooro imtixaanka | app/templates/admin/results_dashboard.html | 31 | Select placeholder |
| Dashboard-ku wuxuu si otomaatig ah u soo bandhigayaa sanadka dugsiyeedka ee active-ka ah — waad iska bedeli kartaa si aad u eegto sano hore. | Dhismuhu wuxuu si otomaatig ah u soo bandhigayaa sanadka dugsiyeedka ee firfircoonka ah — waad iska bedeli kartaa si aad u eegto sano hore. | app/templates/admin/results_dashboard.html | 38 | Auto note |
| Revert to Active | Noqo Firfircoon | app/templates/admin/results_dashboard.html | 40 | Revert button |
| Wadarta Ardayda | Wadarta Ardayda | app/templates/admin/results_dashboard.html | 47 | Stat label |
| Maadooyinka la Xareeyay | Maadooyinka la Xareeyay | app/templates/admin/results_dashboard.html | 51 | Stat label |
| Buuxinta Natiijooyinka | Buuxinta Natiijooyinka | app/templates/admin/results_dashboard.html | 55 | Stat label |
| Fasallada Firfircoon | Fasallada Firfircoon | app/templates/admin/results_dashboard.html | 59 | Stat label |
| Dooro Level | Dooro Heerka | app/templates/admin/results_dashboard.html | 63 | Step label |
| Dooro Fasalka | Dooro Fasalka | app/templates/admin/results_dashboard.html | 72 | Step label |
| arday | arday | app/templates/admin/results_dashboard.html | 77 | Student count label |
| Fasallo lama helin level-ka la doortay. | Fasallo lama helin heerka la doortay. | app/templates/admin/results_dashboard.html | 83 | Empty state |
| Dooro imtixaan si aad u aragto dashboard-ka. | Dooro imtixaanka si aad u aragto dhismaha. | app/templates/admin/results_dashboard.html | 89 | Empty state |

---

## Students Module

### Students Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Wadarta Ardayda | Wadarta Ardayda | app/templates/admin/students_management.html | 2 | Page title |
| Total Students | Wadarta Ardayda | app/templates/admin/students_management.html | 8 | Summary card label |
| Secondary | Dhexe | app/templates/admin/students_management.html | 9 | Summary card label |
| Upper Primary | Sare | app/templates/admin/students_management.html | 10 | Summary card label |
| Lower Primary | Hoose | app/templates/admin/students_management.html | 11 | Summary card label |
| Kindergarten | Dugsiga Hore | app/templates/admin/students_management.html | 12 | Summary card label |
| Active Students | Ardayda Firfircoona | app/templates/admin/students_management.html | 13 | Summary card label |
| Sanad Dugsiyeedka | Sanadka Dugsiga | app/templates/admin/students_management.html | 18 | Filter label |
| Level | Heer | app/templates/admin/students_management.html | 19 | Filter label |
| Dhammaan | Dhammaan | app/templates/admin/students_management.html | 20 | Filter option (All) |
| Fasalka | Fasalka | app/templates/admin/students_management.html | 21 | Filter label |
| Xaalada | Xaalada | app/templates/admin/students_management.html | 22 | Filter label |
| Raadi arday (magac, ID)... | Raadi arday (magac, ID)... | app/templates/admin/students_management.html | 23 | Search placeholder |
| Cali Arday Cusub | Ku dar Arday Cusub | app/templates/admin/students_management.html | 26 | Button label |
| Template | Template-ka | app/templates/admin/students_management.html | 27 | Button label |
| Excel Import | Soojiinta Excel | app/templates/admin/students_management.html | 28 | Button label |
| Excel Export | Dhoofinta Excel | app/templates/admin/students_management.html | 29 | Button label |
| Previous | Hore | app/templates/admin/students_management.html | 31 | Pagination button |
| Next | Xiga | app/templates/admin/students_management.html | 32 | Pagination button |
| Page X of Y (Z students) | Boggax X Y (Z arday) | app/templates/admin/students_management.html | 33 | Pagination text |
| Select | Dooro | app/templates/admin/students_management.html | 38 | Table header |
| ID | ID | app/templates/admin/students_management.html | 39 | Table header |
| Name | Magac | app/templates/admin/students_management.html | 40 | Table header |
| Class | Fasal | app/templates/admin/students_management.html | 41 | Table header |
| Level | Heer | app/templates/admin/students_management.html | 42 | Table header |
| Section | Qayb | app/templates/admin/students_management.html | 43 | Table header |
| Dooro arday | Dooro arday | app/templates/admin/students_management.html | 44 | Action label |
| Guji arday si aad u eegto faahfaahinta | Guji arday si aad u eegto faahfaahinta | app/templates/admin/students_management.html | 45 | Action label |
| Student Code | Tirada Ardayda | app/templates/admin/students_management.html | 50 | Form label |
| Full Name | Magac oo dhan | app/templates/admin/students_management.html | 51 | Form label |
| Mother's Name | Magaca Hooyada | app/templates/admin/students_management.html | 52 | Form label |
| Phone | Telifoon | app/templates/admin/students_management.html | 53 | Form label |
| Macluumaadka Dugsiyeedka | Macluumaadka Dugsiyeedka | app/templates/admin/students_management.html | 54 | Section heading |
| Kaydi | Kaydi | app/templates/admin/students_management.html | 55 | Button label |
| Promote to Next Class | U dhis Fasalka Xiga | app/templates/admin/students_management.html | 56 | Button label |
| No classes found. | Fasallo lama helin. | app/templates/admin/students_management.html | 57 | Empty state |
| No students found. | Arday lama helin. | app/templates/admin/students_management.html | 58 | Empty state |
| Locked | La xiray | app/templates/admin/students_management.html | 59 | Status label |
| Active | Firfircoon | app/templates/admin/students_management.html | 60 | Status label |

### Student Form

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Edit Student | Tifatir Arday | app/templates/admin/student_form.html | 2 | Page title |
| Add Student | Ku dar Arday | app/templates/admin/student_form.html | 3 | Page title |
| Student Profile | Faahfaahinta Ardayda | app/templates/admin/student_form.html | 6 | Section heading |
| Student ID | Tirada Ardayda | app/templates/admin/student_form.html | 8 | Form label |
| Full Name | Magac oo dhan | app/templates/admin/student_form.html | 9 | Form label |
| Mother Name | Magaca Hooyada | app/templates/admin/student_form.html | 10 | Form label |
| Phone Number | Lambarka Telifoonka | app/templates/admin/student_form.html | 11 | Form label |
| Academic Year | Sanadka Dugsiga | app/templates/admin/student_form.html | 12 | Form label |
| Academic Level | Heerka Akademicska | app/templates/admin/student_form.html | 13 | Form label |
| Class | Fasal | app/templates/admin/student_form.html | 14 | Form label |
| Section | Qayb | app/templates/admin/student_form.html | 15 | Form label |
| Student Photo | Sawirka Ardayda | app/templates/admin/student_form.html | 16 | Form label |
| Special Comment | Faallo gaar ah | app/templates/admin/student_form.html | 17 | Form label |
| Lock Reason | Sababta Xirista | app/templates/admin/student_form.html | 18 | Form label |
| Lock Result | Xir Natiijada | app/templates/admin/student_form.html | 19 | Form label |
| Active Student | Arday Firfircoon | app/templates/admin/student_form.html | 20 | Form label |
| Save Student | Kaydi Ardayda | app/templates/admin/student_form.html | 21 | Button label |
| Incident History | Taariikhda Dhacdada | app/templates/admin/student_form.html | 22 | Section heading |
| Recent examination incident reports for this student. | Warbixinno dhacdada imtixaanka dhow ah ardaydan. | app/templates/admin/student_form.html | 23 | Section description |
| Report # | Warbixin # | app/templates/admin/student_form.html | 24 | Table header |
| Category | Qayb | app/templates/admin/student_form.html | 25 | Table header |
| Severity | Xad dhaafka ah | app/templates/admin/student_form.html | 26 | Table header |
| Date | Taariikh | app/templates/admin/student_form.html | 27 | Table header |
| Status | Xaalada | app/templates/admin/student_form.html | 28 | Table header |
| Actions | Dhaqaaqyo | app/templates/admin/student_form.html | 29 | Table header |
| Pending Review | La eegayaa | app/templates/admin/student_form.html | 30 | Status label |
| Under Investigation | La baarayaa | app/templates/admin/student_form.html | 31 | Status label |
| Resolved | La xaliyay | app/templates/admin/student_form.html | 32 | Status label |
| Rejected | La diiday | app/templates/admin/student_form.html | 33 | Status label |
| View Details | Eeg Faahfaahinta | app/templates/admin/student_form.html | 34 | Action label |
| View All Incidents | Eeg Dhacdada Dhammaan | app/templates/admin/student_form.html | 35 | Link label |
| No photo uploaded | Sawir lama soo saaray | app/templates/admin/student_form.html | 36 | Empty state |
| Photo saved | Sawir la kaydiyay | app/templates/admin/student_form.html | 37 | Success message |

---

## Teachers Module

### Teacher Portal

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Teacher Portal | Portal-ka Macalimiinta | app/templates/teacher/login.html | 9 | Login page eyebrow |
| School | Dugsiga | app/templates/teacher/login.html | 10 | School name placeholder |
| Sign in to view your classes, students, and examination results. | Ku soo gudub si aad u aragto fasalladaaga, ardayda, iyo natiijooyinka imtixaanka. | app/templates/teacher/login.html | 11 | Login description |
| Username | Magaca isticmaalka | app/templates/teacher/login.html | 12 | Form label |
| Password | Ereyga sirta ah | app/templates/teacher/login.html | 13 | Form label |
| Sign In | Ku soo gudub | app/templates/teacher/login.html | 14 | Button label |
| Forgot password? | Ereyga sirta ah way baabtay? | app/templates/teacher/login.html | 15 | Link label |
| Administrators should use the admin login. | Maamulayaasha waa inay isticmaalaan login-ka maamulka. | app/templates/teacher/login.html | 16 | Help text |

### Teacher Dashboard

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Total Exams | Wadarta Imtixaanka | app/templates/teacher/dashboard.html | 8 | Stat label |
| Exams created | Imtixaan la abuuray | app/templates/teacher/dashboard.html | 10 | Stat subtitle |
| Students Took Latest Exam | Ardayda Imtixaanka Ugu Dhow | app/templates/teacher/dashboard.html | 17 | Stat label |
| % of total | % wadarta | app/templates/teacher/dashboard.html | 19 | Stat subtitle |
| Students Passed | Ardayda La Xaliyay | app/templates/teacher/dashboard.html | 26 | Stat label |
| % pass rate | % heerka guulaha | app/templates/teacher/dashboard.html | 28 | Stat subtitle |
| Students Failed | Ardayda La Guuldareyay | app/templates/teacher/dashboard.html | 35 | Stat label |
| % fail rate | % heerka guuldareyska | app/templates/teacher/dashboard.html | 37 | Stat subtitle |
| Students Absent | Ardayda Joogay | app/templates/teacher/dashboard.html | 44 | Stat label |
| % absent rate | % heerka joogitaanka | app/templates/teacher/dashboard.html | 46 | Stat subtitle |
| Class Performance Overview | Faahfaahinta Wada-shaqada Fasalka | app/templates/teacher/dashboard.html | 54 | Section heading |
| Top Performing | Ugu Fiican | app/templates/teacher/dashboard.html | 62 | Column heading |
| Average Performing | Dhexdhexaad | app/templates/teacher/dashboard.html | 79 | Column heading |
| Low Performing | Ugu Xumaa | app/templates/teacher/dashboard.html | 97 | Column heading |
| No data available | Macluumaad lama helin | app/templates/teacher/dashboard.html | 71, 89, 107 | Empty state |
| Recent Exams | Imtixaanada Dhow | app/templates/teacher/dashboard.html | 119 | Card heading |
| Exam Name | Magaca Imtixaanka | app/templates/teacher/dashboard.html | 124 | Table header |
| Class | Fasal | app/templates/teacher/dashboard.html | 125 | Table header |
| Subject | Maado | app/templates/teacher/dashboard.html | 126 | Table header |
| Average | Dhexdhexaad | app/templates/teacher/dashboard.html | 127 | Table header |
| Date | Taariikh | app/templates/teacher/dashboard.html | 128 | Table header |
| Status | Xaalada | app/templates/teacher/dashboard.html | 129 | Table header |
| Published | La daah-furay | app/templates/teacher/dashboard.html | 138 | Status label |
| Draft | Qorshaha | app/templates/teacher/dashboard.html | 138 | Status label |
| No recent exams | Imtixaan dhow ah ma jiro | app/templates/teacher/dashboard.html | 141 | Empty state |
| Top Students | Ardayda Ugu Fiican | app/templates/teacher/dashboard.html | 150 | Card heading |
| No student data available | Macluumaad ardayda lama helin | app/templates/teacher/dashboard.html | 172 | Empty state |
| Exam Analytics | Xisaab-yada Imtixaanka | app/templates/teacher/dashboard.html | 184 | Card heading |
| Excellent | Fiican | app/templates/teacher/dashboard.html | 193 | Legend label |
| Good | Wanaagsan | app/templates/teacher/dashboard.html | 197 | Legend label |
| Average | Dhexdhexaad | app/templates/teacher/dashboard.html | 202 | Legend label |
| Poor | Xun | app/templates/teacher/dashboard.html | 207 | Legend label |
| Fail | Guuldarey | app/templates/teacher/dashboard.html | 212 | Legend label |
| Overall Average | Dhexdhexaad Guud | app/templates/teacher/dashboard.html | 218 | Label |
| Class Average Overview | Faahfaahinta Dhexdhexaadka Fasalka | app/templates/teacher/dashboard.html | 227 | Card heading |
| No class data available | Macluumaad fasalka lama helin | app/templates/teacher/dashboard.html | 240 | Empty state |
| Quick Actions | Dhaqaaqyo Degdeg ah | app/templates/teacher/dashboard.html | 250 | Section heading |
| Create New Exam | Abuur Imtixaan Cusub | app/templates/teacher/dashboard.html | 255 | Action card label |
| Enter Marks | Geli Dhibcaha | app/templates/teacher/dashboard.html | 259 | Action card label |
| View Results | Eeg Natiijooyinka | app/templates/teacher/dashboard.html | 263 | Action card label |
| Generate Report Cards | Abuur Baasaboorta | app/templates/teacher/dashboard.html | 267 | Action card label |
| Exam Analytics | Xisaab-yada Imtixaanka | app/templates/teacher/dashboard.html | 271 | Action card label |
| Question Bank | Bankka Su'aalaha | app/templates/teacher/dashboard.html | 275 | Action card label |
| Student Performance | Wada-shaqada Ardayda | app/templates/teacher/dashboard.html | 279 | Action card label |
| Publish Results | Daah-fur Natiijooyinka | app/templates/teacher/dashboard.html | 283 | Action card label |
| Subject Analysis | Falanqaynta Maaddada | app/templates/teacher/dashboard.html | 287 | Action card label |
| Important Overview | Faahfaahinta Muhiimka ah | app/templates/teacher/dashboard.html | 295 | Section heading |
| Pending Mark Entry | Gelinta Dhibcaha La Sugayo | app/templates/teacher/dashboard.html | 301 | Overview label |
| Awaiting Publication | La Sugayo Daah-furka | app/templates/teacher/dashboard.html | 308 | Overview label |
| Recently Published | La Daah-furay Dhowaan | app/templates/teacher/dashboard.html | 315 | Overview label |
| Students Requiring Support | Ardayda La Baahanayo Taageero | app/templates/teacher/dashboard.html | 322 | Overview label |
| Best Performing Class | Fasalka Ugu Wanaagsan | app/templates/teacher/dashboard.html | 329 | Overview label |
| Lowest Performing Class | Fasalka Ugu Xumaa | app/templates/teacher/dashboard.html | 336 | Overview label |
| Highest Scoring Student | Ardayda Ugu Dhibcaha Badan | app/templates/teacher/dashboard.html | 343 | Overview label |
| Lowest Class Average | Dhexdhexaadka Fasalka Ugu Yar | app/templates/teacher/dashboard.html | 350 | Overview label |

### Teacher Authentication Messages

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| This area is only available to teacher accounts. | Goobtan waa la heli karaa xisaabta macalimiinta oo dhan. | app/routes_teacher_portal.py | 80, 101 | Flash message (danger) |
| Please change your password before continuing. | Fadlan beddel ereyga sirta ah ka hor inta aad sii socoto. | app/routes_teacher_portal.py | 83, 106 | Flash message (warning) |
| You do not have permission to access this feature. | Waxaa lagu ogolayn inaad isticmaasho waxtan. | app/routes_teacher_portal.py | 86 | Flash message (danger) |
| Invalid username or password. | Magaca isticmaalka ama ereyga sirta ah waa khalkhaali ah. | app/teacher_services.py | 386 | Login error message |
| This account is not authorized for the Teacher Portal. | Xisaabtan ma lagu ogolyahay Portal-ka Macalimiinta. | app/teacher_services.py | 389 | Login error message |
| Current password is incorrect. | Ereyga sirta ah hadda waa khalkhaali ah. | app/routes_teacher_portal.py | 138 | Flash message (danger) |
| Passwords do not match. | Ereyada sirta ah ma midba midkaabaan. | app/routes_teacher_portal.py | 144 | Flash message (danger) |
| Password changed successfully. | Ereyga sirta ah waa la beddelay si guul leh. | app/routes_teacher_portal.py | 150 | Flash message (success) |
| You have been logged out. | Waxaad ka baxtay. | app/routes_teacher_portal.py | 112 | Flash message (success) |
| If the account exists, your request has been logged. Please contact your school administrator. | Haddii xisaabta jirto, codsigaaga waa la qabtay. Fadlan la xiriir maamulaha dugsigaaga. | app/routes_teacher_portal.py | 124 | Flash message (success) |
| Settings saved. | Dejinta waa la kaydiyay. | app/routes_teacher_portal.py | 416 | Flash message (success) |
| Password must be at least {min_length} characters. | Ereyga sirta ah waa inuu yahay ugu yaraan {min_length} xaraf. | app/teacher_services.py | 210 | Password validation error |
| Password must include letters and numbers. | Ereyga sirta ah waa inuu ka kooban yahay xaraf iyo tiro. | app/teacher_services.py | 213 | Password validation error |

---

## Invigilators Module

### Invigilator Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Exam Invigilators | Rukhsadaha Imtixaanka | app/templates/admin/base.html | 30 | Sidebar menu item |
| Exam Invigilator Login | Login-ka Rukhsadaha Imtixaanka | app/templates/invigilator/login.html | 191 | Heading |
| Secure access for examination staff | Helitaanka nadiif ah ee shaqaalaha imtixaanka | app/templates/invigilator/login.html | 192 | Description |
| Username | Magaca isticmaalka | app/templates/invigilator/login.html | 208 | Form label |
| Password | Ereyga sirta ah | app/templates/invigilator/login.html | 213 | Form label |
| Show Password | Ereyga Sirta Ah | app/templates/invigilator/login.html | 215 | Checkbox label |
| Remember Login | Xusuusa Login-ka | app/templates/invigilator/login.html | 219 | Checkbox label |
| Login | Ku soo gudub | app/templates/invigilator/login.html | 223 | Button label |
| Forgot Password? | Ereyga Sirta Ah Way Baabtay? | app/templates/invigilator/login.html | 228 | Link label |
| Authorized personnel only. Contact administrator if you need access. | Shaqaale la ogol yahay oo keliya. La xiriir maamulaha haddii aad u baahato helitaanka. | app/templates/invigilator/login.html | 229 | Help text |
| Invigilator ID already exists. | Tirada Rukhsadaha Imtixaanka hore ayaa jirta. | app/routes_admin.py | 1203 | Flash message (danger) |
| Username already exists. | Magaca isticmaalka hore ayaa jirta. | app/routes_admin.py | 1207 | Flash message (danger) |
| Password must be at least {min_length} characters. | Ereyga sirta ah waa inuu yahay ugu yaraan {min_length} xaraf. | app/routes_invigilator.py | 36 | Password validation error |
| Password must contain numbers only. | Ereyga sirta ah waa inuu ka kooban yahay tiro oo keliya. | app/routes_invigilator.py | 38 | Password validation error |
| Password must contain letters only. | Ereyga sirta ah waa inuu ka kooban yahay xaraf oo keliya. | app/routes_invigilator.py | 40 | Password validation error |
| Password must include letters and numbers. | Ereyga sirta ah waa inuu ka kooban yahay xaraf iyo tiro. | app/routes_invigilator.py | 42 | Password validation error |

---

## Classes Module

### Class Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Class Management | Maamulka Fasalka | app/templates/admin/classes.html | 2 | Page title |
| Class Directory | Direktoriyadda Fasalka | app/templates/admin/classes.html | 5 | Section heading |
| Add Class | Ku dar Fasal | app/templates/admin/classes.html | 6 | Section heading |
| Name | Magac | app/templates/admin/classes.html | 8 | Form label |
| Description | Sharaxaad | app/templates/admin/classes.html | 9 | Form label |
| Add Class | Ku dar Fasal | app/templates/admin/classes.html | 10 | Button label |
| Save | Kaydi | app/templates/admin/classes.html | 11 | Button label |
| Delete | Tirtir | app/templates/admin/classes.html | 12 | Button label |
| Name | Magac | app/templates/admin/classes.html | 13 | Table header |
| Description | Sharaxaad | app/templates/admin/classes.html | 14 | Table header |
| Actions | Dhaqaaqyo | app/templates/admin/classes.html | 15 | Table header |
| No classes found. | Fasallo lama helin. | app/templates/admin/classes.html | 16 | Empty state |

### Academic Structure Classes

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Academic Classes | Fasallada Akademicska | app/templates/academic_structure/classes.html | 2 | Page title |
| Academic Classes | Fasallada Akademicska | app/templates/academic_structure/classes.html | 5 | Page heading |
| New Class | Fasal Cusub | app/templates/academic_structure/classes.html | 7 | Button label |
| Level | Heer | app/templates/academic_structure/classes.html | 15 | Table header |
| Class Name | Magaca Fasalka | app/templates/academic_structure/classes.html | 16 | Table header |
| Sort Order | Tartanka | app/templates/academic_structure/classes.html | 17 | Table header |
| Sections | Qaybaha | app/templates/academic_structure/classes.html | 18 | Table header |
| Status | Xaalada | app/templates/academic_structure/classes.html | 19 | Table header |
| Actions | Dhaqaaqyo | app/templates/academic_structure/classes.html | 20 | Table header |
| Active | Firfircoon | app/templates/academic_structure/classes.html | 32 | Status badge |
| Inactive | Fir-fircoona | app/templates/academic_structure/classes.html | 34 | Status badge |
| Delete this class? | Tirtir fasalkan? | app/templates/academic_structure/classes.html | 42 | Confirm dialog |

---

## Subjects Module

### Subject Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Subject Management | Maamulka Maaddada | app/templates/admin/subjects.html | 2 | Page title |
| Subject Directory | Direktoriyadda Maaddada | app/templates/admin/subjects.html | 5 | Section heading |
| Add Subject | Ku dar Maado | app/templates/admin/subjects.html | 6 | Section heading |
| Name | Magac | app/templates/admin/subjects.html | 8 | Form label |
| Max Score | Dhibcaha Ugu Badan | app/templates/admin/subjects.html | 9 | Form label |
| Sort Order | Tartanka | app/templates/admin/subjects.html | 10 | Form label |
| Add Subject | Ku dar Maado | app/templates/admin/subjects.html | 11 | Button label |
| Save | Kaydi | app/templates/admin/subjects.html | 12 | Button label |
| Delete | Tirtir | app/templates/admin/subjects.html | 13 | Button label |
| Name | Magac | app/templates/admin/subjects.html | 14 | Table header |
| Max Score | Dhibcaha Ugu Badan | app/templates/admin/subjects.html | 15 | Table header |
| Order | Tartanka | app/templates/admin/subjects.html | 16 | Table header |
| Actions | Dhaqaaqyo | app/templates/admin/subjects.html | 17 | Table header |
| No subjects found. | Maadooyin lama helin. | app/templates/admin/subjects.html | 18 | Empty state |

---

## Exams Module

### Exam Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Exam Management | Maamulka Imtixaanka | app/templates/admin/exams.html | 2 | Page title |
| Exam Directory | Direktoriyadda Imtixaanka | app/templates/admin/exams.html | 5 | Section heading |
| Create Exam | Abuur Imtixaan | app/templates/admin/exams.html | 6 | Section heading |
| Name | Magac | app/templates/admin/exams.html | 8 | Form label |
| Academic Year | Sanadka Dugsiga | app/templates/admin/exams.html | 9 | Form label |
| Published | La daah-furay | app/templates/admin/exams.html | 10 | Form label |
| Create Exam | Abuur Imtixaan | app/templates/admin/exams.html | 11 | Button label |
| Save | Kaydi | app/templates/admin/exams.html | 12 | Button label |
| Publish or unpublish | Daah-fur ama qar | app/templates/admin/exams.html | 13 | Button label |
| Delete | Tirtir | app/templates/admin/exams.html | 14 | Button label |
| Name | Magac | app/templates/admin/exams.html | 15 | Table header |
| Academic Year | Sanadka Dugsiga | app/templates/admin/exams.html | 16 | Table header |
| Status | Xaalada | app/templates/admin/exams.html | 17 | Table header |
| Actions | Dhaqaaqyo | app/templates/admin/exams.html | 18 | Table header |
| Published | La daah-furay | app/templates/admin/exams.html | 19 | Status label |
| Draft | Qorshaha | app/templates/admin/exams.html | 20 | Status label |
| No exams found. | Imtixaan lama helin. | app/templates/admin/exams.html | 21 | Empty state |

---

## Results Module

### Result Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Result Management | Maamulka Natiijooyinka | app/templates/admin/results.html | 2 | Page title |
| Add or Edit Results | Ku dar ama Tifatir Natiijooyinka | app/templates/admin/results.html | 5 | Section heading |
| Latest Results | Natiijooyinka Ugu Dhow | app/templates/admin/results.html | 6 | Section heading |
| Student | Arday | app/templates/admin/results.html | 8 | Form label |
| Exam | Imtixaan | app/templates/admin/results.html | 9 | Form label |
| Subject | Maado | app/templates/admin/results.html | 10 | Form label |
| Score | Dhibcaha | app/templates/admin/results.html | 11 | Form label |
| Publish these result rows | Daah-fur taxadarahan natiijooyinka | app/templates/admin/results.html | 12 | Checkbox label |
| Save Results | Kaydi Natiijooyinka | app/templates/admin/results.html | 13 | Button label |
| Import Results | Soojiinta Natiijooyinka | app/templates/admin/results.html | 14 | Button label |
| Template | Template-ka | app/templates/admin/results.html | 15 | Link label |
| Export Results | Dhoofinta Natiijooyinka | app/templates/admin/results.html | 16 | Link label |
| Student | Arday | app/templates/admin/results.html | 17 | Table header |
| Exam | Imtixaan | app/templates/admin/results.html | 17 | Table header |
| Subject | Maado | app/templates/admin/results.html | 17 | Table header |
| Score | Dhibcaha | app/templates/admin/results.html | 17 | Table header |
| Published | La daah-furay | app/templates/admin/results.html | 17 | Table header |
| Actions | Dhaqaaqyo | app/templates/admin/results.html | 17 | Table header |
| Yes | Haa | app/templates/admin/results.html | 18 | Status label |
| No | Maya | app/templates/admin/results.html | 19 | Status label |
| Edit Result | Tifatir Natiijada | app/templates/admin/results.html | 20 | Action label |
| Print | Daabac | app/templates/admin/results.html | 21 | Action label |
| Delete | Tirtir | app/templates/admin/results.html | 22 | Action label |
| Add subjects before entering results | Ku dar maadooyin ka hor inta aad gelinayo natiijooyinka | app/templates/admin/results.html | 23 | Help message |
| No results yet. | Weli natiijo ma jiro. | app/templates/admin/results.html | 24 | Empty state |

### Advanced Results

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Advanced Results | Natiijooyinka Sare | app/templates/admin/advanced_results.html | 2 | Page title |
| Rows | Taxadaraha | app/templates/admin/advanced_results.html | 9 | Stat label |
| Students | Ardayda | app/templates/admin/advanced_results.html | 10 | Stat label |
| Published | La daah-furay | app/templates/admin/advanced_results.html | 11 | Stat label |
| Locked | La xiray | app/templates/admin/advanced_results.html | 12 | Stat label |
| Pass Rate | Heerka Guulaha | app/templates/admin/advanced_results.html | 13 | Stat label |
| Exam Average | Dhexdhexaadka Imtixaanka | app/templates/admin/advanced_results.html | 14 | Stat label |
| Professional Filters | Shaqooyin Xirfad leh | app/templates/admin/advanced_results.html | 18 | Section heading |
| Filter by academic year, exam, level, class, section, student, publication, or lock status. | Saadojiir sanadka dugsiga, imtixaanka, heerka, fasalka, qaybta, ardayda, daah-furka, ama xaalada xirista. | app/templates/admin/advanced_results.html | 18 | Section description |
| Search | Raadi | app/templates/admin/advanced_results.html | 20 | Form label |
| Student, ID, subject | Arday, ID, maado | app/templates/admin/advanced_results.html | 20 | Placeholder |
| Academic Year | Sanadka Dugsiga | app/templates/admin/advanced_results.html | 21 | Form label |
| All Years | Dhammaan Sannadka | app/templates/admin/advanced_results.html | 21 | Option |
| Exam | Imtixaan | app/templates/admin/advanced_results.html | 22 | Form label |
| All Exams | Dhammaan Imtixaanka | app/templates/admin/advanced_results.html | 22 | Option |
| Level | Heer | app/templates/admin/advanced_results.html | 23 | Form label |
| All Levels | Dhammaan Heerka | app/templates/admin/advanced_results.html | 23 | Option |
| Class | Fasal | app/templates/admin/advanced_results.html | 24 | Form label |
| All Classes | Dhammaan Fasallada | app/templates/admin/advanced_results.html | 24 | Option |
| Section | Qayb | app/templates/admin/advanced_results.html | 25 | Form label |
| All Sections | Dhammaan Qaybaha | app/templates/admin/advanced_results.html | 25 | Option |
| Status | Xaalada | app/templates/admin/advanced_results.html | 26 | Form label |
| All | Dhammaan | app/templates/admin/advanced_results.html | 26 | Option |
| Published | La daah-furay | app/templates/admin/advanced_results.html | 26 | Option |
| Unpublished | La qaray | app/templates/admin/advanced_results.html | 26 | Option |
| Locked | La xiray | app/templates/admin/advanced_results.html | 26 | Option |
| Apply | Dhex-gal | app/templates/admin/advanced_results.html | 27 | Button label |
| Statistics | Xisaab-yada | app/templates/admin/advanced_results.html | 32 | Section heading |
| Subject averages, highest students, lowest students, pass and fail rates. | Dhexdhexaadka maaddada, ardayda ugu dhibcaha badan, ardayda ugu dhibcaha yar, heerka guulaha iyo guuldareyska. | app/templates/admin/advanced_results.html | 32 | Section description |
| Subject Averages | Dhexdhexaadka Maaddada | app/templates/admin/advanced_results.html | 34 | Card heading |
| No subject averages yet. | Dhexdhexaadka maaddada weli ma jiro. | app/templates/admin/advanced_results.html | 34 | Empty state |
| Top Students | Ardayda Ugu Fiican | app/templates/admin/advanced_results.html | 35 | Card heading |
| No ranked data. | Macluumaad tartan lama helin. | app/templates/admin/advanced_results.html | 35 | Empty state |
| Lowest Students | Ardayda Ugu Dhibcaha Yar | app/templates/admin/advanced_results.html | 36 | Card heading |
| No ranked data. | Macluumaad tartan lama helin. | app/templates/admin/advanced_results.html | 36 | Empty state |
| Pass / Fail | Guul / Guuldarey | app/templates/admin/advanced_results.html | 37 | Card heading |
| Pass Rate | Heerka Guulaha | app/templates/admin/advanced_results.html | 37 | Label |
| Fail Rate | Heerka Guuldareyska | app/templates/admin/advanced_results.html | 37 | Label |
| Export Excel | Dhoofinta Excel | app/templates/admin/advanced_results.html | 42 | Button label |
| Publish | Daah-fur | app/templates/admin/advanced_results.html | 43 | Button label |
| Unpublish | Qar | app/templates/admin/advanced_results.html | 44 | Button label |
| Lock | Xir | app/templates/admin/advanced_results.html | 45 | Button label |
| Unlock | Fur | app/templates/admin/advanced_results.html | 46 | Button label |
| Delete | Tirtir | app/templates/admin/advanced_results.html | 47 | Button label |
| Hierarchical Results | Natiijooyinka Qaybaha | app/templates/admin/advanced_results.html | 51 | Section heading |
| Academic Year -> Exam -> Level -> Class -> Section -> Students. | Sanadka Dugsiga -> Imtixaan -> Heer -> Fasal -> Qayb -> Ardayda. | app/templates/admin/advanced_results.html | 51 | Section description |
| Select | Dooro | app/templates/admin/advanced_results.html | 65 | Table header |
| Student | Arday | app/templates/admin/advanced_results.html | 65 | Table header |
| Subject | Maado | app/templates/admin/advanced_results.html | 65 | Table header |
| Score | Dhibcaha | app/templates/admin/advanced_results.html | 65 | Table header |
| Published | La daah-furay | app/templates/admin/advanced_results.html | 65 | Table header |
| Locked | La xiray | app/templates/admin/advanced_results.html | 65 | Table header |
| Print | Daabac | app/templates/admin/advanced_results.html | 65 | Table header |
| Yes | Haa | app/templates/admin/advanced_results.html | 67 | Table cell |
| No | Maya | app/templates/admin/advanced_results.html | 67 | Table cell |
| No results found. | Natiijo lama helin. | app/templates/admin/advanced_results.html | 81 | Empty state |

### Result Entry

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Whole-Class Result Entry | Gelinta Natiijooyinka Fasalka oo Dhan | app/templates/admin/result_entry.html | 3 | Page title |
| Exam Entry | Gelinta Imtixaanka | app/templates/admin/result_entry.html | 12 | Eyebrow label |
| Select the academic context first, then enter marks. Scores save automatically. | Marka hore dooro xaalada akademicska, kadibna geli dhibcaha. Dhibcaha waa la kaydiyaa otomaatig ah. | app/templates/admin/result_entry.html | 20 | Description |
| Ready | Diyaar u ah | app/templates/admin/result_entry.html | 24 | Save status |
| Academic Year | Sanadka Dugsiga | app/templates/admin/result_entry.html | 32 | Filter title |
| Exam Type | Nooca Imtixaanka | app/templates/admin/result_entry.html | 44 | Filter title |
| Level | Heer | app/templates/admin/result_entry.html | 56 | Filter title |
| Class | Fasal | app/templates/admin/result_entry.html | 69 | Filter title |
| Select level | Dooro heer | app/templates/admin/result_entry.html | 58 | Option |
| Select class | Dooro fasal | app/templates/admin/result_entry.html | 71 | Option |
| All sections | Dhammaan qaybaha | app/templates/admin/result_entry.html | 77 | Option |
| Select an exam type | Dooro nooca imtixaanka | app/templates/admin/result_entry.html | 96 | Empty heading |
| Choose an academic year and exam type before loading students. | Dooro sanad dugsiga iyo nooca imtixaanka ka hor inta aad soo dejinayso ardayda. | app/templates/admin/result_entry.html | 97 | Empty description |
| error | Khalad | app/templates/admin/result_entry.html | 181 | Icon mapping key |
| Score must be 0-{maxScore} | Dhibcaha waa inuu yahay 0-{maxScore} | app/templates/admin/result_entry.html | 214 | Validation error message |
| Save failed. | Kaydinta way guuldareysatay. | app/templates/admin/result_entry.html | 251 | Error message |

### Result Edit

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Edit Result | Tifatir Natiijada | app/templates/admin/result_edit.html | 2 | Page title |
| Total | Wadarta | app/templates/admin/result_edit.html | 7 | Summary label |
| Average | Dhexdhexaad | app/templates/admin/result_edit.html | 8 | Summary label |
| Grade | Darajada | app/templates/admin/result_edit.html | 9 | Summary label |
| Status | Xaalada | app/templates/admin/result_edit.html | 10 | Summary label |
| Edit Student Info | Tifatir Macluumaadka Ardayda | app/templates/admin/result_edit.html | 13 | Button label |
| Edit Exam Info | Tifatir Macluumaadka Imtixaanka | app/templates/admin/result_edit.html | 14 | Button label |
| Edit Subjects | Tifatir Maadooyinka | app/templates/admin/result_edit.html | 15 | Button label |
| Report Display Settings | Dejinta Muuqalka Warbixinta | app/templates/admin/result_edit.html | 16 | Button label |
| Subject Scores | Dhibcaha Maaddada | app/templates/admin/result_edit.html | 22 | Section heading |
| Edit marks, grade overrides, subject remarks, and publish visibility. | Tifatir dhibcaha, darajada, faallooyinka maaddada, iyo muuqalka daah-furka. | app/templates/admin/result_edit.html | 22 | Section description |
| Subject | Maado | app/templates/admin/result_edit.html | 25 | Table header |
| Score | Dhibcaha | app/templates/admin/result_edit.html | 25 | Table header |
| Auto Grade | Darajada Otomaatiga ah | app/templates/admin/result_edit.html | 25 | Table header |
| Grade Override | Darajada Dib u eegista | app/templates/admin/result_edit.html | 25 | Table header |
| Subject Remark | Faallo Maaddada | app/templates/admin/result_edit.html | 25 | Table header |
| Published | La daah-furay | app/templates/admin/result_edit.html | 25 | Table header |
| Max | Ugu badan | app/templates/admin/result_edit.html | 31 | Table cell prefix |
| Optional | Ikhtiyaari ah | app/templates/admin/result_edit.html | 34 | Placeholder |
| Optional subject remark | Faallo maaddada ikhtiyaari ah | app/templates/admin/result_edit.html | 35 | Placeholder |
| Visible | Muuqda | app/templates/admin/result_edit.html | 36 | Checkbox label |
| Save Result Changes | Kaydi Isbedelka Natiijada | app/templates/admin/result_edit.html | 43 | Button label |
| Print Report | Daabac Warbixin | app/templates/admin/result_edit.html | 44 | Button label |
| Back | Dib | app/templates/admin/result_edit.html | 45 | Button label |

### Class Roster

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Liiska Natiijada Fasalka | Liiska Natiijada Fasalka | app/templates/admin/class_roster.html | 3, 19 | Page title |
| Class Result List | Liiska Natiijada Fasalka | app/templates/admin/class_roster.html | 15 | Eyebrow label |
| arday | arday | app/templates/admin/class_roster.html | 20 | Student count label |
| Export Excel | Dhoofinta Excel | app/templates/admin/class_roster.html | 23 | Button label |
| Export PDF | Dhoofinta PDF | app/templates/admin/class_roster.html | 24 | Button label |
| Academic Year | Sanadka Dugsiga | app/templates/admin/class_roster.html | 32 | Filter title |
| Exam Type | Nooca Imtixaanka | app/templates/admin/class_roster.html | 44 | Filter title |
| Level | Heer | app/templates/admin/class_roster.html | 56 | Filter title |
| Class | Fasal | app/templates/admin/class_roster.html | 69 | Filter title |
| Select level | Dooro heer | app/templates/admin/class_roster.html | 58 | Option |
| Select class | Dooro fasal | app/templates/admin/class_roster.html | 71 | Option |
| All sections | Dhammaan qaybaha | app/templates/admin/class_roster.html | 77 | Option |
| Raadi arday ID ama magac... | Raadi arday ID ama magac... | app/templates/admin/class_roster.html | 89 | Search placeholder |
| Select an exam type | Dooro nooca imtixaanka | app/templates/admin/class_roster.html | 96 | Empty heading |
| Choose an academic year and exam type before loading a class list. | Dooro sanad dugsiga iyo nooca imtixaanka ka hor inta aad soo dejinayso liiska fasalka. | app/templates/admin/class_roster.html | 97 | Empty description |

### Grade Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Grade Management — Simplified | Maamulka Darajada — Fudud | app/templates/admin/grade_management.html | 3, 4, 13 | Page title |
| Grade Management | Maamulka Darajada | app/templates/admin/grade_management.html | 12 | Eyebrow label |
| Academic Year -> Exam Type | hal scale oo si toos ah loogu dabaqo dhammaan fasallada imtixaankan qaaday. | Sanadka Dugsiga -> Nooca Imtixaanka hal scale oo si toos ah loogu dabaqo dhammaan fasallada imtixaankan qaaday. | app/templates/admin/grade_management.html | 14 | Description |
| Sanad Dugsiyeedka | Sanadka Dugsiga | app/templates/admin/grade_management.html | 18 | Selector label |
| Exam Type | Nooca Imtixaanka | app/templates/admin/grade_management.html | 26 | Selector label |
| Global | Caalamka | app/templates/admin/grade_management.html | 28 | Option |
| Applies To | La Dhex-galo | app/templates/admin/grade_management.html | 35 | Label |
| All Classes | Dhammaan Fasallada | app/templates/admin/grade_management.html | 36 | Label |
| Generate Scale | Abuur Scale | app/templates/admin/grade_management.html | 38 | Button label |
| Global Scale: This exam uses the global grade scale until custom rows are saved for the selected exam. | Scale Caalamka: Imtixaankan wuxuu isticmaalaa scale darajada caalamka ilaa taxadaraha gaarka ah la kaydiyo imtixaanka la doortay. | app/templates/admin/grade_management.html | 43 | Info banner |
| Grade | Darajada | app/templates/admin/grade_management.html | 54 | Table header |
| Min | Yar | app/templates/admin/grade_management.html | 55 | Table header |
| Max | Badan | app/templates/admin/grade_management.html | 56 | Table header |
| Point | Dhib | app/templates/admin/grade_management.html | 57 | Table header |
| Comment | Faallo | app/templates/admin/grade_management.html | 58 | Table header |
| Status | Xaalada | app/templates/admin/grade_management.html | 59 | Table header |
| Colors | Midabka | app/templates/admin/grade_management.html | 60 | Table header |
| Preview | Eeg | app/templates/admin/grade_management.html | 61 | Table header |
| Pass | Guul | app/templates/admin/grade_management.html | 74 | Option |
| Fail | Guuldarey | app/templates/admin/grade_management.html | 75 | Option |
| Active | Firfircoon | app/templates/admin/grade_management.html | 78 | Checkbox label |
| A+ | A+ | app/templates/admin/grade_management.html | 96 | Placeholder |
| 95 | 95 | app/templates/admin/grade_management.html | 97 | Placeholder |
| 100 | 100 | app/templates/admin/grade_management.html | 98 | Placeholder |
| 4.0 | 4.0 | app/templates/admin/grade_management.html | 99 | Placeholder |
| Outstanding | Fiican | app/templates/admin/grade_management.html | 100 | Placeholder |
| Save Grade Scales | Kaydi Darajada Scale | app/templates/admin/grade_management.html | 116 | Button label |

### Result Validation Messages

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Invalid score. | Dhibcaha waa khalkhaali ah. | app/routes_advanced_results.py | 1594 | JSON error message |
| Score must be between 0 and {max_score}. | Dhibcaha waa inuu u dhexeeyaa 0 iyo {max_score}. | app/routes_advanced_results.py | 1598 | JSON error message |
| {student.student_code} - {subject.name}: Score {score} exceeds max {subject.max_score} | {student.student_code} - {subject.name}: Dhibcaha {score} waa ka badan {subject.max_score} | app/routes_advanced_results.py | 1670 | Validation error |
| {student.student_code} - {subject.name}: Invalid score '{raw_score}' | {student.student_code} - {subject.name}: Dhibcaha khalkhaali ah '{raw_score}' | app/routes_advanced_results.py | 1673 | Validation error |
| Please select a class for this student. | Fadlan dooro fasal ardaydan. | app/routes_advanced_results.py | 2472 | ValueError |
| Photo must be JPG, PNG, or WEBP. | Sawirka waa inuu yahay JPG, PNG, ama WEBP. | app/routes_advanced_results.py | 2481 | ValueError |
| Level not found. | Heer lama helin. | app/routes_advanced_results.py | 402, 422, 450, 140 | Flash message (danger) |
| Academic level not found. | Heerka akademicska lama helin. | app/routes_advanced_results.py | 61, 113, 140 | Flash message (danger) |
| Class not found. | Fasal lama helin. | app/routes_advanced_results.py | 478, 498 | Flash message (danger) |
| Academic class not found. | Fasalka akademicska lama helin. | app/routes_advanced_results.py | 114 | Flash message (danger) |
| Academic section not found. | Qaybta akademicska lama helin. | app/routes_advanced_results.py | 201 | Flash message (danger) |

---

## Attendance Module

### Attendance Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Attendance Management | Maamulka Dhexdhexaadka | app/templates/admin/attendance.html | 2 | Page title |
| Search & Filters | Raadi & Shaqooyin | app/templates/admin/attendance.html | 5 | Section heading |
| Mark Attendance | Calaamad Dhexdhexaadka | app/templates/admin/attendance.html | 6 | Section heading |
| Attendance History | Taariikhda Dhexdhexaadka | app/templates/admin/attendance.html | 7 | Section heading |
| Search | Raadi | app/templates/admin/attendance.html | 8 | Form label |
| Academic Year | Sanadka Dugsiga | app/templates/admin/attendance.html | 9 | Form label |
| Exam | Imtixaan | app/templates/admin/attendance.html | 10 | Form label |
| Class | Fasal | app/templates/admin/attendance.html | 11 | Form label |
| Level | Heer | app/templates/admin/attendance.html | 12 | Form label |
| Section | Qayb | app/templates/admin/attendance.html | 13 | Form label |
| Student | Arday | app/templates/admin/attendance.html | 14 | Form label |
| Status | Xaalada | app/templates/admin/attendance.html | 15 | Form label |
| Date | Taariikh | app/templates/admin/attendance.html | 16 | Form label |
| Note | Faallo | app/templates/admin/attendance.html | 17 | Form label |
| Bulk Scope | Scope-ka Badan | app/templates/admin/attendance.html | 18 | Form label |
| Apply Filters | Dhex-gal Shaqooyinka | app/templates/admin/attendance.html | 19 | Button label |
| Save Single | Kaydi Mid | app/templates/admin/attendance.html | 20 | Button label |
| Mark Bulk Attendance | Calaamad Dhexdhexaadka Badan | app/templates/admin/attendance.html | 21 | Button label |
| Export Excel | Dhoofinta Excel | app/templates/admin/attendance.html | 22 | Link label |
| Export PDF | Dhoofinta PDF | app/templates/admin/attendance.html | 23 | Link label |
| Print Sheet | Daabac Warqad | app/templates/admin/attendance.html | 24 | Link label |
| Date | Taariikh | app/templates/admin/attendance.html | 25 | Table header |
| Student | Arday | app/templates/admin/attendance.html | 25 | Table header |
| Class | Fasal | app/templates/admin/attendance.html | 25 | Table header |
| Exam | Imtixaan | app/templates/admin/attendance.html | 25 | Table header |
| Status | Xaalada | app/templates/admin/attendance.html | 25 | Table header |
| Note | Faallo | app/templates/admin/attendance.html | 25 | Table header |
| Actions | Dhaqaaqyo | app/templates/admin/attendance.html | 25 | Table header |
| No attendance records found. | Dhibcood dhexdhexaad lama helin. | app/templates/admin/attendance.html | 26 | Empty state |
| No students found for the selected filters. | Arday lama helin shaqooyinka la doortay. | app/templates/admin/attendance.html | 27 | Empty state |

---

## Settings Module

### Settings Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Settings | Dejinta | app/templates/admin/base.html | 34 | Sidebar menu item |
| School Branding | Sumadda Dugsiga | app/templates/admin/settings.html | Section heading | Form label |
| School Name | Magaca Dugsiga | app/templates/admin/settings.html | Form label |
| Motto | Shahaada | app/templates/admin/settings.html | Form label |
| Address | Cinwaanka | app/templates/admin/settings.html | Form label |
| Phone | Telifoon | app/templates/admin/settings.html | Form label |
| Email | Imayl | app/templates/admin/settings.html | Form label |
| Website | Websaydhka | app/templates/admin/settings.html | Form label |
| Principal Name | Magaca Madaxa | app/templates/admin/settings.html | Form label |
| Enable Phone Verification | Ogolaashada Telifoonka | app/templates/admin/settings.html | Form label |
| School Logo | Logo-ka Dugsiga | app/templates/admin/settings.html | Form label |
| Footer Text | Qoraalka Dhexe | app/templates/admin/settings.html | Form label |
| Global Student Photo Style | Sawirka Ardayda Caalamka | app/templates/admin/settings.html | Section heading | Form label |
| Photo Shape | Sawirka | app/templates/admin/settings.html | Form label |
| Photo Size | Xajmiga Sawirka | app/templates/admin/settings.html | Form label |
| Photo Border | Xadhka Sawirka | app/templates/admin/settings.html | Form label |
| Photo Shadow | Dhararka Sawirka | app/templates/admin/settings.html | Form label |
| Admin Dashboard | Dhismaha Maamulka | app/templates/admin/settings.html | Section heading | Form label |
| Dashboard Title | Cinwaanka Dhismaha | app/templates/admin/settings.html | Form label |
| Dashboard Subtitle | Cinwaanka Dhismaha | app/templates/admin/settings.html | Form label |
| Default Language | Luuqada Hore | app/templates/admin/settings.html | Form label |
| Theme | Mawduuca | app/templates/admin/settings.html | Form label |
| Primary Color | Midabka Hore | app/templates/admin/settings.html | Form label |
| Secondary Color | Midabka Labaad | app/templates/admin/settings.html | Form label |
| Sidebar Color | Midabka Sidebar-ka | app/templates/admin/settings.html | Form label |
| Admin Logo | Logo-ka Maamulka | app/templates/admin/settings.html | Form label |
| Dashboard Background | Dhararka Dhismaha | app/templates/admin/settings.html | Form label |
| Visible Cards | Kaaradaha Muuqda | app/templates/admin/settings.html | Form label |
| Homepage Widgets | Widget-ka Bogga Hore | app/templates/admin/settings.html | Form label |
| Search Page Footer Customization | Dejinta Qoraalka Dhexe Bogga Raadinta | app/templates/admin/settings.html | Section heading | Form label |
| Footer Text | Qoraalka Dhexe | app/templates/admin/settings.html | Form label |
| Footer Font Size | Xajmiga Foonka Qoraalka Dhexe | app/templates/admin/settings.html | Form label |
| Footer Font Weight | Miisaanka Foonka Qoraalka Dhexe | app/templates/admin/settings.html | Form label |
| Footer Text Color | Midabka Qoraalka Dhexe | app/templates/admin/settings.html | Form label |
| Footer Background Color | Midabka Dhararka Qoraalka Dhexe | app/templates/admin/settings.html | Form label |
| Footer Border Color | Midabka Xadhka Qoraalka Dhexe | app/templates/admin/settings.html | Form label |
| Footer Visibility | Muuqadda Qoraalka Dhexe | app/templates/admin/settings.html | Form label |
| UI Customization | Dejinta UI | app/templates/admin/settings.html | Section heading | Form label |
| Typography Controls | Xakamaynta Typography | app/templates/admin/settings.html | Section heading | Form label |
| Social & Contact Links | Link-ka Bulshada & La Xiriirka | app/templates/admin/settings.html | Section heading | Form label |
| Signature Management | Maamulka Tixraaca | app/templates/admin/settings.html | Section heading | Form label |
| Report Card Designer | Naqshadeyaha Baasaboorta | app/templates/admin/settings.html | Section heading | Form label |
| Student ID Verification Page | Bogga Xaqiijinta ID-ga Ardayda | app/templates/admin/settings.html | Section heading | Form label |
| Color Theme | Mawduuca Midabka | app/templates/admin/settings.html | Form label |
| Typography | Typography | app/templates/admin/settings.html | Form label |
| Border Radius | Radius-ka Xadhka | app/templates/admin/settings.html | Form label |
| Display Mode | Mode-ka Muuqadda | app/templates/admin/settings.html | Form label |
| Font Family | Qoyska Foonka | app/templates/admin/settings.html | Form label |
| Font Weight | Miisaanka Foonka | app/templates/admin/settings.html | Form label |
| Base Font Size | Xajmiga Foonka Hore | app/templates/admin/settings.html | Form label |
| Card Radius | Radius-ka Kaaradda | app/templates/admin/settings.html | Form label |
| Button Radius | Radius-ka Badhanka | app/templates/admin/settings.html | Form label |
| Table Radius | Radius-ka Jadwalka | app/templates/admin/settings.html | Form label |
| Dark Mode | Mode-ka Madow | app/templates/admin/settings.html | Form label |
| Light Mode | Mode-ka Cad | app/templates/admin/settings.html | Form label |
| Compact Mode | Mode-ka Yar | app/templates/admin/settings.html | Form label |
| Comfortable Mode | Mode-ka Raaxo leh | app/templates/admin/settings.html | Form label |
| Page Title | Cinwaanka Bogga | app/templates/admin/settings.html | Form label |
| Subtitle | Cinwaanka | app/templates/admin/settings.html | Form label |
| Input Labels | Laabelka Gelinta | app/templates/admin/settings.html | Form label |
| Input Placeholder | Placeholder-ka Gelinta | app/templates/admin/settings.html | Form label |
| Buttons | Badhanka | app/templates/admin/settings.html | Form label |
| Footer | Dhexe | app/templates/admin/settings.html | Form label |
| Copyright Text | Qoraalka Copyright-ka | app/templates/admin/settings.html | Form label |
| Student Information | Macluumaadka Ardayda | app/templates/admin/settings.html | Form label |
| Dashboard Headings | Cinwaanka Dhismaha | app/templates/admin/settings.html | Form label |
| Table Text | Qoraalka Jadwalka | app/templates/admin/settings.html | Form label |
| WhatsApp | WhatsApp | app/templates/admin/settings.html | Form label |
| Facebook | Facebook | app/templates/admin/settings.html | Form label |
| Instagram | Instagram | app/templates/admin/settings.html | Form label |
| Telegram | Telegram | app/templates/admin/settings.html | Form label |
| X Twitter | X Twitter | app/templates/admin/settings.html | Form label |
| Email Link | Link-ka Imaylka | app/templates/admin/settings.html | Form label |
| Call Center | Marka Wacda | app/templates/admin/settings.html | Form label |
| Google Maps | Google Maps | app/templates/admin/settings.html | Form label |
| Principal Signature | Tixraaca Madaxa | app/templates/admin/settings.html | Form label |
| Vice Principal Signature | Tixraaca Madaxa Labaad | app/templates/admin/settings.html | Form label |
| Examination Officer Signature | Tixraaca Rukhsada Imtixaanka | app/templates/admin/settings.html | Form label |
| School Stamp | Tamarka Dugsiga | app/templates/admin/settings.html | Form label |
| Report Header Style | Style-ka Cinwaanka Warbixinta | app/templates/admin/settings.html | Form label |
| Font Family | Qoyska Foonka | app/templates/admin/settings.html | Form label |
| Report Primary Color | Midabka Hore ee Warbixinta | app/templates/admin/settings.html | Form label |
| Report Accent Color | Midabka Accent-ka ee Warbixinta | app/templates/admin/settings.html | Form label |
| Border Style | Style-ka Xadhka | app/templates/admin/settings.html | Form label |
| Background | Dhararka | app/templates/admin/settings.html | Form label |
| Watermark | Watermark-ka | app/templates/admin/settings.html | Form label |
| Logo Position | Goobta Logo-ka | app/templates/admin/settings.html | Form label |
| QR Position | Goobta QR-ka | app/templates/admin/settings.html | Form label |
| Photo Position | Goobta Sawirka | app/templates/admin/settings.html | Form label |
| Table Style | Style-ka Jadwalka | app/templates/admin/settings.html | Form label |
| Comment Box | Box-ka Faalada | app/templates/admin/settings.html | Form label |
| Principal Comment | Faallada Madaxa | app/templates/admin/settings.html | Form label |
| Report Footer | Dhexe Warbixinta | app/templates/admin/settings.html | Form label |
| Logo Size | Xajmiga Logo-ka | app/templates/admin/settings.html | Form label |
| Header Padding | Padding-ka Cinwaanka | app/templates/admin/settings.html | Form label |
| Header Primary Color | Midabka Hore ee Cinwaanka | app/templates/admin/settings.html | Form label |
| Header Secondary Color | Midabka Labaad ee Cinwaanka | app/templates/admin/settings.html | Form label |
| Show Watermark Logo | Muuji Logo-ka Watermark-ka | app/templates/admin/settings.html | Form label |
| Exam Type | Nooca Imtixaanka | app/templates/admin/settings.html | Form label |
| Photo Size | Xajmiga Sawirka | app/templates/admin/settings.html | Form label |
| Border Width | Ballaca Xadhka | app/templates/admin/settings.html | Form label |
| Border Color | Midabka Xadhka | app/templates/admin/settings.html | Form label |
| Border Radius | Radius-ka Xadhka | app/templates/admin/settings.html | Form label |
| Photo Shadow | Dhararka Sawirka | app/templates/admin/settings.html | Form label |
| Badge Text | Qoraalka Badge-ka | app/templates/admin/settings.html | Form label |
| Badge Primary Color | Midabka Hore ee Badge-ka | app/templates/admin/settings.html | Form label |
| Badge Secondary Color | Midabka Labaad ee Badge-ka | app/templates/admin/settings.html | Form label |
| Border Radius | Radius-ka Xadhka | app/templates/admin/settings.html | Form label |
| Enable Badge Animation | Ogolaashada Animation-ka Badge-ka | app/templates/admin/settings.html | Form label |
| Status Card Color | Midabka Kaaradda Xaalada | app/templates/admin/settings.html | Form label |
| Status Card Dark Color | Midabka Madow ee Kaaradda Xaalada | app/templates/admin/settings.html | Form label |
| Show Verification Stamp | Muuji Tamarka Xaqiijinta | app/templates/admin/settings.html | Form label |
| Stamp Size | Xajmiga Tamarka | app/templates/admin/settings.html | Form label |
| Stamp Color | Midabka Tamarka | app/templates/admin/settings.html | Form label |
| Card Border Radius | Radius-ka Xadhka Kaaradda | app/templates/admin/settings.html | Form label |
| Card Padding | Padding-ka Kaaradda | app/templates/admin/settings.html | Form label |
| Card Spacing | Space-ka Kaaradda | app/templates/admin/settings.html | Form label |
| Glass Effect | Saabka Bilyaanka | app/templates/admin/settings.html | Form label |
| Show School Logo | Muuji Logo-ka Dugsiga | app/templates/admin/settings.html | Form label |
| Show Student Photo | Muuji Sawirka Ardayda | app/templates/admin/settings.html | Form label |
| Show Student Name | Muuji Magaca Ardayda | app/templates/admin/settings.html | Form label |
| Show Student ID | Muuji ID-ga Ardayda | app/templates/admin/settings.html | Form label |
| Show Mother's Name | Muuji Magaca Hooyada | app/templates/admin/settings.html | Form label |
| Show Class | Muuji Fasalka | app/templates/admin/settings.html | Form label |
| Show Section | Muuji Qaybta | app/templates/admin/settings.html | Form label |
| Show Academic Year | Muuji Sanadka Dugsiga | app/templates/admin/settings.html | Form label |
| Show Exam Type | Muuji Nooca Imtixaanka | app/templates/admin/settings.html | Form label |
| Show Issue Date | Muuji Taariikhda Soo saarista | app/templates/admin/settings.html | Form label |
| Show Expiry Date | Muuji Taariikhda Dhamaanka | app/templates/admin/settings.html | Form label |
| Show Verification Badge | Muuji Badge-ka Xaqiijinta | app/templates/admin/settings.html | Form label |
| Show Status Card | Muuji Kaaradda Xaalada | app/templates/admin/settings.html | Form label |
| Show Verification Stamp | Muuji Tamarka Xaqiijinta | app/templates/admin/settings.html | Form label |
| Show Verification Code | Muuji Code-ka Xaqiijinta | app/templates/admin/settings.html | Form label |
| Show Date & Time | Muuji Taariikhda & Waqtiga | app/templates/admin/settings.html | Form label |
| Show Footer | Muuji Dhexe | app/templates/admin/settings.html | Form label |
| Show Watermark | Muuji Watermark-ka | app/templates/admin/settings.html | Form label |
| Show Icons | Muuji Icon-ka | app/templates/admin/settings.html | Form label |
| Show Background Decorations | Muuji Dhararka Dibadda | app/templates/admin/settings.html | Form label |
| Show Header | Muuji Cinwaanka | app/templates/admin/settings.html | Form label |
| Show Verification Area | Muuji Goobta Xaqiijinta | app/templates/admin/settings.html | Form label |
| Base Font Family | Qoyska Foonka Hore | app/templates/admin/settings.html | Form label |
| Base Font Size | Xajmiga Foonka Hore | app/templates/admin/settings.html | Form label |
| Base Font Weight | Miisaanka Foonka Hore | app/templates/admin/settings.html | Form label |
| Base Text Color | Midabka Qoraalka Hore | app/templates/admin/settings.html | Form label |
| Letter Spacing | Space-ka Xarafka | app/templates/admin/settings.html | Form label |
| Line Height | Dhererka Line-ka | app/templates/admin/settings.html | Form label |
| Text Alignment | Toosinta Qoraalka | app/templates/admin/settings.html | Form label |

### Change Password

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Change Password | Beddel Ereyga Sirta Ah | app/templates/admin/change_password.html | 2 | Page title |
| Password Security | Nabadgelyada Ereyga Sirta Ah | app/templates/admin/change_password.html | 4 | Section heading |
| Use a strong password with at least eight characters. | Isticmaal erey sirta ah oo adag oo leh ugu yaraan siddeed xaraf. | app/templates/admin/change_password.html | 4 | Help text |
| Current Password | Ereyga Sirta Ah Hadda | app/templates/admin/change_password.html | 4 | Form label |
| New Password | Ereyga Sirta Ah Cusub | app/templates/admin/change_password.html | 4 | Form label |
| Confirm Password | Xaqiiji Ereyga Sirta Ah | app/templates/admin/change_password.html | 4 | Form label |
| Change Password | Beddel Ereyga Sirta Ah | app/templates/admin/change_password.html | 4 | Button label |

### User Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Users | Isticmaalayaasha | app/templates/admin/base.html | 33 | Sidebar menu item |
| Add Admin | Ku dar Maamul | app/templates/admin/users.html | 2 | Page title |
| Create administrators and assign individual permissions. | Abuur maamulayaasha si aad u qeybiyo ogolaansho gaar ah. | app/templates/admin/users.html | 6 | Section heading |
| Username | Magaca isticmaalka | app/templates/admin/users.html | 7 | Form label |
| Full Name | Magac oo dhan | app/templates/admin/users.html | 8 | Form label |
| Role | Door | app/templates/admin/users.html | 9 | Form label |
| Admin Photo | Sawirka Maamulka | app/templates/admin/users.html | 10 | Form label |
| Password | Ereyga sirta ah | app/templates/admin/users.html | 11 | Form label |
| Active | Firfircoon | app/templates/admin/users.html | 12 | Checkbox label |
| Add Admin | Ku dar Maamul | app/templates/admin/users.html | 18 | Button label |
| Username | Magaca isticmaalka | app/templates/admin/users.html | 23 | Table header |
| Name | Magac | app/templates/admin/users.html | 23 | Table header |
| Role | Door | app/templates/admin/users.html | 23 | Table header |
| Permissions | Ogolaanshaha | app/templates/admin/users.html | 23 | Table header |
| Active | Firfircoon | app/templates/admin/users.html | 23 | Table header |
| Reset Password | Dib u bilow ereyga sirta ah | app/templates/admin/users.html | 23 | Table header |
| Yes | Haa | app/templates/admin/users.html | 24 | Status label |
| No | Maya | app/templates/admin/users.html | 24 | Status label |
| New password | Ereyga sirta ah cusub | app/templates/admin/users.html | 24 | Placeholder |

### Academic Years

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Academic Year Management | Maamulka Sanadka Dugsiga | app/templates/admin/academic_years.html | 2 | Page title |
| Admin | Maamul | app/templates/admin/academic_years.html | 25 | Breadcrumb |
| Academic Years | Sannadka Dugsiga | app/templates/admin/academic_years.html | 27 | Breadcrumb active |
| Academic Years | Sannadka Dugsiga | app/templates/admin/academic_years.html | 36 | Page heading |
| Switch the current academic year for new work. | Badal sanadka dugsiga hadda ee shaqo cusub. | app/templates/admin/academic_years.html | 37 | Page description |
| Add Academic Year | Ku dar Sanad Dugsiga | app/templates/admin/academic_years.html | 43 | Section heading |
| Name | Magac | app/templates/admin/academic_years.html | 48 | Form label |
| 2025-2026 | 2025-2026 | app/templates/admin/academic_years.html | 49 | Placeholder |
| Add Academic Year | Ku dar Sanad Dugsiga | app/templates/admin/academic_years.html | 53 | Button label |
| Name | Magac | app/templates/admin/academic_years.html | 64 | Table header |
| Status | Xaalada | app/templates/admin/academic_years.html | 65 | Table header |
| Actions | Dhaqaaqyo | app/templates/admin/academic_years.html | 66 | Table header |
| Current | Hadda | app/templates/admin/academic_years.html | 81 | Status label |
| Available | La heli karo | app/templates/admin/academic_years.html | 81 | Status label |
| Save | Kaydi | app/templates/admin/academic_years.html | 85 | Button tooltip |
| Make current | Noqo hadda | app/templates/admin/academic_years.html | 92 | Button tooltip |
| Delete | Tirtir | app/templates/admin/academic_years.html | 98 | Button tooltip |
| No academic years found. | Sannad dugsiga lama helin. | app/templates/admin/academic_years.html | 106 | Empty state |
| Name is required. | Magac waa lagu baahan yahay. | app/routes_admin.py | 1938, 1970, 2077, 2172, 2383 | JSON error message |
| Academic year already exists. | Sanad dugsiga hore ayaa jirta. | app/routes_admin.py | 1944, 1972 | JSON error message |
| Academic year is required. | Sanad dugsiga waa lagu baahan yahay. | app/routes_admin.py | 2078 | JSON error message |

### Configuration Dashboard

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Configuration Dashboard | Dhismaha Dejinta | app/templates/admin/results_setup.html | 3, 4 | Page title |
| Read Only Workspace | Goob Akhris oo keliya | app/templates/admin/results_setup.html | 17 | Kicker |
| Configuration is | Dejinta waa | app/templates/admin/results_setup.html | 18 | Hero title |
| Last Updated | La Cusubayay | app/templates/admin/results_setup.html | 24 | Status label |
| Updated By | La Cusubayay | app/templates/admin/results_setup.html | 28 | Status label |
| System Status | Xaalada Nidaamka | app/templates/admin/results_setup.html | 32 | Status label |
| Healthy | Si fiican u shaqeynaya | app/templates/admin/results_setup.html | 35 | Status badge |
| Configuration Status | Xaalada Dejinta | app/templates/admin/results_setup.html | 39 | Status label |
| Read Only | Akhris oo keliya | app/templates/admin/results_setup.html | 42 | Status badge |
| Open Configuration Center | Fur Marka Dejinta | app/templates/admin/results_setup.html | 48 | Button label |
| Academic Years | Sannadka Dugsiga | app/templates/admin/results_setup.html | 63 | Card title |
| Manage academic calendar | Maamulka kalendarka akademicska | app/templates/admin/results_setup.html | 64 | Card description |
| Total | Wadarta | app/templates/admin/results_setup.html | 70 | Stat label |
| Active | Firfircoon | app/templates/admin/results_setup.html | 74 | Stat label |
| Archived | Kaydsan | app/templates/admin/results_setup.html | 78 | Stat label |
| Current: | Hadda: | app/templates/admin/results_setup.html | 83 | Card label |
| View Details | Eeg Faahfaahinta | app/templates/admin/results_setup.html | 87 | Button label |
| Exam Types | Noocyada Imtixaanka | app/templates/admin/results_setup.html | 99 | Card title |
| Manage examination types | Maamulka noocyada imtixaanka | app/templates/admin/results_setup.html | 100 | Card description |
| Total | Wadarta | app/templates/admin/results_setup.html | 106 | Stat label |
| Active | Firfircoon | app/templates/admin/results_setup.html | 110 | Stat label |
| Archived | Kaydsan | app/templates/admin/results_setup.html | 114 | Stat label |
| Types: | Noocyada: | app/templates/admin/results_setup.html | 119 | Card label |
| View Details | Eeg Faahfaahinta | app/templates/admin/results_setup.html | 123 | Button label |
| Levels & Classes | Heerka & Fasallada | app/templates/admin/results_setup.html | 135 | Card title |
| Manage academic levels | Maamulka heerka akademicska | app/templates/admin/results_setup.html | 136 | Card description |
| Levels | Heerka | app/templates/admin/results_setup.html | 142 | Stat label |
| Classes | Fasallada | app/templates/admin/results_setup.html | 146 | Stat label |
| Archived | Kaydsan | app/templates/admin/results_setup.html | 150 | Stat label |
| Setup incomplete. Please configure: {', '.join(missing)} | Dejinta way dhammaatay. Fadlan dejin: {', '.join(missing)} | app/services.py | 867 | Flash message (warning) |

### Configuration Center Notifications

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Dependency Check Failed | Baarista Wixii La Baahanayay Way Guuldareysatay | app/templates/admin/config_center.html | 509 | Notification title |
| Could not check dependencies. | Lama baari karin wixii la baahanayay. | app/templates/admin/config_center.html | 509, 532 | Notification message |
| Password Required | Ereyga Sirta Ah Waa Lagu Baahan Yahay | app/templates/admin/config_center.html | 559 | Notification title |
| Enter your administrator password. | Geli ereyga sirta ah ee maamulkaaga. | app/templates/admin/config_center.html | 559 | Notification message |
| Authentication Failed | Xaqiijintay Way Guuldareysatay | app/templates/admin/config_center.html | 570 | Notification title |
| Invalid password. | Ereyga sirta ah waa khalkhaali ah. | app/templates/admin/config_center.html | 570 | Notification message |
| Password confirmation failed. | Xaqiijinta ereyga sirta ah way guuldareysatay. | app/templates/admin/config_center.html | 576 | Notification message |
| Action Blocked | Dhaqaaqda La Xiray | app/templates/admin/config_center.html | 592 | Notification title |
| Action could not be completed. | Dhaqaaqda lama dhamaystirin karo. | app/templates/admin/config_center.html | 592 | Notification message |
| Action failed. | Dhaqaaqda way guuldareysatay. | app/templates/admin/config_center.html | 595 | Notification message |
| Saved | La Kaydiyay | app/templates/admin/config_center.html | 633 | Notification title |
| Configuration saved. | Dejinta waa la kaydiyay. | app/templates/admin/config_center.html | 633 | Notification message |
| Save Failed | Kaydinta Way Guuldareysatay | app/templates/admin/config_center.html | 636 | Notification title |
| Configuration could not be saved. | Dejinta lama kaydi karo. | app/templates/admin/config_center.html | 636 | Notification message |
| Save failed. | Kaydinta way guuldareysatay. | app/templates/admin/config_center.html | 639 | Notification message |
| Error | Khalad | app/templates/admin/config_center.html | 532, 576, 595, 639 | Notification title |

---

## ID Cards Module

### ID Card Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| ID Cards | Baasaboorta | app/templates/admin/base.html | 29 | Sidebar menu item |
| Student ID Cards | Baasaboorta Ardayda | app/templates/admin/id_cards.html | 2 | Page title |
| ID Card Template Manager | Maamulaha Template-ka Baasaboorta | app/templates/admin/id_cards.html | 5 | Section heading |
| ID Card Designer | Naqshadeyaha Baasaboorta | app/templates/admin/id_cards.html | 6 | Section heading |
| Find Students | Raadi Ardayda | app/templates/admin/id_cards.html | 7 | Section heading |
| Bulk Operations | Dhaqaaqyo Badan | app/templates/admin/id_cards.html | 8 | Section heading |
| Recent ID Card Issues | Dhibcood Baasaboorta Dhow | app/templates/admin/id_cards.html | 9 | Section heading |
| Active Template | Template-ka Firfircoon | app/templates/admin/id_cards.html | 10 | Form label |
| Card Size | Xajmiga Kaaradda | app/templates/admin/id_cards.html | 11 | Form label |
| Orientation | Toosinta | app/templates/admin/id_cards.html | 12 | Form label |
| Background | Dhararka | app/templates/admin/id_cards.html | 13 | Form label |
| Primary | Hore | app/templates/admin/id_cards.html | 14 | Form label |
| Accent | Accent | app/templates/admin/id_cards.html | 15 | Form label |
| Font | Foonka | app/templates/admin/id_cards.html | 16 | Form label |
| Border | Xadh | app/templates/admin/id_cards.html | 17 | Form label |
| Rounded Corners | Goobaha Goobaysan | app/templates/admin/id_cards.html | 18 | Form label |
| Logo Position | Goobta Logo-ka | app/templates/admin/id_cards.html | 19 | Form label |
| Photo Position | Goobta Sawirka | app/templates/admin/id_cards.html | 20 | Form label |
| QR Position | Goobta QR-ka | app/templates/admin/id_cards.html | 21 | Form label |
| Icons | Icon-ka | app/templates/admin/id_cards.html | 22 | Form label |
| Labels | Laabelka | app/templates/admin/id_cards.html | 23 | Form label |
| Spacing | Space-ka | app/templates/admin/id_cards.html | 24 | Form label |
| Print Margins | Margin-ka Daabaca | app/templates/admin/id_cards.html | 25 | Form label |
| Barcode | Barcode-ka | app/templates/admin/id_cards.html | 26 | Form label |
| Valid Months | Bilaha La Xaqiijin Karo | app/templates/admin/id_cards.html | 27 | Form label |
| Exam Type | Nooca Imtixaanka | app/templates/admin/id_cards.html | 28 | Form label |
| Header Title | Cinwaanka Cinwaanka | app/templates/admin/id_cards.html | 29 | Form label |
| Signature | Tixraac | app/templates/admin/id_cards.html | 30 | Form label |
| School Stamp | Tamarka Dugsiga | app/templates/admin/id_cards.html | 31 | Form label |
| Watermark | Watermark-ka | app/templates/admin/id_cards.html | 32 | Form label |
| Footer Contact Text | Qoraalka La Xiriirka Dhexe | app/templates/admin/id_cards.html | 33 | Form label |
| Scope | Scope-ka | app/templates/admin/id_cards.html | 34 | Form label |
| Class | Fasal | app/templates/admin/id_cards.html | 35 | Form label |
| Level | Heer | app/templates/admin/id_cards.html | 36 | Form label |
| Section | Qayb | app/templates/admin/id_cards.html | 37 | Form label |
| Search | Raadi | app/templates/admin/id_cards.html | 38 | Form label |
| Student | Arday | app/templates/admin/id_cards.html | 39 | Table header |
| Class | Fasal | app/templates/admin/id_cards.html | 39 | Table header |
| Issue | Soo saar | app/templates/admin/id_cards.html | 39 | Table header |
| Expiry | Dhamaan | app/templates/admin/id_cards.html | 39 | Table header |
| Status | Xaalada | app/templates/admin/id_cards.html | 39 | Table header |
| Actions | Dhaqaaqyo | app/templates/admin/id_cards.html | 39 | Table header |
| Use Template | Isticmaal Template-ka | app/templates/admin/id_cards.html | 40 | Button label |
| Active | Firfircoon | app/templates/admin/id_cards.html | 41 | Button label |
| Save Designer | Kaydi Naqshadeyaha | app/templates/admin/id_cards.html | 42 | Button label |
| Apply | Dhex-gal | app/templates/admin/id_cards.html | 43 | Button label |
| Generate Bulk IDs | Abuur ID-yo Badan | app/templates/admin/id_cards.html | 44 | Button label |
| Generate | Abuur | app/templates/admin/id_cards.html | 45 | Button label |
| No students found. | Arday lama helin. | app/templates/admin/id_cards.html | 46 | Empty state |
| No ID cards generated yet. | ID-yo lama abuurin hadda. | app/templates/admin/id_cards.html | 47 | Empty state |

---

## Incidents Module

### Incident Management

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Incident Reports | Warbixininta Dhacdada | app/templates/admin/base.html | 31 | Sidebar menu item |
| Incident Settings | Dejinta Dhacdada | app/templates/admin/base.html | 32 | Sidebar menu item |
| Exam Incident Reports | Warbixininta Dhacdada Imtixaanka | app/templates/admin/incidents.html | 2 | Page title |
| Dashboard | Dhismaha | app/templates/admin/incidents.html | 13 | Breadcrumb |
| Incident Reports | Warbixininta Dhacdada | app/templates/admin/incidents.html | 15 | Breadcrumb active |
| Settings | Dejinta | app/templates/admin/incidents.html | 17 | Section heading |
| Hide Filters | Qar Shaqooyinka | app/templates/admin/incidents.html | 18 | Button label |
| Academic Year | Sanadka Dugsiga | app/templates/admin/incidents.html | 19 | Filter label |
| Exam Type | Nooca Imtixaanka | app/templates/admin/incidents.html | 20 | Filter label |
| Level | Heer | app/templates/admin/incidents.html | 21 | Filter label |
| Class | Fasal | app/templates/admin/incidents.html | 22 | Filter label |
| Search reports... | Raadi warbixinno... | app/templates/admin/incidents.html | 23 | Search placeholder |
| All Statuses | Dhammaan Xaaladaha | app/templates/admin/incidents.html | 24 | Filter label |
| Pending Review | La Eegayaa | app/templates/admin/incidents.html | 25 | Filter label |
| Under Investigation | La Baarayaa | app/templates/admin/incidents.html | 26 | Filter label |
| Resolved | La Xaliyay | app/templates/admin/incidents.html | 27 | Filter label |
| Rejected | La Diiday | app/templates/admin/incidents.html | 28 | Filter label |
| All Severities | Dhammaan Xad-dhaafka | app/templates/admin/incidents.html | 29 | Filter label |
| All Categories | Dhammaan Qaybaha | app/templates/admin/incidents.html | 30 | Filter label |
| Exam Room | Qolka Imtixaanka | app/templates/admin/incidents.html | 31 | Filter label |
| Subject | Maado | app/templates/admin/incidents.html | 32 | Filter label |
| All Sessions | Dhammaan Kulamada | app/templates/admin/incidents.html | 33 | Filter label |
| Reset | Dib u bilow | app/templates/admin/incidents.html | 34 | Button label |
| Apply Filters | Dhex-gal Shaqooyinka | app/templates/admin/incidents.html | 35 | Button label |
| Total Reports | Wadarta Warbixinno | app/templates/admin/incidents.html | 36 | Stat card label |
| Critical | Aduun | app/templates/admin/incidents.html | 37 | Stat card label |
| High priority incidents | Dhacdado muhiimka ah | app/templates/admin/incidents.html | 38 | Stat card description |
| Serious | Jidh | app/templates/admin/incidents.html | 39 | Stat card label |
| Requires attention | Waa lagu baahan yahay diir | app/templates/admin/incidents.html | 40 | Stat card description |

### Incident View

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| View Incident Report | Eeg Warbixinta Dhacdada | app/templates/admin/incident_view.html | 2 | Page title |
| Incident Report Details | Faahfaahinta Warbixinta Dhacdada | app/templates/admin/incident_view.html | 3 | Page title |
| Back to Reports | Dib Warbixinno | app/templates/admin/incident_view.html | 8 | Button label |
| Edit Report | Tifatir Warbixin | app/templates/admin/incident_view.html | 11 | Button label |
| Report Number | Lambarka Warbixinta | app/templates/admin/incident_view.html | 20 | Label |
| Student Information | Macluumaadka Ardayda | app/templates/admin/incident_view.html | 33 | Section heading |
| Student ID: | Tirada Ardayda: | app/templates/admin/incident_view.html | 45 | Label |
| Class: | Fasal: | app/templates/admin/incident_view.html | 49 | Label |
| Section: | Qayb: | app/templates/admin/incident_view.html | 53 | Label |
| Academic Year: | Sanadka Dugsiga: | app/templates/admin/incident_view.html | 57 | Label |
| Invigilator Information | Macluumaadka Rukhsadaha Imtixaanka | app/templates/admin/incident_view.html | 67 | Section heading |
| Invigilator ID: | Tirada Rukhsadaha Imtixaanka: | app/templates/admin/incident_view.html | 79 | Label |
| Username: | Magaca isticmaalka: | app/templates/admin/incident_view.html | 83 | Label |
| Role: | Door: | app/templates/admin/incident_view.html | 87 | Label |
| Submission Date: | Taariikhda Soo saarista: | app/templates/admin/incident_view.html | 91 | Label |
| Incident Details | Faahfaahinta Dhacdada | app/templates/admin/incident_view.html | 100 | Section heading |

### Incident Form

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Submit Incident Report | Soo dir Warbixinta Dhacdada | app/templates/incident_form.html | 2 | Page title |
| EXAMINATION INCIDENT REPORT | WARBIXINTA DHACDADA IMTIXAANKA | app/templates/incident_form.html | 16 | Header badge |
| Back | Dib | app/templates/incident_form.html | 22 | Link label |
| Student ID | Tirada Ardayda | app/templates/incident_form.html | 48 | Label |
| Class | Fasal | app/templates/incident_form.html | 55 | Label |
| Section | Qayb | app/templates/incident_form.html | 62 | Label |
| Academic Year | Sanadka Dugsiga | app/templates/incident_form.html | 69 | Label |
| Exam Type | Nooca Imtixaanka | app/templates/incident_form.html | 76 | Label |
| No Active Exam Found | Imtixaan Firfircoon lama helin | app/templates/incident_form.html | 77 | Empty value |
| Status | Xaalada | app/templates/incident_form.html | 83 | Label |
| ACTIVE STUDENT | ARDAY FIRFIRCOON | app/templates/incident_form.html | 84 | Status value |
| Invigilator Information | Macluumaadka Rukhsadaha Imtixaanka | app/templates/incident_form.html | 105 | Section heading |
| Full Name | Magac oo dhan | app/templates/incident_form.html | 110 | Label |
| Invigilator ID | Tirada Rukhsadaha Imtixaanka | app/templates/incident_form.html | 117 | Label |
| Username | Magaca isticmaalka | app/templates/incident_form.html | 124 | Label |
| Role | Door | app/templates/incident_form.html | 131 | Label |
| Incident Details | Faahfaahinta Dhacdada | app/templates/incident_form.html | 149 | Section heading |
| Incident Category | Qaybta Dhacdada | app/templates/incident_form.html | 153 | Label |
| Select category | Dooro qayb | app/templates/incident_form.html | 155 | Option |
| Severity Level | Heerka Xad-dhaafka | app/templates/incident_form.html | 164 | Label |
| Exam Type | Nooca Imtixaanka | app/templates/incident_form.html | 178 | Label |
| No Active Exam Found | Imtixaan Firfircoon lama helin | app/templates/incident_form.html | 180 | Readonly value |
| Subject | Maado | app/templates/incident_form.html | 186 | Label |
| Select subject (optional) | Dooro maado (ikhtiyaari ah) | app/templates/incident_form.html | 188 | Option |
| Exam Room | Qolka Imtixaanka | app/templates/incident_form.html | 200 | Label |
| Please complete all highlighted required fields before submitting. | Fadlan dhamaystir dhammaan xeeraha la iftiimay ka hor inta aad soo dirayso. | app/templates/incident_form.html | 144 | Validation message |
| Please select a Category. | Fadlan dooro Qayb. | app/templates/incident_form.html | 154 | Validation message |
| Please select a Severity Level. | Fadlan dooro Heerka Xad-dhaafka. | app/templates/incident_form.html | 168 | Validation message |
| Please select a Subject. | Fadlan dooro Maado. | app/templates/incident_form.html | 187 | Validation message |
| This field is required. | Xerkan waa lagu baahan yahay. | app/templates/incident_form.html | 551 | Default validation message |
| file(s) selected | file(s) la doortay | app/templates/incident_form.html | 592 | Upload success message |

### Incident Success

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Incident Report Submitted | Warbixinta Dhacdada La Soo diray | app/templates/incident_success.html | 2 | Page title |
| Incident Report Submitted Successfully | Warbixinta Dhacdada La Soo diray Si Guul Leh | app/templates/incident_success.html | 13 | Success heading |
| Your report has been recorded and will be reviewed by administration. | Warbixintaada waa la qabtay oo waxaa la eegayaa maamulka. | app/templates/incident_success.html | 14 | Success message |
| Report Number: | Lambarka Warbixinta: | app/templates/incident_success.html | 18 | Label |
| Student: | Arday: | app/templates/incident_success.html | 22 | Label |
| Student ID: | Tirada Ardayda: | app/templates/incident_success.html | 26 | Label |
| Category: | Qayb: | app/templates/incident_success.html | 30 | Label |
| Severity: | Xad-dhaafka: | app/templates/incident_success.html | 34 | Label |
| Status: | Xaalada: | app/templates/incident_success.html | 40 | Label |
| Submitted: | La Soo diray: | app/templates/incident_success.html | 44 | Label |
| Scan Another QR Code | Akhri QR Code Kale | app/templates/incident_success.html | 51 | Button label |
| Logout | Ka bax | app/templates/incident_success.html | 54 | Button label |
| You will be notified when the administration reviews this report. | Waxaa la soo waco marka maamulku eego warbixintan. | app/templates/incident_success.html | 60 | Note message |

### Incident Validation Messages

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Invalid incident date | Taariikhda dhacdada waa khalkhaali ah | app/routes_public.py | 32 | ValueError |
| Invalid incident time | Waqtiga dhacdada waa khalkhaali ah | app/routes_public.py | 42 | ValueError |
| Please log in as an invigilator to submit an incident report. | Fadlan ku soo gudub sida rukhsadaha imtixaanka si aad u soo dirto warbixinta dhacdada. | app/routes_public.py | 354 | Flash message (warning) |
| Incident Time is required. | Waqtiga Dhacdada waa lagu baahan yahay. | app/routes_public.py | 398 | Validation error |
| Incident categories and severity levels must be configured before submitting reports. | Qaybaha dhacdada iyo heerka xad-dhaafka waa in la dejin ka hor inta aad soo dirto warbixinno. | app/routes_public.py | 411 | Flash message (danger) |
| No active exam found for this student. | Imtixaan firfircoon lama helin ardaydan. | app/routes_public.py | 417 | Flash message (danger) |
| Please enter a valid incident date and time. | Fadlan geli taariikh iyo waqtiga dhacdada sax ah. | app/routes_public.py | 423 | Flash message (danger) |
| Student ID not found. | Tirada Ardayda lama helin. | app/routes_public.py | 204 | JSON error message |

---

## Public Pages Module

### Result Portal

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Result Portal | Portal-ka Natiijooyinka | app/templates/portal.html | 2 | Page title suffix |
| Contact / Help | La Xiriir / Caawimaad | app/templates/portal.html | 99 | Link title |
| Help | Caawimaad | app/templates/portal.html | 100 | Link label |
| Language | Luuqada | app/templates/portal.html | 104 | Select aria-label |
| Somali | Soomaali | app/templates/portal.html | 105 | Option |
| English | English | app/templates/portal.html | 106 | Option |
| Arabic | Carabi | app/templates/portal.html | 107 | Option |
| Turkish | Turkish | app/templates/portal.html | 108 | Option |
| School | Dugsiga | app/templates/portal.html | 15 | School name placeholder |
| NATIIJADA IMTIXAANKA FINAL-KA | NATIIJADA IMTIXAANKA FINAL-KA | app/templates/portal.html | 122 | Exam title |
| Academic Year | Sanadka Dugsiga | app/templates/portal.html | 123 | Label |
| photo | sawir | app/templates/portal.html | 134, 177, 179 | Alt text |
| Default student avatar | Avatar ardayda hore | app/templates/portal.html | 179 | Alt text |
| Verified | La Xaqiijiyay | app/templates/portal.html | 136 | Badge label |
| Step 1 of 2 | Tallaabo 1 of 2 | app/templates/portal.html | 140 | Progress label |
| Select Academic Year | Dooro Sanad Dugsiga | app/templates/portal.html | 140 | Progress title |
| Step 2 of 2 | Tallaabo 2 of 2 | app/templates/portal.html | 163 | Progress title (JS) |
| Select Exam Type | Dooro Nooca Imtixaanka | app/templates/portal.html | 163 | Progress title (JS) |
| Select Academic Year | Dooro Sanad Dugsiga | app/templates/portal.html | 142 | Step heading |
| Choose the academic record you want to view. | Dooro qoraalka akademicska aad rabto inaad eegto. | app/templates/portal.html | 142 | Step description |
| Academic Year | Sanadka Dugsiga | app/templates/portal.html | 142 | Choice subtitle |
| Select Exam Type | Dooro Nooca Imtixaanka | app/templates/portal.html | 143 | Step heading |
| Choose an examination from the selected academic year. | Dooro imtixaan ka mid ah sanadka dugsiga la doortay. | app/templates/portal.html | 143 | Step description |
| Examination | Imtixaan | app/templates/portal.html | 143 | Choice subtitle |
| No published examinations are available for this year. | Imtixaan la daah-furay ma helo sanadkan. | app/templates/portal.html | 143 | Empty state |
| Back | Dib | app/templates/portal.html | 145 | Button label |
| ARAG NATIIJADA | EEG NATIIJADA | app/templates/portal.html | 145 | Button label |
| Academic record | Qoraalka akademicska | app/templates/portal.html | 185 | Kicker |
| Select an academic record to continue. | Dooro qoraalka akademicska si aad u sii socoto. | app/templates/portal.html | 187 | Description |
| Academic Year | Sanadka Dugsiga | app/templates/portal.html | 195 | Label |
| Exam Type | Nooca Imtixaanka | app/templates/portal.html | 203 | Label |
| ARAG NATIIJADA | EEG NATIIJADA | app/templates/portal.html | 210 | Button label |
| Fadlan Halakan geli Tira-taxanaha | Fadlan Halakan geli Tira-taxanaha | app/templates/portal.html | 240 | Placeholder |
| Fadlan halakan geli tira-taxanaha | Fadlan halakan geli tira-taxanaha | app/templates/portal.html | 241 | Label |
| Phone Number | Lambarka Telifoonka | app/templates/portal.html | 245, 246 | Label |
| RAADI | RAADI | app/templates/portal.html | 249 | Button label |
| Geli ID-ga si aad u aragto natiijada | Geli ID-ga si aad u aragto natiijada | app/templates/portal.html | 250 | Hint text |
| photo | sawir | app/templates/portal.html | 270, 271 | Alt text |
| Default student avatar | Avatar ardayda hore | app/templates/portal.html | 270 | Alt text |
| logo | logo | app/templates/portal.html | 271 | Alt text |
| Mother's Name | Magaca Hooyada | app/templates/portal.html | 276 | Label |
| Student ID | Tirada Ardayda | app/templates/portal.html | 277 | Label |
| Student Class | Fasalka Ardayda | app/templates/portal.html | 278 | Label |
| Exam Type | Nooca Imtixaanka | app/templates/portal.html | 279 | Label |
| Date Issued | Taariikhda Soo saarista | app/templates/portal.html | 280 | Label |
| Subject Percentage | Dhibcaha Maaddada | app/templates/portal.html | 281 | Label |
| logo | logo | app/templates/portal.html | 284 | Alt text |
| School Name | Magaca Dugsiga | app/templates/portal.html | 285 | Label |
| School Motto | Shahaada Dugsiga | app/templates/portal.html | 286 | Label |
| Academic Year | Sanadka Dugsiga | app/templates/portal.html | 294 | Label |
| SOO KOOBID | SOO KOOBID | app/templates/portal.html | 319 | Heading |
| Total Subjects | Wadarta Maaddada | app/templates/portal.html | 320 | Label |
| Total Marks | Wadarta Dhibcaha | app/templates/portal.html | 321 | Label |
| Total Obtained Marks | Wadarta Dhibcaha La Helay | app/templates/portal.html | 322 | Label |
| Average Percentage | Dhibcaha Dhexdhexaadka | app/templates/portal.html | 323 | Label |
| Overall Grade | Darajada Guud | app/templates/portal.html | 324 | Label |
| Position in Class | Goobta Fasalka | app/templates/portal.html | 325 | Label |
| Final Status | Xaalada Dhamaystirka | app/templates/portal.html | 326 | Label |
| PROMOTED | LA DIB U DHISAY | app/templates/portal.html | 326 | Status value |
| NOT PROMOTED | LA DIB U DHISAY | app/templates/portal.html | 326 | Status value |
| COMMENT | FAALLO | app/templates/portal.html | 330 | Heading |
| SIGNATURE | TIXRAAC | app/templates/portal.html | 336 | Label |
| Official signature | Tixraac rasmi ah | app/templates/portal.html | 338 | Alt text |
| Signature | Tixraac | app/templates/portal.html | 340 | Placeholder |
| STAMP | TAMARKA | app/templates/portal.html | 344 | Label |
| School stamp | Tamarka dugsiga | app/templates/portal.html | 346 | Alt text |
| TIS | TIS | app/templates/portal.html | 348 | Placeholder |
| Grade Scale | Scale Darajada | app/templates/portal.html | 358 | Heading |
| Percentage | Dhibcaha | app/templates/portal.html | 360 | Table header |
| Grade | Darajada | app/templates/portal.html | 360 | Table header |
| Point | Dhib | app/templates/portal.html | 360 | Table header |
| Performance Overview | Faahfaahinta Wada-shaqada | app/templates/portal.html | 367 | Heading |
| Students | Ardayda | app/templates/portal.html | 170 | Center label |
| Average | Dhexdhexaad | app/templates/portal.html | 175 | Center label |
| Tap or hover a segment | Guji ama dhex-gal qayb | app/templates/portal.html | 377 | Tooltip |
| Download Report | Dhoof Warbixin | app/templates/portal.html | 383 | Button label |
| PDF | PDF | app/templates/portal.html | 383 | Button subtitle |
| Print Result | Daabac Natiijada | app/templates/portal.html | 384 | Button label |
| Print | Daabac | app/templates/portal.html | 384 | Button subtitle |
| Share Result | Wadaag Natiijada | app/templates/portal.html | 385 | Button label |
| Share | Wadaag | app/templates/portal.html | 385 | Button subtitle |
| All Rights Reserved. | Dhammaan Xuquuqaha Waa La Kaydiyay. | app/templates/portal.html | 392 | Footer text |
| Phone | Telifoon | app/templates/portal.html | 395 | Link aria-label |
| WhatsApp | WhatsApp | app/templates/portal.html | 397 | Link aria-label |
| Facebook | Facebook | app/templates/portal.html | 398 | Link aria-label |
| Telegram | Telegram | app/templates/portal.html | 399 | Link aria-label |
| Website | Websaydhka | app/templates/portal.html | 401 | Link aria-label |
| Gmail | Gmail | app/templates/portal.html | 403 | Link aria-label |
| Map | Map | app/templates/portal.html | 405 | Link aria-label |
| error | khalad | app/templates/portal.html | 425 | Error variable |

### Verification Page

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Invalid Result | Natiijada Khalkhaali ah | app/templates/verify.html | 2 | Page title (default) |
| Student | Arday | app/templates/verify.html | 73 | Eyebrow label |
| Student ID | Tirada Ardayda | app/templates/verify.html | 77 | Label |
| Class | Fasal | app/templates/verify.html | 78 | Label |
| Examination | Imtixaan | app/templates/verify.html | 79 | Label |
| Academic Year | Sanadka Dugsiga | app/templates/verify.html | 80 | Label |
| Result Summary | Xogta Natiijada | app/templates/verify.html | 86 | Section heading |
| Total Marks | Wadarta Dhibcaha | app/templates/verify.html | 89 | Label |
| Percentage | Dhibcaha | app/templates/verify.html | 92 | Label |
| Verification Details | Faahfaahinta Xaqiijinta | app/templates/verify.html | 98 | Section heading |
| Verification Status | Xaalada Xaqiijinta | app/templates/verify.html | 100 | Label |
| Verification ID | Tirada Xaqiijinta | app/templates/verify.html | 101 | Label |
| VERIFIED | LA XAQIJIYAY | app/templates/verify.html | 101 | Default value |
| Verified Date | Taariikhda Xaqiijinta | app/templates/verify.html | 102 | Label |
| Verified Time | Waqtiga Xaqiijinta | app/templates/verify.html | 103 | Label |
| Issued by | La soo saaray | app/templates/verify.html | 118 | Label |
| Official Digital Seal | Tamarka Dijitaalka Rasmi ah | app/templates/verify.html | 113 | Seal text |
| Unavailable | La heli karo | app/templates/verify.html | 126 | Status label |
| Academic verification is currently unavailable. | Xaqiijinta akademicska hadda waa la heli karo. | app/templates/verify.html | 127 | Description |
| This verification link is invalid or no longer active. | Link-ka Xaqiijinta waa khalkhaali ah ama weli firfircoon ma aha. | app/templates/verify.html | 127 | Description |
| logo | logo | app/templates/verify.html | 40, 42 | Alt text |
| photo | sawir | app/templates/verify.html | 64, 66 | Alt text |
| Default student photo | Sawir ardayda hore | app/templates/verify.html | 66 | Alt text |
| official seal | tamarka rasmi ah | app/templates/verify.html | 110 | Alt text |
| Invalid Result | Natiijada Khalkhaali ah | app/templates/verify.html | 126 | Status label |
| Invalid Result | Natiijada Khalkhaali ah | app/templates/verify.html | 2 | Page title (default) |

### Verified ID Card

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Verified Student ID | Tirada Ardayda La Xaqiijiyay | app/templates/verify_id.html | 2 | Page title |
| Invalid ID Card | Baasaboorta Khalkhaali ah | app/templates/verify_id.html | 2 | Page title |
| Official Student Identity Verification | Xaqiijinta Aqoonsiga Ardayda Rasmi ah | app/templates/verify_id.html | 182 | Header subtitle |
| logo | logo | app/templates/verify_id.html | 165, 167, 176, 178 | Alt text |
| watermark | watermark | app/templates/verify_id.html | 165, 167 | Alt text |
| VERIFIED STUDENT | ARDAY LA XAQIJIYAY | app/templates/verify_id.html | 191 | Badge text |
| Student ID | Tirada Ardayda | app/templates/verify_id.html | 216 | Label |
| Mother's Name | Magaca Hooyada | app/templates/verify_id.html | 224 | Label |
| Class / Grade | Fasal / Darajada | app/templates/verify_id.html | 232 | Label |
| Section | Qayb | app/templates/verify_id.html | 247 | Label |
| Academic Year | Sanadka Dugsiga | app/templates/verify_id.html | 262 | Label |
| Exam Type | Nooca Imtixaanka | app/templates/verify_id.html | 269 | Label |
| No Active Exam Found | Imtixaan Firfircoon lama helin | app/templates/verify_id.html | 270 | Empty value |
| Issue Date | Taariikhda Soo saarista | app/templates/verify_id.html | 276 | Label |
| Expiry Date | Taariikhda Dhamaanka | app/templates/verify_id.html | 283 | Label |
| Status | Xaalada | app/templates/verify_id.html | 297 | Heading |
| This student is currently active and in good standing. | Ardaydan hadda waa firfircoon oo waa mid wanaagsan. | app/templates/verify_id.html | 299 | Status message |
| Official Verification Stamp | Tamarka Xaqiijinta Rasmi ah | app/templates/verify_id.html | 308 | Alt text |
| OFFICIALLY | RASMII AH | app/templates/verify_id.html | 314 | Stamp main text |
| VERIFIED | LA XAQIJIYAY | app/templates/verify_id.html | 315 | Stamp sub text |
| Verification Code | Code-ka Xaqiijinta | app/templates/verify_id.html | 327 | Label |
| Date & Time | Taariikh & Waqtiga | app/templates/verify_id.html | 334 | Label |
| This student ID has been officially verified by | Tirada ardaydan waxaa la xaqiijiyay rasmi ah | app/templates/verify_id.html | 347 | Footer text |
| SULTAN | SULTAN | app/templates/verify_id.html | 350 | Copyright text |
| 2026 | 2026 | app/templates/verify_id.html | 350 | Copyright year |
| Invalid ID Card | Baasaboorta Khalkhaali ah | app/templates/verify_id.html | 361 | Heading |
| This verification link is invalid or no longer recognized by the system. | Link-ka xaqiijinta waa khalkhaali ah ama nidaamku weli yaqaan. | app/templates/verify_id.html | 362 | Description |
| Back to Portal | Dib Portal-ka | app/templates/verify_id.html | 363 | Button label |
| photo | sawir | app/templates/verify_id.html | 200, 202 | Alt text |

### Locked Result

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Result Temporarily Withheld | Natiijada Waa La Xiray Dhowaan | app/templates/locked_result.html | 2 | Page title |
| Result Lock Notice | Ogaysiiska Xirista Natiijada | app/templates/locked_result.html | 8 | Eyebrow label |
| Your examination result has been temporarily withheld. | Natiijada imtixaankaaga waa la xiray dhowaan. | app/templates/locked_result.html | 9 | Main message |
| Please visit the Finance Office to complete the required clearance before your result can be released. | Fadlan booqo Xafiiska Maaliyada si aad u dhamaystirto xirista lagu baahan yahay ka hor inta aad daah-furto natiijadaada. | app/templates/locked_result.html | 10 | Instructions |
| Student ID | Tirada Ardayda | app/templates/locked_result.html | 12 | Label |
| Student | Arday | app/templates/locked_result.html | 13 | Label |
| Reason | Sabab | app/templates/locked_result.html | 14 | Label |
| Clearance required | Xirista lagu baahan yahay | app/templates/locked_result.html | 14 | Default value |
| Back to Portal | Dib Portal-ka | app/templates/locked_result.html | 16 | Button label |

### Print Report

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Report Card - | Baasaboorta - | app/templates/print_report.html | 5 | Page title prefix |
| Magaca Ardeyga | Magaca Ardeyga | app/templates/print_report.html | 87 | Heading |
| Magaca Hooyada | Magaca Hooyada | app/templates/print_report.html | 94 | Label |
| Tirataxaane (ID) | Tirataxaane (ID) | app/templates/print_report.html | 95 | Label |
| Fasalka | Fasalka | app/templates/print_report.html | 96 | Label |
| Download Date | Taariikhda Dhoofinta | app/templates/print_report.html | 97 | Label |
| Maado | Maado | app/templates/print_report.html | 109 | Table header |
| Full Marks | Dhibcaha Ugu Badan | app/templates/print_report.html | 109 | Table header |
| Marks Obtained | Dhibcaha La Helay | app/templates/print_report.html | 109 | Table header |
| Grade | Darajada | app/templates/print_report.html | 109 | Table header |
| Remarks | Faallooyinka | app/templates/print_report.html | 109 | Table header |
| Total Marks | Wadarta Dhibcaha | app/templates/print_report.html | 126 | Label |
| Marks Obtained | Dhibcaha La Helay | app/templates/print_report.html | 127 | Label |
| Percentage | Dhibcaha | app/templates/print_report.html | 128 | Label |
| Grade | Darajada | app/templates/print_report.html | 129 | Label |
| Rank | Tartanka | app/templates/print_report.html | 130 | Label |
| In Class | Fasalka | app/templates/print_report.html | 130 | Subtitle |
| Teacher signature | Tixraaca macalimka | app/templates/print_report.html | 139 | Alt text |
| Signature | Tixraac | app/templates/print_report.html | 139, 144, 145 | Placeholder |
| Class Teacher | Macalimka Fasalka | app/templates/print_report.html | Tixraac | Label |
| Teacher Signature | Tixraaca Macalimka | app/templates/print_report.html | 141 | Subtitle |
| Official signature | Tixraac rasmi ah | app/templates/print_report.html | 144 | Alt text |
| School stamp | Tamarka dugsiga | app/templates/print_report.html | 149 | Alt text |
| TIS | TIS | app/templates/print_report.html | 149 | Placeholder |
| photo | sawir | app/templates/print_report.html | 67, 90 | Alt text |
| logo | logo | app/templates/print_report.html | 67 | Alt text |
| Verification QR Code | QR Code-ka Xaqiijinta | app/templates/print_report.html | 100 | Alt text |

### QR Landing

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Student QR Code | QR Code-ka Ardayda | app/templates/qr_landing.html | 2 | Page title |
| School Logo | Logo-ka Dugsiga | app/templates/qr_landing.html | 12 | Alt text |
| School | Dugsiga | app/templates/qr_landing.html | 15 | School name placeholder |
| Scan QR Code to Access Student Information | Akhri QR Code si aad u hesho macluumaadka ardayda | app/templates/qr_landing.html | 16 | Subtitle |
| Verify Student | Xaqiiji Arday | app/templates/qr_landing.html | 25 | Card heading |
| Verify the student's official identity and view their ID card information. | Xaqiiji aqoonsiga rasmi ah ee ardayda iyo eeg macluumaadka baasaboorta. | app/templates/qr_landing.html | 26 | Card description |
| Public Access | Helitaanka Bulshada | app/templates/qr_landing.html | 28 | Badge label |
| Submit Incident Report | Soo dir Warbixinta Dhacdada | app/templates/qr_landing.html | 40 | Card heading |
| Report an examination incident involving this student (Teachers & Admin only). | Warbixin dhacdada imtixaanka ardaydan (Macalimiinta & Maamulka oo keliya). | app/templates/qr_landing.html | 41 | Card description |
| Staff Only | Shaqaale oo keliya | app/templates/qr_landing.html | 43 | Badge label |
| Secure • Professional • Reliable | Nadiif • Xirfad leh • La yaqiin karo | app/templates/qr_landing.html | 53 | Footer copyright |

---

## Audit Module

### Audit Logs

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Audit Log | Qoraalka Baaritaanka | app/templates/admin/base.html | 35 | Sidebar menu item |
| Audit Log | Qoraalka Baaritaanka | app/templates/admin/audit_logs.html | 2 | Page title |
| Security Audit Log | Qoraalka Baaritaanka Nabadgelyada | app/templates/admin/audit_logs.html | 5 | Section heading |
| Login, logout, publishing, locking, settings, permissions, and import activity. | Login, logout, daah-fur, xir, dejinta, ogolaanshaha, iyo dhaqaaqda soo jiita. | app/templates/admin/audit_logs.html | 5 | Section description |
| Date / Time | Taariikh / Waqtiga | app/templates/admin/audit_logs.html | 8 | Table header |
| Username | Magaca isticmaalka | app/templates/admin/audit_logs.html | 8 | Table header |
| IP Address | Cinwaanka IP | app/templates/admin/audit_logs.html | 8 | Table header |
| Action | Dhaqaaq | app/templates/admin/audit_logs.html | 8 | Table header |
| Details | Faahfaahinta | app/templates/admin/audit_logs.html | 8 | Table header |
| No audit records yet. | Qoraal baaritaan weli ma jiro. | app/templates/admin/audit_logs.html | 13 | Empty state |

---

## Analytics Module

### Analytics Dashboard

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Analytics — Infographic | Xisaab-yada — Infographic | app/templates/admin/analytics.html | 3 | Page title |
| Academic Year | Sanadka Dugsiga | app/templates/admin/analytics.html | 13 | Breadcrumb |
| Exam Type | Nooca Imtixaanka | app/templates/admin/analytics.html | 15 | Breadcrumb |
| Analytics | Xisaab-yada | app/templates/admin/analytics.html | 17 | Breadcrumb active |
| Select Exam | Dooro Imtixaan | app/templates/admin/analytics.html | 26 | Option |
| Level | Heer | app/templates/admin/analytics.html | 37 | Filter label |
| All Levels | Dhammaan Heerka | app/templates/admin/analytics.html | 39 | Option |
| Class | Fasal | app/templates/admin/analytics.html | 47 | Filter label |
| All Classes | Dhammaan Fasallada | app/templates/admin/analytics.html | 49 | Option |
| Section | Qayb | app/templates/admin/analytics.html | 57 | Filter label |
| All Sections | Dhammaan Qaybaha | app/templates/admin/analytics.html | 59 | Option |
| Subject | Maado | app/templates/admin/analytics.html | 67 | Filter label |
| All Subjects | Dhammaan Maadooyinka | app/templates/admin/analytics.html | 69 | Option |
| Total Students | Wadarta Ardayda | app/templates/admin/analytics.html | 84 | KPI label |
| Active enrollment | Diiwaanka firfircoonka ah | app/templates/admin/analytics.html | 85 | KPI subtitle |
| Total Results | Wadarta Natiijooyinka | app/templates/admin/analytics.html | 94 | KPI label |
| Recorded grades | Darajada la qabtay | app/templates/admin/analytics.html | 95 | KPI subtitle |
| Overall Average | Dhexdhexaad Guud | app/templates/admin/analytics.html | 104 | KPI label |
| Class performance |  Wada-shaqada fasalka | app/templates/admin/analytics.html | 105 | KPI subtitle |
| Pass Rate | Heerka Guulaha | app/templates/admin/analytics.html | 114 | KPI label |
| passed | la xaliyay | app/templates/admin/analytics.html | 115 | KPI subtitle |
| Fail Rate | Heerka Guuldareyska | app/templates/admin/analytics.html | 124 | KPI label |
| failed | la guuldareyay | app/templates/admin/analytics.html | 125 | KPI subtitle |
| Highest Score | Dhibcaha Ugu Badan | app/templates/admin/analytics.html | 134 | KPI label |
| Top achievement | Guul ugu sarreysa | app/templates/admin/analytics.html | 135 | KPI subtitle |
| Grade Distribution | Qaybinta Darajada | app/templates/admin/analytics.html | 142 | Card heading |
| Subject-wise Performance | Wada-shaqada Maaddada | app/templates/admin/analytics.html | 193 | Card heading |
| students ( | ardayda ( | app/templates/admin/analytics.html | 182 | Legend text |
| %) | %) | app/templates/admin/analytics.html | 182 | Legend text |
| No data available | Macluumaad lama helin | app/templates/admin/analytics.html | 186 | Empty state |

---

## Academic Structure Module

### Academic Structure

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| System Setup | Dejinta Nidaamka | app/templates/academic_structure/index.html | 2 | Page title |
| Redirecting to System Setup... | La wadaaggo Dejinta Nidaamka... | app/templates/academic_structure/index.html | 8 | Heading |
| All academic configuration has been moved to the System Setup page. | Dhammaan dejinta akademicska waa la wareejiyay bogga Dejinta Nidaamka. | app/templates/academic_structure/index.html | 9 | Description |
| Academic Levels | Heerka Akademicska | app/templates/academic_structure/levels.html | 2 | Page title |
| Academic Levels | Heerka Akademicska | app/templates/academic_structure/levels.html | 5 | Page heading |
| New Level | Heer Cusub | app/templates/academic_structure/levels.html | 7 | Button label |
| Name | Magac | app/templates/academic_structure/levels.html | 15 | Table header |
| Sort Order | Tartanka | app/templates/academic_structure/levels.html | 16 | Table header |
| Classes | Fasallada | app/templates/academic_structure/levels.html | 17 | Table header |
| Status | Xaalada | app/templates/academic_structure/levels.html | 18 | Table header |
| Actions | Dhaqaaqyo | app/templates/academic_structure/levels.html | 19 | Table header |
| Active | Firfircoon | app/templates/academic_structure/levels.html | 30 | Status badge |
| Inactive | Fir-fircoona | app/templates/academic_structure/levels.html | 32 | Status badge |
| Delete this level? | Tirtir heerkan? | app/templates/academic_structure/levels.html | 40 | Confirm dialog |
| Academic Sections | Qaybaha Akademicska | app/templates/academic_structure/sections.html | 2 | Page title |
| Academic Sections | Qaybaha Akademicska | app/templates/academic_structure/sections.html | 5 | Page heading |
| New Section | Qayb Cusub | app/templates/academic_structure/sections.html | 7 | Button label |
| Level | Heer | app/templates/academic_structure/sections.html | 15 | Table header |
| Class | Fasal | app/templates/academic_structure/sections.html | 16 | Table header |
| Section Name | Magaca Qaybta | app/templates/academic_structure/sections.html | 17 | Table header |
| Sort Order | Tartanka | app/templates/academic_structure/sections.html | 18 | Table header |
| Status | Xaalada | app/templates/academic_structure/sections.html | 19 | Table header |
| Actions | Dhaqaaqyo | app/templates/academic_structure/sections.html | 20 | Table header |
| Active | Firfircoon | app/templates/academic_structure/sections.html | 32 | Status badge |
| Inactive | Fir-fircoona | app/templates/academic_structure/sections.html | 34 | Status badge |
| Delete this section? | Tirtir qaybtan? | app/templates/academic_structure/sections.html | 42 | Confirm dialog |
| Academic level not found. | Heerka akademicska lama helin. | app/routes_academic_structure.py | 61 | Flash message (danger) |
| Academic class not found. | Fasalka akademicska lama helin. | app/routes_academic_structure.py | 113 | Flash message (danger) |
| Academic section not found. | Qaybta akademicska lama helin. | app/routes_academic_structure.py | 201 | Flash message (danger) |
| Academic level already exists. | Heerka akademicska hore ayaa jirta. | app/routes_admin.py | 2143, 2174 | JSON error message |
| Class already exists in this level. | Fasal hore ayaa jirta heerkan. | app/routes_admin.py | 2245, 2277 | JSON error message |
| Academic level is required. | Heerka akademicska waa lagu baahan yahay. | app/routes_admin.py | 2275 | JSON error message |

---

## Login & Authentication Module

### Admin Authentication

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Current password is incorrect. | Ereyga sirta ah hadda waa khalkhaali ah. | app/routes_auth.py | 67 | Flash message (danger) |
| Password must be at least 8 characters. | Ereyga sirta ah waa inuu yahay ugu yaraan siddeed xaraf. | app/routes_auth.py | 69 | Flash message (danger) |
| Passwords do not match. | Ereyada sirta ah ma midba midkaabaan. | app/routes_auth.py | 71 | Flash message (danger) |
| Password must be at least {min_length} characters. | Ereyga sirta ah waa inuu yahay ugu yaraan {min_length} xaraf. | app/routes_admin.py | 76 | Password validation error |
| Password must contain numbers only. | Ereyga sirta ah waa inuu ka kooban yahay tiro oo keliya. | app/routes_admin.py | 78 | Password validation error |
| Password must contain letters only. | Ereyga sirta ah waa inuu ka kooban yahay xaraf oo keliya. | app/routes_admin.py | 80 | Password validation error |
| Password must include letters and numbers. | Ereyga sirta ah waa inuu ka kooban yahay xaraf iyo tiro. | app/routes_admin.py | 82 | Password validation error |
| Admin photo must be JPG, PNG, or WEBP. | Sawirka maamulka waa inuu yahay JPG, PNG, ama WEBP. | app/routes_admin.py | 572 | Flash message (danger) |
| New password must be at least 8 characters. | Ereyga sirta ah cusub waa inuu yahay ugu yaraan siddeed xaraf. | app/routes_admin.py | 599 | Flash message (danger) |
| Uploaded images must be JPG, PNG, or WEBP. | Sawirrada la soo jiitay waa inay yahiin JPG, PNG, ama WEBP. | app/routes_admin.py | 963 | Flash message (danger) |
| Uploaded subject icons must be JPG, PNG, or WEBP. | Icon-ka maaddada la soo jiitay waa inuu yahay JPG, PNG, ama WEBP. | app/routes_admin.py | 975 | Flash message (danger) |

### Teacher Authentication

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Teacher ID is required and must be entered manually. | Tirada macalimka waa lagu baahan yahay oo waa inuu la geliyo gacanta. | app/routes_teachers.py | 96 | ValueError |
| Teacher ID already exists. | Tirada macalimka hore ayaa jirta. | app/routes_teachers.py | 99 | ValueError |
| Photo must be JPG, PNG, or WEBP. | Sawirka waa inuu yahay JPG, PNG, ama WEBP. | app/routes_teachers.py | 126 | ValueError |
| Passwords do not match. | Ereyada sirta ah ma midba midkaabaan. | app/routes_teachers.py | 154 | ValueError |
| Teacher saved successfully. | Macalimku waa la kaydiyay si guul leh. | app/routes_teachers.py | 166 | Flash message (success) |
| Teacher deleted. | Macalimku waa la tirtiray. | app/routes_teachers.py | 212 | Flash message (success) |
| Teacher permissions saved. | Ogolaanshaha macalimka waa la kaydiyay. | app/routes_teachers.py | 225 | Flash message (success) |
| Teacher settings saved. | Dejinta macalimka waa la kaydiyay. | app/routes_teachers.py | 293 | Flash message (success) |
| Teacher code already exists: {code} | Code-ka macalimka hore ayaa jirta: {code} | app/teacher_services.py | 169 | ValueError |
| Teacher code is required when auto-generation is disabled. | Code-ka macalimka waa lagu baahan yahay marka abuurista otomaatigga la xiro. | app/teacher_services.py | 172 | ValueError |
| Teacher code format must include {seq:04d} style placeholder. | Format-ka code-ka macalimka waa inuu ka kooban yahay placeholder-ka {seq:04d}. | app/teacher_services.py | 176 | ValueError |
| Unable to generate a unique teacher code. | Lama abuuri karo code macalim oo gaar ah. | app/teacher_services.py | 191 | ValueError |
| Username already exists: {username} | Magaca isticmaalka hore ayaa jirta: {username} | app/teacher_services.py | 224 | ValueError |
| Password is required for new teacher accounts. | Ereyga sirta ah waa lagu baahan yahay xisaabta macalimka cusub. | app/teacher_services.py | 235 | ValueError |
| Password must be at least {min_length} characters. | Ereyga sirta ah waa inuu yahay ugu yaraan {min_length} xaraf. | app/teacher_services.py | 210 | Password validation error |
| Password must include letters and numbers. | Ereyga sirta ah waa inuu ka kooban yahay xaraf iyo tiro. | app/teacher_services.py | 213 | Password validation error |

### Import Wizard

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Import Preview | Eeg Soojinta | app/templates/admin/import_wizard.html | 2 | Page title |
| Review validation results before committing. Imports with errors cannot be saved. | Eeg natiijada xaqiijinta ka hor inta aad dhamaystirto. Soojinta khalad ma kaydi karo. | app/templates/admin/import_wizard.html | 5 | Section description |
| Import blocked. Fix the errors below and upload again. | Soojinta la xiray. Qal khaladda hoos iyo soo jiitir mar kale. | app/templates/admin/import_wizard.html | 7 | Error message |
| Validation passed. {rows|length} rows ready. | Xaqiijinta waa guul. {rows|length} taxadar diyaar u ah. | app/templates/admin/import_wizard.html | 12 | Success message |
| Confirm Import | Xaqiiji Soojinta | app/templates/admin/import_wizard.html | 30 | Button label |
| Selected exam does not exist. | Imtixaanka la doortay ma jiro. | app/import_wizard.py | 75 | Import validation error |
| Row {row}: full_name is required. | Taxadar {row}: full_name waa lagu baahan yahay. | app/import_wizard.py | 110 | Import validation error |
| Row {row}: class does not exist: {data['class']} | Taxadar {row}: fasal ma jiro: {data['class']} | app/import_wizard.py | 112 | Import validation error |
| Row {row}: academic year does not exist: {data['academic_year']} | Taxadar {row}: sanad dugsiga ma jiro: {data['academic_year']} | app/import_wizard.py | 114 | Import validation error |
| Row {row}: student ID does not exist: {data['student_id']} | Taxadar {row}: tirada ardayda ma jiro: {data['student_id']} | app/import_wizard.py | 120 | Import validation error |
| Row {row}: subject does not exist: {data['subject']} | Taxadar {row}: maado ma jiro: {data['subject']} | app/import_wizard.py | 122 | Import validation error |

---

## JavaScript Files

### App.js

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Gudbay | Gudbay | app/static/js/app.js | 29 | Status value (Somali for "Pass") |

### Teacher Dashboard.js

| English Text | Somali Translation | File Path | Line | UI Location |
|-------------|------------------|-----------|------|-------------|
| Performance | Wada-shaqada | app/static/js/teacher-dashboard.js | 26 | Chart dataset label |

---

## Notes

- This document contains all user-visible English text extracted from the Exam System project
- Somali translations are suggested and should be reviewed by native Somali speakers
- Some text may already be in Somali (e.g., "Gudbay", "NATIIJADA IMTIXAANKA FINAL-KA") - these should be kept as-is
- Line numbers refer to the location in the source files
- UI locations indicate where the text appears in the interface (button, label, heading, menu, placeholder, table header, notification, validation message, etc.)
- This guide should be used as a reference for implementing internationalization (i18n) in the application

---

**Document Version:** 1.0  
**Last Updated:** July 23, 2026  
**Project:** Exam System Internationalization

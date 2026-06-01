# PMO Testcase Spec — Playwright Automation Arena

Tài liệu testcase phục vụ viết automation cho website mục tiêu: <https://bsv-nhungnguyen.github.io/>.

- Nguồn business testcase: Google Sheet `gid=194545409`.
- Mục tiêu: chuẩn hoa theo format PMO de map 1-1 vao test script Playwright.
- Pham vi: Frames/Iframes, Windows/Popups, Dialogs, Visual Regressions, Tracing, Hooks.

## 1) Thong tin chung

| Truong | Gia tri |
| --- | --- |
| Project | Playwright test 08.05.2026 |
| AUT | https://bsv-nhungnguyen.github.io/ |
| Test Type | UI Automation / E2E |
| Tool du kien | Playwright + Test Runner |
| Moi truong | Chromium (co the mo rong Firefox/WebKit) |
| Dinh danh testcase | `PMO-PLW-XXX` |

## 2) Danh sach testcase (PMO standard)

### PMO-PLW-001 — Iframe don submit thanh cong

| Truong | Noi dung |
| --- | --- |
| Module | Frames & Iframes |
| Muc tieu | Xac nhan thao tac trong simple iframe va submit form thanh cong |
| Pre-condition | Truy cap trang AUT, section `Frames & Iframes` |
| Test Data | Input bat ky, vi du: `hello iframe` |
| Test Steps | 1) Nhap gia tri vao `Simple Frame Form` trong iframe. 2) Click `Submit`. |
| Expected Result | Hien thi text `Success: Gia tri nhap!` trong iframe |
| Automation Checkpoint | Dinh vi dung frame, thao tac input/button trong frame va assert text trong frame |
| Priority | High |

### PMO-PLW-002 — Load nested frames va verify Iframe A

| Truong | Noi dung |
| --- | --- |
| Module | Frames & Iframes |
| Muc tieu | Xac nhan load nested frames va hien thi dung noi dung Iframe A |
| Pre-condition | Truy cap trang AUT |
| Test Steps | 1) Click `Load Nested Frames (A -> B -> C)` |
| Expected Result | Iframe A hien thi dung: title `Iframe A`, nut `Click button`, nut `Open Iframe B` |
| Automation Checkpoint | Define frame A chinh xac va assert cac element bat buoc |
| Priority | High |

### PMO-PLW-003 — Mo Iframe B tu Iframe A

| Truong | Noi dung |
| --- | --- |
| Module | Frames & Iframes |
| Muc tieu | Xac nhan mo duoc Iframe B va noi dung dung |
| Pre-condition | Da load nested frames |
| Test Steps | 1) Tu Iframe A, click `Open Iframe B` |
| Expected Result | Iframe B hien thi title `Iframe B`, nut `Click button`, nut `Open Iframe C` |
| Automation Checkpoint | Chuyen context frame A -> frame B dung va assert cac locator |
| Priority | High |

### PMO-PLW-004 — Mo Iframe C qua chuoi A -> B -> C

| Truong | Noi dung |
| --- | --- |
| Module | Frames & Iframes |
| Muc tieu | Xac nhan dieu huong nested frame den cap C |
| Pre-condition | Da load nested frames |
| Test Steps | 1) Mo Iframe B trong Iframe A. 2) Mo Iframe C trong Iframe B. |
| Expected Result | Iframe C hien thi title `Iframe C` va nut `Click button` |
| Automation Checkpoint | Chuyen frame theo nhieu tang va assert noi dung cap cuoi |
| Priority | High |

### PMO-PLW-005 — Click button trong Iframe C

| Truong | Noi dung |
| --- | --- |
| Module | Frames & Iframes |
| Muc tieu | Xac nhan action trong frame cap sau cung |
| Pre-condition | Da mo den Iframe C |
| Test Steps | 1) Click nut `Click button` trong Iframe C |
| Expected Result | Hien thi message `Iframe C Clicked!` |
| Automation Checkpoint | Click trong frame C va assert message sau action |
| Priority | High |

### PMO-PLW-006 — Open New Tab va thao tac tren tab moi

| Truong | Noi dung |
| --- | --- |
| Module | Windows & Popups |
| Muc tieu | Xac nhan handle tab moi thanh cong |
| Pre-condition | Truy cap trang AUT, section `Windows & Popups` |
| Test Steps | 1) Click `Open New Tab (playwright.dev)`. 2) Tren tab moi click `Get started`. |
| Expected Result | Tab moi hien thi title/heading `Installation` |
| Automation Checkpoint | Bat su kien page moi, switch context tab va assert title |
| Priority | High |

### PMO-PLW-007 — Open Popup Window

| Truong | Noi dung |
| --- | --- |
| Module | Windows & Popups |
| Muc tieu | Xac nhan popup mo dung noi dung |
| Pre-condition | Truy cap trang AUT |
| Test Steps | 1) Click `Open Popup Window` |
| Expected Result | Popup hien thi voi noi dung `Popup Activated` |
| Automation Checkpoint | Bat popup page va assert text trong popup |
| Priority | Medium |

### PMO-PLW-008 — Open in-page modal

| Truong | Noi dung |
| --- | --- |
| Module | Windows & Popups |
| Muc tieu | Xac nhan modal duoc hien thi dung |
| Pre-condition | Truy cap trang AUT |
| Test Steps | 1) Click `Open In-page Modal` |
| Expected Result | Modal hien thi tieu de `Secure Confirmation` |
| Automation Checkpoint | Assert modal visible va dung title |
| Priority | High |

### PMO-PLW-009 — Confirm modal voi verification code

| Truong | Noi dung |
| --- | --- |
| Module | Windows & Popups |
| Muc tieu | Xac nhan luong confirm modal tra ket qua dung |
| Pre-condition | Modal `Secure Confirmation` dang mo |
| Test Data | Verification code bat ky, vi du `123456` |
| Test Steps | 1) Nhap verification code. 2) Click `Confirm`. |
| Expected Result | Khu vuc ket qua hien thi `Verified: <code da nhap>` |
| Automation Checkpoint | Assert ket qua sau confirm dung voi input |
| Priority | High |

### PMO-PLW-010 — Cancel modal

| Truong | Noi dung |
| --- | --- |
| Module | Windows & Popups |
| Muc tieu | Xac nhan luong cancel khong submit gia tri |
| Pre-condition | Modal `Secure Confirmation` dang mo |
| Test Steps | 1) Nhap code bat ky. 2) Click `Cancel`. |
| Expected Result | Khong hien thi gia tri vua nhap trong `modal-result` |
| Automation Checkpoint | Assert result khong chua input da nhap |
| Priority | Medium |

### PMO-PLW-011 — Trigger Alert hien thi dung message

| Truong | Noi dung |
| --- | --- |
| Module | Native Dialogs |
| Muc tieu | Xac nhan browser alert duoc trigger |
| Pre-condition | Truy cap section `Native Dialogs` |
| Test Steps | 1) Click `Trigger Alert` |
| Expected Result | Alert hien thi message `This is a browser alert!` |
| Automation Checkpoint | Listen su kien dialog va assert message |
| Priority | High |

### PMO-PLW-012 — Accept Alert

| Truong | Noi dung |
| --- | --- |
| Module | Native Dialogs |
| Muc tieu | Xac nhan thao tac `OK` tren alert |
| Pre-condition | Alert da hien thi |
| Test Steps | 1) Click `OK` tren alert |
| Expected Result | Alert dong lai thanh cong |
| Automation Checkpoint | `dialog.accept()` va assert khong con alert mo |
| Priority | Medium |

### PMO-PLW-013 — Trigger Confirm hien thi `Continue?`

| Truong | Noi dung |
| --- | --- |
| Module | Native Dialogs |
| Muc tieu | Xac nhan confirm dialog hien thi dung noi dung |
| Pre-condition | Truy cap section `Native Dialogs` |
| Test Steps | 1) Click `Trigger Confirm` |
| Expected Result | Dialog hien thi message `Continue?` |
| Automation Checkpoint | Assert dialog type confirm va dung message |
| Priority | High |

### PMO-PLW-014 — Confirm dialog voi OK

| Truong | Noi dung |
| --- | --- |
| Module | Native Dialogs |
| Muc tieu | Xac nhan nhan `OK` tra ket qua `Confirmed` |
| Pre-condition | Confirm dialog dang mo |
| Test Steps | 1) Click `OK` |
| Expected Result | `confirm-result` hien thi `Confirmed` |
| Automation Checkpoint | Accept dialog va assert ket qua |
| Priority | High |

### PMO-PLW-015 — Confirm dialog voi Cancel

| Truong | Noi dung |
| --- | --- |
| Module | Native Dialogs |
| Muc tieu | Xac nhan nhan `Cancel` tra ket qua `Cancelled` |
| Pre-condition | Confirm dialog dang mo |
| Test Steps | 1) Click `Cancel` |
| Expected Result | `confirm-result` hien thi `Cancelled` |
| Automation Checkpoint | Dismiss dialog va assert ket qua |
| Priority | High |

### PMO-PLW-016 — Prompt dialog nhap text va OK

| Truong | Noi dung |
| --- | --- |
| Module | Native Dialogs |
| Muc tieu | Xac nhan prompt nhan gia tri input |
| Pre-condition | Truy cap section `Native Dialogs` |
| Test Data | Input bat ky, vi du: `hello prompt` |
| Test Steps | 1) Click `Trigger Prompt`. 2) Dien text. 3) Click `OK`. |
| Expected Result | `prompt-result` hien thi dung text da nhap |
| Automation Checkpoint | `dialog.accept(promptText)` va assert output |
| Priority | High |

### PMO-PLW-017 — Prompt dialog voi Cancel

| Truong | Noi dung |
| --- | --- |
| Module | Native Dialogs |
| Muc tieu | Xac nhan cancel prompt tra ket qua mac dinh |
| Pre-condition | Prompt dialog dang mo |
| Test Steps | 1) Click `Cancel` |
| Expected Result | `prompt-result` hien thi `Dismissed` |
| Automation Checkpoint | `dialog.dismiss()` va assert output |
| Priority | Medium |

### PMO-PLW-018 — Full page screenshot trong moi truong hop

| Truong | Noi dung |
| --- | --- |
| Module | Visual Regressions |
| Muc tieu | Xac nhan co the chup full page screenshot |
| Pre-condition | Config screenshot mode cho pass/fail |
| Test Steps | 1) Click `Normal State`. 2) Assert text `System Normal`. 3) Chup hinh full page. |
| Expected Result | File anh full page duoc tao tai folder chi dinh |
| Automation Checkpoint | `page.screenshot(fullPage=True)` va verify file ton tai |
| Priority | Medium |

### PMO-PLW-019 — Element screenshot chi luu khi testcase pass (khong tao file)

| Truong | Noi dung |
| --- | --- |
| Module | Visual Regressions |
| Muc tieu | Xac nhan che do retain-on-failure khong luu anh khi testcase pass |
| Pre-condition | Config screenshot chi luu khi failed |
| Test Steps | 1) Click `Normal State`. 2) Assert `System Normal`. 3) Chup element screenshot theo config on-failure. |
| Expected Result | Khong co file screenshot duoc tao |
| Automation Checkpoint | Verify thu muc output khong co artifact sau case pass |
| Priority | Medium |

### PMO-PLW-020 — Element screenshot luu khi testcase fail

| Truong | Noi dung |
| --- | --- |
| Module | Visual Regressions |
| Muc tieu | Xac nhan screenshot duoc luu neu testcase fail |
| Pre-condition | Config screenshot chi luu khi failed |
| Test Steps | 1) Click `Failure State`. 2) Co y assert sai de testcase fail. |
| Expected Result | Co file element screenshot duoc tao |
| Automation Checkpoint | Verify artifact duoc tao khi fail |
| Priority | Medium |

### PMO-PLW-021 — Video recording trong moi truong hop

| Truong | Noi dung |
| --- | --- |
| Module | Visual Regressions |
| Muc tieu | Xac nhan quay video du thao tac cua sequence |
| Pre-condition | Config video always |
| Test Steps | 1) Click `Play Sequence`. 2) Assert trang thai den `Sequence complete!`. |
| Expected Result | Video duoc tao, ghi nhan du cac buoc sequence |
| Automation Checkpoint | Verify video file ton tai sau test run |
| Priority | Medium |

### PMO-PLW-022 — Video chi luu khi failed (pass case)

| Truong | Noi dung |
| --- | --- |
| Module | Visual Regressions |
| Muc tieu | Xac nhan pass case khong tao video khi mode on-failure |
| Pre-condition | Config video retain-on-failure |
| Test Steps | 1) Click `Play Sequence`. 2) Wait toi da 10s de assert `Sequence complete!`. |
| Expected Result | Test pass va khong co video file |
| Automation Checkpoint | Verify khong co artifact video khi pass |
| Priority | Medium |

### PMO-PLW-023 — Video chi luu khi failed (fail case)

| Truong | Noi dung |
| --- | --- |
| Module | Visual Regressions |
| Muc tieu | Xac nhan fail case tao video khi mode on-failure |
| Pre-condition | Config video retain-on-failure |
| Test Steps | 1) Click `Play Sequence`. 2) Wait toi da 1s de assert `Sequence complete!` (co y timeout) |
| Expected Result | Test fail va co video file duoc tao |
| Automation Checkpoint | Verify video artifact ton tai khi fail |
| Priority | Medium |

### PMO-PLW-024 — Tracing always cho submit thanh cong

| Truong | Noi dung |
| --- | --- |
| Module | Tracing & Submission |
| Muc tieu | Xac nhan trace duoc tao du testcase pass |
| Pre-condition | Config tracing always |
| Test Data | Input 2 truong bat ky |
| Test Steps | 1) Dien du 2 o input. 2) Click `Submit Form`. |
| Expected Result | Hien thi `Submitted: <du lieu da nhap>` va trace duoc luu day du step |
| Automation Checkpoint | Verify file trace ton tai va mo duoc trong trace viewer |
| Priority | High |

### PMO-PLW-025 — Tracing on-failure voi case fail

| Truong | Noi dung |
| --- | --- |
| Module | Tracing & Submission |
| Muc tieu | Xac nhan trace chi tao khi testcase that bai |
| Pre-condition | Config tracing retain-on-failure |
| Test Steps | 1) De trong 2 o input. 2) Click `Submit Form`. 3) Assert ket qua mong doi thanh cong (co y sai) |
| Expected Result | Test fail; trang hien thi `Both fields are required`; trace duoc tao |
| Automation Checkpoint | Verify trace artifact ton tai khi fail |
| Priority | High |

### PMO-PLW-026 — Tracing on-failure voi case pass

| Truong | Noi dung |
| --- | --- |
| Module | Tracing & Submission |
| Muc tieu | Xac nhan pass case khong tao trace khi mode on-failure |
| Pre-condition | Config tracing retain-on-failure |
| Test Data | Input hop le cho 2 truong |
| Test Steps | 1) Dien du 2 o input. 2) Click `Submit Form`. 3) Assert message `Submitted: ...` |
| Expected Result | Test pass va khong co file trace |
| Automation Checkpoint | Verify khong co trace artifact khi pass |
| Priority | High |

### PMO-PLW-027 — Hook beforeAll thong bao artifact path

| Truong | Noi dung |
| --- | --- |
| Module | Hooks Demo |
| Muc tieu | Xac nhan hook beforeAll chay truoc tat ca testcase |
| Pre-condition | Co cau hinh hook global |
| Test Steps | 1) Tao `beforeAll` log thong bao duong dan artifact. 2) Run test file. |
| Expected Result | Terminal hien thi log dang `[beforeAll] Setup ... artifacts ...` |
| Automation Checkpoint | Verify output terminal dung format message |
| Priority | Medium |

### PMO-PLW-028 — Hook afterAll thong bao ket thuc session

| Truong | Noi dung |
| --- | --- |
| Module | Hooks Demo |
| Muc tieu | Xac nhan hook afterAll chay sau tat ca testcase |
| Pre-condition | Co cau hinh hook global |
| Test Steps | 1) Tao `afterAll` log ket thuc session. 2) Run test file den het. |
| Expected Result | Terminal hien thi `[afterAll] Ket thuc test session - don dep moi truong` |
| Automation Checkpoint | Verify afterAll duoc goi 1 lan sau cung |
| Priority | Medium |

### PMO-PLW-029 — Hook beforeEach auto login + create record

| Truong | Noi dung |
| --- | --- |
| Module | Hooks Demo |
| Muc tieu | Xac nhan beforeEach thuc hien setup truoc moi test |
| Pre-condition | Trang `Hooks Demo` co form login va tao record |
| Test Data | Username `admin`, Password `password123`, Record name bat ky |
| Test Steps | 1) Trong `beforeEach`, tu dong login. 2) Nhap `Record Name`. 3) Click `Create Record`. |
| Expected Result | Record moi duoc tao va hien thi tren man hinh |
| Automation Checkpoint | Reuse setup fixture de testcase khong phai goi lai login |
| Priority | High |

### PMO-PLW-030 — Hook afterEach auto delete record

| Truong | Noi dung |
| --- | --- |
| Module | Hooks Demo |
| Muc tieu | Xac nhan afterEach cleanup record sau moi testcase |
| Pre-condition | Da tao record trong testcase/beforeEach |
| Test Steps | 1) Sau moi testcase, `afterEach` tim record vua tao. 2) Click `Delete`. |
| Expected Result | Record duoc xoa khoi danh sach sau testcase |
| Automation Checkpoint | Dam bao test data khong bi ton du giua cac testcase |
| Priority | High |

---

## 3) Quy tac map testcase -> script automation

- Ten file goi y: `tests/test_playwright_arena.spec.ts` (hoac `.py` neu dung pytest-playwright).
- Naming test: `test_pmo_plw_001_iframe_simple_submit_success` ... `test_pmo_plw_030_after_each_cleanup`.
- Tach theo describe/suite:
  - `frames_iframes`
  - `windows_popups_dialogs`
  - `visual_regression_artifacts`
  - `tracing`
  - `hooks`
- Gan tag/chon run:
  - `@smoke`: PMO-PLW-001, 006, 008, 011, 014, 016, 024, 029, 030
  - `@regression`: toan bo 30 case
  - `@artifact`: 018 -> 026

## 4) Ghi chu PMO

- Tat ca testcase deu theo cau truc: `Pre-condition -> Steps -> Expected -> Automation checkpoint`.
- Case 020, 023, 025 la testcase co y fail de xac nhan behavior luu artifact theo config.
- Case 026 la cap doi chieu cua 025 de xac nhan pass case khong tao trace trong mode `retain-on-failure`.

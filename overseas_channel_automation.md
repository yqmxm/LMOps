# 海外渠道资源自动化收集方案（按你给的两类目标重构）

## 1. 目标人群（仅保留当前两类）

### A 类：欧洲 + 东南亚市场的 OPC 个体 / 小型商业主体
> 目标：与“有自有品牌与商业价值的人”建立联系，并用 AI 帮其提效与放大价值。

重点细分：
- 数字游民品牌（Digital Nomad Brand）
- 个人独立品牌（Personal Indie Brand）
- 独立游戏与艺术虚拟数字互动叙事开发者
- 独立专家顾问（策略、增长、品牌、技术、内容）
- 提供商业化服务的中小企业（微型 agency / studio / boutique firm）

你的核心诉求：**找到可触达联系人并建立沟通（合作、服务、联合产品化）**。

### B 类：欧洲新能源从业人员（有一定决策权）
> 目标：识别其产业链中的现实需求，并建立业务联系。

重点细分：
- 设备制造与系统集成
- EPC / 项目开发 / 工程交付
- 储能、充电、能源管理软件
- 供应链采购与技术选型岗位

你的核心诉求：**识别“有需求 + 有决策影响力”的从业者并推进对话**。

---

## 2. 地域聚焦与优先级
- **第一优先**：欧洲（两类人群都覆盖）
- **第二优先**：东南亚（先覆盖 A 类 OPC 群体）

建议先做“欧洲深挖 + 东南亚验证”双轨：
- 欧洲：同时跑 A/B 两类线索
- 东南亚：先跑 A 类，形成标准打法后再扩 B 类相关能源周边生态

---

## 3. 渠道策略（按人群而非泛渠道）

### 3.1 A 类（OPC / 独立品牌 / 小型服务商）
**主渠道（高优先）**
- LinkedIn（个人品牌、顾问、创始人）
- X（Twitter）（数字游民、独立开发者、创作者）
- YouTube / Podcast 简介页（可找到商业联系方式）
- Product Hunt / Indie Hackers（独立产品与创作者生态）

**补充渠道（中优先）**
- Reddit 垂直社区
- Behance / Dribbble（创意与设计服务群体）
- Substack / 个人官网（品牌叙事与服务报价线索）

### 3.2 B 类（欧洲新能源从业者）
**主渠道（高优先）**
- LinkedIn（岗位、公司、项目、决策链）
- 欧洲行业展会参展商/演讲嘉宾名单
- 欧洲公开招标 / 项目公告 / 行业协会成员目录

**补充渠道（中优先）**
- 行业媒体访谈与案例
- 公司新闻稿与采购合作公告

---

## 4. 线索字段（围绕“联系 + 转化”设计）
- `target_class`：A_OPC / B_ENERGY
- `region`：EU / SEA
- `country`：国家
- `source_platform`：来源平台
- `source_url`：原始链接
- `captured_at`：抓取时间（UTC）
- `entity_name`：姓名/品牌/公司
- `entity_type`：individual / studio / sme / enterprise
- `role_title`：岗位或身份标签
- `decision_level`：influencer / manager / director / founder
- `contact_hint`：邮箱/私信入口/官网表单
- `intent_signal`：需求信号
- `pain_point_signal`：痛点信号（效率、获客、交付、成本、增长）
- `offer_fit`：与你可提供价值的匹配项（AI运营提效/内容自动化/增长系统等）
- `timeline_hint`：需求时间（紧急/季度内/长期）
- `opportunity_score`：机会评分（0-100）
- `priority_tier`：P1 / P2 / P3
- `next_action`：建议下一步动作
- `status`：new / contacted / replied / meeting / proposal / won / lost

---

## 5. 识别规则（把“谁值得联系”机器化）

### 5.1 A 类 OPC 识别关键词
- 身份词：indie / freelancer / consultant / founder / creator / studio
- 商业词：open for projects / taking clients / partnership / collaboration
- 痛点词：lead gen / productivity / content ops / automation / scaling

### 5.2 B 类新能源识别关键词
- 身份词：procurement / sourcing / project manager / engineering manager / business development
- 需求词：supplier / tender / RFP / integration / deployment
- 产业词：solar / wind / battery / BESS / EV charging / energy management

### 5.3 决策权判定（简化版）
- Founder / Director / Head：高权重
- Manager / Lead：中高权重
- Specialist / Analyst：中权重（需补链路）

---

## 6. 评分与优先级（直接驱动行动）

评分建议：
`opportunity_score = 决策权30% + 需求明确度30% + 痛点强度20% + 联系可达性20%`

优先级：
- **P1（24小时内触达）**：分数 ≥ 80，且可直接联系
- **P2（72小时内触达）**：分数 60-79
- **P3（培育池）**：分数 < 60

---

## 7. 触达策略（你最终要“建立联系”）

### 7.1 A 类触达模板方向
- 切入点：
  - “我看了你在 ___ 的内容/项目，发现你在 ___ 上已经很强。”
  - “我们可以用 AI 帮你把 ___（获客/内容/交付）效率放大。”
- CTA：
  - “是否愿意约 15 分钟，看看是否有 1-2 个可以立即试点的点？”

### 7.2 B 类触达模板方向
- 切入点：
  - “看到你们在 ___ 项目/环节的进展，推测在 ___ 上可能有现实约束。”
  - “我们可在 ___（流程效率/数据协同/供应链响应）提供可量化改进。”
- CTA：
  - “是否可以安排一次短会，快速确认是否值得做小范围 PoC？”

---

## 8. 合规边界
- 仅采集公开可访问信息，遵守平台 ToS 与 robots。
- 不采集敏感个人隐私数据，不做违规抓取。
- 建立退订、删除、审计机制，确保可追溯。

---

## 9. 四周执行计划（只为两类目标服务）
- **第1周**：确定 A/B 两类关键词库与国家清单；接入 LinkedIn + X + 招标/展会名单。
- **第2周**：完成去重、评分、P1/P2/P3；产出首批联系人清单。
- **第3周**：接入触达工作流（邮件/私信模板）；跟踪回复与会议预约。
- **第4周**：按回复率/会议率复盘，优化关键词、评分权重、触达话术。

---

## 10. KPI（验证“有没有拿到商机”）
- 每周新增 P1 联系人数（按 A/B 分类）
- 48 小时触达完成率
- 回复率（reply rate）
- 会议转化率（contact -> meeting）
- 商机转化率（meeting -> proposal -> won）

---

## 11. 最小任务清单
- [ ] 搭建 `collectors/`：优先 LinkedIn、X、展会/招标名单抓取。
- [ ] 搭建 `classifier/`：A_OPC 与 B_ENERGY 自动分类。
- [ ] 搭建 `scorer/`：计算 `opportunity_score` 与 `priority_tier`。
- [ ] 搭建 `outreach_queue/`：按 P1/P2 自动生成每日联系名单与建议话术。

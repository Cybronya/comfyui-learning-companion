---
name: text_to_image_lora_sampler_clip_11
type: Text To Image
frequency: 23
level: strong
coverage: 0.90213
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489.json, 数字人/数字人/MiniMax H3 Director多功能导演台视频处理生成工具_2101402833722634242.json, 视频生成/图生视频/8步lora+sage加速｜MiniMax H3导演台图生视频1分钟直出_2089372941757796354.json, 视频生成/图生视频/AIMixer导演台4step｜MiniMax H3图生视频创作_2090572888154927106.json, 视频生成/图生视频/AI视频MiniMaxH3Director工作流｜节点化组织视频生成流程_2101920429580574721.json, 视频生成/图生视频/AI视频丨MiniMaxH3Director丨视频生成_2101607609433411585.json, 视频生成/图生视频/Dasiwa-MiniMax H3导演台全能工作流｜图生视频_2095571011541491713.json, 视频生成/图生视频/H3导演台多参模式 多模态视频创作处理工具_2099930977765249025.json, 视频生成/图生视频/H3导演台短时间线整理版 本地参考生成精简工作流_2098837430488092674.json, 视频生成/图生视频/H3导演台短时间线整理版｜图生视频分镜时间轴一目了然_2099137949844725761.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台全能参考加首尾帧全节点注释_2108635614169100290.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考加首尾帧_2111125388918349826.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考首尾帧全注释_2108428760713351170.json, 视频生成/图生视频/MiniMax H3 导演台｜超强电影感叙事短片 角色表演在线_2097530606128295938.json, 视频生成/图生视频/MiniMax H3导演台全能v2，文生视频图生视频一站搞定_2111193650389676034.json, 视频生成/图生视频/MiniMax H3导演台全能工作流 长视频多段编排视频生成_2105395237672800258.json, 视频生成/图生视频/MiniMax H3导演台全能工作流 长视频多段编排视频生成_2108714092356792321.json, 视频生成/图生视频/MiniMax H3导演台多镜头分镜 图生视频创作工具_2098832499236495361.json, 视频生成/图生视频/MiniMax H3导演台电影感工作流｜叙事短片角色表演生成_2097500208790859778.json, 视频生成/图生视频/MiniMaxH3导演台 图生视频多镜头分镜创作工具_2098716052917153793.json, 视频生成/文生视频/MiniMax H3导演台全能工作流视频处理生成工具_2101765600380014594.json, 视频生成/文生视频/MiniMax H3导演台全能工作流视频处理生成工具_2102185481298595842.json, 视频生成/文生视频/海螺H3全能导演台V2 SelfLife视频生成处理工具_2101747376624070658.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（数字人/数字人/LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489.json、数字人/数字人/MiniMax H3 Director多功能导演台视频处理生成工具_2101402833722634242.json、视频生成/图生视频/8步lora+sage加速｜MiniMax H3导演台图生视频1分钟直出_2089372941757796354.json、视频生成/图生视频/AIMixer导演台4step｜MiniMax H3图生视频创作_2090572888154927106.json、视频生成/图生视频/AI视频MiniMaxH3Director工作流｜节点化组织视频生成流程_2101920429580574721.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 22/23 个有
- `MiniMaxH3DirectorRefine` —— 21/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 21/23 个有
- `UpscaleModelLoader` —— 20/23 个有
- `CreateVideo` —— 19/23 个有
- `SaveVideo` —— 19/23 个有
- `PathchSageAttentionKJ` —— 17/23 个有
- `PreviewAny` —— 17/23 个有
- `BasicScheduler` —— 16/23 个有
- `SaveImage` —— 15/23 个有
- `MiniMaxH3DirectorFaceRefine` —— 6/23 个有
- `MiniMaxH3DirectorSelfLift` —— 6/23 个有
- `VHS_VideoCombine` —— 6/23 个有
- `CR Text` —— 3/23 个有
- `Fast Groups Bypasser (rgthree)` —— 3/23 个有
- `Switch` —— 3/23 个有
- `LoraLoaderBypassModelOnly` —— 2/23 个有
- `PrimitiveStringMultiline` —— 2/23 个有
- `FastGroupsBypassSwitch` —— 1/23 个有
- `Label (rgthree)` —— 1/23 个有
- `ModelAttentionBackend` —— 1/23 个有
- `PreViewVideo` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高发问题（26/23 个样本）：Steps较低可能导致细节不足

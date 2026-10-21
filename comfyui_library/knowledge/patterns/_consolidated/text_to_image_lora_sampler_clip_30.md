---
name: text_to_image_lora_sampler_clip_30
type: Text To Image
frequency: 19
level: strong
coverage: 0.903211
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/H3导演台全能工作流 文生图生视频多模态创作_2099568602486759425.json, 图片生成/文生图/MiniMax H3导演台全能工作流 文生图生视频多模态_2099187853480779778.json, 数字人/数字人/LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489.json, 数字人/数字人/MiniMax H3 Director多功能导演台视频处理生成工具_2101402833722634242.json, 视频生成/图生视频/8步lora+sage加速｜MiniMax H3导演台图生视频1分钟直出_2089372941757796354.json, 视频生成/图生视频/AI视频MiniMaxH3Director工作流｜节点化组织视频生成流程_2101920429580574721.json, 视频生成/图生视频/AI视频丨MiniMaxH3Director丨视频生成_2101607609433411585.json, 视频生成/图生视频/Dasiwa-MiniMax H3导演台全能工作流｜图生视频_2095571011541491713.json, 视频生成/图生视频/H3导演台多参模式 多模态视频创作处理工具_2099930977765249025.json, 视频生成/图生视频/H3导演台短时间线整理版 本地参考生成精简工作流_2098837430488092674.json, 视频生成/图生视频/H3导演台短时间线整理版｜图生视频分镜时间轴一目了然_2099137949844725761.json, 视频生成/图生视频/MiniMax H3 导演台｜超强电影感叙事短片 角色表演在线_2097530606128295938.json, 视频生成/图生视频/MiniMax H3导演台全能v2，文生视频图生视频一站搞定_2111193650389676034.json, 视频生成/图生视频/MiniMax H3导演台全能工作流 长视频多段编排视频生成_2105395237672800258.json, 视频生成/图生视频/MiniMax H3导演台全能工作流 长视频多段编排视频生成_2108714092356792321.json, 视频生成/图生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2099769452786184193.json, 视频生成/图生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2100031181533302785.json, 视频生成/图生视频/允希V8.2闭唇正脸一秒轻触首尾帧｜单图外接口播版_2111330532469600258.json, 视频生成/图生视频/允希V8.2闭唇正脸主体参考版｜单图外接一秒轻触_2111335218408943617.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/H3导演台全能工作流 文生图生视频多模态创作_2099568602486759425.json、图片生成/文生图/MiniMax H3导演台全能工作流 文生图生视频多模态_2099187853480779778.json、数字人/数字人/LTX2.5商业级数字人｜目前最好文生图图生图_2092392285458751489.json、数字人/数字人/MiniMax H3 Director多功能导演台视频处理生成工具_2101402833722634242.json、视频生成/图生视频/8步lora+sage加速｜MiniMax H3导演台图生视频1分钟直出_2089372941757796354.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 19 个 workflow 都包含：
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
- `CreateVideo` —— 18/19 个有
- `MiniMaxH3DirectorRefine` —— 18/19 个有
- `SaveVideo` —— 18/19 个有
- `UpscaleModelLoader` —— 18/19 个有
- `PreviewAny` —— 17/19 个有
- `BasicScheduler` —— 16/19 个有
- `孤海注释` —— 16/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 15/19 个有
- `PathchSageAttentionKJ` —— 14/19 个有
- `SaveImage` —— 12/19 个有
- `MiniMaxH3DirectorFaceRefine` —— 5/19 个有
- `MiniMaxH3DirectorSelfLift` —— 5/19 个有
- `EmptyImage` —— 4/19 个有
- `PreviewImage` —— 4/19 个有
- `PrimitiveStringMultiline` —— 4/19 个有
- `ModelAttentionBackend` —— 3/19 个有
- `VHS_VideoCombine` —— 3/19 个有
- `BlockSparseAttention` —— 2/19 个有
- `ExtendIntermediateSigmas` —— 2/19 个有
- `LoadImage` —— 2/19 个有
- `MiniMaxH3DirectorGroupsCombine` —— 2/19 个有
- `MiniMaxH3SigmaShift` —— 2/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `LoraLoaderBypassModelOnly` —— 1/19 个有
- `MiniMaxH3DirectorGroupImageToVideo` —— 1/19 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 1/19 个有
- `ModelPreviewOverrideKJ` —— 1/19 个有
- `PreViewVideo` —— 1/19 个有
- `Video Slice` —— 1/19 个有
- `easy cleanGpuUsed` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（21/19 个样本）：Steps较低可能导致细节不足

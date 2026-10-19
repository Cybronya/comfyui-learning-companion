---
name: text_to_image_lora_sampler_clip_60
type: Text To Image
frequency: 13
level: strong
coverage: 0.897692
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/seedvr2超分工作流｜数字人视频提清｜低清素材秒变高清_2104833908113235969.json, 视频生成/图生视频/H3导演台长视频生成段间引导turbo图生视频_2088250475895418882.json, 视频生成/图生视频/MiniMax H3导演台1分钟直出｜8步lora+sage加速图生视频_2089686353972912129.json, 视频生成/图生视频/MiniMax H3导演台自用版｜8步lora+sage加速直出1分钟视频_2089018131384717314.json, 视频生成/图生视频/MiniMax H3导演台｜全能图生视频工作流生成_2095955595504476162.json, 视频生成/图生视频/MiniMaxH3导演台工作流｜图生视频分镜掌控_2098707033821372417.json, 视频生成/图生视频/导演台全能创作台｜MiniMax H3 图生视频一站搞定_2096229973320364033.json, 视频生成/图生视频/导演台全能工作流｜MiniMax H3图生视频生成_2095943329958686722.json, 视频生成/图生视频/导演台双采样全能工作流｜MiniMax H3图生视频_2092073134999556097.json, 视频生成/文生视频/MiniMax H3 导演台满血版｜Ref2va全能工作流文生图生视频_2097524361732386817.json, 视频生成/文生视频/MiniMax H3导演台满血版工作流｜Ref2va全能视频生成_2097498585955917826.json, 视频生成/文生视频/MiniMax H3电影质感导演台二采放大分镜合成8步加速工具_2101033192529686530.json, 视频生成/文生视频/MiniMaxH3 AIO造梦工厂｜图生视频文生视频视频生视频一站搞定_2097879124835659777.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（数字人/数字人/seedvr2超分工作流｜数字人视频提清｜低清素材秒变高清_2104833908113235969.json、视频生成/图生视频/H3导演台长视频生成段间引导turbo图生视频_2088250475895418882.json、视频生成/图生视频/MiniMax H3导演台1分钟直出｜8步lora+sage加速图生视频_2089686353972912129.json、视频生成/图生视频/MiniMax H3导演台自用版｜8步lora+sage加速直出1分钟视频_2089018131384717314.json、视频生成/图生视频/MiniMax H3导演台｜全能图生视频工作流生成_2095955595504476162.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3Director` —— 12/13 个有
- `CreateVideo` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/13 个有
- `PathchSageAttentionKJ` —— 10/13 个有
- `PreviewAny` —— 10/13 个有
- `MiniMaxH3DirectorRefine` —— 8/13 个有
- `UpscaleModelLoader` —— 8/13 个有
- `BasicScheduler` —— 7/13 个有
- `VHS_VideoCombine` —— 3/13 个有
- `SaveImage` —— 2/13 个有
- `ImageScale` —— 1/13 个有
- `Int` —— 1/13 个有
- `ModelPreviewOverrideKJ` —— 1/13 个有
- `PixaromaLoraLoader` —— 1/13 个有
- `RIFE VFI` —— 1/13 个有
- `SeedVR2` —— 1/13 个有
- `SeedVR2BlockSwap` —— 1/13 个有
- `VHS_LoadVideo` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足

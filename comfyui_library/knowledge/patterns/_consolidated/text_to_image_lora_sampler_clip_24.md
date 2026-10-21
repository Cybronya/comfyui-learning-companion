---
name: text_to_image_lora_sampler_clip_24
type: Text To Image
frequency: 21
level: strong
coverage: 0.890952
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, PreviewAny, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3导演台满血版Ref2va全能视频生成 多模态创作_2099188524363898882.json, 视频生成/文生视频/H3导演台满血版Ref2va全能视频生成 多模态创作_2099573426963963905.json, 视频生成/文生视频/H3导演台视频编辑模式_视频处理编辑工具_2100505084298883073.json, 视频生成/文生视频/H3导演台视频编辑模式视频后期处理工具包_2101020573185953794.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流｜人物去油效果稳_2096887110086254594.json, 视频生成/文生视频/MiniMax H3 导演台满血版｜Ref2va全能工作流文生图生视频_2097524361732386817.json, 视频生成/文生视频/MiniMax H3导演台全能工作流视频处理生成工具_2101765600380014594.json, 视频生成/文生视频/MiniMax H3导演台全能工作流视频处理生成工具_2102185481298595842.json, 视频生成/文生视频/MiniMax H3导演台全能工作流，文生视频一站式创作方案_2103630754046631937.json, 视频生成/文生视频/MiniMax H3导演台全能工作流，文生视频视频生视频图生视频方案_2107525467845779457.json, 视频生成/文生视频/MiniMax H3导演台全能机｜灵感来了直接开拍，反推提示词免手写_2099411307467468802.json, 视频生成/文生视频/MiniMax H3导演台满血版工作流｜Ref2va全能视频生成_2097498585955917826.json, 视频生成/文生视频/MiniMax H3｜导演台全能工作流，文生视频图生视频视频生视频三合一_2107283103852089346.json, 视频生成/文生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2098941942678773761.json, 视频生成/文生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2099053865718075393.json, 视频生成/文生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2099679213619073025.json, 视频生成/文生视频/一次60秒全能生成｜海螺H3搅拌手大佬版导演台_2092749641665306626.json, 视频生成/文生视频/一次60秒出片｜海螺 H3 导演台搅拌手大佬版_2090893932635967490.json, 视频生成/文生视频/导演台一次60秒｜海螺H3搅拌手大佬版全能s_2091190910787874818.json, 视频生成/文生视频/搅拌手大佬版导演台｜海螺H3全能60秒生成_2091195180161519618.json, 视频生成/文生视频/海螺H3全能导演台V2 SelfLife视频生成处理工具_2101747376624070658.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/文生视频/H3导演台满血版Ref2va全能视频生成 多模态创作_2099188524363898882.json、视频生成/文生视频/H3导演台满血版Ref2va全能视频生成 多模态创作_2099573426963963905.json、视频生成/文生视频/H3导演台视频编辑模式_视频处理编辑工具_2100505084298883073.json、视频生成/文生视频/H3导演台视频编辑模式视频后期处理工具包_2101020573185953794.json、视频生成/文生视频/MiniMax H3 导演台全能工作流｜人物去油效果稳_2096887110086254594.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DirectorRefine` —— 19/21 个有
- `孤海注释` —— 19/21 个有
- `BasicScheduler` —— 18/21 个有
- `UpscaleModelLoader` —— 17/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/21 个有
- `PathchSageAttentionKJ` —— 13/21 个有
- `SaveImage` —— 13/21 个有
- `PreviewImage` —— 9/21 个有
- `EmptyImage` —— 8/21 个有
- `LoraLoaderBypassModelOnly` —— 6/21 个有
- `MiniMaxH3DirectorFaceRefine` —— 6/21 个有
- `MiniMaxH3DirectorSelfLift` —— 6/21 个有
- `VHS_VideoCombine` —— 6/21 个有
- `Fast Groups Bypasser (rgthree)` —— 5/21 个有
- `FastGroupsBypassSwitch` —— 5/21 个有
- `LoadImage` —— 1/21 个有
- `ModelAttentionBackend` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高发问题（25/21 个样本）：Steps较低可能导致细节不足

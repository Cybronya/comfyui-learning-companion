---
name: text_to_image_lora_sampler_clip_15
type: Text To Image
frequency: 21
level: strong
coverage: 0.860286
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2099769452786184193.json, 视频生成/图生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2100031181533302785.json, 视频生成/文生视频/H3导演台全能工作流 灵感直接开拍多模态视频创作_2099209155545493505.json, 视频生成/文生视频/H3导演台全能工作流 灵感直接开拍多模态视频创作_2099581764892188673.json, 视频生成/文生视频/H3导演台多合一工作流 文生图生视频全模态_2099548139941351426.json, 视频生成/文生视频/H3导演台工作流，文生视频视频生视频图生视频全覆盖方案_2106116054211710977.json, 视频生成/文生视频/H3导演台满血版Ref2va全能视频生成 多模态创作_2099188524363898882.json, 视频生成/文生视频/H3导演台满血版Ref2va全能视频生成 多模态创作_2099573426963963905.json, 视频生成/文生视频/H3导演台视频编辑模式_视频处理编辑工具_2100505084298883073.json, 视频生成/文生视频/H3导演台视频编辑模式视频后期处理工具包_2101020573185953794.json, 视频生成/文生视频/MiniMax H3导演台全能工作流，文生视频一站式创作方案_2103630754046631937.json, 视频生成/文生视频/MiniMax H3导演台全能工作流，文生视频视频生视频图生视频方案_2107525467845779457.json, 视频生成/文生视频/MiniMax H3导演台全能机｜灵感来了直接开拍，反推提示词免手写_2099411307467468802.json, 视频生成/文生视频/MiniMax H3导演台多合一工作流 文生图生视频全模态_2099179860689252353.json, 视频生成/文生视频/MiniMax H3导演台多合一工作流，文生视频视频生视频图生视频全覆盖_2103265148579434498.json, 视频生成/文生视频/MiniMax H3｜导演台全能工作流，文生视频图生视频视频生视频三合一_2107283103852089346.json, 视频生成/文生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2098941942678773761.json, 视频生成/文生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2099053865718075393.json, 视频生成/文生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2099679213619073025.json, 视频生成/文生视频/Minimax H3导演台多合一工作流｜文生图生视频生成_2097802408180142081.json, 视频生成/文生视频/Minimax H3导演台多合一｜文生图生视频一应俱全，一个流全包_2099510260229824513.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2099769452786184193.json、视频生成/图生视频/MiniMax_H3导演台满血版工作流｜Ref2va全能视频生成_2100031181533302785.json、视频生成/文生视频/H3导演台全能工作流 灵感直接开拍多模态视频创作_2099209155545493505.json、视频生成/文生视频/H3导演台全能工作流 灵感直接开拍多模态视频创作_2099581764892188673.json、视频生成/文生视频/H3导演台多合一工作流 文生图生视频全模态_2099548139941351426.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：86%

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
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 19/21 个有
- `MiniMaxH3DirectorRefine` —— 19/21 个有
- `SaveImage` —— 18/21 个有
- `UpscaleModelLoader` —— 17/21 个有
- `孤海注释` —— 17/21 个有
- `PreviewAny` —— 16/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/21 个有
- `PathchSageAttentionKJ` —— 14/21 个有
- `PreviewImage` —— 13/21 个有
- `EmptyImage` —— 10/21 个有
- `Fast Groups Bypasser (rgthree)` —— 5/21 个有
- `GetNode` —— 5/21 个有
- `SetNode` —— 5/21 个有
- `StringToInt` —— 5/21 个有
- `LoadImage` —— 3/21 个有
- `MiniMaxH3DirectorFaceRefine` —— 3/21 个有
- `MiniMaxH3DirectorSelfLift` —— 3/21 个有

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
| Steps较低可能导致细节不足 | 24/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高发问题（24/21 个样本）：Steps较低可能导致细节不足

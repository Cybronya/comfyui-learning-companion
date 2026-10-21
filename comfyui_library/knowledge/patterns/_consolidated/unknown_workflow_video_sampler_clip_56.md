---
name: unknown_workflow_video_sampler_clip_56
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.980667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1904449590517534721.json, 视频生成/图生视频/1930507082674421762.json, 视频生成/图生视频/1930543153353510913.json, 视频生成/图生视频/1991482549792940034.json, 视频生成/图生视频/1904428749629358081.json, 视频生成/图生视频/1985686489952657410.json, 视频生成/图生视频/2008112193308467202.json, 视频生成/图生视频/1935896617889558530.json, 视频生成/图生视频/1894951787738824705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1904449590517534721.json、视频生成/图生视频/1930507082674421762.json、视频生成/图生视频/1930543153353510913.json、视频生成/图生视频/1991482549792940034.json、视频生成/图生视频/1904428749629358081.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 5/9 个有
- `Int` —— 1/9 个有
- `JanusImageUnderstanding` —— 1/9 个有
- `JanusModelLoader` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `StringFunction|pysssss` —— 1/9 个有
- `TeaCache` —— 1/9 个有
- `TextInput_` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 9 | 85% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 9 | 86% |
| 采样算法 | uni_pc | - | 9 | 56% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，9 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，9 个样本，取值集中（一致性 86%）
- 采样算法 最常用 uni_pc，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）

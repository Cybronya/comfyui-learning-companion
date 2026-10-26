---
name: unknown_workflow_video_sampler_clip_111
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.990667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.1图生视频加速Janus提示词反推版_1904449590517534721.json, 视频生成/图生视频/Wan2.1 I2V 图生视频 480p_1930507082674421762.json, 视频生成/图生视频/Wan2.1 I2V 图生视频 720p_1930543153353510913.json, 视频生成/图生视频/Wan2.1 图生视频工作流_1991482549792940034.json, 视频生成/图生视频/Wan2.1(阿里万相)-图生视频_1904428749629358081.json, 视频生成/图生视频/万相-Wan2.1-图生视频_1901974657921081346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/WAN2.1图生视频加速Janus提示词反推版_1904449590517534721.json、视频生成/图生视频/Wan2.1 I2V 图生视频 480p_1930507082674421762.json、视频生成/图生视频/Wan2.1 I2V 图生视频 720p_1930543153353510913.json、视频生成/图生视频/Wan2.1 图生视频工作流_1991482549792940034.json、视频生成/图生视频/Wan2.1(阿里万相)-图生视频_1904428749629358081.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ImageResizeKJ` —— 3/6 个有
- `JanusImageUnderstanding` —— 1/6 个有
- `JanusModelLoader` —— 1/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `StringFunction|pysssss` —— 1/6 个有
- `TeaCache` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 6 | 86% |
| 采样算法 | uni_pc | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，6 个样本，取值集中（一致性 86%）
- 采样算法 最常用 uni_pc，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）

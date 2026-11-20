---
name: unknown_workflow_video_sampler_clip_124
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9176
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJ, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [图片生成/图生图/万相wan2.1极致图生视频ComfyUI_1906877379761905665.json, 平台全量/B站：AI绘画师-万相wan2.1 图生视频 ComfyUI org工作流_1906341291280486401.json, 平台全量/【趣味】wan2.1官方图生视频工作流+teacache加速_1897940491827105794.json, 视频生成/图生视频/万相-Wan2.1-图生视频_1901974657921081346.json, 视频生成/图生视频/万相wan2.1 图生视频 ComfyUI org 官方流  B站 楚门的AI世界_1894951787738824705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_124

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/万相wan2.1极致图生视频ComfyUI_1906877379761905665.json、平台全量/B站：AI绘画师-万相wan2.1 图生视频 ComfyUI org工作流_1906341291280486401.json、平台全量/【趣味】wan2.1官方图生视频工作流+teacache加速_1897940491827105794.json、视频生成/图生视频/万相-Wan2.1-图生视频_1901974657921081346.json、视频生成/图生视频/万相wan2.1 图生视频 ComfyUI org 官方流  B站 楚门的AI世界_1894951787738824705.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `ModelSamplingSD3` —— 2/5 个有
- `TextInput_` —— 2/5 个有
- `ImageScaleDownToSize` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `TeaCache` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_video_sampler_clip_193
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.669333
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScaleBy, KSamplerAdvanced, Label (rgthree), ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, PrimitiveStringMultiline, RIFE VFI, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, mxSlider2D]
problems: []
missing: [Label (rgthree), Pick From Batch (mtb), RIFE VFI, easy cleanGpuUsed, Seed (rgthree)]
members: [视频生成/文生视频/1979104736274190338.json, 视频生成/文生视频/smoothMix2.0文生视频_1983518201407578113.json, 视频生成/文生视频/smoothMix首尾帧_1983522956250914818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_193

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1979104736274190338.json、视频生成/文生视频/smoothMix2.0文生视频_1983518201407578113.json、视频生成/文生视频/smoothMix首尾帧_1983522956250914818.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `mxSlider2D`

**可变部分**（部分 workflow 才有）：
- `Power Lora Loader (rgthree)` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `ColorMatch` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、Pick From Batch (mtb)、RIFE VFI、easy cleanGpuUsed、Seed (rgthree)

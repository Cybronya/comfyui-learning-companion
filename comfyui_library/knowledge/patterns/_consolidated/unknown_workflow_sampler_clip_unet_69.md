---
name: unknown_workflow_sampler_clip_unet_69
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.897308
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLSampler (BSS) 画质提升-ZImage_2062006258563108866.json, 图片生成/文生图/Flux2 Klein 文生图_2020763009353785346.json, 图片生成/文生图/Flux2 Klein 文生图_2025932476836749314.json, 图片生成/文生图/Flux2 Klein 文生图_2028304337616769026.json, 图片生成/文生图/Flux3_Klein图像编辑工作流_2111476889922662402.json, 图片生成/文生图/Z-Image-Turbo基础文生图-工作流_2011542094619353089.json, 图片生成/文生图/Z-Image_turbo工作流_2066470777045741570.json, 图片生成/文生图/Z-image文生图_2098605302726873090.json, 图片生成/文生图/Z_image_turbo文生图原版工作流-B站UP主@好奇漫步_1995897359357919233.json, 图片生成/文生图/danotebook-ernie-image-turbo_2062464622694854657.json, 图片生成/文生图/flux.2-4b-文生图-标准版-（必收藏）_2052387127085813761.json, 图片生成/文生图/flux3_image_klein多图编辑_2011011965199589378.json, 图片生成/文生图/图像编辑 FLUX 3 Image Klein_2112063690060156930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_69

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/FLSampler (BSS) 画质提升-ZImage_2062006258563108866.json、图片生成/文生图/Flux2 Klein 文生图_2020763009353785346.json、图片生成/文生图/Flux2 Klein 文生图_2025932476836749314.json、图片生成/文生图/Flux2 Klein 文生图_2028304337616769026.json、图片生成/文生图/Flux3_Klein图像编辑工作流_2111476889922662402.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/13 个有
- `EmptyFlux2LatentImage` —— 6/13 个有
- `LoadImage` —— 6/13 个有
- `EmptySD3LatentImage` —— 5/13 个有
- `ReferenceMultiLatent` —— 3/13 个有
- `BatchImagesNode` —— 2/13 个有
- `Image Comparer (rgthree)` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `TextGenerate` —— 2/13 个有
- `ComfySwitchNode` —— 1/13 个有
- `FLS_SamplerV4` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `PreviewImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 4 - 50 | 13 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 13 | 44% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 4 - 50，13 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，13 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）

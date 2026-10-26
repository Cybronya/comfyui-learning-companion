---
name: unknown_workflow_controlnet_inpaint_sampler_6
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.914
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, CropFaces, DetectFaces, ImageSmartSharpen+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LoadImage, Mask Invert, MaskFastGrow, MaskPreview+, PreviewImage, SaveImage, VAEDecode, WarpFacesBack]
problems: []
missing: []
members: [图片生成/图生图/人像高清换脸（双人）_1900359750603763713.json, 图片生成/图生图/人像高清换脸（双人）_1916705842937401345.json, 图片生成/图生图/👾怪獸-双人换脸👾vip_1989193408679907330.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人像高清换脸（双人）_1900359750603763713.json、图片生成/图生图/人像高清换脸（双人）_1916705842937401345.json、图片生成/图生图/👾怪獸-双人换脸👾vip_1989193408679907330.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `CropFaces`
- `DetectFaces`
- `ImageSmartSharpen+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LoadImage`
- `Mask Invert`
- `MaskFastGrow`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `WarpFacesBack`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.65 | 0.55 - 0.65 | 3 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.55 - 0.65，3 个样本，取值集中（一致性 92%）

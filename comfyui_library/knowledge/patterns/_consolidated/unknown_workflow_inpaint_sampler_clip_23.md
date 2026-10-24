---
name: unknown_workflow_inpaint_sampler_clip_23
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9016
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop+, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, MaskToImage, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX_Redux_电商模特换装_1896041388389826561.json, 图片生成/图生图/FLUX淘宝一键换装换鞋_2014910556368543745.json, 图片生成/图生图/Flux_服装迁移换装_1900211139815403521.json, 图片生成/图生图/【极致精准换装】FLUX 一键快速迁移换装_1929459573017493505.json, 图片生成/图生图/电商场景生成模特，保持模特不变_1899787202992156674.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX_Redux_电商模特换装_1896041388389826561.json、图片生成/图生图/FLUX淘宝一键换装换鞋_2014910556368543745.json、图片生成/图生图/Flux_服装迁移换装_1900211139815403521.json、图片生成/图生图/【极致精准换装】FLUX 一键快速迁移换装_1929459573017493505.json、图片生成/图生图/电商场景生成模特，保持模特不变_1899787202992156674.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageCrop+`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageToMask` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `StyleModelApply` —— 4/5 个有
- `GetImageSize+` —— 3/5 个有
- `GroundingDinoModelLoader (segment anything)` —— 3/5 个有
- `GroundingDinoSAMSegment (segment anything)` —— 3/5 个有
- `Image Filter Adjustments` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `SAMModelLoader (segment anything)` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `ConstrainImage|pysssss` —— 2/5 个有
- `ImageResize+` —— 2/5 个有
- `InspyrenetRembg` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `Image To Mask` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LayerColor: Brightness & Contrast` —— 1/5 个有
- `LayerUtility: ColorImage V2` —— 1/5 个有
- `ReduxAdvanced` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有
- `preview_mask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 35 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 35，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

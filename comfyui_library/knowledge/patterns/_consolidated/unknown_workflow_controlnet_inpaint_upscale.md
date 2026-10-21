---
name: unknown_workflow_controlnet_inpaint_upscale
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.824333
common_nodes: [Any Switch (rgthree), BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DWPreprocessor, DetailDaemonSamplerNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageBatchMulti, ImageBatchToList+, ImageScaleToTotalPixels, ImageTile+, ImageUntile+, InpaintCropImproved, InpaintStitchImproved, KSamplerSelect, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview, ModelPatchLoader, PreviewBridge, PreviewImage, SamplerCustom, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy cleanGpuUsed, easy imageSize, easy imageSizeBySide, easy positive, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/z-image 姿势控制 超写实 人物一致性组图-四宫格  SeedVR2高清修复放大_2069617990353641473.json, 图片生成/文生图/z-image 姿势控制 超写实 人物一致性组图-四宫格  SeedVR2高清修复放大_2072929062275866626.json, 图片生成/文生图/z-image-造像-人物一致性组图-四宫格-v2_2002280350581702658.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/z-image 姿势控制 超写实 人物一致性组图-四宫格  SeedVR2高清修复放大_2069617990353641473.json、图片生成/文生图/z-image 姿势控制 超写实 人物一致性组图-四宫格  SeedVR2高清修复放大_2072929062275866626.json、图片生成/文生图/z-image-造像-人物一致性组图-四宫格-v2_2002280350581702658.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `DetailDaemonSamplerNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageBatchMulti`
- `ImageBatchToList+`
- `ImageScaleToTotalPixels`
- `ImageTile+`
- `ImageUntile+`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `KSamplerSelect`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview`
- `ModelPatchLoader`
- `PreviewBridge`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy positive`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）

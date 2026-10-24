---
name: unknown_workflow_inpaint_sampler_clip_54
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.829333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GrowMaskWithBlur, ImageConcanate, ImageCrop+, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerMask: MaskPreview, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/生图-图换装手动遮罩-flux_fill_nunchaku_1983512677819588609.json, 图片生成/图生图/生图-图换装自动遮罩-flux_fill_nunchaku_1972659750909485057.json, 图片生成/图生图/省心，不用画遮罩。换装_1907723273931792385.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/生图-图换装手动遮罩-flux_fill_nunchaku_1983512677819588609.json、图片生成/图生图/生图-图换装自动遮罩-flux_fill_nunchaku_1972659750909485057.json、图片生成/图生图/省心，不用画遮罩。换装_1907723273931792385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageCrop+`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LayerMask: MaskPreview`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `Int` —— 2/3 个有
- `LayerMask: SegformerB2ClothesUltra` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `NunchakuFluxDiTLoader` —— 2/3 个有
- `CR Upscale Image` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 50 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 50，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

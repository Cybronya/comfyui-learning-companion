---
name: unknown_workflow_inpaint_sampler_clip_8
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.926833
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageResize+, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku万物迁移_1915993542517526530.json, 图片生成/图生图/图片-局部重绘+迁移_1988538977122738178.json, 图片生成/图生图/情趣模特换装—保留细节_1948324669716869121.json, 图片生成/图生图/换衣服_2044438942073757697.json, 图片生成/图生图/换装迁移-无需白底_2020075554245976066.json, 图片生成/图生图/谢test_1989218734952812545.json, 平台全量/FLUX Redux 一键换装_1908015548150460417.json, 平台全量/TOP1  高级高精度换装_1911334626147692546.json, 平台全量/一键换装_1975794504412303362.json, 平台全量/一键换装_全身半身都可换（服装还原度高 细节非常好）_1919937461982793730.json, 平台全量/换装-电商一键换装_1892584124547293185.json, 平台全量/高级自动换装_1915610252920950785.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/nunchaku万物迁移_1915993542517526530.json、图片生成/图生图/图片-局部重绘+迁移_1988538977122738178.json、图片生成/图生图/情趣模特换装—保留细节_1948324669716869121.json、图片生成/图生图/换衣服_2044438942073757697.json、图片生成/图生图/换装迁移-无需白底_2020075554245976066.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageResize+`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCrop+` —— 11/12 个有
- `LayerUtility: ColorImage` —— 11/12 个有
- `UNETLoader` —— 11/12 个有
- `easy imageSize` —— 11/12 个有
- `DifferentialDiffusion` —— 10/12 个有
- `LayerUtility: CropByMask V2` —— 9/12 个有
- `LoraLoader` —— 9/12 个有
- `ConditioningZeroOut` —— 8/12 个有
- `DF_Image_scale_to_side` —— 8/12 个有
- `LayerMask: MaskStroke` —— 8/12 个有
- `LayerUtility: PurgeVRAM` —— 8/12 个有
- `SUPIR_Upscale` —— 8/12 个有
- `Mask Fill Holes` —— 7/12 个有
- `Fast Groups Bypasser (rgthree)` —— 5/12 个有
- `Image Comparer (rgthree)` —— 5/12 个有
- `LayerMask: MaskPreview` —— 5/12 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `DepthAnythingV2Preprocessor` —— 1/12 个有
- `GrowMaskWithBlur` —— 1/12 个有
- `Image Filter Adjustments` —— 1/12 个有
- `Int` —— 1/12 个有
- `LayerColor: Brightness & Contrast` —— 1/12 个有
- `LayerFilter: FilmV2` —— 1/12 个有
- `LayerMask: PersonMaskUltra` —— 1/12 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/12 个有
- `LayerUtility: ImageReel` —— 1/12 个有
- `LayerUtility: ImageReelComposit` —— 1/12 个有
- `NunchakuFluxDiTLoader` —— 1/12 个有
- `workflow>语义分割` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 12 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 9 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，12 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，9 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）

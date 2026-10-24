---
name: unknown_workflow_inpaint_sampler_clip_20
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.914667
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageResize+, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/nunchaku万物迁移_1915993542517526530.json, 图片生成/图生图/图片-局部重绘+迁移_1988538977122738178.json, 图片生成/图生图/情趣模特换装—保留细节_1948324669716869121.json, 图片生成/图生图/换衣服_2044438942073757697.json, 图片生成/图生图/换装迁移-无需白底_2020075554245976066.json, 图片生成/图生图/谢test_1989218734952812545.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/nunchaku万物迁移_1915993542517526530.json、图片生成/图生图/图片-局部重绘+迁移_1988538977122738178.json、图片生成/图生图/情趣模特换装—保留细节_1948324669716869121.json、图片生成/图生图/换衣服_2044438942073757697.json、图片生成/图生图/换装迁移-无需白底_2020075554245976066.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
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
- `ImageCrop+` —— 5/6 个有
- `LayerUtility: ColorImage` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `easy imageSize` —— 5/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `LayerMask: MaskStroke` —— 3/6 个有
- `LayerUtility: CropByMask V2` —— 3/6 个有
- `LayerUtility: PurgeVRAM` —— 3/6 个有
- `LoraLoader` —— 3/6 个有
- `Mask Fill Holes` —— 3/6 个有
- `DF_Image_scale_to_side` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `LayerMask: MaskPreview` —— 2/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/6 个有
- `SUPIR_Upscale` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Image Filter Adjustments` —— 1/6 个有
- `Int` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `NunchakuFluxDiTLoader` —— 1/6 个有
- `workflow>语义分割` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_inpaint_sampler_clip_10
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.93625
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX+Redux+自动换装工作流FLUX换装工作流(极速版)_1912373846224138242.json, 图片生成/图生图/Flux+fill+redux+模特换装（手动遮罩版）_1920350633486909441.json, 图片生成/图生图/T恤上身服装印花印字绣花绣字工作流_1944407798463778817.json, 图片生成/图生图/V4.0版本丨flux生成场景模特_1888457810202484738.json, 图片生成/图生图/nunchakus 自动换装工作流(极速版)_1937349490502213633.json, 图片生成/图生图/一键融入背景工作流_1899461559234772994.json, 图片生成/图生图/完美换装V8-REDUX512新版万物迁移_1921484371700695042.json, 图片生成/图生图/换装工作流_2018704819317379074.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX+Redux+自动换装工作流FLUX换装工作流(极速版)_1912373846224138242.json、图片生成/图生图/Flux+fill+redux+模特换装（手动遮罩版）_1920350633486909441.json、图片生成/图生图/T恤上身服装印花印字绣花绣字工作流_1944407798463778817.json、图片生成/图生图/V4.0版本丨flux生成场景模特_1888457810202484738.json、图片生成/图生图/nunchakus 自动换装工作流(极速版)_1937349490502213633.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Blank` —— 7/8 个有
- `UNETLoader` —— 6/8 个有
- `easy imageSize` —— 6/8 个有
- `ImpactInt` —— 5/8 个有
- `Crop (mtb)` —— 4/8 个有
- `GrowMask` —— 4/8 个有
- `ReduxAdvanced` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `ImageCrop+` —— 3/8 个有
- `Int` —— 3/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `LayerMask: PersonMaskUltra V2` —— 2/8 个有
- `NunchakuFluxDiTLoader` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/8 个有
- `LayerMask: SegformerClothesPipelineLoader` —— 1/8 个有
- `LayerMask: SegformerUltraV2` —— 1/8 个有
- `LoaderGGUF` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `Note _O` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 8 | 100% |
| Prompt 约束强度(CFG) | 1.005 | 1 - 8 | 8 | 0% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | normal | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.005，观测区间 1 - 8，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 normal，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

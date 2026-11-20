---
name: unknown_workflow_inpaint_sampler_clip_18
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.928889
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX+Redux+自动换装工作流FLUX换装工作流(极速版)_1912373846224138242.json, 图片生成/图生图/Flux+fill+redux+模特换装（手动遮罩版）_1920350633486909441.json, 图片生成/图生图/T恤上身服装印花印字绣花绣字工作流_1944407798463778817.json, 图片生成/图生图/V4.0版本丨flux生成场景模特_1888457810202484738.json, 图片生成/图生图/nunchakus 自动换装工作流(极速版)_1937349490502213633.json, 图片生成/图生图/一键融入背景工作流_1899461559234772994.json, 图片生成/图生图/完美换装V8-REDUX512新版万物迁移_1921484371700695042.json, 图片生成/图生图/换装工作流_2018704819317379074.json, 平台全量/flux nunchakus + redux + openpose自动换装工作流(极速版)_1938470998121316354.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX+Redux+自动换装工作流FLUX换装工作流(极速版)_1912373846224138242.json、图片生成/图生图/Flux+fill+redux+模特换装（手动遮罩版）_1920350633486909441.json、图片生成/图生图/T恤上身服装印花印字绣花绣字工作流_1944407798463778817.json、图片生成/图生图/V4.0版本丨flux生成场景模特_1888457810202484738.json、图片生成/图生图/nunchakus 自动换装工作流(极速版)_1937349490502213633.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
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
- `Image Blank` —— 8/9 个有
- `easy imageSize` —— 7/9 个有
- `UNETLoader` —— 6/9 个有
- `Crop (mtb)` —— 5/9 个有
- `GrowMask` —— 5/9 个有
- `ImpactInt` —— 5/9 个有
- `ReduxAdvanced` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `Int` —— 4/9 个有
- `LoraLoader` —— 4/9 个有
- `ImageCrop+` —— 3/9 个有
- `LayerMask: PersonMaskUltra V2` —— 3/9 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/9 个有
- `NunchakuFluxDiTLoader` —— 3/9 个有
- `Anything Everywhere` —— 1/9 个有
- `ControlNetApplyAdvanced` —— 1/9 个有
- `ControlNetLoader` —— 1/9 个有
- `DWPreprocessor` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageUpscaleWithModel` —— 1/9 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/9 个有
- `LayerMask: SegformerClothesPipelineLoader` —— 1/9 个有
- `LayerMask: SegformerUltraV2` —— 1/9 个有
- `LoaderGGUF` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `Note _O` —— 1/9 个有
- `SetUnionControlNetType` —— 1/9 个有
- `UpscaleModelLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 9 | 100% |
| Prompt 约束强度(CFG) | 1.01 | 1 - 8 | 9 | 0% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | normal | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.01，观测区间 1 - 8，9 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 normal，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

---
name: text_to_image_controlnet_inpaint_upscale
type: Text To Image
frequency: 10
level: moderate
coverage: 0.8432
common_nodes: [ApplyInstantID, BasicGuider, BasicScheduler, BboxDetectorSEGS, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, Crop Face, DF_Image_scale_to_side, DisplayText, DualCLIPLoader, EmptyLatentImage, GrowMask, ImageComposite+, ImageCrop+, ImageResize+, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, KSamplerSelect, Load RetinaFace, LoadImage, Mask Crop Region, MaskBlur+, MaskToImage, MiniCPM_VQA, PreviewImage, RandomNoise, SAMDetectorCombined, SAMLoader, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringConstant, Switch any [Crystools], TextCombinerTwo, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy mathString]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/影视级海报可换脸_2098976803565166593.json, 图片生成/图生图/影视级海报可换脸_2099133615199309826.json, 图片生成/图生图/影视级海报可换脸_2100072604265697282.json, 图片生成/图生图/影视级海报可换脸_2100854695140093953.json, 图片生成/图生图/影视级海报可换脸_2101125891068882946.json, 图片生成/图生图/影视级海报换脸工作流｜电影质感排版现成，主角换成人像就能发_2099424765944614913.json, 图片生成/图生图/武侠海报封面（可换脸）_2039969643821015042.json, 图片生成/文生图/商用级人像写真工作流，自用版本。_1917802869850832898.json, 图片生成/文生图/影视级海报（可换脸）_2094309374767489025.json, 图片生成/文生图/影视级海报（可换脸）_2094319722920767490.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/影视级海报可换脸_2098976803565166593.json、图片生成/图生图/影视级海报可换脸_2099133615199309826.json、图片生成/图生图/影视级海报可换脸_2100072604265697282.json、图片生成/图生图/影视级海报可换脸_2100854695140093953.json、图片生成/图生图/影视级海报可换脸_2101125891068882946.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `ApplyInstantID`
- `BasicGuider`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `Crop Face`
- `DF_Image_scale_to_side`
- `DisplayText`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `GrowMask`
- `ImageComposite+`
- `ImageCrop+`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `KSamplerSelect`
- `Load RetinaFace`
- `LoadImage`
- `Mask Crop Region`
- `MaskBlur+`
- `MaskToImage`
- `MiniCPM_VQA`
- `PreviewImage`
- `RandomNoise`
- `SAMDetectorCombined`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StringConstant`
- `Switch any [Crystools]`
- `TextCombinerTwo`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy mathString`

**可变部分**（部分 workflow 才有）：
- `Image Overlay` —— 9/10 个有
- `JjkText` —— 9/10 个有
- `LayerColor: ColorAdapter` —— 9/10 个有
- `LoraLoader` —— 9/10 个有
- `EmptyImage` —— 4/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `AIO_Preprocessor` —— 1/10 个有
- `CLIPLoader` —— 1/10 个有
- `ControlNetApplySD3` —— 1/10 个有
- `FluxGuidance` —— 1/10 个有
- `Int Literal` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LayerColor: Brightness & Contrast` —— 1/10 个有
- `ModelSamplingFlux` —— 1/10 个有
- `SetUnionControlNetType` —— 1/10 个有
- `solarL_SaveImagesToZip` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 15 | 10 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 10 | 22% |
| 采样算法 | euler_ancestral | - | 10 | 90% |
| 调度器 | sgm_uniform | - | 10 | 80% |
| 重绘幅度 | 0.5 | 0.5 - 1 | 10 | 72% |
| LoRA 模型强度 | 0.6 | 0.6 - 0.6 | 9 | 100% |
| LoRA 文本强度 | 0.6 | 0.6 - 0.6 | 9 | 100% |
| 宽度 | 768 | 80 - 1296 | 10 | 64% |
| 高度 | 1024 | 80 - 1912 | 10 | 60% |
| ControlNet 权重 | 0.85 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 15，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，10 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler_ancestral，10 个样本，一致性 90%
- 调度器 最常用 sgm_uniform，10 个样本，一致性 80%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 1，10 个样本
- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.6，9 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.6，观测区间 0.6 - 0.6，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 80 - 1296，10 个样本
- 高度 中位数 1024，观测区间 80 - 1912，10 个样本

---
name: text_to_image_controlnet_inpaint_upscale
type: Text To Image
frequency: 3
level: strong
coverage: 0.784333
common_nodes: [ApplyInstantID, BasicGuider, BasicScheduler, BboxDetectorSEGS, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, Crop Face, DF_Image_scale_to_side, DisplayText, DualCLIPLoader, EmptyLatentImage, GrowMask, ImageComposite+, ImageCrop+, ImageResize+, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, KSamplerSelect, Load RetinaFace, LoadImage, Mask Crop Region, MaskBlur+, MaskToImage, MiniCPM_VQA, PreviewImage, RandomNoise, SAMDetectorCombined, SAMLoader, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StringConstant, Switch any [Crystools], TextCombinerTwo, UNETLoader, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy mathString]
problems: []
missing: [Crop Face, ImageComposite+, ImageCrop+, Int Literal, Label (rgthree), LayerColor: Brightness & Contrast, Load RetinaFace, Mask Crop Region, MaskBlur+, Switch any [Crystools], easy cleanGpuUsed, easy mathString, ImageResize+]
members: [图片生成/文生图/1917802869850832898.json, 图片生成/文生图/影视级海报（可换脸）_2094309374767489025.json, 图片生成/文生图/影视级海报（可换脸）_2094319722920767490.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_upscale

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1917802869850832898.json、图片生成/文生图/影视级海报（可换脸）_2094309374767489025.json、图片生成/文生图/影视级海报（可换脸）_2094319722920767490.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Image Overlay` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LayerColor: ColorAdapter` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ControlNetApplySD3` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `Int Literal` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerColor: Brightness & Contrast` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 15 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.5 - 0.75 | 3 | 80% |
| 宽度 | 768 | 768 - 1296 | 3 | 74% |
| 高度 | 1024 | 1024 - 1912 | 3 | 68% |
| ControlNet 权重 | 0.85 | - | 1 | 100% |
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 15，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.75，3 个样本
- 宽度 中位数 768，观测区间 768 - 1296，3 个样本
- 高度 中位数 1024，观测区间 1024 - 1912，3 个样本
- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Crop Face、ImageComposite+、ImageCrop+、Int Literal、Label (rgthree)

---
name: text_to_image_controlnet_inpaint_sampler
type: Text To Image
frequency: 6
level: moderate
coverage: 0.804167
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, CropMask, EmptyLatentImage, FaceAnalysisModels, FaceBoundingBox, GrowMask, Image Comparer (rgthree), ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, RepeatLatentBatch, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/sdxl+controlnet+instantid+放大人像写真工作流_2001999132841656322.json, 图片生成/图生图/sdxl+controlnet+instantid+放大人像写真工作流_2009254162868998146.json, 图片生成/图生图/人像写真工作流(z-image+instanid+放大)_2009965331032317953.json, 图片生成/图生图/人像写真（反推提示词+z-image生图+换face）_2017134809528668162.json, 图片生成/文生图/SDXL+contronet+换脸+SD放大面部修复工作流_1988882107839680513.json, 图片生成/文生图/文生图+换脸放大模型工作流_1988772214726078465.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_sampler

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/sdxl+controlnet+instantid+放大人像写真工作流_2001999132841656322.json、图片生成/图生图/sdxl+controlnet+instantid+放大人像写真工作流_2009254162868998146.json、图片生成/图生图/人像写真工作流(z-image+instanid+放大)_2009965331032317953.json、图片生成/图生图/人像写真（反推提示词+z-image生图+换face）_2017134809528668162.json、图片生成/文生图/SDXL+contronet+换脸+SD放大面部修复工作流_1988882107839680513.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `CropMask`
- `EmptyLatentImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskBlur+`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `UpscaleModelLoader` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LoraLoader` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `VAELoader` —— 4/6 个有
- `CR Text Concatenate` —— 3/6 个有
- `CannyEdgePreprocessor` —— 3/6 个有
- `ControlNetApplySD3` —— 3/6 个有
- `DepthAnythingPreprocessor` —— 3/6 个有
- `ImageScaleBy` —— 3/6 个有
- `ImageUpscaleWithModel` —— 3/6 个有
- `OpenposePreprocessor` —— 3/6 个有
- `SUPIR_Upscale` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `easy imageSize` —— 3/6 个有
- `CLIPLoader` —— 2/6 个有
- `DualCLIPLoader` —— 2/6 个有
- `TextInputBasic` —— 2/6 个有
- `UltimateSDUpscale` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `CR Aspect Ratio` —— 1/6 个有
- `Display Any (rgthree)` —— 1/6 个有
- `FaceDetailer` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `UltralyticsDetectorProvider` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 25 | 6 | 63% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 5 | 6 | 34% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | karras | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 832 | 768 - 1024 | 6 | 87% |
| 高度 | 1088 | 1024 - 1536 | 6 | 81% |
| LoRA 模型强度 | 0.8 | 0.6 - 0.8 | 4 | 88% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 5，6 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 karras，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 832，观测区间 768 - 1024，6 个样本，取值集中（一致性 87%）
- 高度 中位数 1088，观测区间 1024 - 1536，6 个样本，取值集中（一致性 81%）
- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 0.8，4 个样本，取值集中（一致性 88%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）

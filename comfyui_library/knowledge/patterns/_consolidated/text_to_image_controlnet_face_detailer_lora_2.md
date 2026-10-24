---
name: text_to_image_controlnet_face_detailer_lora_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.897
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Latent Batch Size, CR Text Concatenate, ConditioningZeroOut, ConstrainImage|pysssss, ControlNetApplySD3, ControlNetLoader, DepthAnythingPreprocessor, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, ExpressionEditor, FaceDetailer, Float, FluxGuidance, GetImageSize+, ImpactInt, JanusImageUnderstanding, JanusModelLoader, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, MirroredImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, ShowText|pysssss, StyleModelApply, StyleModelLoader, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/循环批量超级仿图工作流2_1982812634879787010.json, 图片生成/图生图/洗稿丨洗图丨图生图丨小红书风格_1892481793889898497.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_face_detailer_lora_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/循环批量超级仿图工作流2_1982812634879787010.json、图片生成/图生图/洗稿丨洗图丨图生图丨小红书风格_1892481793889898497.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Latent Batch Size`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ExpressionEditor`
- `FaceDetailer`
- `Float`
- `FluxGuidance`
- `GetImageSize+`
- `ImpactInt`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `MirroredImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 1/2 个有
- `CR Overlay Transparent Image` —— 1/2 个有
- `ETN_Translate` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `RHExtractImage` —— 1/2 个有
- `RHUploadZip` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy sleep` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

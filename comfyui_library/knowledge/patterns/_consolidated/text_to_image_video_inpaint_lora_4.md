---
name: text_to_image_video_inpaint_lora_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.959
common_nodes: [AnySwitch, BasicScheduler, BlendInpaint, BlockifyMask, CFGGuider, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CM_FloatBinaryOperation, CM_FloatToInt, CM_IntToFloat, CropByMask, DrawMaskOnImage, DrawViTPose, EmptyLatentImage, GrowMask, ImageAndMaskPreview, ImageCropMerge, ImageFromBatch, ImageScale, ImageScaleToTotalPixels, ImageToMask, Int, KSampler, KSamplerSelect, LayerMask: PersonMaskUltra V2, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, LoadImage, Lora Loader Stack (rgthree), LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, ModelSamplingAuraFlow, OnnxDetectionModelLoader, PerturbedAttentionGuidance, PoseAndFaceDetection, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, RepeatImageBatch, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy boolean, easy cleanGpuUsed, easy imageSize, easy int, easy isMaskEmpty, easy mathInt, easy seed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/Owen3.5 反推图生图+套图_2040437491571888130.json, 图片生成/图生图/生图+套图（华圣）_2037723349052297217.json]
source: knowledge_consolidation
---

# text_to_image_video_inpaint_lora_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Owen3.5 反推图生图+套图_2040437491571888130.json、图片生成/图生图/生图+套图（华圣）_2037723349052297217.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `AnySwitch`
- `BasicScheduler`
- `BlendInpaint`
- `BlockifyMask`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CM_FloatBinaryOperation`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CropByMask`
- `DrawMaskOnImage`
- `DrawViTPose`
- `EmptyLatentImage`
- `GrowMask`
- `ImageAndMaskPreview`
- `ImageCropMerge`
- `ImageFromBatch`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch1way`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `OnnxDetectionModelLoader`
- `PerturbedAttentionGuidance`
- `PoseAndFaceDetection`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReferenceLatent`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy int`
- `easy isMaskEmpty`
- `easy mathInt`
- `easy seed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 75% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
key: 视频生成/图生视频/LTX-2.3 character-sheet参考视频_2075079874481577986.json
name: LTX-2.3 character-sheet参考视频_2075079874481577986.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 character-sheet参考视频_2075079874481577986.json
hash: d200b73ad653a254
coverage: 0.522581
learned_at: 2026-10-15 22:41:21
nodes: [GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PrimitiveFloat, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, ComfyNumberConvert, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVEmptyLatentAudio, SetNode, GetNode, GetNode, SetNode, GetNode, LTXVConcatAVLatent, GetNode, LTXVConditioning, SetNode, CLIPTextEncode, SetNode, GetNode, GetNode, SetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, RandomNoise, CFGGuider, ManualSigmas, LTX2SamplingPreviewOverride, GetNode, GetNode, LTXVChunkFeedForward, LTX2AttentionTunerPatch, SamplerCustomAdvanced, SetNode, VAEDecodeAudio, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, ComfySwitchNode, SamplerCustomAdvanced, SimpleCalculatorKJ, PrimitiveBoolean, ComfySwitchNode, ComfySwitchNode, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, PrimitiveBoolean, GetNode, GetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, LTXIdentityOverlapConditioning, GetNode, KSamplerSelect, ImageResizeKJv2, LTX2MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, RandomNoise, MarkdownNote, LoraLoaderModelOnly, ModelSamplingSD3, BasicScheduler, ManualSigmas, INTConstant, INTConstant, INTConstant, ImageCropV2, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, UNETLoader, ComfySwitchNode, LTX2SamplingPreviewOverride, TextGenerate, LTX2_NAG, StringConcatenate, StringConcatenate, LTXVConcatAVLatent, LTXIdentityOverlapConditioning, ComfySwitchNode, LTXVCropGuides, GetNode, SetNode, VAEDecodeTiled, GetNode, GetNode, ConditioningZeroOut, CLIPLoader, VAELoader, KSampler, ImageConcatMulti, VAEEncode, TextEncodeQwenImageEditPlusAdvance_lrzjason, Context (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, ResizeImageMaskNode, SetNode, CropFace, ImageResizeKJv2, easy cleanGpuUsed, PrimitiveStringMultiline, LoadImage, Power Lora Loader (rgthree), SetNode, PreviewImage, EmptySD3LatentImage, AIO_Preprocessor, LoadImage, UNETLoader, PreviewImage, CreateVideo, SaveVideo]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 25, "sampler_name": "er_sde", "scheduler": "beta57", "seed": 810617380969503, "steps": 8, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX-2.3 character-sheet参考视频_2075079874481577986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075079874481577986.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（155 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfyNumberConvert`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `VAEDecodeAudio` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `SamplerCustomAdvanced` ★核心
- `SimpleCalculatorKJ`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `PrimitiveBoolean`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXIdentityOverlapConditioning`
- `GetNode`
- `KSamplerSelect` ★核心
- `ImageResizeKJv2`
- `LTX2MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `BasicScheduler`
- `ManualSigmas`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageCropV2`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `LTX2SamplingPreviewOverride`
- `TextGenerate`
- `LTX2_NAG`
- `StringConcatenate`
- `StringConcatenate`
- `LTXVConcatAVLatent`
- `LTXIdentityOverlapConditioning`
- `ComfySwitchNode`
- `LTXVCropGuides`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `ImageConcatMulti`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Context (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ResizeImageMaskNode`
- `SetNode`
- `CropFace`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Power Lora Loader (rgthree)`
- `SetNode`
- `PreviewImage`
- `EmptySD3LatentImage`
- `AIO_Preprocessor`
- `LoadImage`
- `UNETLoader` ★核心
- `PreviewImage`
- `CreateVideo`
- `SaveVideo`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `810617380969503`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **52%**（81/155）

**有卡**：`ComfyNumberConvert`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`LTX2SamplingPreviewOverride`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`SimpleCalculatorKJ`、`PrimitiveBoolean`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`KSamplerSelect`、`LTXIdentityOverlapConditioning`、`ImageResizeKJv2`、`LTX2MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`BasicScheduler`、`INTConstant`、`ImageCropV2`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`UNETLoader`、`TextGenerate`、`LTX2_NAG`、`StringConcatenate`、`VAEDecodeTiled`、`ConditioningZeroOut`、`CLIPLoader`、`KSampler`、`ImageConcatMulti`、`VAEEncode`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`Context (rgthree)`、`VAEDecode`、`ResizeImageMaskNode`、`CropFace`、`easy cleanGpuUsed`、`LoadImage`、`Power Lora Loader (rgthree)`、`EmptySD3LatentImage`、`AIO_Preprocessor`、`CreateVideo`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

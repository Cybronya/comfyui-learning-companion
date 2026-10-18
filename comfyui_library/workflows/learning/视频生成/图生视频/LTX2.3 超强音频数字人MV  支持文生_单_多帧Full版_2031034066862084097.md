---
key: 视频生成/图生视频/LTX2.3 超强音频数字人MV  支持文生_单_多帧Full版_2031034066862084097.json
name: LTX2.3 超强音频数字人MV  支持文生_单_多帧Full版_2031034066862084097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 超强音频数字人MV  支持文生_单_多帧Full版_2031034066862084097.json
hash: 55ad025c7c53038c
coverage: 0.851485
learned_at: 2026-10-15 22:35:29
nodes: [KSamplerSelect, CFGGuider, easy convertAnything, LTXVConcatAVLatent, ManualSigmas, CLIPTextEncode, PreviewAny, RH_LLMAPI_Pro_Node, easy ifElse, easy indexAnything, EmptyLTXVLatentVideo, MarkdownNote, easy forLoopEnd, LoadImage, LoadImage, SimpleMathDual+, GetImageSize, LTXVAudioVAEEncode, SolidMask, Audio Duration (mtb), SetLatentNoiseMask, MathExpression|pysssss, LoadImage, Any Switch (rgthree), LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, CreateVideo, Any Switch (rgthree), LTXVAudioVAEDecode, LTXVCropGuides, LayerUtility: PurgeVRAM V2, CLIPTextEncode, LTX2_NAG, LTXVEnhanceAVideoKJ, VAEDecodeTiled, Sigmas Rescale, LTXVCropGuides, SaveVideo, ImageBatchMulti, LTXVConditioning, PrimitiveString, easy imagesSplitImage, LTXVImgToVideoConditionOnly, easy compare, easy int, LTX2SamplingPreviewOverride, LTXVPreprocess, LTXVAddGuideMulti, easy anythingIndexSwitch, ImageResizeKJv2, easy indexAnything, MathExpression|pysssss, Any Switch (rgthree), easy lengthAnything, easy batchAnything, CreateVideo, LTXVLatentUpsampler, easy blocker, PrimitiveInt, PrimitiveFloat, RandomNoise, easy positive, easy anythingIndexSwitch, easy anythingIndexSwitch, LTXVAddGuideMulti, KSamplerSelect, LTXVEmptyLatentAudio, ManualSigmas, SaveVideo, LoadAudio, PrimitiveInt, AudioCrop, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, easy indexAnything, easy indexAnything, easy indexAnything, easy forLoopStart, TextSplitByDelimiter, easy indexAnything, SimpleMath+, LTXVImgToVideoConditionOnly, CFGGuider, VAEDecodeTiled, LTXVAudioVAEDecode, Any Switch (rgthree), easy mathInt, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, easy int, ImpactSwitch, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 超强音频数字人MV  支持文生_单_多帧Full版_2031034066862084097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031034066862084097.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `easy convertAnything`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `RH_LLMAPI_Pro_Node`
- `easy ifElse`
- `easy indexAnything`
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `easy forLoopEnd`
- `LoadImage`
- `LoadImage`
- `SimpleMathDual+`
- `GetImageSize`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `Audio Duration (mtb)`
- `SetLatentNoiseMask`
- `MathExpression|pysssss`
- `LoadImage`
- `Any Switch (rgthree)`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CreateVideo`
- `Any Switch (rgthree)`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LTXVEnhanceAVideoKJ`
- `VAEDecodeTiled` ★核心
- `Sigmas Rescale`
- `LTXVCropGuides`
- `SaveVideo`
- `ImageBatchMulti`
- `LTXVConditioning`
- `PrimitiveString`
- `easy imagesSplitImage`
- `LTXVImgToVideoConditionOnly`
- `easy compare`
- `easy int`
- `LTX2SamplingPreviewOverride`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`
- `easy anythingIndexSwitch`
- `ImageResizeKJv2`
- `easy indexAnything`
- `MathExpression|pysssss`
- `Any Switch (rgthree)`
- `easy lengthAnything`
- `easy batchAnything`
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `easy blocker`
- `PrimitiveInt`
- `PrimitiveFloat`
- `RandomNoise`
- `easy positive`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `LTXVAddGuideMulti`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `SaveVideo`
- `LoadAudio`
- `PrimitiveInt`
- `AudioCrop`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy forLoopStart`
- `TextSplitByDelimiter`
- `easy indexAnything`
- `SimpleMath+`
- `LTXVImgToVideoConditionOnly`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Any Switch (rgthree)`
- `easy mathInt`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy int`
- `ImpactSwitch`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（86/101）

**有卡**：`KSamplerSelect`、`CFGGuider`、`easy convertAnything`、`LTXVConcatAVLatent`、`ManualSigmas`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`easy indexAnything`、`EmptyLTXVLatentVideo`、`easy forLoopEnd`、`LoadImage`、`SimpleMathDual+`、`GetImageSize`、`LTXVAudioVAEEncode`、`SolidMask`、`Audio Duration (mtb)`、`SetLatentNoiseMask`、`MathExpression|pysssss`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`RandomNoise`、`CreateVideo`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LayerUtility: PurgeVRAM V2`、`LTX2_NAG`、`LTXVEnhanceAVideoKJ`、`VAEDecodeTiled`、`Sigmas Rescale`、`SaveVideo`、`ImageBatchMulti`、`LTXVConditioning`、`easy imagesSplitImage`、`LTXVImgToVideoConditionOnly`、`easy compare`、`easy int`、`LTX2SamplingPreviewOverride`、`LTXVPreprocess`、`LTXVAddGuideMulti`、`easy anythingIndexSwitch`、`ImageResizeKJv2`、`easy lengthAnything`、`easy batchAnything`、`LTXVLatentUpsampler`、`easy blocker`、`easy positive`、`LTXVEmptyLatentAudio`、`LoadAudio`、`AudioCrop`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`easy forLoopStart`、`TextSplitByDelimiter`、`SimpleMath+`、`easy mathInt`、`PrimitiveBoolean`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

---
key: 数字人/数字人/LTX2.3 视频二次创作 删减增加元素 更改视频 视频编辑_2057650056811077633.json
name: LTX2.3 视频二次创作 删减增加元素 更改视频 视频编辑_2057650056811077633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 视频二次创作 删减增加元素 更改视频 视频编辑_2057650056811077633.json
hash: 8f3a74f646f7f136
coverage: 0.421875
learned_at: 2026-10-26 01:55:53
nodes: [SetNode, GetImageSize, SolidMask, LTXVAudioVAEEncode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LTXVCropGuides, LTXVEmptyLatentAudio, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, LTXVConcatAVLatent, EmptyAudio, TrimAudioDuration, VAEEncode, ImageResizeKJv2, Reroute, KSamplerSelect, BasicScheduler, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, easy convertAnything, GetNode, GetImageRangeFromBatch, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcanate, SetNode, UNETLoader, ImageConcanate, GetNode, Note, GetNode, SetNode, Reroute, SetLatentNoiseMask, Note, Note, CLIPLoader, SetNode, SetNode, SetNode, GetNode, ImageScaleBy, LTXVPreprocess, LTXVAddGuideMulti, VHS_VideoCombine, SetNode, VAEDecode, SetNode, SetNode, SetNode, SamplerCustomAdvanced, Reroute, CFGGuider, Note, ManualSigmas, APGGuider, easy cleanGpuUsed, SetNode, GetNode, LTXVConditioning, LTXVAddGuide, SetNode, UnetLoaderGGUF, CLIPTextEncode, CLIPTextEncode, ShowText|pysssss, TextGenerate, ImageScaleBy, LoraLoaderModelOnly, SetNode, ResizeImageMaskNode, GetNode, GetNode, LoraLoaderModelOnly, GetNode, StringConcatenate, SetNode, GetNode, SimpleCalculatorKJ, SetNode, SetNode, Note, PrimitiveFloat, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RandomNoise, Textbox, PrimitiveFloat, Label (rgthree), VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, PrimitiveFloat, PrimitiveInt, LoadAudio, RecordAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 数字人/数字人/LTX2.3 视频二次创作 删减增加元素 更改视频 视频编辑_2057650056811077633.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 视频二次创作 删减增加元素 更改视频 视频编辑_2057650056811077633.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（128 个）：
- `SetNode`
- `GetImageSize`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVConcatAVLatent`
- `EmptyAudio`
- `TrimAudioDuration`
- `VAEEncode` ★核心
- `ImageResizeKJv2`
- `Reroute`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `easy convertAnything`
- `GetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `SetNode`
- `UNETLoader` ★核心
- `ImageConcanate`
- `GetNode`
- `Note`
- `GetNode`
- `SetNode`
- `Reroute`
- `SetLatentNoiseMask`
- `Note`
- `Note`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageScaleBy`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`
- `VHS_VideoCombine`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `CFGGuider`
- `Note`
- `ManualSigmas`
- `APGGuider`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `LTXVAddGuide`
- `SetNode`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `TextGenerate`
- `ImageScaleBy`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `StringConcatenate`
- `SetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `SetNode`
- `Note`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `Textbox`
- `PrimitiveFloat`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LoadAudio`
- `RecordAudio`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **42%**（54/128）

**有卡**：`GetImageSize`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVCropGuides`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`EmptyAudio`、`TrimAudioDuration`、`VAEEncode`、`ImageResizeKJv2`、`KSamplerSelect`、`BasicScheduler`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`easy convertAnything`、`GetImageRangeFromBatch`、`ImageConcanate`、`UNETLoader`、`SetLatentNoiseMask`、`CLIPLoader`、`ImageScaleBy`、`LTXVPreprocess`、`LTXVAddGuideMulti`、`VHS_VideoCombine`、`VAEDecode`、`SamplerCustomAdvanced`、`CFGGuider`、`ManualSigmas`、`APGGuider`、`easy cleanGpuUsed`、`LTXVConditioning`、`LTXVAddGuide`、`UnetLoaderGGUF`、`CLIPTextEncode`、`TextGenerate`、`LoraLoaderModelOnly`、`ResizeImageMaskNode`、`StringConcatenate`、`SimpleCalculatorKJ`、`RandomNoise`、`Textbox`、`Label (rgthree)`、`VHS_LoadVideo`、`LoadAudio`、`RecordAudio`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

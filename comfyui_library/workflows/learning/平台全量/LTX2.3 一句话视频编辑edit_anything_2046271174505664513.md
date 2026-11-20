---
key: 平台全量/LTX2.3 一句话视频编辑edit_anything_2046271174505664513.json
name: LTX2.3 一句话视频编辑edit_anything_2046271174505664513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 一句话视频编辑edit_anything_2046271174505664513.json
hash: 88615d40ea1bf3ac
coverage: 0.396947
learned_at: 2026-11-14 00:37:38
nodes: [SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetImageSize, SolidMask, LTXVAudioVAEEncode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, RecordAudio, GetNode, GetNode, GetNode, LTXVCropGuides, SetNode, VAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, GetNode, SetNode, GetNode, LTXVSeparateAVLatent, SimpleCalculatorKJ, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, Reroute, SetLatentNoiseMask, Note, PrimitiveFloat, PrimitiveFloat, SetNode, SetNode, EmptyAudio, SetNode, TrimAudioDuration, Note, GetNode, VAEEncode, SetNode, SetNode, Note, PrimitiveFloat, PrimitiveInt, GetNode, GetNode, GetNode, ImageConcanate, GetNode, SetNode, GetNode, ImageConcanate, Note, SetNode, SetNode, Note, GetNode, Reroute, CLIPTextEncode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, CLIPTextEncode, LTXVConditioning, ImageScaleBy, ResizeImageMaskNode, GetNode, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, MarkdownNote, Reroute, SetNode, UNETLoader, APGGuider, ManualSigmas, Reroute, KSamplerSelect, BasicScheduler, CFGGuider, MarkdownNote, ShowText|pysssss, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, LoadAudio, UnetLoaderGGUF, CLIPLoader, LoraLoaderModelOnly, easy convertAnything, StringConcatenate, TextGenerate, easy cleanGpuUsed, LTXVAddGuide, Reroute, CreateVideo, LTXVPreprocess, RandomNoise, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_LoadVideo, PrimitiveNode, SaveVideo, ImageScaleBy, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 平台全量/LTX2.3 一句话视频编辑edit_anything_2046271174505664513.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 一句话视频编辑edit_anything_2046271174505664513.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（131 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `RecordAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SimpleCalculatorKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `Reroute`
- `SetLatentNoiseMask`
- `Note`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `EmptyAudio`
- `SetNode`
- `TrimAudioDuration`
- `Note`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `Note`
- `PrimitiveFloat`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImageConcanate`
- `Note`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `Reroute`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ImageScaleBy`
- `ResizeImageMaskNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `MarkdownNote`
- `Reroute`
- `SetNode`
- `UNETLoader` ★核心
- `APGGuider`
- `ManualSigmas`
- `Reroute`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `MarkdownNote`
- `ShowText|pysssss`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `easy convertAnything`
- `StringConcatenate`
- `TextGenerate`
- `easy cleanGpuUsed`
- `LTXVAddGuide`
- `Reroute`
- `CreateVideo`
- `LTXVPreprocess`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `PrimitiveNode`
- `SaveVideo`
- `ImageScaleBy`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **40%**（52/131）

**有卡**：`GetImageSize`、`SolidMask`、`LTXVAudioVAEEncode`、`RecordAudio`、`LTXVCropGuides`、`VAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SimpleCalculatorKJ`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`EmptyAudio`、`TrimAudioDuration`、`VAEEncode`、`ImageConcanate`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVConditioning`、`ImageScaleBy`、`ResizeImageMaskNode`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`UNETLoader`、`APGGuider`、`ManualSigmas`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LoadAudio`、`UnetLoaderGGUF`、`CLIPLoader`、`easy convertAnything`、`StringConcatenate`、`TextGenerate`、`easy cleanGpuUsed`、`LTXVAddGuide`、`CreateVideo`、`LTXVPreprocess`、`RandomNoise`、`VHS_VideoCombine`、`VHS_LoadVideo`、`SaveVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

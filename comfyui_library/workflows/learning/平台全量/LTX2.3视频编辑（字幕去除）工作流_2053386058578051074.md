---
key: 平台全量/LTX2.3视频编辑（字幕去除）工作流_2053386058578051074.json
name: LTX2.3视频编辑（字幕去除）工作流_2053386058578051074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3视频编辑（字幕去除）工作流_2053386058578051074.json
hash: ed06c8a120a3b799
coverage: 0.403509
learned_at: 2026-11-14 00:39:03
nodes: [SetNode, GetImageSize, SolidMask, LTXVAudioVAEEncode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LTXVCropGuides, LTXVEmptyLatentAudio, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, LTXVConcatAVLatent, EmptyAudio, TrimAudioDuration, VAEEncode, KSamplerSelect, BasicScheduler, DualCLIPLoader, LatentUpscaleModelLoader, easy convertAnything, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcanate, SetNode, ImageConcanate, GetNode, Note, SetNode, Reroute, SetLatentNoiseMask, Note, Note, PrimitiveFloat, SetNode, SetNode, SetNode, GetNode, ImageScaleBy, LTXVPreprocess, SetNode, VAEDecode, SetNode, SetNode, SetNode, SamplerCustomAdvanced, Reroute, CFGGuider, Note, ManualSigmas, APGGuider, easy cleanGpuUsed, SetNode, GetNode, LTXVConditioning, LTXVAddGuide, RecordAudio, ImageScaleBy, VHS_VideoCombine, GetNode, PrimitiveInt, SetNode, GetNode, SimpleCalculatorKJ, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RandomNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_LoadVideo, GetNode, Textbox, UNETLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, GetNode, SetNode, PrimitiveFloat, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, Label (rgthree), LoadAudio, VHS_VideoCombine, SetNode, ResizeImageMaskNode, GetNode, Reroute, GetNode, PrimitiveFloat, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 平台全量/LTX2.3视频编辑（字幕去除）工作流_2053386058578051074.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3视频编辑（字幕去除）工作流_2053386058578051074.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（114 个）：
- `SetNode`
- `GetImageSize`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
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
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `SetNode`
- `ImageConcanate`
- `GetNode`
- `Note`
- `SetNode`
- `Reroute`
- `SetLatentNoiseMask`
- `Note`
- `Note`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageScaleBy`
- `LTXVPreprocess`
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
- `RecordAudio`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `GetNode`
- `Textbox`
- `UNETLoader` ★核心
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `LoadAudio`
- `VHS_VideoCombine`
- `SetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `PrimitiveFloat`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **40%**（46/114）

**有卡**：`GetImageSize`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVCropGuides`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`EmptyAudio`、`TrimAudioDuration`、`VAEEncode`、`KSamplerSelect`、`BasicScheduler`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`easy convertAnything`、`ImageConcanate`、`SetLatentNoiseMask`、`ImageScaleBy`、`LTXVPreprocess`、`VAEDecode`、`SamplerCustomAdvanced`、`CFGGuider`、`ManualSigmas`、`APGGuider`、`easy cleanGpuUsed`、`LTXVConditioning`、`LTXVAddGuide`、`RecordAudio`、`VHS_VideoCombine`、`SimpleCalculatorKJ`、`RandomNoise`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`Textbox`、`UNETLoader`、`VAELoaderKJ`、`CLIPTextEncode`、`Label (rgthree)`、`LoadAudio`、`ResizeImageMaskNode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LatentUpscaleModelLoader

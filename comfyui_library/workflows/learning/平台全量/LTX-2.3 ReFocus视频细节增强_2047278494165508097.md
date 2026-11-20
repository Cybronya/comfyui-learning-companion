---
key: 平台全量/LTX-2.3 ReFocus视频细节增强_2047278494165508097.json
name: LTX-2.3 ReFocus视频细节增强_2047278494165508097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.3 ReFocus视频细节增强_2047278494165508097.json
hash: c94c9c5200a90a29
coverage: 0.376068
learned_at: 2026-11-14 00:36:50
nodes: [SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetImageSize, SolidMask, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, RecordAudio, GetNode, GetNode, LTXVCropGuides, SetNode, SamplerCustomAdvanced, VAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, GetNode, SetNode, GetNode, LTXVSeparateAVLatent, LTXVConditioning, SimpleCalculatorKJ, SetNode, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, GetNode, Reroute, Note, RandomNoise, PrimitiveFloat, SetNode, SetNode, ResizeImageMaskNode, GetNode, SetNode, Note, ManualSigmas, KSamplerSelect, BasicScheduler, GetNode, easy cleanGpuUsed, SetNode, GetNode, MarkdownNote, SetNode, Note, PrimitiveFloat, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, ImageScaleBy, ImageConcanate, GetNode, GetNode, LTXVPreprocess, SetNode, Note, GetNode, Note, Reroute, GetNode, Reroute, ImageConcanate, SetNode, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, GetNode, SetLatentNoiseMask, LTXVConcatAVLatent, easy convertAnything, PrimitiveFloat, LTXVAudioVAEEncode, VHS_VideoCombine, EmptyAudio, TrimAudioDuration, GetNode, GetNode, LoadAudio, ImageScaleBy, CLIPTextEncode, CreateVideo, SaveVideo, VHS_LoadVideo, VHS_VideoCombine, LTXVAddGuide, CFGGuider, VAEEncode, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 平台全量/LTX-2.3 ReFocus视频细节增强_2047278494165508097.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.3 ReFocus视频细节增强_2047278494165508097.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（117 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SolidMask`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
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
- `LTXVCropGuides`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `SimpleCalculatorKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Note`
- `RandomNoise`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `SetNode`
- `Note`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `SetNode`
- `Note`
- `PrimitiveFloat`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `Note`
- `GetNode`
- `Note`
- `Reroute`
- `GetNode`
- `Reroute`
- `ImageConcanate`
- `SetNode`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `GetNode`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `easy convertAnything`
- `PrimitiveFloat`
- `LTXVAudioVAEEncode` ★核心
- `VHS_VideoCombine`
- `EmptyAudio`
- `TrimAudioDuration`
- `GetNode`
- `GetNode`
- `LoadAudio`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `SaveVideo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LTXVAddGuide`
- `CFGGuider`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **38%**（44/117）

**有卡**：`GetImageSize`、`SolidMask`、`RecordAudio`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`VAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`SimpleCalculatorKJ`、`CLIPTextEncode`、`RandomNoise`、`ResizeImageMaskNode`、`ManualSigmas`、`KSamplerSelect`、`BasicScheduler`、`easy cleanGpuUsed`、`ImageScaleBy`、`ImageConcanate`、`LTXVPreprocess`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`easy convertAnything`、`LTXVAudioVAEEncode`、`VHS_VideoCombine`、`EmptyAudio`、`TrimAudioDuration`、`LoadAudio`、`CreateVideo`、`SaveVideo`、`VHS_LoadVideo`、`LTXVAddGuide`、`CFGGuider`、`VAEEncode`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LatentUpscaleModelLoader

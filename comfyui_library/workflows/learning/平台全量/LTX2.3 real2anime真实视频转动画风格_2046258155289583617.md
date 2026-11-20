---
key: 平台全量/LTX2.3 real2anime真实视频转动画风格_2046258155289583617.json
name: LTX2.3 real2anime真实视频转动画风格_2046258155289583617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 real2anime真实视频转动画风格_2046258155289583617.json
hash: e6b7954ecdc20a30
coverage: 0.376068
learned_at: 2026-11-14 00:37:37
nodes: [SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetImageSize, SolidMask, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, RecordAudio, GetNode, GetNode, LTXVCropGuides, SetNode, SamplerCustomAdvanced, VAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, GetNode, SetNode, GetNode, LTXVSeparateAVLatent, LTXVConditioning, SimpleCalculatorKJ, SetNode, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, GetNode, Reroute, Note, PrimitiveFloat, SetNode, SetNode, ResizeImageMaskNode, GetNode, SetNode, Note, ManualSigmas, KSamplerSelect, CFGGuider, BasicScheduler, GetNode, VAEEncode, easy cleanGpuUsed, SetNode, GetNode, MarkdownNote, SetNode, Note, PrimitiveFloat, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, ImageConcanate, GetNode, GetNode, LTXVPreprocess, SetNode, Note, GetNode, Note, Reroute, GetNode, ImageConcanate, SetNode, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, CreateVideo, GetNode, ImageScaleBy, SetLatentNoiseMask, LTXVConcatAVLatent, easy convertAnything, LTXVAddGuide, PrimitiveFloat, LTXVAudioVAEEncode, EmptyAudio, TrimAudioDuration, GetNode, GetNode, VHS_VideoCombine, LoadAudio, LoraLoaderModelOnly, CLIPTextEncode, RandomNoise, Reroute, ImageScaleBy, VHS_LoadVideo, SaveVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 平台全量/LTX2.3 real2anime真实视频转动画风格_2046258155289583617.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 real2anime真实视频转动画风格_2046258155289583617.json`

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
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `SetNode`
- `Note`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `BasicScheduler`
- `GetNode`
- `VAEEncode` ★核心
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
- `ImageConcanate`
- `SetNode`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `GetNode`
- `ImageScaleBy`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `easy convertAnything`
- `LTXVAddGuide`
- `PrimitiveFloat`
- `LTXVAudioVAEEncode` ★核心
- `EmptyAudio`
- `TrimAudioDuration`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `Reroute`
- `ImageScaleBy`
- `VHS_LoadVideo`
- `SaveVideo`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **38%**（44/117）

**有卡**：`GetImageSize`、`SolidMask`、`RecordAudio`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`VAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`SimpleCalculatorKJ`、`CLIPTextEncode`、`ResizeImageMaskNode`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`BasicScheduler`、`VAEEncode`、`easy cleanGpuUsed`、`ImageConcanate`、`LTXVPreprocess`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`ImageScaleBy`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`easy convertAnything`、`LTXVAddGuide`、`LTXVAudioVAEEncode`、`EmptyAudio`、`TrimAudioDuration`、`VHS_VideoCombine`、`LoadAudio`、`LoraLoaderModelOnly`、`RandomNoise`、`VHS_LoadVideo`、`SaveVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LatentUpscaleModelLoader

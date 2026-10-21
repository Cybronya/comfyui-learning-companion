---
key: 图片生成/文生图/LTX2.3数字人-(修仙传角色)_2064873985099255809.json
name: LTX2.3数字人-(修仙传角色)_2064873985099255809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LTX2.3数字人-(修仙传角色)_2064873985099255809.json
hash: a1553ca4c67a4588
coverage: 0.821782
learned_at: 2026-10-19 23:21:38
nodes: [RandomNoise, LTXVConcatAVLatent, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, RandomNoise, CFGGuider, EmptyLTXVLatentVideo, PrimitiveBoolean, LTXVEmptyLatentAudio, LTXVConcatAVLatent, Note, Note, PrimitiveInt, ResizeImagesByLongerEdge, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LTXVPreprocess, LTXVConditioning, CLIPTextEncode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, VHS_VideoCombine, easy anythingIndexSwitch, GetNode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, easy anythingIndexSwitch, CM_IntUnaryCondition, easy showAnything, CR String To Boolean, LoadAudio, LoraLoaderModelOnly, SetNode, GetNode, LTXVTiledVAEDecode, LTXVTiledVAEDecode, easy int, MelBandRoFormerSampler, MelBandRoFormerModelLoader, PreviewAudio, GetImageSize, VHS_VideoCombine, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoader, UNETLoader, ImpactConditionalBranch, LoadAudio, LoadAudio, IndexTTS2Run, TrimAudioDuration, PrimitiveFloat, PrimitiveFloat, easy showAnything, LoadAudio, SoundFlow_GetLength, LoraLoaderModelOnly, LTXVImgToVideoInplace, KSamplerSelect, KSamplerSelect, PrimitiveStringMultiline, JoinStrings, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, SetNode, LTXVScheduler, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, Reroute, SamplerCustomAdvanced, ImageScaleToTotalPixels, SimpleMath+, PrimitiveInt, easy int, CLIPTextEncode, LoadImage, PrimitiveStringMultiline, CR Prompt Text, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 图片生成/文生图/LTX2.3数字人-(修仙传角色)_2064873985099255809.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LTX2.3数字人-(修仙传角色)_2064873985099255809.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（101 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `Note`
- `Note`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LTXVPreprocess`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `GetNode`
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `easy anythingIndexSwitch`
- `CM_IntUnaryCondition`
- `easy showAnything`
- `CR String To Boolean`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `LTXVTiledVAEDecode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `easy int`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `PreviewAudio`
- `GetImageSize`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `ImpactConditionalBranch`
- `LoadAudio`
- `LoadAudio`
- `IndexTTS2Run`
- `TrimAudioDuration`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `easy showAnything`
- `LoadAudio`
- `SoundFlow_GetLength`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveStringMultiline`
- `JoinStrings`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `SetNode`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `SimpleMath+`
- `PrimitiveInt`
- `easy int`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `CR Prompt Text`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（83/101）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LayerUtility: PurgeVRAM V2`、`LTXVPreprocess`、`LTXVConditioning`、`CLIPTextEncode`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LoadAudio`、`CM_IntUnaryCondition`、`CR String To Boolean`、`LTXVTiledVAEDecode`、`easy int`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`PreviewAudio`、`GetImageSize`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`VAELoader`、`UNETLoader`、`ImpactConditionalBranch`、`IndexTTS2Run`、`TrimAudioDuration`、`SoundFlow_GetLength`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`JoinStrings`、`LTX2_NAG`、`LTXVScheduler`、`LTXVLatentUpsampler`、`ImageScaleToTotalPixels`、`SimpleMath+`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

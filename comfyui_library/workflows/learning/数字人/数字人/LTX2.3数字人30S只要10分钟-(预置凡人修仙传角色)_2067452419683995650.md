---
key: 数字人/数字人/LTX2.3数字人30S只要10分钟-(预置凡人修仙传角色)_2067452419683995650.json
name: LTX2.3数字人30S只要10分钟-(预置凡人修仙传角色)_2067452419683995650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3数字人30S只要10分钟-(预置凡人修仙传角色)_2067452419683995650.json
hash: 22c89ba76d626795
coverage: 0.813187
learned_at: 2026-10-26 01:56:01
nodes: [RandomNoise, CFGGuider, EmptyLTXVLatentVideo, PrimitiveBoolean, LTXVEmptyLatentAudio, Note, PrimitiveInt, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, ComfyMathExpression, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, easy anythingIndexSwitch, GetNode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, LoadAudio, LoadAudio, easy anythingIndexSwitch, CM_IntUnaryCondition, easy showAnything, CR String To Boolean, LoadAudio, CR Prompt Text, LoraLoaderModelOnly, SetNode, GetImageSize, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoader, UNETLoader, MarkdownNote, ImpactConditionalBranch, IndexTTS2Run, TrimAudioDuration, PrimitiveFloat, easy showAnything, SoundFlow_GetLength, LoraLoaderModelOnly, KSamplerSelect, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SamplerCustomAdvanced, SimpleMath+, PrimitiveInt, LTX2_NAG, BasicScheduler, ModelSamplingSD3, LTXVSeparateAVLatent, GetNode, Note, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, JoinStrings, PrimitiveStringMultiline, LTXVTiledVAEDecode, ComfyMathExpression, ComfyMathExpression, VHS_VideoCombine, LTXVConcatAVLatent, PreviewAudio, LTXVImgToVideoInplace, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, PrimitiveStringMultiline, LoadImage, PrimitiveFloat, easy int, ImageScaleToTotalPixels, LoadAudio, easy int, MelBandRoFormerSampler, MelBandRoFormerModelLoader, ResizeImagesByLongerEdge, LTXVPreprocess, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.3数字人30S只要10分钟-(预置凡人修仙传角色)_2067452419683995650.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3数字人30S只要10分钟-(预置凡人修仙传角色)_2067452419683995650.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（91 个）：
- `RandomNoise`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `LTXVEmptyLatentAudio` ★核心
- `Note`
- `PrimitiveInt`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
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
- `easy anythingIndexSwitch`
- `CM_IntUnaryCondition`
- `easy showAnything`
- `CR String To Boolean`
- `LoadAudio`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetImageSize`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `ImpactConditionalBranch`
- `IndexTTS2Run`
- `TrimAudioDuration`
- `PrimitiveFloat`
- `easy showAnything`
- `SoundFlow_GetLength`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SimpleMath+`
- `PrimitiveInt`
- `LTX2_NAG`
- `BasicScheduler`
- `ModelSamplingSD3`
- `LTXVSeparateAVLatent`
- `GetNode`
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `JoinStrings`
- `PrimitiveStringMultiline`
- `LTXVTiledVAEDecode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `PreviewAudio`
- `LTXVImgToVideoInplace`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveFloat`
- `easy int`
- `ImageScaleToTotalPixels`
- `LoadAudio`
- `easy int`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（74/91）

**有卡**：`RandomNoise`、`CFGGuider`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`easy anythingIndexSwitch`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LoadAudio`、`CM_IntUnaryCondition`、`CR String To Boolean`、`CR Prompt Text`、`GetImageSize`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`VAELoader`、`UNETLoader`、`ImpactConditionalBranch`、`IndexTTS2Run`、`TrimAudioDuration`、`SoundFlow_GetLength`、`KSamplerSelect`、`SamplerCustomAdvanced`、`SimpleMath+`、`LTX2_NAG`、`BasicScheduler`、`ModelSamplingSD3`、`LTXVSeparateAVLatent`、`LayerUtility: PurgeVRAM V2`、`JoinStrings`、`LTXVTiledVAEDecode`、`VHS_VideoCombine`、`LTXVConcatAVLatent`、`PreviewAudio`、`LTXVImgToVideoInplace`、`LoadImage`、`easy int`、`ImageScaleToTotalPixels`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

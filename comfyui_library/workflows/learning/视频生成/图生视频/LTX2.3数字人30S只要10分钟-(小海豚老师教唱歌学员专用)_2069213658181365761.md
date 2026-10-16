---
key: 视频生成/图生视频/LTX2.3数字人30S只要10分钟-(小海豚老师教唱歌学员专用)_2069213658181365761.json
name: LTX2.3数字人30S只要10分钟-(小海豚老师教唱歌学员专用)_2069213658181365761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2069213658181365761.json
hash: 7cfabd054d2f8f2b
coverage: 0.811111
learned_at: 2026-10-15 22:40:26
nodes: [RandomNoise, CFGGuider, EmptyLTXVLatentVideo, PrimitiveBoolean, LTXVEmptyLatentAudio, Note, PrimitiveInt, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, ComfyMathExpression, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, easy anythingIndexSwitch, GetNode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, LoadAudio, LoadAudio, easy anythingIndexSwitch, CM_IntUnaryCondition, easy showAnything, CR String To Boolean, LoadAudio, CR Prompt Text, LoraLoaderModelOnly, SetNode, GetImageSize, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoader, UNETLoader, MarkdownNote, ImpactConditionalBranch, IndexTTS2Run, TrimAudioDuration, easy showAnything, SoundFlow_GetLength, LoraLoaderModelOnly, KSamplerSelect, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SamplerCustomAdvanced, SimpleMath+, PrimitiveInt, LTX2_NAG, BasicScheduler, ModelSamplingSD3, LTXVSeparateAVLatent, GetNode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, JoinStrings, PrimitiveStringMultiline, LTXVTiledVAEDecode, ComfyMathExpression, ComfyMathExpression, VHS_VideoCombine, LTXVConcatAVLatent, LTXVImgToVideoInplace, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, PrimitiveFloat, easy int, ImageScaleToTotalPixels, easy int, MelBandRoFormerSampler, MelBandRoFormerModelLoader, ResizeImagesByLongerEdge, LTXVPreprocess, LoadImage, PrimitiveStringMultiline, PrimitiveFloat, LoadAudio, PreviewAudio, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3数字人30S只要10分钟-(小海豚老师教唱歌学员专用)_2069213658181365761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069213658181365761.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（90 个）：
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
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `JoinStrings`
- `PrimitiveStringMultiline`
- `LTXVTiledVAEDecode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `PrimitiveFloat`
- `easy int`
- `ImageScaleToTotalPixels`
- `easy int`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `LoadAudio`
- `PreviewAudio`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（73/90）

**有卡**：`RandomNoise`、`CFGGuider`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`easy anythingIndexSwitch`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LoadAudio`、`CM_IntUnaryCondition`、`CR String To Boolean`、`CR Prompt Text`、`GetImageSize`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`VAELoader`、`UNETLoader`、`ImpactConditionalBranch`、`IndexTTS2Run`、`TrimAudioDuration`、`SoundFlow_GetLength`、`KSamplerSelect`、`SamplerCustomAdvanced`、`SimpleMath+`、`LTX2_NAG`、`BasicScheduler`、`ModelSamplingSD3`、`LTXVSeparateAVLatent`、`LayerUtility: PurgeVRAM V2`、`JoinStrings`、`LTXVTiledVAEDecode`、`VHS_VideoCombine`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`easy int`、`ImageScaleToTotalPixels`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoadImage`、`PreviewAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

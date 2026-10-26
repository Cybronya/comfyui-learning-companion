---
key: 数字人/数字人/LTX2.3高动态数字人带一致性保持(预置凡人修仙传角色)_2064430603466010626.json
name: LTX2.3高动态数字人带一致性保持(预置凡人修仙传角色)_2064430603466010626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3高动态数字人带一致性保持(预置凡人修仙传角色)_2064430603466010626.json
hash: 0004d2190778f38d
coverage: 0.819048
learned_at: 2026-10-26 01:56:14
nodes: [RandomNoise, CFGGuider, EmptyLTXVLatentVideo, PrimitiveBoolean, LTXVEmptyLatentAudio, Note, PrimitiveInt, ResizeImagesByLongerEdge, CLIPTextEncode, CLIPTextEncode, ComfyMathExpression, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, easy anythingIndexSwitch, GetNode, SetLatentNoiseMask, SolidMask, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, LoadAudio, LoadAudio, easy anythingIndexSwitch, CM_IntUnaryCondition, easy showAnything, CR String To Boolean, LoadAudio, CR Prompt Text, LoraLoaderModelOnly, SetNode, easy int, GetImageSize, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, UNETLoader, MarkdownNote, ImpactConditionalBranch, IndexTTS2Run, TrimAudioDuration, easy showAnything, SoundFlow_GetLength, SetNode, SimpleMath+, PrimitiveInt, Note, PreviewAudio, MelBandRoFormerModelLoader, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, VAELoader, Reroute, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVLatentUpsampler, CFGGuider, RandomNoise, LTXVSeparateAVLatent, LTXVConcatAVLatent, ManualSigmas, VHS_VideoCombine, KSamplerSelect, KSamplerSelect, LTXVScheduler, LTXVConcatAVLatent, MelBandRoFormerSampler, LTXVAudioVAEEncode, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, PrimitiveFloat, easy int, LTXVPreprocess, LTX2_NAG, LTXVConditioning, ImageScaleToTotalPixels, LayerUtility: PurgeVRAM V2, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, SamplerCustomAdvanced, LayerUtility: PurgeVRAM V2, llama_cpp_model_loader, llama_cpp_parameters, JoinStringMulti, PrimitiveStringMultiline, llama_cpp_instruct_adv, Evaluate Strings, ShowText|pysssss, LoadImage, PrimitiveStringMultiline, LoadAudio, PrimitiveFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, GetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.3高动态数字人带一致性保持(预置凡人修仙传角色)_2064430603466010626.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3高动态数字人带一致性保持(预置凡人修仙传角色)_2064430603466010626.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（105 个）：
- `RandomNoise`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `LTXVEmptyLatentAudio` ★核心
- `Note`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
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
- `easy int`
- `GetImageSize`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `MarkdownNote`
- `ImpactConditionalBranch`
- `IndexTTS2Run`
- `TrimAudioDuration`
- `easy showAnything`
- `SoundFlow_GetLength`
- `SetNode`
- `SimpleMath+`
- `PrimitiveInt`
- `Note`
- `PreviewAudio`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `VAELoader`
- `Reroute`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `PrimitiveFloat`
- `easy int`
- `LTXVPreprocess`
- `LTX2_NAG`
- `LTXVConditioning`
- `ImageScaleToTotalPixels`
- `LayerUtility: PurgeVRAM V2`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `JoinStringMulti`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `Evaluate Strings`
- `ShowText|pysssss`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `GetNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（86/105）

**有卡**：`RandomNoise`、`CFGGuider`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`CLIPTextEncode`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`easy anythingIndexSwitch`、`SetLatentNoiseMask`、`SolidMask`、`LoadAudio`、`CM_IntUnaryCondition`、`CR String To Boolean`、`CR Prompt Text`、`easy int`、`GetImageSize`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`UNETLoader`、`ImpactConditionalBranch`、`IndexTTS2Run`、`TrimAudioDuration`、`SoundFlow_GetLength`、`SimpleMath+`、`PreviewAudio`、`MelBandRoFormerModelLoader`、`VAELoader`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`ManualSigmas`、`VHS_VideoCombine`、`KSamplerSelect`、`LTXVScheduler`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`LTXVPreprocess`、`LTX2_NAG`、`LTXVConditioning`、`ImageScaleToTotalPixels`、`LayerUtility: PurgeVRAM V2`、`SamplerCustomAdvanced`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`JoinStringMulti`、`llama_cpp_instruct_adv`、`Evaluate Strings`、`LoadImage`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

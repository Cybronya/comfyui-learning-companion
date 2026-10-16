---
key: 视频生成/图生视频/zhishi_scail.json_2077586586442752001.json
name: zhishi_scail.json_2077586586442752001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2077586586442752001.json
hash: 43663260cac8f251
coverage: 0.819672
learned_at: 2026-10-15 22:41:41
nodes: [EmptyLTXVLatentVideo, LatentUpscaleModelLoader, KSamplerSelect, ModelSamplingSD3, ImageScaleToTotalPixels, PrimitiveStringMultiline, GetImageSize, AudioSeparation, easy showAnything, easy showAnything, PrimitiveInt, SoundFlow_GetLength, SetLatentNoiseMask, TranscribeConfig, SubtitleOptimizer, JoinStrings, easy showAnything, LTXVConcatAVLatent, LTXVImgToVideoInplace, PrimitiveBoolean, LTXVConditioning, CLIPTextEncode, RandomNoise, ImageResizeKJv2, SimpleMath+, TrimAudioDuration, PrimitiveFloat, SolidMask, LTXVAudioVAEEncode, LoraLoaderModelOnly, UNETLoader, PrimitiveFloat, LayerUtility: TextJoin, ComfyMathExpression, PrimitiveInt, LTXVTiledVAEDecode, ComfyMathExpression, ComfyMathExpression, LoraLoaderModelOnly, LTX2_NAG, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, LoraLoaderModelOnly, SamplerCustomAdvanced, VHS_VideoCombine, CLIPTextEncode, LayerUtility: PurgeVRAM V2, VideoTranscribe, CFGGuider, DualCLIPLoader, BasicScheduler, LTXVSeparateAVLatent, HAIGC_TimestampTextReplace, PrimitiveNode, HAIGC_VideoSubtitleTimestampPro, JjkText, VAELoader, PrimitiveStringMultiline, VAELoaderKJ, LoadImage, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/zhishi_scail.json_2077586586442752001.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2077586586442752001.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `ImageScaleToTotalPixels`
- `PrimitiveStringMultiline`
- `GetImageSize`
- `AudioSeparation`
- `easy showAnything`
- `easy showAnything`
- `PrimitiveInt`
- `SoundFlow_GetLength`
- `SetLatentNoiseMask`
- `TranscribeConfig`
- `SubtitleOptimizer`
- `JoinStrings`
- `easy showAnything`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `ImageResizeKJv2`
- `SimpleMath+`
- `TrimAudioDuration`
- `PrimitiveFloat`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `LayerUtility: TextJoin`
- `ComfyMathExpression`
- `PrimitiveInt`
- `LTXVTiledVAEDecode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VideoTranscribe`
- `CFGGuider`
- `DualCLIPLoader`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `HAIGC_TimestampTextReplace`
- `PrimitiveNode`
- `HAIGC_VideoSubtitleTimestampPro`
- `JjkText`
- `VAELoader`
- `PrimitiveStringMultiline`
- `VAELoaderKJ`
- `LoadImage`
- `LoadAudio`

## 知识

覆盖率 **82%**（50/61）

**有卡**：`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`KSamplerSelect`、`ModelSamplingSD3`、`ImageScaleToTotalPixels`、`GetImageSize`、`AudioSeparation`、`SoundFlow_GetLength`、`SetLatentNoiseMask`、`TranscribeConfig`、`SubtitleOptimizer`、`JoinStrings`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`ImageResizeKJv2`、`SimpleMath+`、`TrimAudioDuration`、`SolidMask`、`LTXVAudioVAEEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`LayerUtility: TextJoin`、`ComfyMathExpression`、`LTXVTiledVAEDecode`、`LTX2_NAG`、`LayerUtility: PurgeVRAM V2`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`VideoTranscribe`、`CFGGuider`、`DualCLIPLoader`、`BasicScheduler`、`LTXVSeparateAVLatent`、`HAIGC_TimestampTextReplace`、`HAIGC_VideoSubtitleTimestampPro`、`VAELoader`、`VAELoaderKJ`、`LoadImage`、`LoadAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

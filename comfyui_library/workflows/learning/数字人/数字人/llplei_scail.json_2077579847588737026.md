---
key: 数字人/数字人/llplei_scail.json_2077579847588737026.json
name: llplei_scail.json_2077579847588737026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/llplei_scail.json_2077579847588737026.json
hash: 61c685b81927fa21
coverage: 0.822581
learned_at: 2026-10-26 01:59:03
nodes: [EmptyLTXVLatentVideo, LatentUpscaleModelLoader, KSamplerSelect, ModelSamplingSD3, ImageScaleToTotalPixels, PrimitiveStringMultiline, GetImageSize, AudioSeparation, easy showAnything, PrimitiveInt, SoundFlow_GetLength, SetLatentNoiseMask, TranscribeConfig, SubtitleOptimizer, JoinStrings, easy showAnything, LTXVConcatAVLatent, LTXVImgToVideoInplace, PrimitiveBoolean, LTXVConditioning, CLIPTextEncode, RandomNoise, ImageResizeKJv2, SimpleMath+, TrimAudioDuration, PrimitiveFloat, SolidMask, LTXVAudioVAEEncode, LoraLoaderModelOnly, PrimitiveFloat, LayerUtility: TextJoin, ComfyMathExpression, PrimitiveInt, LTXVTiledVAEDecode, ComfyMathExpression, ComfyMathExpression, LoraLoaderModelOnly, LTX2_NAG, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, LoraLoaderModelOnly, SamplerCustomAdvanced, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, VideoTranscribe, GoogleTranslateTextNode, CFGGuider, DualCLIPLoader, LTXVSeparateAVLatent, HAIGC_TimestampTextReplace, PrimitiveNode, HAIGC_VideoSubtitleTimestampPro, JjkText, VAELoader, VAELoaderKJ, UNETLoader, CLIPTextEncode, easy showAnything, BasicScheduler, PrimitiveStringMultiline, LoadImage, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/llplei_scail.json_2077579847588737026.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/llplei_scail.json_2077579847588737026.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（62 个）：
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `ImageScaleToTotalPixels`
- `PrimitiveStringMultiline`
- `GetImageSize`
- `AudioSeparation`
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
- `LayerUtility: PurgeVRAM V2`
- `VideoTranscribe`
- `GoogleTranslateTextNode`
- `CFGGuider`
- `DualCLIPLoader`
- `LTXVSeparateAVLatent`
- `HAIGC_TimestampTextReplace`
- `PrimitiveNode`
- `HAIGC_VideoSubtitleTimestampPro`
- `JjkText`
- `VAELoader`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `BasicScheduler`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadAudio`

## 知识

覆盖率 **82%**（51/62）

**有卡**：`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`KSamplerSelect`、`ModelSamplingSD3`、`ImageScaleToTotalPixels`、`GetImageSize`、`AudioSeparation`、`SoundFlow_GetLength`、`SetLatentNoiseMask`、`TranscribeConfig`、`SubtitleOptimizer`、`JoinStrings`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`ImageResizeKJv2`、`SimpleMath+`、`TrimAudioDuration`、`SolidMask`、`LTXVAudioVAEEncode`、`LoraLoaderModelOnly`、`LayerUtility: TextJoin`、`ComfyMathExpression`、`LTXVTiledVAEDecode`、`LTX2_NAG`、`LayerUtility: PurgeVRAM V2`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`VideoTranscribe`、`GoogleTranslateTextNode`、`CFGGuider`、`DualCLIPLoader`、`LTXVSeparateAVLatent`、`HAIGC_TimestampTextReplace`、`HAIGC_VideoSubtitleTimestampPro`、`VAELoader`、`VAELoaderKJ`、`UNETLoader`、`BasicScheduler`、`LoadImage`、`LoadAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

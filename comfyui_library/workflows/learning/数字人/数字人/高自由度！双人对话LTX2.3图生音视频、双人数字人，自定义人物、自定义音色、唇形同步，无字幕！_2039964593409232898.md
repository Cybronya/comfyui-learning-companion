---
key: 数字人/数字人/高自由度！双人对话LTX2.3图生音视频、双人数字人，自定义人物、自定义音色、唇形同步，无字幕！_2039964593409232898.json
name: 高自由度！双人对话LTX2.3图生音视频、双人数字人，自定义人物、自定义音色、唇形同步，无字幕！_2039964593409232898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/高自由度！双人对话LTX2.3图生音视频、双人数字人，自定义人物、自定义音色、唇形同步，无字幕！_2039964593409232898.json
hash: 02d08b2be20d511f
coverage: 0.900901
learned_at: 2026-10-26 02:06:07
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, MelBandRoFormerModelLoader, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVLatentUpsampler, Reroute, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, DualCLIPLoader, UNETLoader, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, PrimitiveBoolean, LTXVPreprocess, ResizeImagesByLongerEdge, ResizeImageMaskNode, PrimitiveInt, ComfyMathExpression, intToFloat _O, ComfyMathExpression, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, VAEEncode, KSamplerSelect, VAELoader, EmptyLatentImage, ReferenceLatent, CFGGuider, Flux2Scheduler, MelBandRoFormerSampler, SolidMask, CreateVideo, PrimitiveInt, EmptyLTXVLatentVideo, AudioCrop, ShowText|pysssss, Apply Whisper, UNETLoader, ReferenceLatent, ReferenceLatent, UNETLoader, PurgeVRAM_UTK, CLIPLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeTiled, SamplerCustomAdvanced, TT_img_enc, SaveImage, LoraLoaderModelOnly, easy showAnything, Qwen3TTSVoiceClone, SaveVideo, PrimitiveInt, AudioCrop, ShowText|pysssss, Apply Whisper, LoadAudio, Qwen3TTSVoiceClone, LoadAudio, LoadImage, TDQwen3TTSModelLoader, TrimAudioDuration, SimpleCalculatorKJ, LTXVAudioVAEDecode, SaveAudio, SaveAudio, GetAudioDurationFromAudio, AudioConcat, math_calculate, VAEDecode, PreviewImage, RandomNoise, PreviewImage, SaveAudio, PurgeVRAM_UTK, SaveAudio, Text, Text, ShowAnything|Mie, LoadImage, PreviewImage, CLIPTextEncode, LTXVSeparateAVLatent, CFGGuider, LoraLoaderModelOnly, LoadImage, PrimitiveStringMultiline, VAEEncode, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 720, "width": 1280}
---

# 数字人/数字人/高自由度！双人对话LTX2.3图生音视频、双人数字人，自定义人物、自定义音色、唇形同步，无字幕！_2039964593409232898.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/高自由度！双人对话LTX2.3图生音视频、双人数字人，自定义人物、自定义音色、唇形同步，无字幕！_2039964593409232898.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `MelBandRoFormerModelLoader`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `PrimitiveBoolean`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `ComfyMathExpression`
- `intToFloat _O`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ReferenceLatent`
- `CFGGuider`
- `Flux2Scheduler`
- `MelBandRoFormerSampler` ★核心
- `SolidMask`
- `CreateVideo`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `AudioCrop`
- `ShowText|pysssss`
- `Apply Whisper`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `PurgeVRAM_UTK`
- `CLIPLoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `TT_img_enc`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `Qwen3TTSVoiceClone`
- `SaveVideo`
- `PrimitiveInt`
- `AudioCrop`
- `ShowText|pysssss`
- `Apply Whisper`
- `LoadAudio`
- `Qwen3TTSVoiceClone`
- `LoadAudio`
- `LoadImage`
- `TDQwen3TTSModelLoader`
- `TrimAudioDuration`
- `SimpleCalculatorKJ`
- `LTXVAudioVAEDecode` ★核心
- `SaveAudio`
- `SaveAudio`
- `GetAudioDurationFromAudio`
- `AudioConcat`
- `math_calculate`
- `VAEDecode` ★核心
- `PreviewImage`
- `RandomNoise`
- `PreviewImage`
- `SaveAudio`
- `PurgeVRAM_UTK`
- `SaveAudio`
- `Text`
- `Text`
- `ShowAnything|Mie`
- `LoadImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（100/111）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`MelBandRoFormerModelLoader`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVLatentUpsampler`、`LTXVConditioning`、`CLIPTextEncode`、`DualCLIPLoader`、`UNETLoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`PrimitiveBoolean`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`ComfyMathExpression`、`intToFloat _O`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`EmptyLatentImage`、`Flux2Scheduler`、`MelBandRoFormerSampler`、`SolidMask`、`CreateVideo`、`EmptyLTXVLatentVideo`、`AudioCrop`、`Apply Whisper`、`PurgeVRAM_UTK`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`TT_img_enc`、`SaveImage`、`Qwen3TTSVoiceClone`、`SaveVideo`、`LoadAudio`、`LoadImage`、`TDQwen3TTSModelLoader`、`TrimAudioDuration`、`SimpleCalculatorKJ`、`LTXVAudioVAEDecode`、`SaveAudio`、`GetAudioDurationFromAudio`、`AudioConcat`、`math_calculate`、`VAEDecode`、`Text`、`ShowAnything|Mie`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

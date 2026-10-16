---
key: 视频生成/图生视频/Ltx2.3四段拼接视频-时间轴【还需优化】_2064511634030288897.json
name: Ltx2.3四段拼接视频-时间轴【还需优化】_2064511634030288897.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064511634030288897.json
hash: 58be7a4c7e877e31
coverage: 0.484733
learned_at: 2026-10-15 22:39:25
nodes: [SetNode, GetNode, GetNode, 1hew_AudioDuration, 1hew_AudioDuration, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, LTXVConditioning, SetNode, SetNode, CM_IntToFloat, MelBandRoFormerSampler, DiffusionModelLoaderKJ, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, SetNode, MelBandRoFormerModelLoader, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, LTXVAudioVAEEncode, SetLatentNoiseMask, GetNode, EmptyLTXVLatentVideo, GetNode, Int, SetNode, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, GetNode, LTXVImgToVideoInplace, VAEDecodeTiled, SetNode, LTXVConcatAVLatent, LTXVLatentUpsampler, GetNode, GetNode, LatentUpscaleModelLoader, Int, Int, SetNode, SolidMask, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, ManualSigmas, LTXVSeparateAVLatent, GetNode, MathExpression|pysssss, MathExpression|pysssss, GetNode, OmniVoiceVoiceCloneTTS, OmniVoiceVoiceCloneTTS, GetNode, GetNode, GetNode, GetNode, Qwen3ASRLoader, Qwen3ASRTranscribe, SetNode, GetNode, GetNode, MelBandRoFormerSampler, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, GetNode, SetNode, SolidMask, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, GetNode, CFGGuider, CLIPTextEncode, CLIPTextEncode, BatchImagesNode, SetNode, SetNode, CFGGuider, SetNode, GetNode, GetNode, SetNode, GetNode, 1hew_AudioDuration, 1hew_AudioDuration, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerSampler, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, GetNode, SetNode, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, MathExpression|pysssss, OmniVoiceVoiceCloneTTS, OmniVoiceVoiceCloneTTS, GetNode, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerSampler, LTXVAudioVAEEncode, SetLatentNoiseMask, EmptyLTXVLatentVideo, GetNode, SetNode, SolidMask, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, GetNode, LTXVImgToVideoInplace, VAEDecodeTiled, SetNode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, GetNode, GetNode, ManualSigmas, LTXVSeparateAVLatent, GetNode, RandomNoise, GetNode, SetNode, SetNode, SetNode, LoadAudio, LoadImage, LTX2_NAG, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SolidMask, SetNode, SetNode, GetNode, GetNode, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, GetNode, LTXVImgToVideoInplace, VAEDecodeTiled, SetNode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, GetNode, GetNode, ManualSigmas, LTXVSeparateAVLatent, GetNode, GetNode, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, SamplerCustomAdvanced, GetNode, LTXVImgToVideoInplace, VAEDecodeTiled, SetNode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, GetNode, GetNode, ManualSigmas, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, AudioConcatenate, AudioConcatenate, AudioConcatenate, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, CM_IntToFloat, MathExpression|pysssss, LTXVSeparateAVLatent, VHS_VideoCombine, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Ltx2.3四段拼接视频-时间轴【还需优化】_2064511634030288897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064511634030288897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（262 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `1hew_AudioDuration`
- `1hew_AudioDuration`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `CM_IntToFloat`
- `MelBandRoFormerSampler` ★核心
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `Int`
- `SetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `LatentUpscaleModelLoader`
- `Int`
- `Int`
- `SetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `OmniVoiceVoiceCloneTTS`
- `OmniVoiceVoiceCloneTTS`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `BatchImagesNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `1hew_AudioDuration`
- `1hew_AudioDuration`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `MathExpression|pysssss`
- `OmniVoiceVoiceCloneTTS`
- `OmniVoiceVoiceCloneTTS`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadAudio`
- `LoadImage`
- `LTX2_NAG`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AudioConcatenate`
- `AudioConcatenate`
- `AudioConcatenate`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`

## 知识

覆盖率 **48%**（127/262）

**有卡**：`1hew_AudioDuration`、`LTXVConditioning`、`CM_IntToFloat`、`MelBandRoFormerSampler`、`DiffusionModelLoaderKJ`、`DualCLIPLoader`、`VAELoaderKJ`、`MelBandRoFormerModelLoader`、`ImageResizeKJv2`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`EmptyLTXVLatentVideo`、`Int`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`SolidMask`、`LTXVSeparateAVLatent`、`MathExpression|pysssss`、`OmniVoiceVoiceCloneTTS`、`Qwen3ASRLoader`、`Qwen3ASRTranscribe`、`CFGGuider`、`CLIPTextEncode`、`BatchImagesNode`、`LoadAudio`、`LoadImage`、`LTX2_NAG`、`AudioConcatenate`、`VHS_VideoCombine`、`CR Prompt Text`

**用到的条目**：CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler、LTXVConcatAVLatent

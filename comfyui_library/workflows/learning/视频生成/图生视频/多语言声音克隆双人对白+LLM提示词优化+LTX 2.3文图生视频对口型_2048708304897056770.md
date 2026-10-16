---
key: 视频生成/图生视频/多语言声音克隆双人对白+LLM提示词优化+LTX 2.3文图生视频对口型_2048708304897056770.json
name: 多语言声音克隆双人对白+LLM提示词优化+LTX 2.3文图生视频对口型_2048708304897056770.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2048708304897056770.json
hash: 55a9f18edace75b6
coverage: 0.675676
learned_at: 2026-10-15 22:37:11
nodes: [GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerModelLoader, SimpleMath+, MelBandRoFormerSampler, GetNode, GetNode, GetNode, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVChunkFeedForward, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, GetNode, GetNode, LTXVImgToVideoInplace, ImageResizeKJv2, LTXVPreprocess, SetNode, LoadImage, GetNode, LTXVAudioVAEEncode, TrimAudioDuration, Display Any (rgthree), ResizeImagesByLongerEdge, SaveVideo, ShowText|pysssss, CLIPTextEncode, GetNode, LTXVConditioning, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, CreateVideo, SetNode, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVSeparateAVLatent, CLIPTextEncode, LTXVCropGuides, LTXVSeparateAVLatent, VAEDecodeTiled, SetNode, GetNode, SimpleMath+, JoinStrings, AudioCrop, TextInput_, SetNode, GetNode, TextInput_, GetNode, SetNode, ACE_Integer, SetNode, SetNode, ACE_Integer, ACE_Integer, PrimitiveNode, RH_LLMAPI_Pro_Node, Text, LoadAudio, LoadAudio, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, Qwen3ASRTranscribe, Qwen3ASRTranscribe, GetNode, PrimitiveStringMultiline, OmniVoiceMultiSpeakerTTS, GetAudioDurationFromAudio, SetNode, SimpleMath+, SetNode, easy showAnything, Qwen3ASRLoader, PreviewAudio, SetNode, easy showAnything, CR Prompt Text, GetNode, GetNode, SetNode, PreviewAudio, PreviewAudio, PrimitiveBoolean, AudioInfo, UNETLoader, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/多语言声音克隆双人对白+LLM提示词优化+LTX 2.3文图生视频对口型_2048708304897056770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048708304897056770.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `SimpleMath+`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `SetNode`
- `LoadImage`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `TrimAudioDuration`
- `Display Any (rgthree)`
- `ResizeImagesByLongerEdge`
- `SaveVideo`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVConditioning`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `JoinStrings`
- `AudioCrop`
- `TextInput_`
- `SetNode`
- `GetNode`
- `TextInput_`
- `GetNode`
- `SetNode`
- `ACE_Integer`
- `SetNode`
- `SetNode`
- `ACE_Integer`
- `ACE_Integer`
- `PrimitiveNode`
- `RH_LLMAPI_Pro_Node`
- `Text`
- `LoadAudio`
- `LoadAudio`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Qwen3ASRTranscribe`
- `Qwen3ASRTranscribe`
- `GetNode`
- `PrimitiveStringMultiline`
- `OmniVoiceMultiSpeakerTTS`
- `GetAudioDurationFromAudio`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `easy showAnything`
- `Qwen3ASRLoader`
- `PreviewAudio`
- `SetNode`
- `easy showAnything`
- `CR Prompt Text`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewAudio`
- `PreviewAudio`
- `PrimitiveBoolean`
- `AudioInfo`
- `UNETLoader` ★核心
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **68%**（75/111）

**有卡**：`EmptyLTXVLatentVideo`、`MelBandRoFormerModelLoader`、`SimpleMath+`、`MelBandRoFormerSampler`、`SolidMask`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`ImageResizeKJv2`、`LTXVPreprocess`、`LoadImage`、`LTXVAudioVAEEncode`、`TrimAudioDuration`、`Display Any (rgthree)`、`ResizeImagesByLongerEdge`、`SaveVideo`、`CLIPTextEncode`、`LTXVConditioning`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`CreateVideo`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`JoinStrings`、`AudioCrop`、`TextInput_`、`ACE_Integer`、`RH_LLMAPI_Pro_Node`、`Text`、`LoadAudio`、`MathExpression|pysssss`、`Qwen3ASRTranscribe`、`OmniVoiceMultiSpeakerTTS`、`GetAudioDurationFromAudio`、`Qwen3ASRLoader`、`PreviewAudio`、`CR Prompt Text`、`PrimitiveBoolean`、`AudioInfo`、`UNETLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

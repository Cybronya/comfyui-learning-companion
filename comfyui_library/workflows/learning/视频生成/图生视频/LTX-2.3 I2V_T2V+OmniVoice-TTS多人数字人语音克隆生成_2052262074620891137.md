---
key: 视频生成/图生视频/LTX-2.3 I2V_T2V+OmniVoice-TTS多人数字人语音克隆生成_2052262074620891137.json
name: LTX-2.3 I2V_T2V+OmniVoice-TTS多人数字人语音克隆生成_2052262074620891137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 I2V_T2V+OmniVoice-TTS多人数字人语音克隆生成_2052262074620891137.json
hash: 14ad9706c0f3ea07
coverage: 0.48538
learned_at: 2026-10-15 22:37:27
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, MarkdownNote, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, PrimitiveBoolean, LTXVChunkFeedForward, LTX2AttentionTunerPatch, MarkdownNote, CFGGuider, GetNode, GetNode, SetNode, GetNode, SetNode, GetImageSize, ResizeImageMaskNode, GetNode, GetNode, GetNode, SimpleCalculatorKJ, SetNode, EmptyLTXVLatentVideo, SetNode, GetNode, LTXVConcatAVLatent, SetNode, Reroute, Any Switch (rgthree), GetNode, GetNode, GetNode, SetNode, SetLatentNoiseMask, GetNode, SolidMask, LTXVAudioVAEEncode, CLIPTextEncode, KSamplerSelect, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, SamplerCustomAdvanced, SetNode, LazySwitchKJ, StringConcatenate, Reroute, Reroute, GetNode, GetNode, easy showAnything, GetNode, LTXVImgToVideoInplace, LTXVConditioning, LTXVPreprocess, SetNode, ModelSamplingSD3, BasicScheduler, ManualSigmas, Label (rgthree), OmniVoiceWhisperLoader, LoadAudio, PreviewAudio, PrimitiveStringMultiline, SetNode, OmniVoiceVoiceCloneTTS, Fast Groups Bypasser (rgthree), SetNode, MarkdownNote, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, SetNode, Power Lora Loader (rgthree), TextGenerateLTX2Prompt, PrimitiveStringMultiline, GetNode, ImageResizeKJv2, LTXVImgToVideoInplace, RandomNoise, LTXVLatentUpsampler, LatentUpscaleModelLoader, GetNode, PrimitiveBoolean, OmniVoiceMultiSpeakerTTS, GetNode, LTXVSeparateAVLatent, GetNode, LTXVAudioVAEDecode, VAEDecodeTiled, VRAM_Debug, SamplerCustomAdvanced, VRAM_Debug, RandomNoise, SeedGenerator, DualCLIPLoaderGGUF, MarkdownNote, UnetLoaderGGUF, PrimitiveFloat, INTConstant, MarkdownNote, Audio Duration (mtb), SimpleCalculatorKJ, SimpleCalculatorKJ, SimpleCalculatorKJ, LazySwitchKJ, KSamplerSelect, BasicScheduler, ModelSamplingSD3, ManualSigmas, LTX2_NAG, SetNode, GetNode, CFGGuider, UNETLoader, UNETLoader, LoraLoaderModelOnly, VHS_VideoCombine, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, Fast Groups Bypasser (rgthree), LoadImage, INTConstant, INTConstant, PrimitiveStringMultiline, ImageConcatMulti, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, VHS_VideoCombine, LoadAudio, LoadAudio, PreviewAudio, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX-2.3 I2V_T2V+OmniVoice-TTS多人数字人语音克隆生成_2052262074620891137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052262074620891137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（171 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveBoolean`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `MarkdownNote`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetImageSize`
- `ResizeImageMaskNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `Reroute`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `GetNode`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `LazySwitchKJ`
- `StringConcatenate`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVConditioning`
- `LTXVPreprocess`
- `SetNode`
- `ModelSamplingSD3`
- `BasicScheduler`
- `ManualSigmas`
- `Label (rgthree)`
- `OmniVoiceWhisperLoader`
- `LoadAudio`
- `PreviewAudio`
- `PrimitiveStringMultiline`
- `SetNode`
- `OmniVoiceVoiceCloneTTS`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `MarkdownNote`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `SetNode`
- `Power Lora Loader (rgthree)`
- `TextGenerateLTX2Prompt`
- `PrimitiveStringMultiline`
- `GetNode`
- `ImageResizeKJv2`
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `GetNode`
- `PrimitiveBoolean`
- `OmniVoiceMultiSpeakerTTS`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VRAM_Debug`
- `SamplerCustomAdvanced` ★核心
- `VRAM_Debug`
- `RandomNoise`
- `SeedGenerator`
- `DualCLIPLoaderGGUF`
- `MarkdownNote`
- `UnetLoaderGGUF` ★核心
- `PrimitiveFloat`
- `INTConstant`
- `MarkdownNote`
- `Audio Duration (mtb)`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `LazySwitchKJ`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ModelSamplingSD3`
- `ManualSigmas`
- `LTX2_NAG`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `PrimitiveStringMultiline`
- `ImageConcatMulti`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `LoadAudio`
- `LoadAudio`
- `PreviewAudio`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **49%**（83/171）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`PrimitiveBoolean`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`CFGGuider`、`GetImageSize`、`ResizeImageMaskNode`、`SimpleCalculatorKJ`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LazySwitchKJ`、`StringConcatenate`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTXVPreprocess`、`ModelSamplingSD3`、`BasicScheduler`、`ManualSigmas`、`Label (rgthree)`、`OmniVoiceWhisperLoader`、`LoadAudio`、`PreviewAudio`、`OmniVoiceVoiceCloneTTS`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`Power Lora Loader (rgthree)`、`TextGenerateLTX2Prompt`、`ImageResizeKJv2`、`RandomNoise`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`OmniVoiceMultiSpeakerTTS`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`VRAM_Debug`、`SeedGenerator`、`DualCLIPLoaderGGUF`、`UnetLoaderGGUF`、`INTConstant`、`Audio Duration (mtb)`、`LTX2_NAG`、`UNETLoader`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`LoadImage`、`ImageConcatMulti`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

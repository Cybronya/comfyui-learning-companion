---
key: 视频生成/图生视频/LTX2.3-声音设计数字人_2055814003481423873.json
name: LTX2.3-声音设计数字人_2055814003481423873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055814003481423873.json
hash: 2568bd6c791ccd4f
coverage: 1
learned_at: 2026-10-15 22:37:58
nodes: [RandomNoise, SamplerCustomAdvanced, KSamplerSelect, ImageResizeKJv2, DualCLIPLoader, VAELoaderKJ, SimpleMath+, VAELoaderKJ, UNETLoader, CFGGuider, ManualSigmas, CR Prompt Text, OmniVoiceVoiceDesignTTS, CR Prompt Text, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVCropGuides, LTXVAudioVAEDecode, CreateVideo, LTXVConcatAVLatent, PathchSageAttentionKJ, LTXVConditioning, LTXVImgToVideoInplace, TrimAudioDuration, SolidMask, SetLatentNoiseMask, LTXVAudioVAEEncode, SaveAudioMP3, CLIPTextEncode, LTXVPreprocess, EmptyLTXVLatentVideo, CR Prompt Text, CR Prompt Text, INTConstant, INTConstant, INTConstant, PromptRelaySmartEncode, SaveVideo, AudioInfo, SimpleMath+, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3-声音设计数字人_2055814003481423873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055814003481423873.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ImageResizeKJv2`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `SimpleMath+`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `CFGGuider`
- `ManualSigmas`
- `CR Prompt Text`
- `OmniVoiceVoiceDesignTTS`
- `CR Prompt Text`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `TrimAudioDuration`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SaveAudioMP3`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `CR Prompt Text`
- `CR Prompt Text`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PromptRelaySmartEncode`
- `SaveVideo`
- `AudioInfo`
- `SimpleMath+`
- `LoadImage`

## 知识

覆盖率 **100%**（41/41）

**有卡**：`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ImageResizeKJv2`、`DualCLIPLoader`、`VAELoaderKJ`、`SimpleMath+`、`UNETLoader`、`CFGGuider`、`ManualSigmas`、`CR Prompt Text`、`OmniVoiceVoiceDesignTTS`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`TrimAudioDuration`、`SolidMask`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SaveAudioMP3`、`CLIPTextEncode`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`INTConstant`、`PromptRelaySmartEncode`、`SaveVideo`、`AudioInfo`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent

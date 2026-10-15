---
key: 视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json
name: ltx2.3 多人对话工作流-宠物对话_2039689143625719809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json
hash: b076c3c6c80faecf
coverage: 0.888889
learned_at: 2026-10-15 22:47:22
nodes: [ManualSigmas, SamplerCustomAdvanced, RandomNoise, RandomNoise, KSamplerSelect, LatentUpscaleModelLoader, CFGGuider, CFGGuider, Reroute, SamplerCustomAdvanced, LTXVLatentUpsampler, SetNode, DualCLIPLoader, LTXVConditioning, VAELoaderKJ, ManualSigmas, Int, PrimitiveInt, SimpleMath+, MelBandRoFormerSampler, LTXVAudioVAEEncode, CLIPTextEncode, LTXVAudioVAEDecode, UNETLoader, SetLatentNoiseMask, ComfyMathExpression, MelBandRoFormerModelLoader, PrimitiveNode, ImageResizeKJv2, GetNode, SoundFlow_GetLength, TrimAudioDuration, SimpleMath+, SimpleMath+, QZ_ResolutionPreset, CM_FloatToInt, PreviewAudio, FB_Qwen3TTSDialogueInference, PreviewAudio, VAELoaderKJ, ShowAnything|Mie, ConcatTextOfUtils, LTXVSeparateAVLatent, VAEDecodeTiled, CreateVideo, easy cleanGpuUsed, ConcatTextOfUtils, RH_LLMAPI_Pro_Node, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVCropGuides, KSamplerSelect, LTXVConcatAVLatent, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceClonePrompt, CLIPTextEncode, LTXVConcatAVLatent, easy showAnything, FB_Qwen3TTSVoiceDesign, FB_Qwen3TTSVoiceDesign, easy showAnything, FB_Qwen3TTSRoleBank, LoadImage, ttN text, PreviewAudio, SolidMask, CR Text, easy showAnything, RH_LLMAPI_Pro_Node, SaveVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3 多人对话工作流-宠物对话_2039689143625719809.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `CFGGuider`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `DualCLIPLoader`
- `LTXVConditioning`
- `VAELoaderKJ`
- `ManualSigmas`
- `Int`
- `PrimitiveInt`
- `SimpleMath+`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `UNETLoader` ★核心
- `SetLatentNoiseMask`
- `ComfyMathExpression`
- `MelBandRoFormerModelLoader`
- `PrimitiveNode`
- `ImageResizeKJv2`
- `GetNode`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `SimpleMath+`
- `SimpleMath+`
- `QZ_ResolutionPreset`
- `CM_FloatToInt`
- `PreviewAudio`
- `FB_Qwen3TTSDialogueInference`
- `PreviewAudio`
- `VAELoaderKJ`
- `ShowAnything|Mie`
- `ConcatTextOfUtils`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `easy cleanGpuUsed`
- `ConcatTextOfUtils`
- `RH_LLMAPI_Pro_Node`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceClonePrompt`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `easy showAnything`
- `FB_Qwen3TTSVoiceDesign`
- `FB_Qwen3TTSVoiceDesign`
- `easy showAnything`
- `FB_Qwen3TTSRoleBank`
- `LoadImage`
- `ttN text`
- `PreviewAudio`
- `SolidMask`
- `CR Text`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `SaveVideo`

## 知识

覆盖率 **89%**（64/72）

**有卡**：`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`CFGGuider`、`LTXVLatentUpsampler`、`DualCLIPLoader`、`LTXVConditioning`、`VAELoaderKJ`、`Int`、`SimpleMath+`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`LTXVAudioVAEDecode`、`UNETLoader`、`SetLatentNoiseMask`、`ComfyMathExpression`、`MelBandRoFormerModelLoader`、`ImageResizeKJv2`、`SoundFlow_GetLength`、`TrimAudioDuration`、`QZ_ResolutionPreset`、`CM_FloatToInt`、`PreviewAudio`、`FB_Qwen3TTSDialogueInference`、`ShowAnything|Mie`、`ConcatTextOfUtils`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`CreateVideo`、`easy cleanGpuUsed`、`RH_LLMAPI_Pro_Node`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`FB_Qwen3TTSVoiceClonePrompt`、`FB_Qwen3TTSVoiceDesign`、`FB_Qwen3TTSRoleBank`、`LoadImage`、`ttN text`、`SolidMask`、`CR Text`、`SaveVideo`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler

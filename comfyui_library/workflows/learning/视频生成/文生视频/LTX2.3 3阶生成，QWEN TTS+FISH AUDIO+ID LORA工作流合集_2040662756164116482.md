---
key: 视频生成/文生视频/LTX2.3 3阶生成，QWEN TTS+FISH AUDIO+ID LORA工作流合集_2040662756164116482.json
name: LTX2.3 3阶生成，QWEN TTS+FISH AUDIO+ID LORA工作流合集_2040662756164116482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 3阶生成，QWEN TTS+FISH AUDIO+ID LORA工作流合集_2040662756164116482.json
hash: 5c944a20a08f4190
coverage: 0.753968
learned_at: 2026-10-15 22:44:57
nodes: [CFGGuider, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, DualCLIPLoader, VAELoaderKJ, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, LTXVCropGuides, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVCropGuides, GetNode, GetNode, GetNode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVAudioVAEDecode, VAEDecodeTiled, CreateVideo, LTXVSeparateAVLatent, UNETLoader, LTXVLatentUpsampler, LTXVImgToVideoInplace, CLIPTextEncode, LTXVPreprocess, SimpleMath+, SimpleMath+, DF_Int_to_Float, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, GetNode, LTXVImgToVideoInplace, SimpleMath+, VAELoaderKJ, MelBandRoFormerModelLoader, GetNode, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, TrimAudioDuration, SoundFlow_GetLength, CM_FloatToInt, LTXVAudioVAEEncode, MelBandRoFormerSampler, LoadAudio, SetLatentNoiseMask, SolidMask, PreviewAudio, PreviewAudio, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceDesign, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, PreviewAudio, TrimAudioDuration, SoundFlow_GetLength, MelBandRoFormerSampler, LTXVConcatAVLatent, MelBandRoFormerModelLoader, LTXVAudioVAEEncode, SetLatentNoiseMask, GetNode, SolidMask, FB_Qwen3TTSDialogueInference, CM_FloatToInt, easy showAnything, RH_LLMAPI_Pro_Node, ConcatTextOfUtils, ConcatTextOfUtils, CR Text, CR Text, 1hew_SaveVideo, TrimAudioDuration, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MelBandRoFormerModelLoader, ModelMemoryUsageFactorOverride, LoraLoaderModelOnly, GetNode, LTX2_NAG, LoadAudio, MelBandRoFormerSampler, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, easy showAnything, RH_LLMAPI_Pro_Node, PrimitiveNode, PrimitiveNode, Int, LoadImage, Fast Groups Muter (rgthree), RH_LLMAPI_Pro_Node, QZ_ResolutionPreset, ImageResizeKJv2, SaveImage, GetNode, LTXVReferenceAudio, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3 3阶生成，QWEN TTS+FISH AUDIO+ID LORA工作流合集_2040662756164116482.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 3阶生成，QWEN TTS+FISH AUDIO+ID LORA工作流合集_2040662756164116482.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（126 个）：
- `CFGGuider`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `SimpleMath+`
- `SimpleMath+`
- `DF_Int_to_Float`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `SimpleMath+`
- `VAELoaderKJ`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `TrimAudioDuration`
- `SoundFlow_GetLength`
- `CM_FloatToInt`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `LoadAudio`
- `SetLatentNoiseMask`
- `SolidMask`
- `PreviewAudio`
- `PreviewAudio`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceDesign`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `PreviewAudio`
- `TrimAudioDuration`
- `SoundFlow_GetLength`
- `MelBandRoFormerSampler` ★核心
- `LTXVConcatAVLatent`
- `MelBandRoFormerModelLoader`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `GetNode`
- `SolidMask`
- `FB_Qwen3TTSDialogueInference`
- `CM_FloatToInt`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `ConcatTextOfUtils`
- `ConcatTextOfUtils`
- `CR Text`
- `CR Text`
- `1hew_SaveVideo`
- `TrimAudioDuration`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `ModelMemoryUsageFactorOverride`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LTX2_NAG`
- `LoadAudio`
- `MelBandRoFormerSampler` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `PrimitiveNode`
- `PrimitiveNode`
- `Int`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `RH_LLMAPI_Pro_Node`
- `QZ_ResolutionPreset`
- `ImageResizeKJv2`
- `SaveImage`
- `GetNode`
- `LTXVReferenceAudio`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（95/126）

**有卡**：`CFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`DualCLIPLoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`RandomNoise`、`KSamplerSelect`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CreateVideo`、`UNETLoader`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`SimpleMath+`、`DF_Int_to_Float`、`MelBandRoFormerModelLoader`、`EmptyLTXVLatentVideo`、`TrimAudioDuration`、`SoundFlow_GetLength`、`CM_FloatToInt`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`LoadAudio`、`SetLatentNoiseMask`、`SolidMask`、`PreviewAudio`、`FB_Qwen3TTSRoleBank`、`FB_Qwen3TTSVoiceDesign`、`FB_Qwen3TTSVoiceClonePrompt`、`FB_Qwen3TTSDialogueInference`、`RH_LLMAPI_Pro_Node`、`ConcatTextOfUtils`、`CR Text`、`1hew_SaveVideo`、`LTXVEmptyLatentAudio`、`ModelMemoryUsageFactorOverride`、`LoraLoaderModelOnly`、`LTX2_NAG`、`LTXVConditioning`、`Int`、`LoadImage`、`QZ_ResolutionPreset`、`ImageResizeKJv2`、`SaveImage`、`LTXVReferenceAudio`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

---
key: 视频生成/图生视频/LTX-2.3-MSR V2参考生视频-参考音色-自定义音频-全自动版-V1.1_2080476788374986754.json
name: LTX-2.3-MSR V2参考生视频-参考音色-自定义音频-全自动版-V1.1_2080476788374986754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2080476788374986754.json
hash: 685c60742799fb4b
coverage: 0.481283
learned_at: 2026-10-15 22:42:13
nodes: [RandomNoise, GetNode, GetNode, CFGGuider, SetNode, SetNode, LTXVConditioning, ComfyMathExpression, GetNode, SetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, LTXAddVideoICLoRAGuide, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, ComfyMathExpression, VAEDecode, LTXVCropGuides, JjkText, JjkText, CR Text Concatenate, CR Text Concatenate, ProcessString, SomethingToString, ExtractLinesByIndex, Any Switch (rgthree), GetNode, llama_cpp_parameters, GetNode, PreviewAny, GetNode, GetNode, llama_cpp_instruct_adv, LoadImage, LoadImage, BatchImagesNode, SetNode, SetNode, PreviewImage, GetNode, ManualSigmas, LoadImage, VHS_VideoCombine, VHS_VideoCombine, INTConstant, INTConstant, LTXICLoRALoaderModelOnly, MarkdownNote, GetNode, GetNode, PurgeVRAM_UTK, Any Switch (rgthree), SetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LiconMSR, KSamplerSelect, SoundFlow_GetLength, EmptyLTXVLatentVideo, SetNode, LoadImage, LoadImage, VRAMReserver, GetNode, FB_Qwen3TTSVoiceClonePrompt, GetNode, SetNode, SetNode, FB_Qwen3TTSVoiceClonePrompt, CM_IntToFloat, easy showAnything, Note, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, Note, DualCLIPLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, PathchSageAttentionKJ, CheckpointLoaderSimple, SetNode, PreviewAny, JoinStringMulti, GetNode, GetNode, PreviewAny, SetNode, SetNode, INTConstant, Label (rgthree), INTConstant, SetNode, CM_IntToFloat, SetNode, SetNode, SetNode, easy showAnything, Any Switch (rgthree), LTXVAudioVideoMask, GetNode, LTXVAudioVAEEncode, PrimitiveStringMultiline, SetNode, CLIPTextEncode, JjkText, PromptRelayEncode, LoraLoaderModelOnly, LTX2_NAG, LoadAudio, PrimitiveString, LoadAudio, PrimitiveString, PrimitiveStringMultiline, llama_cpp_model_loader, StringConcatenate, GetNode, PreviewAudio, FB_Qwen3TTSRoleBank, Note, GetNode, WhisperSTT, LayerUtility: PurgeVRAM V2, MelBandRoFormerModelLoader, MelBandRoFormerSampler, GetNode, easy showAnything, LayerUtility: PurgeVRAM V2, MelBandRoFormerSampler, PurgeVRAM_UTK, FB_Qwen3TTSDialogueInference, AudioBeforeAfterSilence, CM_IntToFloat, GetNode, GetNode, AudioBeforeAfterSilence, LTXVAudioVAEEncode, GetNode, TextGenerateLTX2Prompt, LayerUtility: PurgeVRAM V2, WhisperSTT, PreviewAudio, LayerUtility: PurgeVRAM V2, PreviewAudio, PreviewAudio, LoadAudio, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LTXVAudioVideoMask, Note, GetNode, SoundFlow_GetLength, easy showAnything, ComfyMathExpression, ComfyMathExpression, GetNode, PreviewAny, PreviewAny, GetNode, GetNode, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 145}
---

# 视频生成/图生视频/LTX-2.3-MSR V2参考生视频-参考音色-自定义音频-全自动版-V1.1_2080476788374986754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080476788374986754.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（187 个）：
- `RandomNoise`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `ComfyMathExpression`
- `GetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `JjkText`
- `JjkText`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `ProcessString`
- `SomethingToString`
- `ExtractLinesByIndex`
- `Any Switch (rgthree)`
- `GetNode`
- `llama_cpp_parameters`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `LoadImage`
- `BatchImagesNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `ManualSigmas`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `LTXICLoRALoaderModelOnly` ★核心
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `PurgeVRAM_UTK`
- `Any Switch (rgthree)`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LiconMSR`
- `KSamplerSelect` ★核心
- `SoundFlow_GetLength`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `VRAMReserver`
- `GetNode`
- `FB_Qwen3TTSVoiceClonePrompt`
- `GetNode`
- `SetNode`
- `SetNode`
- `FB_Qwen3TTSVoiceClonePrompt`
- `CM_IntToFloat`
- `easy showAnything`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `DualCLIPLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `PreviewAny`
- `JoinStringMulti`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `SetNode`
- `SetNode`
- `INTConstant`
- `Label (rgthree)`
- `INTConstant`
- `SetNode`
- `CM_IntToFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `Any Switch (rgthree)`
- `LTXVAudioVideoMask`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `PrimitiveStringMultiline`
- `SetNode`
- `CLIPTextEncode` ★核心
- `JjkText`
- `PromptRelayEncode`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LoadAudio`
- `PrimitiveString`
- `LoadAudio`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `StringConcatenate`
- `GetNode`
- `PreviewAudio`
- `FB_Qwen3TTSRoleBank`
- `Note`
- `GetNode`
- `WhisperSTT`
- `LayerUtility: PurgeVRAM V2`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `easy showAnything`
- `LayerUtility: PurgeVRAM V2`
- `MelBandRoFormerSampler` ★核心
- `PurgeVRAM_UTK`
- `FB_Qwen3TTSDialogueInference`
- `AudioBeforeAfterSilence`
- `CM_IntToFloat`
- `GetNode`
- `GetNode`
- `AudioBeforeAfterSilence`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `TextGenerateLTX2Prompt`
- `LayerUtility: PurgeVRAM V2`
- `WhisperSTT`
- `PreviewAudio`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAudio`
- `PreviewAudio`
- `LoadAudio`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LTXVAudioVideoMask`
- `Note`
- `GetNode`
- `SoundFlow_GetLength`
- `easy showAnything`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `PreviewAny`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **48%**（90/187）

**有卡**：`RandomNoise`、`CFGGuider`、`LTXVConditioning`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVCropGuides`、`CR Text Concatenate`、`ProcessString`、`SomethingToString`、`ExtractLinesByIndex`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LoadImage`、`BatchImagesNode`、`ManualSigmas`、`VHS_VideoCombine`、`INTConstant`、`LTXICLoRALoaderModelOnly`、`PurgeVRAM_UTK`、`LTXVEmptyLatentAudio`、`LiconMSR`、`KSamplerSelect`、`SoundFlow_GetLength`、`EmptyLTXVLatentVideo`、`VRAMReserver`、`FB_Qwen3TTSVoiceClonePrompt`、`CM_IntToFloat`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`JoinStringMulti`、`Label (rgthree)`、`LTXVAudioVideoMask`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`PromptRelayEncode`、`LTX2_NAG`、`LoadAudio`、`llama_cpp_model_loader`、`StringConcatenate`、`PreviewAudio`、`FB_Qwen3TTSRoleBank`、`WhisperSTT`、`LayerUtility: PurgeVRAM V2`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`FB_Qwen3TTSDialogueInference`、`AudioBeforeAfterSilence`、`TextGenerateLTX2Prompt`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

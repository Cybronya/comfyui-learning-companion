---
name: unknown_workflow_video_upscale_latent_upscale_98
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.5205
common_nodes: [Any To Any, Any To String (mtb), Audio Duration (mtb), CFGGuider, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, CR Prompt Text, CR Text, CR Text Concatenate, DF_Int_to_Float, Display Any (rgthree), EmptyLTXVLatentVideo, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, GODMT_SplitString, GetNode, INTConstant, ImageConcatMulti, ImageListToBatch+, ImageResizeKJv2, JWIntegerDiv, JjkText, JoinStrings, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVFirstLastFrameControl_TTP, LTXVLatentUpsampler, LTXVMiddleFrame_TTP, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PreviewImage, RandomNoise, SDVM Image List Repeat, SamplerCustomAdvanced, SaveAudio, SetLatentNoiseMask, SetNode, ShellAgentPluginOutputText, ShowText|pysssss, SimpleCalculatorKJ, SimpleMath+, SolidMask, Text List, TextInput_, TextListSelelct, VAEDecode, VAELoaderKJ, VHS_SelectImages, VHS_VideoCombine, WujiCleaner, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy lengthAnything, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/五组图片可台词对口型首尾帧生视频V3音频驱动_2018146962532470786.json, 视频生成/图生视频/五组图片可台词对口型首尾帧生视频V4音频驱动_2029794744922017793.json, 视频生成/图生视频/五组图片可台词对口型首尾帧生视频V5音频驱动_2031283967088922626.json, 视频生成/图生视频/五组图片可台词对口型首尾帧生视频V6音频驱动_2033464459947151361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_98

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/五组图片可台词对口型首尾帧生视频V3音频驱动_2018146962532470786.json、视频生成/图生视频/五组图片可台词对口型首尾帧生视频V4音频驱动_2029794744922017793.json、视频生成/图生视频/五组图片可台词对口型首尾帧生视频V5音频驱动_2031283967088922626.json、视频生成/图生视频/五组图片可台词对口型首尾帧生视频V6音频驱动_2033464459947151361.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 4 个 workflow 都包含：
- `Any To Any`
- `Any To String (mtb)`
- `Audio Duration (mtb)`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Prompt Text`
- `CR Text`
- `CR Text Concatenate`
- `DF_Int_to_Float`
- `Display Any (rgthree)`
- `EmptyLTXVLatentVideo`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `GODMT_SplitString`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageListToBatch+`
- `ImageResizeKJv2`
- `JWIntegerDiv`
- `JjkText`
- `JoinStrings`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVLatentUpsampler`
- `LTXVMiddleFrame_TTP`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PreviewImage`
- `RandomNoise`
- `SDVM Image List Repeat`
- `SamplerCustomAdvanced`
- `SaveAudio`
- `SetLatentNoiseMask`
- `SetNode`
- `ShellAgentPluginOutputText`
- `ShowText|pysssss`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `SolidMask`
- `Text List`
- `TextInput_`
- `TextListSelelct`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_SelectImages`
- `VHS_VideoCombine`
- `WujiCleaner`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy lengthAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 3/4 个有
- `LTXAVTextEncoderLoader` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `LTXVAudioVAELoader` —— 1/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

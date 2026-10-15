---
key: 视频生成/文生视频/LTX 2.3  数字人对口型优化加速版_2050177856264785921.json
name: LTX 2.3  数字人对口型优化加速版_2050177856264785921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3  数字人对口型优化加速版_2050177856264785921.json
hash: ff6c4050472e3fc6
coverage: 0.860465
learned_at: 2026-10-15 22:44:35
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, CLIPTextEncode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVImgToVideoInplace, SolidMask, ResizeImagesByLongerEdge, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetLatentNoiseMask, ResizeImageMaskNode, LTXVAudioVAEEncode, llama_cpp_parameters, llama_cpp_unload_model, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, Label (rgthree), Label (rgthree), MarkdownNote, MarkdownNote, Fast Groups Bypasser (rgthree), TextInput_, VAELoader, VAELoaderKJ, Label (rgthree), llama_cpp_model_loader, CR Text, PreviewAny, PreviewAny, llama_cpp_parameters, llama_cpp_instruct_adv, CLIPTextEncode, TextInput_, PreviewAudio, PreviewAudio, DualCLIPLoader, LatentUpscaleModelLoader, TrimAudioDuration, LoadAudio, MelBandRoFormerSampler, SimpleMath+, AudioInfo, Display Any (rgthree), MelBandRoFormerModelLoader, AudioCrop, SimpleMath+, PrimitiveInt, SaveVideo, PrimitiveFloat, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, SimpleCalculatorKJ, llama_cpp_model_loader, JoinStrings, ShowText|pysssss, RH_LLMAPI_NODE, llama_cpp_instruct_adv, UNETLoader, LTXVChunkFeedForward, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX 2.3  数字人对口型优化加速版_2050177856264785921.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3  数字人对口型优化加速版_2050177856264785921.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVImgToVideoInplace`
- `SolidMask`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `ResizeImageMaskNode`
- `LTXVAudioVAEEncode` ★核心
- `llama_cpp_parameters`
- `llama_cpp_unload_model`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `TextInput_`
- `VAELoader`
- `VAELoaderKJ`
- `Label (rgthree)`
- `llama_cpp_model_loader`
- `CR Text`
- `PreviewAny`
- `PreviewAny`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `PreviewAudio`
- `PreviewAudio`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `TrimAudioDuration`
- `LoadAudio`
- `MelBandRoFormerSampler` ★核心
- `SimpleMath+`
- `AudioInfo`
- `Display Any (rgthree)`
- `MelBandRoFormerModelLoader`
- `AudioCrop`
- `SimpleMath+`
- `PrimitiveInt`
- `SaveVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SimpleCalculatorKJ`
- `llama_cpp_model_loader`
- `JoinStrings`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`

## 知识

覆盖率 **86%**（74/86）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`ResizeImageMaskNode`、`LTXVAudioVAEEncode`、`llama_cpp_parameters`、`llama_cpp_unload_model`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`PrimitiveBoolean`、`Label (rgthree)`、`TextInput_`、`VAELoader`、`VAELoaderKJ`、`llama_cpp_model_loader`、`CR Text`、`llama_cpp_instruct_adv`、`PreviewAudio`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`TrimAudioDuration`、`LoadAudio`、`MelBandRoFormerSampler`、`SimpleMath+`、`AudioInfo`、`Display Any (rgthree)`、`MelBandRoFormerModelLoader`、`AudioCrop`、`SaveVideo`、`ComfyMathExpression`、`SimpleCalculatorKJ`、`JoinStrings`、`RH_LLMAPI_NODE`、`UNETLoader`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

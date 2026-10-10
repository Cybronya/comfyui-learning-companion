---
key: 视频生成/文生视频/LTX-2.3配音术：实现播客录音变视频🔥_2032093186700615681.json
name: LTX-2.3配音术：实现播客录音变视频🔥_2032093186700615681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3配音术：实现播客录音变视频🔥_2032093186700615681.json
hash: e2487fb90f13567f
coverage: 0.794521
learned_at: 2026-10-11 03:16:45
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CheckpointLoaderSimple, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, LTXVImgToVideoInplace, ResizeImageMaskNode, KSamplerSelect, ComfyMathExpression, Reroute, ComfyMathExpression, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CFGGuider, MarkdownNote, MarkdownNote, llama_cpp_parameters, llama_cpp_model_loader, LTXVAudioVAELoader, CLIPTextEncode, LTXAVTextEncoderLoader, PrimitiveInt, RandomNoise, RandomNoise, LTXVAudioVAEDecode, LoadImage, PrimitiveBoolean, ResizeImagesByLongerEdge, LTXVPreprocess, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVLatentUpsampler, SaveVideo, VAEDecodeTiled, LTXVConcatAVLatent, LTXVImgToVideoInplace, CreateVideo, PreviewAny, FB_Qwen3TTSRoleBank, PreviewAudio, PreviewAudio, MathExpression|pysssss, Bjornulf_ShowInt, PrimitiveInt, PrimitiveInt, FB_Qwen3TTSVoiceDesign, FB_Qwen3TTSVoiceClonePrompt, CR Text, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, CLIPTextEncode, llama_cpp_instruct_adv, TextConcatenator, CR Text, PreviewAny, FB_Qwen3TTSDialogueInference, easy cleanGpuUsed, PreviewAudio, LTXVAudioVAEEncode, AudioInfoNode, SolidMask, SetLatentNoiseMask, easy cleanGpuUsed, Label (rgthree), Label (rgthree)]
patterns: []
missing: [CR Text, CR Text, Label (rgthree), Label (rgthree), MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX-2.3配音术：实现播客录音变视频🔥_2032093186700615681.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3配音术：实现播客录音变视频🔥_2032093186700615681.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `ResizeImageMaskNode`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `Reroute`
- `ComfyMathExpression`
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `MarkdownNote`
- `MarkdownNote`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `RandomNoise`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `LoadImage`
- `PrimitiveBoolean`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `CreateVideo`
- `PreviewAny`
- `FB_Qwen3TTSRoleBank`
- `PreviewAudio`
- `PreviewAudio`
- `MathExpression|pysssss`
- `Bjornulf_ShowInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `FB_Qwen3TTSVoiceDesign`
- `FB_Qwen3TTSVoiceClonePrompt`
- `CR Text`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `TextConcatenator`
- `CR Text`
- `PreviewAny`
- `FB_Qwen3TTSDialogueInference`
- `easy cleanGpuUsed`
- `PreviewAudio`
- `LTXVAudioVAEEncode` ★核心
- `AudioInfoNode`
- `SolidMask`
- `SetLatentNoiseMask`
- `easy cleanGpuUsed`
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（58/73）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CheckpointLoaderSimple`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LTXVImgToVideoInplace`、`ResizeImageMaskNode`、`ComfyMathExpression`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`RandomNoise`、`LTXVAudioVAEDecode`、`LoadImage`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`SaveVideo`、`VAEDecodeTiled`、`CreateVideo`、`FB_Qwen3TTSRoleBank`、`PreviewAudio`、`Bjornulf_ShowInt`、`FB_Qwen3TTSVoiceDesign`、`FB_Qwen3TTSVoiceClonePrompt`、`llama_cpp_instruct_adv`、`TextConcatenator`、`FB_Qwen3TTSDialogueInference`、`LTXVAudioVAEEncode`、`AudioInfoNode`、`SolidMask`、`SetLatentNoiseMask`

**缺卡**（7）：`CR Text`、`CR Text`、`Label (rgthree)`、`Label (rgthree)`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识

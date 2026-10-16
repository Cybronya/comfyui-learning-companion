---
key: 视频生成/图生视频/数字人虚拟歌手MV 全自动_半自动分段精准运镜+动作控制LTX2.3_2050900841577623553.json
name: 数字人虚拟歌手MV 全自动_半自动分段精准运镜+动作控制LTX2.3_2050900841577623553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2050900841577623553.json
hash: 1486b1af0d5fe2a8
coverage: 0.706667
learned_at: 2026-10-15 22:37:20
nodes: [Reroute, DualCLIPLoader, Float, MathExpression|pysssss, VAELoaderKJ, LTXVAudioVAEEncode, KSamplerSelect, SamplerCustom, MathExpression|pysssss, easy showAnything, Audio Duration (mtb), LTXVImgToVideoInplaceKJ, MelBandRoFormerModelLoader, LTXVSeparateAVLatent, Reroute, SolidMask, EmptyLTXVLatentVideo, LTXVConditioning, LTX2_NAG, CLIPTextEncode, PromptRelayEncode, CR Text Concatenate, SetLatentNoiseMask, LTXVConcatAVLatent, llama_cpp_instruct_adv, ImageResizeKJv2, PreviewImage, VAELoaderKJ, VAEDecodeTiled, llama_cpp_parameters, CR Text Replace, Int to String, llama_cpp_model_loader, ShowAnything|Mie, AudioCrop, Reroute, MarkdownNote, Float, MelBandRoFormerSampler, DiffusionModelLoaderKJ, ShowAnything|Mie, SomethingToString, Split String, MarkdownNote, CR Text, MarkdownNote, MarkdownNote, LoadImage, MarkdownNote, VHS_VideoCombine, GuHaiAutoImageSplit, LoadImage, TTResolutionSelector, LoadAudio, CR Text, MarkdownNote, PreviewAny, PreviewAny, SaveImage, MarkdownNote, MarkdownNote, MarkdownNote, PreviewAny, PreviewAny, RH_Translator, PreviewAny, RHHiddenNodes, RHHiddenNodes, Text, Qwen3ASRLoader, Qwen3ASRTranscribe, PreviewAny, PreviewAudio, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/数字人虚拟歌手MV 全自动_半自动分段精准运镜+动作控制LTX2.3_2050900841577623553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050900841577623553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `Reroute`
- `DualCLIPLoader`
- `Float`
- `MathExpression|pysssss`
- `VAELoaderKJ`
- `LTXVAudioVAEEncode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `MathExpression|pysssss`
- `easy showAnything`
- `Audio Duration (mtb)`
- `LTXVImgToVideoInplaceKJ`
- `MelBandRoFormerModelLoader`
- `LTXVSeparateAVLatent`
- `Reroute`
- `SolidMask`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `PromptRelayEncode`
- `CR Text Concatenate`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `llama_cpp_instruct_adv`
- `ImageResizeKJv2`
- `PreviewImage`
- `VAELoaderKJ`
- `VAEDecodeTiled` ★核心
- `llama_cpp_parameters`
- `CR Text Replace`
- `Int to String`
- `llama_cpp_model_loader`
- `ShowAnything|Mie`
- `AudioCrop`
- `Reroute`
- `MarkdownNote`
- `Float`
- `MelBandRoFormerSampler` ★核心
- `DiffusionModelLoaderKJ`
- `ShowAnything|Mie`
- `SomethingToString`
- `Split String`
- `MarkdownNote`
- `CR Text`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `VHS_VideoCombine`
- `GuHaiAutoImageSplit`
- `LoadImage`
- `TTResolutionSelector`
- `LoadAudio`
- `CR Text`
- `MarkdownNote`
- `PreviewAny`
- `PreviewAny`
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewAny`
- `PreviewAny`
- `RH_Translator`
- `PreviewAny`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Text`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `PreviewAny`
- `PreviewAudio`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **71%**（53/75）

**有卡**：`DualCLIPLoader`、`Float`、`MathExpression|pysssss`、`VAELoaderKJ`、`LTXVAudioVAEEncode`、`KSamplerSelect`、`SamplerCustom`、`Audio Duration (mtb)`、`LTXVImgToVideoInplaceKJ`、`MelBandRoFormerModelLoader`、`LTXVSeparateAVLatent`、`SolidMask`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTX2_NAG`、`CLIPTextEncode`、`PromptRelayEncode`、`CR Text Concatenate`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`llama_cpp_instruct_adv`、`ImageResizeKJv2`、`VAEDecodeTiled`、`llama_cpp_parameters`、`CR Text Replace`、`Int to String`、`llama_cpp_model_loader`、`ShowAnything|Mie`、`AudioCrop`、`MelBandRoFormerSampler`、`DiffusionModelLoaderKJ`、`SomethingToString`、`Split String`、`CR Text`、`LoadImage`、`VHS_VideoCombine`、`GuHaiAutoImageSplit`、`TTResolutionSelector`、`LoadAudio`、`SaveImage`、`RH_Translator`、`RHHiddenNodes`、`Text`、`Qwen3ASRLoader`、`Qwen3ASRTranscribe`、`PreviewAudio`

**用到的条目**：CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent、SetLatentNoiseMask

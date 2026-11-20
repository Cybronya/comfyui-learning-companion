---
key: 视频生成/图生视频/Wan2.2_自动反推_Remix3.0_图生视频_2115984231787745282.json
name: Wan2.2_自动反推_Remix3.0_图生视频_2115984231787745282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_自动反推_Remix3.0_图生视频_2115984231787745282.json
hash: 45eb03f401522eeb
coverage: 0.484848
learned_at: 2026-10-30 23:29:03
nodes: [ModelPatchTorchSettings, ModelSamplingSD3, Reroute, Reroute, Reroute, SetNode, SetNode, Reroute, Reroute, SomethingToString, GetNode, Reroute, SetNode, Reroute, Reroute, Reroute, PathchSageAttentionKJ, MarkdownNote, MarkdownNote, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, easy setNode, easy cleanGpuUsed, VAEDecode, MarkdownNote, Reroute, llama_cpp_unload_model, Reroute, Reroute, MarkdownNote, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPTextEncode, CLIPTextEncode, PreviewImage, Reroute, MarkdownNote, GetNode, FL_RIFE, MarkdownNote, easy int, easy int, ModelPassThrough, ModelPassThrough, LoraLoaderModelOnly, ModelPassThrough, PathchSageAttentionKJ, ModelPassThrough, VAELoader, easy showAnything, PainterI2V, MarkdownNote, easy int, UNETLoader, UNETLoader, ModelSamplingSD3, CLIPLoader, CR Prompt Text, llama_cpp_parameters, Reroute, Reroute, CR Text Concatenate, WanMoeKSampler, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, MarkdownNote, CR Prompt Text, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, PreviewAny, easy int, SetNode, SetNode, GetNode, easy showAnything, GetNode, easy showAnything, PreviewAudio, PreviewAudio, easy getNode, PlaySound|pysssss, VHS_VideoCombine, llama_cpp_model_loader, PreviewAudio, WujiAudioLoader, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ImageResizeKJv2, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "res_multistep", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2_自动反推_Remix3.0_图生视频_2115984231787745282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2_自动反推_Remix3.0_图生视频_2115984231787745282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `SomethingToString`
- `GetNode`
- `Reroute`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `PathchSageAttentionKJ`
- `MarkdownNote`
- `MarkdownNote`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy setNode`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `MarkdownNote`
- `Reroute`
- `llama_cpp_unload_model`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Reroute`
- `MarkdownNote`
- `GetNode`
- `FL_RIFE`
- `MarkdownNote`
- `easy int`
- `easy int`
- `ModelPassThrough`
- `ModelPassThrough`
- `LoraLoaderModelOnly` ★核心
- `ModelPassThrough`
- `PathchSageAttentionKJ`
- `ModelPassThrough`
- `VAELoader`
- `easy showAnything`
- `PainterI2V`
- `MarkdownNote`
- `easy int`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `CR Prompt Text`
- `llama_cpp_parameters`
- `Reroute`
- `Reroute`
- `CR Text Concatenate`
- `WanMoeKSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CR Prompt Text`
- `llama_cpp_instruct_adv`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `PreviewAny`
- `easy int`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `easy showAnything`
- `PreviewAudio`
- `PreviewAudio`
- `easy getNode`
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `llama_cpp_model_loader`
- `PreviewAudio`
- `WujiAudioLoader`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `LoadImage`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `res_multistep`

## 知识

覆盖率 **48%**（48/99）

**有卡**：`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SomethingToString`、`PathchSageAttentionKJ`、`easy setNode`、`easy cleanGpuUsed`、`VAEDecode`、`llama_cpp_unload_model`、`CLIPTextEncode`、`FL_RIFE`、`easy int`、`ModelPassThrough`、`LoraLoaderModelOnly`、`VAELoader`、`PainterI2V`、`UNETLoader`、`CLIPLoader`、`CR Prompt Text`、`llama_cpp_parameters`、`CR Text Concatenate`、`WanMoeKSampler`、`llama_cpp_instruct_adv`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`PreviewAudio`、`easy getNode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`llama_cpp_model_loader`、`WujiAudioLoader`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader

---
key: 视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频_2103038735767138305.json
name: ❽「Wan2.2」自动反推 Remix3.0 图生视频_2103038735767138305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频_2103038735767138305.json
hash: f5f5a1b4a9edb0b0
coverage: 0.484848
learned_at: 2026-10-17 02:29:38
nodes: [ModelPatchTorchSettings, ModelSamplingSD3, Reroute, Reroute, Reroute, SetNode, SetNode, Reroute, Reroute, SomethingToString, GetNode, Reroute, SetNode, Reroute, Reroute, Reroute, PathchSageAttentionKJ, MarkdownNote, MarkdownNote, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, easy setNode, easy cleanGpuUsed, VAEDecode, MarkdownNote, Reroute, llama_cpp_unload_model, Reroute, Reroute, MarkdownNote, Reroute, Reroute, Reroute, Reroute, Reroute, PreviewImage, Reroute, MarkdownNote, GetNode, MarkdownNote, easy int, easy int, ModelPassThrough, ModelPassThrough, LoraLoaderModelOnly, ModelPassThrough, PathchSageAttentionKJ, ModelPassThrough, VAELoader, easy showAnything, PainterI2V, MarkdownNote, easy int, UNETLoader, UNETLoader, ModelSamplingSD3, CLIPLoader, CR Prompt Text, llama_cpp_parameters, Reroute, Reroute, CR Text Concatenate, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, MarkdownNote, CR Prompt Text, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, PreviewAny, easy int, SetNode, SetNode, GetNode, easy showAnything, GetNode, easy showAnything, PreviewAudio, PreviewAudio, easy getNode, PlaySound|pysssss, VHS_VideoCombine, llama_cpp_model_loader, PreviewAudio, WujiAudioLoader, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CLIPTextEncode, LoadImage, ImageResizeKJv2, WanMoeKSampler, FL_RIFE, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "res_multistep", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频_2103038735767138305.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频_2103038735767138305.json`

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
- `PreviewImage`
- `Reroute`
- `MarkdownNote`
- `GetNode`
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
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `WanMoeKSampler` ★核心
- `FL_RIFE`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `res_multistep`

## 知识

覆盖率 **48%**（48/99）

**有卡**：`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SomethingToString`、`PathchSageAttentionKJ`、`easy setNode`、`easy cleanGpuUsed`、`VAEDecode`、`llama_cpp_unload_model`、`easy int`、`ModelPassThrough`、`LoraLoaderModelOnly`、`VAELoader`、`PainterI2V`、`UNETLoader`、`CLIPLoader`、`CR Prompt Text`、`llama_cpp_parameters`、`CR Text Concatenate`、`llama_cpp_instruct_adv`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`PreviewAudio`、`easy getNode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`llama_cpp_model_loader`、`WujiAudioLoader`、`CLIPTextEncode`、`LoadImage`、`ImageResizeKJv2`、`WanMoeKSampler`、`FL_RIFE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

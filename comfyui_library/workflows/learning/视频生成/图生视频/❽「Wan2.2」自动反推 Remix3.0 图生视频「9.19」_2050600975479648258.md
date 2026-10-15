---
key: 视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频「9.19」_2050600975479648258.json
name: ❽「Wan2.2」自动反推 Remix3.0 图生视频「9.19」_2050600975479648258
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频「9.19」_2050600975479648258.json
hash: e272d1587fc140d5
coverage: 0.343434
learned_at: 2026-10-15 02:41:29
nodes: [ModelPatchTorchSettings, ModelSamplingSD3, Reroute, Reroute, Reroute, SetNode, SetNode, Reroute, Reroute, SomethingToString, GetNode, Reroute, SetNode, Reroute, Reroute, Reroute, PathchSageAttentionKJ, LoadImage, MarkdownNote, MarkdownNote, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, easy setNode, easy cleanGpuUsed, VAEDecode, MarkdownNote, Reroute, llama_cpp_unload_model, Reroute, Reroute, MarkdownNote, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPTextEncode, CLIPTextEncode, PreviewImage, Reroute, MarkdownNote, GetNode, FL_RIFE, MarkdownNote, easy int, easy int, ModelPassThrough, ModelPassThrough, LoraLoaderModelOnly, ModelPassThrough, PathchSageAttentionKJ, ModelPassThrough, VAELoader, easy showAnything, PainterI2V, MarkdownNote, easy int, UNETLoader, UNETLoader, ModelSamplingSD3, CLIPLoader, CR Prompt Text, llama_cpp_parameters, Reroute, Reroute, CR Text Concatenate, WanMoeKSampler, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, MarkdownNote, CR Prompt Text, llama_cpp_instruct_adv, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, PreviewAny, easy int, SetNode, SetNode, GetNode, easy showAnything, GetNode, easy showAnything, PreviewAudio, PreviewAudio, easy getNode, PlaySound|pysssss, VHS_VideoCombine, llama_cpp_model_loader, PreviewAudio, WujiAudioLoader, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ImageResizeKJv2]
patterns: []
missing: [CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, MathExpression|pysssss, PlaySound|pysssss, easy cleanGpuUsed, easy getNode, easy int, easy int, easy int, easy int, easy setNode, CR Prompt Text, CR Prompt Text]
parameters: {"cfg": 4, "denoise": "res_multistep", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频「9.19」_2050600975479648258.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/❽「Wan2.2」自动反推 Remix3.0 图生视频「9.19」_2050600975479648258.json`

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
- `LoadImage`
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

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `res_multistep`

## 知识

覆盖率 **34%**（34/99）

**有卡**：`ModelPatchTorchSettings`、`ModelSamplingSD3`、`SomethingToString`、`PathchSageAttentionKJ`、`LoadImage`、`VAEDecode`、`llama_cpp_unload_model`、`CLIPTextEncode`、`FL_RIFE`、`ModelPassThrough`、`LoraLoaderModelOnly`、`VAELoader`、`PainterI2V`、`UNETLoader`、`CLIPLoader`、`llama_cpp_parameters`、`WanMoeKSampler`、`llama_cpp_instruct_adv`、`PreviewAudio`、`VHS_VideoCombine`、`llama_cpp_model_loader`、`WujiAudioLoader`、`ImageResizeKJv2`

**缺卡**（14）：`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`PlaySound|pysssss`、`easy cleanGpuUsed`、`easy getNode`、`easy int`、`easy int`、`easy int`、`easy int`、`easy setNode`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

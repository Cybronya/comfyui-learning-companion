---
key: 视频生成/文生视频/Smooth Mix i2V v2.0首尾帧【雄舟天文馆Lora专版】_2041678498137378817.json
name: Smooth Mix i2V v2.0首尾帧【雄舟天文馆Lora专版】_2041678498137378817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Smooth Mix i2V v2.0首尾帧【雄舟天文馆Lora专版】_2041678498137378817.json
hash: a4aafafe21fb9f35
coverage: 0.568627
learned_at: 2026-10-11 19:49:42
nodes: [VHS_VideoCombine, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, WanFirstLastFrameToVideo, VAELoader, CLIPTextEncode, CLIPTextEncode, easy int, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, llama_cpp_model_loader, SetNode, llama_cpp_parameters, easy showAnything, SetNode, llama_cpp_instruct_adv, SetNode, ImageBatchMulti, LoadImage, VAEDecode, easy cleanGpuUsed, RTXVideoSuperResolution, Text Concatenate, PrimitiveStringMultiline, PrimitiveStringMultiline, InversionDemoLazySwitch, ModelSamplingSD3, UNETLoader, SetNode, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, InversionDemoLazySwitch, LoraLoaderModelOnly, LoraLoaderModelOnly, InversionDemoLazySwitch, GetNode, Text Concatenate, InversionDemoLazySwitch, PrimitiveBoolean, PrimitiveStringMultiline, LoadImage, easy positive]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Concatenate, Text Concatenate, easy cleanGpuUsed, easy int, easy positive, ImageResize+]
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Smooth Mix i2V v2.0首尾帧【雄舟天文馆Lora专版】_2041678498137378817.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Smooth Mix i2V v2.0首尾帧【雄舟天文馆Lora专版】_2041678498137378817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（51 个）：
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `WanFirstLastFrameToVideo`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `llama_cpp_model_loader`
- `SetNode`
- `llama_cpp_parameters`
- `easy showAnything`
- `SetNode`
- `llama_cpp_instruct_adv`
- `SetNode`
- `ImageBatchMulti`
- `LoadImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `RTXVideoSuperResolution`
- `Text Concatenate`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `InversionDemoLazySwitch`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `InversionDemoLazySwitch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `InversionDemoLazySwitch`
- `GetNode`
- `Text Concatenate`
- `InversionDemoLazySwitch`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `LoadImage`
- `easy positive`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（29/51）

**有卡**：`VHS_VideoCombine`、`KSamplerAdvanced`、`CLIPLoader`、`WanFirstLastFrameToVideo`、`VAELoader`、`CLIPTextEncode`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`ImageBatchMulti`、`LoadImage`、`VAEDecode`、`RTXVideoSuperResolution`、`InversionDemoLazySwitch`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoaderModelOnly`、`PrimitiveBoolean`

**缺卡**（7）：`LayerUtility: ImageScaleByAspectRatio V2`、`Text Concatenate`、`Text Concatenate`、`easy cleanGpuUsed`、`easy int`、`easy positive`、`ImageResize+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明

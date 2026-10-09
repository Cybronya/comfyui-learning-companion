---
key: 图片生成/图生图/【图片超分】Flux.1.0_洗图超分_1981202730742087681.json
name: 【图片超分】Flux.1.0_洗图超分_1981202730742087681.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【图片超分】Flux.1.0_洗图超分_1981202730742087681.json
hash: 9216c1412b756eda
coverage: 0.510204
learned_at: 2026-10-09 22:36:19
nodes: [easy cleanGpuUsed, CLIPTextEncode, LoraLoaderModelOnly, easy setNode, UNETLoader, LoraLoaderModelOnly, easy cleanGpuUsed, easy getNode, easy getNode, DualCLIPLoader, VAELoader, Anything Everywhere3, easy setNode, easy setNode, easy setNode, easy setNode, ResizeLongestToNode, easy getNode, GetImageSize+, ImageResize+, CLIPTextEncode, ConditioningCombine, ConditioningZeroOut, ControlNetLoader, ControlNetApplyAdvanced, easy cleanGpuUsed, easy getNode, VAEEncode, CR Latent Batch Size, RandomNoise, SamplerCustomAdvanced, BasicGuider, BasicScheduler, KSamplerSelect, easy cleanGpuUsed, easy setNode, easy getNode, Joy_caption_load, easy getNode, easy showAnything, Joy_caption, easy getNode, VAEDecode, LoadImage, SaveImage, ImpactInt, ImpactInt, easy float, easy float]
patterns: []
missing: [easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy float, easy float, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, easy setNode, easy setNode, easy setNode, CR Latent Batch Size, GetImageSize+, ImageResize+]
parameters: {"controlnet_strength": 0.8000000000000002}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `CR Latent Batch Size` 仅有 VAE/Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/【图片超分】Flux.1.0_洗图超分_1981202730742087681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/1981202730742087681.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy setNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `easy getNode`
- `easy getNode`
- `DualCLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `ResizeLongestToNode`
- `easy getNode`
- `GetImageSize+`
- `ImageResize+`
- `CLIPTextEncode` ★核心
- `ConditioningCombine`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy getNode`
- `VAEEncode` ★核心
- `CR Latent Batch Size`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `easy setNode`
- `easy getNode`
- `Joy_caption_load`
- `easy getNode`
- `easy showAnything`
- `Joy_caption`
- `easy getNode`
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `ImpactInt`
- `ImpactInt`
- `easy float`
- `easy float`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **51%**（25/49）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ResizeLongestToNode`、`ConditioningCombine`、`ConditioningZeroOut`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`VAEEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`BasicScheduler`、`KSamplerSelect`、`Joy_caption_load`、`Joy_caption`、`VAEDecode`、`LoadImage`、`SaveImage`、`ImpactInt`

**缺卡**（22）：`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy float`、`easy float`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`、`CR Latent Batch Size`、`GetImageSize+`、`ImageResize+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、ControlNetApplyAdvanced

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Latent Batch Size` 仅有 VAE/Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明

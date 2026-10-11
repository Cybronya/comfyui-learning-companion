---
key: 视频生成/文生视频/wan2.2无限文视频工作流_2042218145586356225.json
name: wan2.2无限文视频工作流_2042218145586356225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2无限文视频工作流_2042218145586356225.json
hash: 89635f3b89786a04
coverage: 0.441379
learned_at: 2026-10-11 19:49:45
nodes: [SetNode, SetNode, GetNode, GetNode, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_GetImageCount, SetNode, GetNode, GetNode, GetNode, GetNode, MathExpression|pysssss, PathchSageAttentionKJ, SetNode, RandomNoise, GetNode, GetNode, GetNode, KSamplerSelect, SetNode, ScheduledCFGGuidance, SamplerCustomAdvanced, BasicScheduler, SplitSigmas, SetNode, SetNode, SetNode, GetNode, DisableNoise, RIFEInterpolation, ImpactInt, GetNode, GetNode, SamplerCustomAdvanced, ScheduledCFGGuidance, VAEDecode, WanImageToVideoSVIPro, DisableNoise, ScheduledCFGGuidance, SamplerCustomAdvanced, ScheduledCFGGuidance, SamplerCustomAdvanced, VAEDecode, Fast Groups Bypasser (rgthree), VAELoader, SetNode, CLIPLoader, RTXVideoSuperResolution, RTXVideoSuperResolution, SetNode, SetNode, RIFEInterpolation, VAEEncode, CLIPTextEncode, CLIPTextEncode, ImpactInt, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, GetNode, VAEEncode, GetNode, MathExpression|pysssss, ForLoopClose, easy showAnything, ForLoopOpen, ModelSamplingSD3, PrimitiveStringMultiline, UNETLoader, GetNode, GetNode, MathExpression|pysssss, GetNode, GetNode, MathExpression|pysssss, easy showAnything, easy showAnything, easy promptLine, CLIPLoader, VAELoader, Text Multiline, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, SaveImage, VAEDecode, GetNode, GetNode, UNETLoader, SetNode, SetNode, llama_cpp_instruct_adv, easy promptLine, MathExpression|pysssss, ImageBatchExtendWithOverlap, GetNode, UNETLoader, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, WanImageToVideoSVIPro, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, KSampler, SomethingToString, SetNode, String Replace (mtb), GetNode, MathExpression|pysssss, easy cleanGpuUsed, SetNode, easy showAnything, PrimitiveStringMultiline, llama_cpp_model_loader, Text Concatenate, easy promptLine, GetNode, GetNode, SetNode, SetNode, EmptySD3LatentImage, ImpactInt, SetNode, PrimitiveFloat, SetNode, ImpactInt, MathExpression|pysssss, ImpactInt, PrimitiveStringMultiline, MarkdownNote]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, String Replace (mtb), Text Concatenate, Text Multiline, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy promptLine, easy promptLine, easy promptLine]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 346656964895841, "steps": 10}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `String Replace (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/wan2.2无限文视频工作流_2042218145586356225.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2无限文视频工作流_2042218145586356225.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（145 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_GetImageCount`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `SetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `SplitSigmas`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `DisableNoise`
- `RIFEInterpolation`
- `ImpactInt`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `ScheduledCFGGuidance`
- `VAEDecode` ★核心
- `WanImageToVideoSVIPro`
- `DisableNoise`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `RTXVideoSuperResolution`
- `RTXVideoSuperResolution`
- `SetNode`
- `SetNode`
- `RIFEInterpolation`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImpactInt`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `MathExpression|pysssss`
- `ForLoopClose`
- `easy showAnything`
- `ForLoopOpen`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `easy promptLine`
- `CLIPLoader`
- `VAELoader`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `llama_cpp_instruct_adv`
- `easy promptLine`
- `MathExpression|pysssss`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideoSVIPro`
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `SomethingToString`
- `SetNode`
- `String Replace (mtb)`
- `GetNode`
- `MathExpression|pysssss`
- `easy cleanGpuUsed`
- `SetNode`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `Text Concatenate`
- `easy promptLine`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `EmptySD3LatentImage`
- `ImpactInt`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `ImpactInt`
- `MathExpression|pysssss`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `MarkdownNote`

## 关键参数

- `seed` = `346656964895841`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **44%**（64/145）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VHS_GetImageCount`、`RandomNoise`、`KSamplerSelect`、`ScheduledCFGGuidance`、`SamplerCustomAdvanced`、`BasicScheduler`、`SplitSigmas`、`DisableNoise`、`RIFEInterpolation`、`ImpactInt`、`VAEDecode`、`WanImageToVideoSVIPro`、`VAELoader`、`CLIPLoader`、`RTXVideoSuperResolution`、`VAEEncode`、`CLIPTextEncode`、`VHS_VideoCombine`、`ForLoopClose`、`ForLoopOpen`、`UNETLoader`、`ModelSamplingAuraFlow`、`SaveImage`、`llama_cpp_instruct_adv`、`ImageBatchExtendWithOverlap`、`LoraLoaderModelOnly`、`KSampler`、`SomethingToString`、`llama_cpp_model_loader`、`EmptySD3LatentImage`

**缺卡**（17）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`String Replace (mtb)`、`Text Concatenate`、`Text Multiline`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy promptLine`、`easy promptLine`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `String Replace (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

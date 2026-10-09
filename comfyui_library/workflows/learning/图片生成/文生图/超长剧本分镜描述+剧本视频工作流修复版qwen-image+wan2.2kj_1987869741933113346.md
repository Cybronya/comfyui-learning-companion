---
key: 图片生成/文生图/超长剧本分镜描述+剧本视频工作流修复版qwen-image+wan2.2kj_1987869741933113346.json
name: 超长剧本分镜描述+剧本视频工作流修复版qwen-image+wan2.2kj_1987869741933113346.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/超长剧本分镜描述+剧本视频工作流修复版qwen-image+wan2.2kj_1987869741933113346.json
hash: 095d547b32d4b764
coverage: 0.636364
learned_at: 2026-10-09 21:16:00
nodes: [ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSampler, PathchSageAttentionKJ, VAELoader, CLIPLoader, UnetLoaderGGUF, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, INTConstant, PrimitiveNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, WanVideoSLG, WanVideoSLG, EmptyLatentImage, SimpleMath+, SetNode, WanVideoTextEncode, CR Prompt List, CR SDXL Aspect Ratio, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, INTConstant, PrimitiveNode, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, WanVideoSLG, WanVideoSLG, JWInteger, ImageResize+, PreviewImage, CR Prompt List, JWInteger, JWInteger, WanVideoSampler, JWInteger, ImageResize+, WanVideoVAELoader, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy lengthAnything, PreviewImage, SimpleMath+, easy showAnything, WanVideoSampler, WanVideoVAELoader, easy forLoopStart, WanVideoDecode, ColorMatch, ImageResize+, WanVideoDecode, ImageBatchJoin, easy forLoopEnd, ColorMatch, easy cleanGpuUsed, List Length, easy showAnything, CreateCFGScheduleFloatList, VHS_VideoCombine, CreateCFGScheduleFloatList, LoadImage, VAEDecode, PreviewImage, GODMT_ListSlice, ImpactImageBatchToImageList, GODMT_ListSlice, SetNode, GetNode, SetNode, GODMT_ListSlice, easy lengthAnything, MathExpression|pysssss, GetNode, GetNode, easy showAnything, CR Prompt List, GetNode, CR Prompt Text, TextBox, WanVideoImageToVideoEncode, WanVideoModelLoader, MathExpression|pysssss, MathExpression|pysssss, Substract Int Int (JPS), JWInteger, JWInteger, TextBox, TextBox, easy imageListToImageBatch, PreviewImage]
patterns: [text_to_image]
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, List Length, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, SimpleMath+, Substract Int Int (JPS), easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageListToImageBatch, easy lengthAnything, easy lengthAnything, CR Prompt List, CR Prompt List, CR Prompt List, CR Prompt Text, CR SDXL Aspect Ratio, ImageResize+, ImageResize+, ImageResize+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 551057179077766, "steps": 4, "width": 512}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `List Length` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Substract Int Int (JPS)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/超长剧本分镜描述+剧本视频工作流修复版qwen-image+wan2.2kj_1987869741933113346.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1987869741933113346.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（121 个）：
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PathchSageAttentionKJ`
- `VAELoader`
- `CLIPLoader`
- `UnetLoaderGGUF` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `JWInteger`
- `INTConstant`
- `PrimitiveNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoSLG`
- `WanVideoSLG`
- `EmptyLatentImage` ★核心
- `SimpleMath+`
- `SetNode`
- `WanVideoTextEncode`
- `CR Prompt List`
- `CR SDXL Aspect Ratio`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `JWInteger`
- `INTConstant`
- `PrimitiveNode`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoSLG`
- `WanVideoSLG`
- `JWInteger`
- `ImageResize+`
- `PreviewImage`
- `CR Prompt List`
- `JWInteger`
- `JWInteger`
- `WanVideoSampler` ★核心
- `JWInteger`
- `ImageResize+`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy lengthAnything`
- `PreviewImage`
- `SimpleMath+`
- `easy showAnything`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `easy forLoopStart`
- `WanVideoDecode`
- `ColorMatch`
- `ImageResize+`
- `WanVideoDecode`
- `ImageBatchJoin`
- `easy forLoopEnd`
- `ColorMatch`
- `easy cleanGpuUsed`
- `List Length`
- `easy showAnything`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `GODMT_ListSlice`
- `ImpactImageBatchToImageList`
- `GODMT_ListSlice`
- `SetNode`
- `GetNode`
- `SetNode`
- `GODMT_ListSlice`
- `easy lengthAnything`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `CR Prompt List`
- `GetNode`
- `CR Prompt Text`
- `TextBox`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Substract Int Int (JPS)`
- `JWInteger`
- `JWInteger`
- `TextBox`
- `TextBox`
- `easy imageListToImageBatch`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `551057179077766`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **64%**（77/121）

**有卡**：`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`、`PathchSageAttentionKJ`、`VAELoader`、`CLIPLoader`、`UnetLoaderGGUF`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`INTConstant`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoSLG`、`EmptyLatentImage`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`、`ColorMatch`、`ImageBatchJoin`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`LoadImage`、`VAEDecode`、`GODMT_ListSlice`、`ImpactImageBatchToImageList`、`TextBox`

**缺卡**（28）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`List Length`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`SimpleMath+`、`Substract Int Int (JPS)`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy forLoopEnd`、`easy forLoopStart`、`easy imageListToImageBatch`、`easy lengthAnything`、`easy lengthAnything`、`CR Prompt List`、`CR Prompt List`、`CR Prompt List`、`CR Prompt Text`、`CR SDXL Aspect Ratio`、`ImageResize+`、`ImageResize+`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `List Length` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Substract Int Int (JPS)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

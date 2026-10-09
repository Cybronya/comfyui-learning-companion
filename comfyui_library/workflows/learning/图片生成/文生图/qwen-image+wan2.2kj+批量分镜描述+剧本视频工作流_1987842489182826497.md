---
key: 图片生成/文生图/qwen-image+wan2.2kj+批量分镜描述+剧本视频工作流_1987842489182826497.json
name: qwen-image+wan2.2kj+批量分镜描述+剧本视频工作流_1987842489182826497.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image+wan2.2kj+批量分镜描述+剧本视频工作流_1987842489182826497.json
hash: b2a3bd33fe622e3e
coverage: 0.633333
learned_at: 2026-10-09 21:16:00
nodes: [ModelSamplingAuraFlow, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSampler, PathchSageAttentionKJ, VAELoader, CLIPLoader, UnetLoaderGGUF, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, INTConstant, PrimitiveNode, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, WanVideoSLG, WanVideoSLG, EmptyLatentImage, CR Prompt Text, SimpleMath+, SetNode, ImageResize+, PreviewImage, WanVideoTextEncode, SetNode, GetNode, CR Prompt List, SetNode, CR SDXL Aspect Ratio, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, INTConstant, PrimitiveNode, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, WanVideoSLG, WanVideoSLG, JWInteger, ImageResize+, PreviewImage, CR Prompt List, JWInteger, JWInteger, WanVideoSampler, JWInteger, JWInteger, JWInteger, GODMT_ListSlice, LoadImage, CreateCFGScheduleFloatList, Substract Int Int (JPS), ImageResize+, WanVideoVAELoader, WanVideoSampler, CreateCFGScheduleFloatList, WanVideoSampler, LayerUtility: PurgeVRAM, GetNode, LayerUtility: PurgeVRAM, GODMT_ListSlice, easy imageListToImageBatch, easy lengthAnything, PreviewImage, MathExpression|pysssss, MathExpression|pysssss, GetNode, easy showAnything, GetNode, easy lengthAnything, MathExpression|pysssss, CR Prompt List, SimpleMath+, easy showAnything, TextBox, TextBox, WanVideoSampler, WanVideoVAELoader, easy forLoopStart, WanVideoDecode, ImpactImageBatchToImageList, ColorMatch, VHS_VideoCombine, ImageResize+, WanVideoDecode, ImageBatchJoin, easy forLoopEnd, ColorMatch, easy cleanGpuUsed, List Length, easy showAnything, VAEDecode, GODMT_ListSlice]
patterns: [text_to_image]
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, List Length, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, SimpleMath+, Substract Int Int (JPS), easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageListToImageBatch, easy lengthAnything, easy lengthAnything, CR Prompt List, CR Prompt List, CR Prompt List, CR Prompt Text, CR SDXL Aspect Ratio, ImageResize+, ImageResize+, ImageResize+, ImageResize+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 551057179077748, "steps": 4, "width": 512}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `List Length` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Substract Int Int (JPS)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt List` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen-image+wan2.2kj+批量分镜描述+剧本视频工作流_1987842489182826497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1987842489182826497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（120 个）：
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
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
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
- `CR Prompt Text`
- `SimpleMath+`
- `SetNode`
- `ImageResize+`
- `PreviewImage`
- `WanVideoTextEncode`
- `SetNode`
- `GetNode`
- `CR Prompt List`
- `SetNode`
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
- `JWInteger`
- `JWInteger`
- `GODMT_ListSlice`
- `LoadImage`
- `CreateCFGScheduleFloatList`
- `Substract Int Int (JPS)`
- `ImageResize+`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GODMT_ListSlice`
- `easy imageListToImageBatch`
- `easy lengthAnything`
- `PreviewImage`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `easy lengthAnything`
- `MathExpression|pysssss`
- `CR Prompt List`
- `SimpleMath+`
- `easy showAnything`
- `TextBox`
- `TextBox`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `easy forLoopStart`
- `WanVideoDecode`
- `ImpactImageBatchToImageList`
- `ColorMatch`
- `VHS_VideoCombine`
- `ImageResize+`
- `WanVideoDecode`
- `ImageBatchJoin`
- `easy forLoopEnd`
- `ColorMatch`
- `easy cleanGpuUsed`
- `List Length`
- `easy showAnything`
- `VAEDecode` ★核心
- `GODMT_ListSlice`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `551057179077748`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **63%**（76/120）

**有卡**：`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`KSampler`、`PathchSageAttentionKJ`、`VAELoader`、`CLIPLoader`、`UnetLoaderGGUF`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`INTConstant`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoSLG`、`EmptyLatentImage`、`WanVideoTextEncode`、`WanVideoSampler`、`GODMT_ListSlice`、`LoadImage`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`TextBox`、`WanVideoDecode`、`ImpactImageBatchToImageList`、`ColorMatch`、`VHS_VideoCombine`、`ImageBatchJoin`、`VAEDecode`

**缺卡**（29）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`List Length`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`SimpleMath+`、`Substract Int Int (JPS)`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy forLoopEnd`、`easy forLoopStart`、`easy imageListToImageBatch`、`easy lengthAnything`、`easy lengthAnything`、`CR Prompt List`、`CR Prompt List`、`CR Prompt List`、`CR Prompt Text`、`CR SDXL Aspect Ratio`、`ImageResize+`、`ImageResize+`、`ImageResize+`、`ImageResize+`

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
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

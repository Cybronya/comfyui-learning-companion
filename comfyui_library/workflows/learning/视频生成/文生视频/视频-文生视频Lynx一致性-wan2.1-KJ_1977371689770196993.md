---
key: 视频生成/文生视频/视频-文生视频Lynx一致性-wan2.1-KJ_1977371689770196993.json
name: 视频-文生视频Lynx一致性-wan2.1-KJ_1977371689770196993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频Lynx一致性-wan2.1-KJ_1977371689770196993.json
hash: 69e783717f514df1
coverage: 0.586957
learned_at: 2026-10-10 23:13:51
nodes: [WanVideoSetBlockSwap, PreviewImage, WanVideoSetLoRAs, PreviewImage, LynxEncodeFaceIP, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoExtraModelSelect, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, ImageFromBatch+, GetNode, QwenLoader, GetNode, WanVideoPromptExtender, SetNode, StringFunction|pysssss, GetNode, GetNode, StringFunction|pysssss, VHS_VideoCombine, SetNode, ImageConcatMulti, GetImageSizeAndCount, WanVideoExtraModelSelect, LoadLynxResampler, LynxInsightFaceCrop, WanVideoTextEncodeCached, WanVideoAddLynxEmbeds, VHS_VideoCombine, LoadImage, WanVideoEmptyEmbeds, SetNode, easy seed, ImpactFloat, CR Prompt Text, easy int, SetNode, MathExpression|pysssss, PrimitiveFloat, Int, Int, easy anythingIndexSwitch]
patterns: []
missing: [ImageFromBatch+, MathExpression|pysssss, StringFunction|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, CR Prompt Text, easy seed]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/视频-文生视频Lynx一致性-wan2.1-KJ_1977371689770196993.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频-文生视频Lynx一致性-wan2.1-KJ_1977371689770196993.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoSetBlockSwap`
- `PreviewImage`
- `WanVideoSetLoRAs`
- `PreviewImage`
- `LynxEncodeFaceIP`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoExtraModelSelect`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageFromBatch+`
- `GetNode`
- `QwenLoader`
- `GetNode`
- `WanVideoPromptExtender`
- `SetNode`
- `StringFunction|pysssss`
- `GetNode`
- `GetNode`
- `StringFunction|pysssss`
- `VHS_VideoCombine`
- `SetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoExtraModelSelect`
- `LoadLynxResampler` ★核心
- `LynxInsightFaceCrop`
- `WanVideoTextEncodeCached`
- `WanVideoAddLynxEmbeds`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoEmptyEmbeds`
- `SetNode`
- `easy seed`
- `ImpactFloat`
- `CR Prompt Text`
- `easy int`
- `SetNode`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `Int`
- `Int`
- `easy anythingIndexSwitch`

## 知识

覆盖率 **59%**（27/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LynxEncodeFaceIP`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`QwenLoader`、`WanVideoPromptExtender`、`VHS_VideoCombine`、`ImageConcatMulti`、`GetImageSizeAndCount`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`WanVideoAddLynxEmbeds`、`LoadImage`、`WanVideoEmptyEmbeds`、`ImpactFloat`、`Int`

**缺卡**（8）：`ImageFromBatch+`、`MathExpression|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`easy anythingIndexSwitch`、`easy int`、`CR Prompt Text`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP、WanVideoSetLoRAs

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

---
key: 图片生成/文生图/视频-文生视频wan2.2-最强过审_1959964511526662146.json
name: 视频-文生视频wan2.2-最强过审_1959964511526662146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/视频-文生视频wan2.2-最强过审_1959964511526662146.json
hash: 9031941caf1c9ffc
coverage: 0.697674
learned_at: 2026-10-07 23:38:10
nodes: [WanVideoSampler, WanVideoSampler, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoDecode, WanVideoVAELoader, VHS_VideoCombine, CreateCFGScheduleFloatList, INTConstant, INTConstant, LoadWanVideoT5TextEncoder, PrimitiveNode, MathExpression|pysssss, TextConcat, CR Prompt Text, ShowText|pysssss, JWStringConcat, easy showAnything, easy showAnything, WanVideoEmptyEmbeds, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, RH_LLMAPI_NODE, GetImageSizeAndCount, ImageFromBatch+, CR Prompt Text, Int, CR Prompt Text, Wan22PromptSelector, Int, Int, WanVideoTextEncode, easy showAnything, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note]
patterns: []
missing: [ImageFromBatch+, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/视频-文生视频wan2.2-最强过审_1959964511526662146.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1959964511526662146.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（43 个）：
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveNode`
- `MathExpression|pysssss`
- `TextConcat`
- `CR Prompt Text`
- `ShowText|pysssss`
- `JWStringConcat`
- `easy showAnything`
- `easy showAnything`
- `WanVideoEmptyEmbeds`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `RH_LLMAPI_NODE`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `CR Prompt Text`
- `Int`
- `CR Prompt Text`
- `Wan22PromptSelector`
- `Int`
- `Int`
- `WanVideoTextEncode`
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`

## 知识

覆盖率 **70%**（30/43）

**有卡**：`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoDecode`、`WanVideoVAELoader`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`INTConstant`、`LoadWanVideoT5TextEncoder`、`TextConcat`、`JWStringConcat`、`WanVideoEmptyEmbeds`、`RH_LLMAPI_NODE`、`GetImageSizeAndCount`、`Int`、`Wan22PromptSelector`、`WanVideoTextEncode`

**缺卡**（7）：`ImageFromBatch+`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明

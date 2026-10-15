---
key: 视频生成/文生视频/视频-文生视频Lynx一致性-wan2.1-KJ_1977371689770196993.json
name: 视频-文生视频Lynx一致性-wan2.1-KJ_1977371689770196993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频Lynx一致性-wan2.1-KJ_1977371689770196993.json
hash: 69e783717f514df1
coverage: 0.76087
learned_at: 2026-10-15 22:49:00
nodes: [WanVideoSetBlockSwap, PreviewImage, WanVideoSetLoRAs, PreviewImage, LynxEncodeFaceIP, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoExtraModelSelect, WanVideoTextEncodeCached, WanVideoSampler, WanVideoDecode, ImageFromBatch+, GetNode, QwenLoader, GetNode, WanVideoPromptExtender, SetNode, StringFunction|pysssss, GetNode, GetNode, StringFunction|pysssss, VHS_VideoCombine, SetNode, ImageConcatMulti, GetImageSizeAndCount, WanVideoExtraModelSelect, LoadLynxResampler, LynxInsightFaceCrop, WanVideoTextEncodeCached, WanVideoAddLynxEmbeds, VHS_VideoCombine, LoadImage, WanVideoEmptyEmbeds, SetNode, easy seed, ImpactFloat, CR Prompt Text, easy int, SetNode, MathExpression|pysssss, PrimitiveFloat, Int, Int, easy anythingIndexSwitch]
patterns: []
missing: []
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

覆盖率 **76%**（35/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LynxEncodeFaceIP`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoExtraModelSelect`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`QwenLoader`、`WanVideoPromptExtender`、`StringFunction|pysssss`、`VHS_VideoCombine`、`ImageConcatMulti`、`GetImageSizeAndCount`、`LoadLynxResampler`、`LynxInsightFaceCrop`、`WanVideoAddLynxEmbeds`、`LoadImage`、`WanVideoEmptyEmbeds`、`easy seed`、`ImpactFloat`、`CR Prompt Text`、`easy int`、`MathExpression|pysssss`、`Int`、`easy anythingIndexSwitch`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、LynxEncodeFaceIP

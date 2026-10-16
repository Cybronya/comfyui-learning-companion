---
key: 视频生成/图生视频/WAN2.2首尾帧_1963913944572248066.json
name: WAN2.2首尾帧_1963913944572248066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1963913944572248066.json
hash: c2f9ea56d0762644
coverage: 0.875
learned_at: 2026-10-15 22:31:33
nodes: [WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, AddLabel, LoadWanVideoT5TextEncoder, ImageResize+, WanVideoClipVisionEncode, ImageResize+, WanVideoSampler, LayerUtility: PurgeVRAM, WanVideoSampler, PreviewImage, easy int, easy int, easy int, easy ifElse, ImageConcatMulti, EmptyImage, AddLabel, PreviewImage, LoadImage, WanVideoVAELoader, WanVideoTextEncode, CreateCFGScheduleFloatList, JWInteger, INTConstant, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, WanVideoLoraSelect, PrimitiveNode, WanVideoImageToVideoEncode, LayerUtility: PurgeVRAM, GetImageSizeAndCount, VHS_VideoCombine, easy ifElse, MathExpression|pysssss, CR Prompt Text, LoadImage, ImageConcatMulti, PrimitiveBoolean, WanVideoDecode, VHS_VideoCombine, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2首尾帧_1963913944572248066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963913944572248066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（48 个）：
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `AddLabel`
- `LoadWanVideoT5TextEncoder`
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `ImageResize+`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `easy int`
- `easy int`
- `easy int`
- `easy ifElse`
- `ImageConcatMulti`
- `EmptyImage`
- `AddLabel`
- `PreviewImage`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `JWInteger`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `LayerUtility: PurgeVRAM`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `easy ifElse`
- `MathExpression|pysssss`
- `CR Prompt Text`
- `LoadImage`
- `ImageConcatMulti`
- `PrimitiveBoolean`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **88%**（42/48）

**有卡**：`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`AddLabel`、`LoadWanVideoT5TextEncoder`、`ImageResize+`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`easy int`、`ImageConcatMulti`、`EmptyImage`、`LoadImage`、`WanVideoVAELoader`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`JWInteger`、`INTConstant`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`MathExpression|pysssss`、`CR Prompt Text`、`PrimitiveBoolean`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

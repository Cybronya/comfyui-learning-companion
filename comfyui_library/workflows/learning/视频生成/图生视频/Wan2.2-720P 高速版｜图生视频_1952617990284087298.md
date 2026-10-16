---
key: 视频生成/图生视频/Wan2.2-720P 高速版｜图生视频_1952617990284087298.json
name: Wan2.2-720P 高速版｜图生视频_1952617990284087298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952617990284087298.json
hash: deadaf58de79c991
coverage: 0.836364
learned_at: 2026-10-15 22:31:02
nodes: [VAELoader, TextBox, TextBox, TextBox, Primitive integer [Crystools], PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, INTConstant, INTConstant, WanVideoLoraSelect, WanVideoTextEncode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoModelLoader, GetNode, WanVideoSetLoRAs, WanVideoModelLoader, SetNode, WanVideoLoraSelect, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, GetNode, SimpleMath+, Primitive integer [Crystools], SimpleMath+, CR Text Replace, TextBox, easy ifElse, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, GetImageSizeAndCount, WanVideoDecode, ImageFromBatch+, WanVideoSampler, ImpactSwitch, TextBox, PrimitiveBoolean, TextBox, LayerUtility: PurgeVRAM, CR Text Concatenate, RH_Captioner, TextBox, easy showAnything, PrimitiveNode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, RHHiddenNodes, ImageResizeKJ, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-720P 高速版｜图生视频_1952617990284087298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952617990284087298.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（55 个）：
- `VAELoader`
- `TextBox`
- `TextBox`
- `TextBox`
- `Primitive integer [Crystools]`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `CR Text Replace`
- `TextBox`
- `easy ifElse`
- `CreateCFGScheduleFloatList`
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `ImageFromBatch+`
- `WanVideoSampler` ★核心
- `ImpactSwitch`
- `TextBox`
- `PrimitiveBoolean`
- `TextBox`
- `LayerUtility: PurgeVRAM`
- `CR Text Concatenate`
- `RH_Captioner`
- `TextBox`
- `easy showAnything`
- `PrimitiveNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **84%**（46/55）

**有卡**：`VAELoader`、`TextBox`、`Primitive integer [Crystools]`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`CR Text Replace`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageFromBatch+`、`PrimitiveBoolean`、`CR Text Concatenate`、`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`RHHiddenNodes`、`ImageResizeKJ`、`LoadImage`

**用到的条目**：VAELoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode

---
key: 视频生成/图生视频/Wan2.2-JK高速版-高清1920 -自动提示词_1952604203145474049.json
name: Wan2.2-JK高速版-高清1920 -自动提示词_1952604203145474049.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-JK高速版-高清1920 -自动提示词_1952604203145474049.json
hash: fbd8e282d10628e2
coverage: 0.824561
learned_at: 2026-10-15 22:31:02
nodes: [VAELoader, TextBox, TextBox, TextBox, Primitive integer [Crystools], PrimitiveNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, INTConstant, INTConstant, WanVideoLoraSelect, WanVideoTextEncode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoModelLoader, GetNode, WanVideoSetLoRAs, WanVideoModelLoader, SetNode, WanVideoLoraSelect, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, GetNode, SimpleMath+, Primitive integer [Crystools], SimpleMath+, CR Text Replace, TextBox, easy ifElse, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, GetImageSizeAndCount, WanVideoDecode, ImageFromBatch+, WanVideoSampler, ImpactSwitch, LoadImage, TextBox, PrimitiveBoolean, TextBox, LayerUtility: PurgeVRAM, CR Text Concatenate, RH_Captioner, TextBox, easy showAnything, PrimitiveNode, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, RHHiddenNodes, ImageResizeKJ, VHS_VideoCombine, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-JK高速版-高清1920 -自动提示词_1952604203145474049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952604203145474049.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（57 个）：
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
- `LoadImage`
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
- `MarkdownNote`

## 知识

覆盖率 **82%**（47/57）

**有卡**：`VAELoader`、`TextBox`、`Primitive integer [Crystools]`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`CR Text Replace`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageFromBatch+`、`LoadImage`、`PrimitiveBoolean`、`CR Text Concatenate`、`RH_Captioner`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`RHHiddenNodes`、`ImageResizeKJ`

**用到的条目**：VAELoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode

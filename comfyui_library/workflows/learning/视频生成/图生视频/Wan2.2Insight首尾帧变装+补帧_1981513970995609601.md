---
key: 视频生成/图生视频/Wan2.2Insight首尾帧变装+补帧_1981513970995609601.json
name: Wan2.2Insight首尾帧变装+补帧_1981513970995609601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2Insight首尾帧变装+补帧_1981513970995609601.json
hash: b9727edba154d3b3
coverage: 0.857143
learned_at: 2026-10-15 22:32:37
nodes: [JWInteger, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, WanVideoSampler, GetImageSizeAndCount, WanVideoDecode, WanVideoVAELoader, RIFE VFI, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, LoadImage, JWInteger, CreateCFGScheduleFloatList, Fast Groups Bypasser (rgthree), MathExpression|pysssss, Wan22PromptSelector, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadWanVideoT5TextEncoder, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSampler, RHHiddenNodes, WanVideoTextEncode, VHS_VideoCombine, RHHiddenNodes, ImpactSwitch, RHHiddenNodes, Text Concatenate, INTConstant, INTConstant, Note, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2Insight首尾帧变装+补帧_1981513970995609601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981513970995609601.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `JWInteger`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `RIFE VFI`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `LoadImage`
- `JWInteger`
- `CreateCFGScheduleFloatList`
- `Fast Groups Bypasser (rgthree)`
- `MathExpression|pysssss`
- `Wan22PromptSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `ImpactSwitch`
- `RHHiddenNodes`
- `Text Concatenate`
- `INTConstant`
- `INTConstant`
- `Note`
- `CR Text`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoVAELoader`、`RIFE VFI`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`MathExpression|pysssss`、`Wan22PromptSelector`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`RHHiddenNodes`、`WanVideoTextEncode`、`Text Concatenate`、`INTConstant`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

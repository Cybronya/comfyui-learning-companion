---
key: 视频生成/图生视频/【华丽变装】Wan2.2-Infinite动态变装（支持首尾帧）_1980423615982297089.json
name: 【华丽变装】Wan2.2-Infinite动态变装（支持首尾帧）_1980423615982297089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【华丽变装】Wan2.2-Infinite动态变装（支持首尾帧）_1980423615982297089.json
hash: 753090ee0295a0e0
coverage: 0.833333
learned_at: 2026-10-15 22:32:30
nodes: [JWInteger, CreateCFGScheduleFloatList, RH_LLMAPI_NODE, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, INTConstant, INTConstant, RIFE VFI, VHS_VideoCombine, WanVideoDecode, GetImageSizeAndCount, Fast Groups Bypasser (rgthree), Wan22PromptSelector, VHS_VideoCombine, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, RHHiddenNodes, MathExpression|pysssss, Text Concatenate, RHHiddenNodes, ImpactSwitch, Note, WanVideoImageToVideoEncode, LoadImage, CR Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【华丽变装】Wan2.2-Infinite动态变装（支持首尾帧）_1980423615982297089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980423615982297089.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（30 个）：
- `JWInteger`
- `CreateCFGScheduleFloatList`
- `RH_LLMAPI_NODE`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `Fast Groups Bypasser (rgthree)`
- `Wan22PromptSelector`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `MathExpression|pysssss`
- `Text Concatenate`
- `RHHiddenNodes`
- `ImpactSwitch`
- `Note`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`JWInteger`、`CreateCFGScheduleFloatList`、`RH_LLMAPI_NODE`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoDecode`、`GetImageSizeAndCount`、`Wan22PromptSelector`、`WanVideoTextEncode`、`WanVideoSampler`、`RHHiddenNodes`、`MathExpression|pysssss`、`Text Concatenate`、`WanVideoImageToVideoEncode`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoTextEncode、WanVideoImageToVideoEncode、Wan22PromptSelector、GetImageSizeAndCount

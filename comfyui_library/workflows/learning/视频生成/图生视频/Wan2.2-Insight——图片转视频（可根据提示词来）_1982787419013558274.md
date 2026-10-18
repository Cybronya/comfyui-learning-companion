---
key: 视频生成/图生视频/Wan2.2-Insight——图片转视频（可根据提示词来）_1982787419013558274.json
name: Wan2.2-Insight——图片转视频（可根据提示词来）_1982787419013558274.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Insight——图片转视频（可根据提示词来）_1982787419013558274.json
hash: 11cd1a96784b8ce6
coverage: 0.875
learned_at: 2026-10-15 22:32:43
nodes: [RIFE VFI, LayerUtility: PurgeVRAM V2, CreateCFGScheduleFloatList, MathExpression|pysssss, LoadWanVideoT5TextEncoder, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Text Concatenate, JWInteger, Note, RHHiddenNodes, WanVideoVAELoader, RHHiddenNodes, WanVideoSetBlockSwap, WanVideoDecode, WanVideoSetBlockSwap, VHS_VideoCombine, GetImageSizeAndCount, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, RHHiddenNodes, INTConstant, INTConstant, LoadImage, JWInteger, SetNode, Wan22PromptSelector, CR Text, RHHiddenNodes, ImpactSwitch, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Insight——图片转视频（可根据提示词来）_1982787419013558274.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982787419013558274.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `RIFE VFI`
- `LayerUtility: PurgeVRAM V2`
- `CreateCFGScheduleFloatList`
- `MathExpression|pysssss`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Text Concatenate`
- `JWInteger`
- `Note`
- `RHHiddenNodes`
- `WanVideoVAELoader`
- `RHHiddenNodes`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `JWInteger`
- `SetNode`
- `Wan22PromptSelector`
- `CR Text`
- `RHHiddenNodes`
- `ImpactSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`RIFE VFI`、`LayerUtility: PurgeVRAM V2`、`CreateCFGScheduleFloatList`、`MathExpression|pysssss`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`Text Concatenate`、`JWInteger`、`RHHiddenNodes`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`INTConstant`、`LoadImage`、`Wan22PromptSelector`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、Wan22PromptSelector

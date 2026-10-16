---
key: 视频生成/图生视频/【人脸一致模型】Wan2.2最强图生视频_1972913233726230530.json
name: 【人脸一致模型】Wan2.2最强图生视频_1972913233726230530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1972913233726230530.json
hash: 66d78a6fd5160fd1
coverage: 0.727273
learned_at: 2026-10-15 22:32:01
nodes: [SetNode, SetNode, SetNode, ShowText|pysssss, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, SetNode, WanVideoVAELoader, GetNode, CreateCFGScheduleFloatList, INTConstant, GetNode, WanVideoImageToVideoEncode, GetNode, WanVideoDecode, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoModelLoader, Text Concatenate, JWInteger, INTConstant, JWInteger, RH_LLMAPI_NODE, easy showAnything, ImpactSwitch, WanVideoSetLoRAs, WanVideoSetBlockSwap, CR Text, WanVideoTextEncode, WanVideoSampler, GetNode, Note, Wan22PromptSelector, WanVideoLoraSelectMulti, MathExpression|pysssss, RIFE VFI, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【人脸一致模型】Wan2.2最强图生视频_1972913233726230530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972913233726230530.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoVAELoader`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Text Concatenate`
- `JWInteger`
- `INTConstant`
- `JWInteger`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `ImpactSwitch`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `CR Text`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `GetNode`
- `Note`
- `Wan22PromptSelector`
- `WanVideoLoraSelectMulti`
- `MathExpression|pysssss`
- `RIFE VFI`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **73%**（32/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`Text Concatenate`、`JWInteger`、`RH_LLMAPI_NODE`、`CR Text`、`WanVideoTextEncode`、`Wan22PromptSelector`、`WanVideoLoraSelectMulti`、`MathExpression|pysssss`、`RIFE VFI`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

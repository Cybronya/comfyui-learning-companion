---
key: 视频生成/图生视频/图生视频（Wan2.2-V1）高质量加速版_1950432359721123842.json
name: 图生视频（Wan2.2-V1）高质量加速版_1950432359721123842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频（Wan2.2-V1）高质量加速版_1950432359721123842.json
hash: 9383b7ee61992c68
coverage: 0.970588
learned_at: 2026-10-15 22:30:54
nodes: [WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoBlockSwap, JWInteger, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, INTConstant, CreateCFGScheduleFloatList, INTConstant, WanVideoVAELoader, WanVideoSampler, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, easy seed, WanVideoImageToVideoEncode, easy int, WanVideoModelLoader, WanVideoModelLoader, LoadImage, ImpactSwitch, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, LayerUtility: TextJoinV2, RH_LLMAPI_NODE, RH_Captioner]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频（Wan2.2-V1）高质量加速版_1950432359721123842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950432359721123842.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `JWInteger`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `easy seed`
- `WanVideoImageToVideoEncode`
- `easy int`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `ImpactSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `LayerUtility: TextJoinV2`
- `RH_LLMAPI_NODE`
- `RH_Captioner`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`JWInteger`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`easy seed`、`WanVideoImageToVideoEncode`、`easy int`、`WanVideoModelLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`LayerUtility: TextJoinV2`、`RH_LLMAPI_NODE`、`RH_Captioner`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

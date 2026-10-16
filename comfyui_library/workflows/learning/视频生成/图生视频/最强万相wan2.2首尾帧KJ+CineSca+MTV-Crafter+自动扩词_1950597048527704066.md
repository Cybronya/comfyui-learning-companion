---
key: 视频生成/图生视频/最强万相wan2.2首尾帧KJ+CineSca+MTV-Crafter+自动扩词_1950597048527704066.json
name: 最强万相wan2.2首尾帧KJ+CineSca+MTV-Crafter+自动扩词_1950597048527704066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950597048527704066.json
hash: 81cb5191d470d164
coverage: 0.97619
learned_at: 2026-10-15 22:30:55
nodes: [PrimitiveNode, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoTextEncode, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, WanVideoSampler, SimpleMath+, Int, LoadImage, LoadImage, WanVideoImageToVideoEncode, WanVideoBlockSwap, VHS_VideoCombine, SeedVR2BlockSwap, VHS_VideoCombine, VHS_VideoCombine, INTConstant, INTConstant, WanVideoEasyCache, SeedVR2, LoadWanVideoT5TextEncoder, WanVideoVAELoader, CR Prompt Text, RHHiddenNodes, easy anythingIndexSwitch, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/最强万相wan2.2首尾帧KJ+CineSca+MTV-Crafter+自动扩词_1950597048527704066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950597048527704066.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `PrimitiveNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `Int`
- `LoadImage`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `SeedVR2BlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `WanVideoEasyCache`
- `SeedVR2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CR Prompt Text`
- `RHHiddenNodes`
- `easy anythingIndexSwitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `JWInteger`

## 知识

覆盖率 **98%**（41/42）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`SimpleMath+`、`Int`、`LoadImage`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`SeedVR2BlockSwap`、`INTConstant`、`WanVideoEasyCache`、`SeedVR2`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CR Prompt Text`、`RHHiddenNodes`、`easy anythingIndexSwitch`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`JWInteger`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode

---
key: 视频生成/图生视频/wan 2.2 图生视频  kj 加速_1950010533321859074.json
name: wan 2.2 图生视频  kj 加速_1950010533321859074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950010533321859074.json
hash: c50af96c69eeb867
coverage: 1
learned_at: 2026-10-15 22:30:51
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetBlockSwap, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, INTConstant, CreateCFGScheduleFloatList, INTConstant, INTConstant, MathExpression|pysssss, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/wan 2.2 图生视频  kj 加速_1950010533321859074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950010533321859074.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `MathExpression|pysssss`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`INTConstant`、`CreateCFGScheduleFloatList`、`MathExpression|pysssss`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

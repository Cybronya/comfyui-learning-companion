---
key: 视频生成/图生视频/WAN2.2 dancing_1964640487892242434.json
name: WAN2.2 dancing_1964640487892242434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964640487892242434.json
hash: 62e587dc8123ce87
coverage: 0.891892
learned_at: 2026-10-15 22:31:35
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTorchCompileSettings, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, PrimitiveFloat, INTConstant, PrimitiveFloat, VHS_VideoCombine, WanVideoDecode, WanVideoTextEncode, WanVideoSampler, PrimitiveFloat, CreateCFGScheduleFloatList, WanVideoSampler, INTConstant, PreviewImage, INTConstant, INTConstant, INTConstant, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, ImageResizeKJv2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, easy positive]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2 dancing_1964640487892242434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964640487892242434.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTorchCompileSettings`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveFloat`
- `INTConstant`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `PrimitiveFloat`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `INTConstant`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `easy positive`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LoadImage`、`easy positive`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

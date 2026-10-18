---
key: 视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json
name: Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json
hash: 7c8a4cb4cb79f1ae
coverage: 0.964286
learned_at: 2026-10-15 22:33:56
nodes: [CreateCFGScheduleFloatList, WanVideoDecode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, ImageResizeKJv2, easy seed, INTConstant, INTConstant, WanVideoSampler, WanVideoSetLoRAs, WanVideoSampler, GetImageSizeAndCount, VHS_VideoCombine, WanVideoImageToVideoEncode, Note, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadImage, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005434183445086209.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `easy seed`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoTextEncode`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`easy seed`、`INTConstant`、`WanVideoSampler`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader

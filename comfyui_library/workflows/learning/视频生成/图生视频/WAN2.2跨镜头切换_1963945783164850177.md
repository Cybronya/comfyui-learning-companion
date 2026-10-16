---
key: 视频生成/图生视频/WAN2.2跨镜头切换_1963945783164850177.json
name: WAN2.2跨镜头切换_1963945783164850177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1963945783164850177.json
hash: 5e2b92e2acfb8b27
coverage: 0.840909
learned_at: 2026-10-15 22:31:34
nodes: [WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, PrimitiveFloat, INTConstant, ImageStitch, PreviewImage, LoadImage, PrimitiveFloat, LoadImage, LoadImage, PreviewImage, easy humanSegmentation, VHS_VideoCombine, WanVideoDecode, WanVideoTextEncode, WanVideoSampler, PrimitiveFloat, CreateCFGScheduleFloatList, WanVideoSampler, INTConstant, PreviewImage, INTConstant, PreviewImage, INTConstant, INTConstant, easy positive, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoVAELoader, WanVideoModelLoader, ImageResizeKJv2, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2跨镜头切换_1963945783164850177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963945783164850177.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveFloat`
- `INTConstant`
- `ImageStitch`
- `PreviewImage`
- `LoadImage`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `easy humanSegmentation`
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
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `easy positive`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`ImageStitch`、`LoadImage`、`easy humanSegmentation`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`easy positive`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoModelLoader`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

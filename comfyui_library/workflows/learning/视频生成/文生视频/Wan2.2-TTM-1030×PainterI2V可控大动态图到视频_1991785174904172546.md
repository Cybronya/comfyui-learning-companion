---
key: 视频生成/文生视频/Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546.json
name: Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546.json
hash: 56e607b1e0ff4a2d
coverage: 0.926829
learned_at: 2026-10-15 22:47:13
nodes: [Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, WanVideoModelLoader, WanVideoModelLoader, easy seed, WanVideoTextEncode, PrimitiveNode, easy globalSeed, INTConstant, INTConstant, String Literal, WanVideoEncode, ImageToMask, WanVideoImageToVideoEncode, WanVideoDecode, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, LoadImage, VHS_LoadVideo, VHS_LoadVideo, WanVideoAddTTMLatents, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy seed`
- `WanVideoTextEncode`
- `PrimitiveNode`
- `easy globalSeed`
- `INTConstant`
- `INTConstant`
- `String Literal`
- `WanVideoEncode`
- `ImageToMask`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `WanVideoAddTTMLatents`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`WanVideoModelLoader`、`easy seed`、`WanVideoTextEncode`、`easy globalSeed`、`INTConstant`、`String Literal`、`WanVideoEncode`、`ImageToMask`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`LoadImage`、`VHS_LoadVideo`、`WanVideoAddTTMLatents`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode

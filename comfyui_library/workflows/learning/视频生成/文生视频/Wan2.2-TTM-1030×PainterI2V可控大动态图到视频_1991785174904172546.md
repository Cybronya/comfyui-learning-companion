---
key: 视频生成/文生视频/Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546.json
name: Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-TTM-1030×PainterI2V可控大动态图到视频_1991785174904172546.json
hash: 56e607b1e0ff4a2d
coverage: 0.853659
learned_at: 2026-10-11 02:57:38
nodes: [Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, WanVideoModelLoader, WanVideoModelLoader, easy seed, WanVideoTextEncode, PrimitiveNode, easy globalSeed, INTConstant, INTConstant, String Literal, WanVideoEncode, ImageToMask, WanVideoImageToVideoEncode, WanVideoDecode, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, LoadImage, VHS_LoadVideo, VHS_LoadVideo, WanVideoAddTTMLatents, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: [String Literal, easy globalSeed, easy seed]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **85%**（35/41）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoTextEncode`、`INTConstant`、`WanVideoEncode`、`ImageToMask`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`LoadImage`、`VHS_LoadVideo`、`WanVideoAddTTMLatents`、`VHS_VideoCombine`

**缺卡**（3）：`String Literal`、`easy globalSeed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明

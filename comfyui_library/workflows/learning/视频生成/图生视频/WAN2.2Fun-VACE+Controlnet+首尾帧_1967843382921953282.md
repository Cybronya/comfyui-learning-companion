---
key: 视频生成/图生视频/WAN2.2Fun-VACE+Controlnet+首尾帧_1967843382921953282.json
name: WAN2.2Fun-VACE+Controlnet+首尾帧_1967843382921953282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967843382921953282.json
hash: e1a1b9e4c9f9dcae
coverage: 0.971429
learned_at: 2026-10-15 22:31:43
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoVACEStartToEndFrame, ImageConcatMulti, LoadImage, ImageResizeKJv2, ImageResizeKJv2, LoadImage, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, PrimitiveInt, WanVideoVACEEncode, WanVideoTextEncode, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, INTConstant, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2Fun-VACE+Controlnet+首尾帧_1967843382921953282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967843382921953282.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoVACEStartToEndFrame`
- `ImageConcatMulti`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PrimitiveInt`
- `WanVideoVACEEncode`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`VHS_VideoCombine`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`WanVideoVACEStartToEndFrame`、`ImageConcatMulti`、`LoadImage`、`ImageResizeKJv2`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoVACEEncode`、`WanVideoTextEncode`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode

---
key: 视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json
name: Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json
hash: e1c51860aa6de63b
coverage: 1
learned_at: 2026-10-15 22:31:39
nodes: [CreateCFGScheduleFloatList, WanVideoDecode, INTConstant, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, INTConstant, WanVideoVACEModelSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, ImageResizeKJv2, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, VHS_VideoInfo, ImageResizeKJv2, DWPreprocessor, WanVideoVACEEncode, WanVideoSampler, WanVideoSampler, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Fun Vace视频驱动图片——动作迁移_1966850900927057922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966850900927057922.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `WanVideoVACEModelSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `VHS_VideoInfo`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoDecode`、`INTConstant`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoVACEModelSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`VHS_VideoInfo`、`DWPreprocessor`、`WanVideoVACEEncode`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode

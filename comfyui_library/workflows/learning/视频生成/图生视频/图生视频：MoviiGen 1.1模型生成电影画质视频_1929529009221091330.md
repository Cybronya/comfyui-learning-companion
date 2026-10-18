---
key: 视频生成/图生视频/图生视频：MoviiGen 1.1模型生成电影画质视频_1929529009221091330.json
name: 图生视频：MoviiGen 1.1模型生成电影画质视频_1929529009221091330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频：MoviiGen 1.1模型生成电影画质视频_1929529009221091330.json
hash: 917c292a10ed9694
coverage: 0.655172
learned_at: 2026-10-15 22:30:01
nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, SetNode, WanVideoExperimentalArgs, WanVideoSLG, SetNode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader, WanVideoVACEModelSelect, WanVideoBlockSwap, SetNode, WanVideoModelLoader, LoadImage, ImageResizeKJv2, WanVideoTextEncode, VHS_VideoCombine, WanVideoVACEStartToEndFrame, WanVideoDecode, RIFE VFI, GetImageSizeAndCount, MaskPreview, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频：MoviiGen 1.1模型生成电影画质视频_1929529009221091330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1929529009221091330.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `WanVideoDecode`
- `RIFE VFI`
- `GetImageSizeAndCount`
- `MaskPreview`
- `PreviewImage`

## 知识

覆盖率 **66%**（19/29）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoTorchCompileSettings`、`WanVideoVACEEncode`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LoadImage`、`ImageResizeKJv2`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`、`WanVideoDecode`、`RIFE VFI`、`GetImageSizeAndCount`、`MaskPreview`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount

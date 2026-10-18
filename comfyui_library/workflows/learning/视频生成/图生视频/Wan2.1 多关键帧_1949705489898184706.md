---
key: 视频生成/图生视频/Wan2.1 多关键帧_1949705489898184706.json
name: Wan2.1 多关键帧_1949705489898184706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 多关键帧_1949705489898184706.json
hash: 3de3d63ff3f3edf2
coverage: 0.914286
learned_at: 2026-10-15 22:30:50
nodes: [WanVideoApplyNAG, WanVideoBlockSwap, ImageScaleToMegapixels, RIFE VFI, VHS_VideoCombine, WanVideoDecode, Int, Int, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, ImageResize+, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, WanVideoSampler, WanVideoVACEEncode, WanVideoExperimentalArgs, ImageResize+, WanVideoVACEStartToEndFrame, PreviewImage, ImageResize+, PreviewImage, WanVideoVACEStartToEndFrame, PreviewImage, ImageResize+, ImageBatchMulti, MaskBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, UpscaleModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 多关键帧_1949705489898184706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949705489898184706.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `ImageScaleToMegapixels`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `Int`
- `Int`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `ImageResize+`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `WanVideoExperimentalArgs`
- `ImageResize+`
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`
- `ImageResize+`
- `PreviewImage`
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`
- `ImageResize+`
- `ImageBatchMulti`
- `MaskBatchMulti`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `UpscaleModelLoader`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoApplyNAG`、`WanVideoBlockSwap`、`ImageScaleToMegapixels`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoDecode`、`Int`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTextEncodeSingle`、`ImageResize+`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`WanVideoSampler`、`WanVideoVACEEncode`、`WanVideoExperimentalArgs`、`ImageBatchMulti`、`MaskBatchMulti`、`LoadImage`、`UpscaleModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、UpscaleModelLoader

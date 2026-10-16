---
key: 视频生成/图生视频/Wan2.1 首尾帧_1949686790592045057.json
name: Wan2.1 首尾帧_1949686790592045057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949686790592045057.json
hash: 09f214eda5103436
coverage: 1
learned_at: 2026-10-15 22:30:49
nodes: [WanVideoApplyNAG, RIFE VFI, VHS_VideoCombine, WanVideoDecode, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, Int, Int, Int, VHS_VideoCombine, WanVideoVACEEncode, WanVideoSampler, LoadWanVideoT5TextEncoder, LoadImage, LoadImage, ImageResize+, ImageResize+, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoModelLoader, WanVideoExperimentalArgs, WanVideoVAELoader, UpscaleModelLoader, ImageScaleToMegapixels, WanVideoBlockSwap]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 首尾帧_1949686790592045057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949686790592045057.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoApplyNAG`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `Int`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `ImageResize+`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoModelLoader`
- `WanVideoExperimentalArgs`
- `WanVideoVAELoader`
- `UpscaleModelLoader`
- `ImageScaleToMegapixels`
- `WanVideoBlockSwap`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`WanVideoApplyNAG`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`Int`、`WanVideoVACEEncode`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`ImageResize+`、`WanVideoTextEncodeSingle`、`WanVideoModelLoader`、`WanVideoExperimentalArgs`、`WanVideoVAELoader`、`UpscaleModelLoader`、`ImageScaleToMegapixels`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode、UpscaleModelLoader

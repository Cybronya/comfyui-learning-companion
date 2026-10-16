---
key: 视频生成/图生视频/通义万相Wan2.1图生视频高清补帧放大_1896064173954695170.json
name: 通义万相Wan2.1图生视频高清补帧放大_1896064173954695170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1896064173954695170.json
hash: 7f8668a1444c0d61
coverage: 1
learned_at: 2026-10-15 22:29:17
nodes: [WanVideoSampler, WanVideoDecode, WanVideoTextEncode, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoModelLoader, WanVideoImageClipEncode, CR Upscale Image, ImageResizeKJ, WanVideoBlockSwap, LoadImage, Int, LoadWanVideoT5TextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相Wan2.1图生视频高清补帧放大_1896064173954695170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1896064173954695170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（16 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoImageClipEncode`
- `CR Upscale Image`
- `ImageResizeKJ`
- `WanVideoBlockSwap`
- `LoadImage`
- `Int`
- `LoadWanVideoT5TextEncoder`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncode`、`VHS_VideoCombine`、`RIFE VFI`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoImageClipEncode`、`CR Upscale Image`、`ImageResizeKJ`、`WanVideoBlockSwap`、`LoadImage`、`Int`、`LoadWanVideoT5TextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

---
key: 视频生成/文生视频/【放大+补帧】最新万相Wan2.1图生视频_1898157679490060290.json
name: 【放大+补帧】最新万相Wan2.1图生视频_1898157679490060290.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【放大+补帧】最新万相Wan2.1图生视频_1898157679490060290.json
hash: abac08df8eef3758
coverage: 0.947368
learned_at: 2026-10-15 22:43:20
nodes: [WanVideoTorchCompileSettings, RIFE VFI, CR Upscale Image, VHS_VideoCombine, WanVideoBlockSwap, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoSampler, ImageResizeKJ, WanVideoImageClipEncode, LoadWanVideoT5TextEncoder, String Literal, WanVideoTextEncode, WanVideoDecode, LoadImage, VHS_VideoCombine, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 视频生成/文生视频/【放大+补帧】最新万相Wan2.1图生视频_1898157679490060290.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1898157679490060290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoTorchCompileSettings`
- `RIFE VFI`
- `CR Upscale Image`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `WanVideoImageClipEncode`
- `LoadWanVideoT5TextEncoder`
- `String Literal`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `LoadImage`
- `VHS_VideoCombine`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoTorchCompileSettings`、`RIFE VFI`、`CR Upscale Image`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSampler`、`ImageResizeKJ`、`WanVideoImageClipEncode`、`LoadWanVideoT5TextEncoder`、`String Literal`、`WanVideoTextEncode`、`WanVideoDecode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

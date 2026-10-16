---
key: 视频生成/文生视频/【大摆锤跳舞】最新图生视频动画wan2.1+放大补帧_1918185073190047746.json
name: 【大摆锤跳舞】最新图生视频动画wan2.1+放大补帧_1918185073190047746.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1918185073190047746.json
hash: 405b05211bca3d5a
coverage: 0.944444
learned_at: 2026-10-15 22:43:22
nodes: [WanVideoDecode, Note, ImageResizeKJ, RIFE VFI, WanVideoBlockSwap, VHS_VideoCombine, easy cleanGpuUsed, WanVideoImageClipEncode, WanVideoSampler, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoModelLoader, CR Upscale Image, LoadImage, WanVideoTextEncode, WanVideoLoraSelect, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/【大摆锤跳舞】最新图生视频动画wan2.1+放大补帧_1918185073190047746.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1918185073190047746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（18 个）：
- `WanVideoDecode`
- `Note`
- `ImageResizeKJ`
- `RIFE VFI`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `CR Upscale Image`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`WanVideoDecode`、`ImageResizeKJ`、`RIFE VFI`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`WanVideoImageClipEncode`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CR Upscale Image`、`LoadImage`、`WanVideoTextEncode`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

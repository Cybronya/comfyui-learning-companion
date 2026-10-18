---
key: 视频生成/图生视频/wan2.1万象图生视频跳舞大摆锤+lora+放大补帧_1911803069842292737.json
name: wan2.1万象图生视频跳舞大摆锤+lora+放大补帧_1911803069842292737.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1万象图生视频跳舞大摆锤+lora+放大补帧_1911803069842292737.json
hash: 6aec3ac485443ba6
coverage: 0.947368
learned_at: 2026-10-15 22:29:31
nodes: [WanVideoSampler, WanVideoDecode, Note, ImageResizeKJ, RIFE VFI, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, LoadImage, WanVideoImageClipEncode, CR Upscale Image, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1万象图生视频跳舞大摆锤+lora+放大补帧_1911803069842292737.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911803069842292737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（19 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `Note`
- `ImageResizeKJ`
- `RIFE VFI`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoImageClipEncode`
- `CR Upscale Image`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`ImageResizeKJ`、`RIFE VFI`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LoadImage`、`WanVideoImageClipEncode`、`CR Upscale Image`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

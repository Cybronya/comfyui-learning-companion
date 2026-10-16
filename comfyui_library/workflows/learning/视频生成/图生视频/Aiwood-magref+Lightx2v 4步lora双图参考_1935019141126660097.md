---
key: 视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935019141126660097.json
name: Aiwood-magref+Lightx2v 4步lora双图参考_1935019141126660097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935019141126660097.json
hash: e08d77a704aaa248
coverage: 0.891892
learned_at: 2026-10-15 22:30:20
nodes: [ImageResizeKJv2, WanVideoBlockSwap, WanVideoImageToVideoEncode, LoadImage, LoadImage, VHS_VideoCombine, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, PreviewImage, LoadWanVideoT5TextEncoder, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, easy imageRemBg, ImageResizeKJv2, easy imageRemBg, PreviewImage, WanVideoClipVisionEncode, ImageResizeKJv2, CLIPVisionLoader, ImageConcanate, PreviewImage, VHS_VideoCombine, ImageConcanate, WanVideoTextEncode, WanVideoLoraSelect, WanVideoVAELoader, WanVideoModelLoader, ImagePadKJ, ImagePadKJ, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935019141126660097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935019141126660097.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `PreviewImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy imageRemBg`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `ImageConcanate`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageConcanate`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `ImagePadKJ`
- `ImagePadKJ`
- `PreviewImage`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`LoadImage`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`easy imageRemBg`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`ImageConcanate`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`ImagePadKJ`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

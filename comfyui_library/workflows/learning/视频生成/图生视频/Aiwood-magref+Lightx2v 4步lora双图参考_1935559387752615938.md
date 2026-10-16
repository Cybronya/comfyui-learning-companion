---
key: 视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935559387752615938.json
name: Aiwood-magref+Lightx2v 4步lora双图参考_1935559387752615938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935559387752615938.json
hash: 401300a3ec0ae8ae
coverage: 0.857143
learned_at: 2026-10-15 22:30:22
nodes: [ImageResizeKJv2, WanVideoBlockSwap, LoadImage, LoadImage, WanVideoDecode, VHS_VideoCombine, PreviewImage, LoadWanVideoT5TextEncoder, easy imageRemBg, ImageResizeKJv2, easy imageRemBg, PreviewImage, WanVideoClipVisionEncode, ImageResizeKJv2, ImageConcanate, PreviewImage, VHS_VideoCombine, ImageConcanate, WanVideoLoraSelect, WanVideoVAELoader, ImagePadKJ, ImagePadKJ, PreviewImage, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoTextEncode, CLIPVisionLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Aiwood-magref+Lightx2v 4步lora双图参考_1935559387752615938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935559387752615938.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（28 个）：
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `LoadImage`
- `LoadImage`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `PreviewImage`
- `LoadWanVideoT5TextEncoder`
- `easy imageRemBg`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `ImageConcanate`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageConcanate`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `ImagePadKJ`
- `ImagePadKJ`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `CLIPVisionLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`ImageResizeKJv2`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`easy imageRemBg`、`WanVideoClipVisionEncode`、`ImageConcanate`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`ImagePadKJ`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`CLIPVisionLoader`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

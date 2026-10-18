---
key: 视频生成/图生视频/wan2.1FusionX超高清图生视频_1934598793851510785.json
name: wan2.1FusionX超高清图生视频_1934598793851510785.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1FusionX超高清图生视频_1934598793851510785.json
hash: 4a2007976e4e54ef
coverage: 0.9375
learned_at: 2026-10-15 22:30:18
nodes: [WanVideoVAELoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoApplyNAG, WanVideoTextEncodeSingle, ImageResizeKJ, WanVideoImageToVideoEncode, PreviewImage, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeSingle, LoadImage, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1FusionX超高清图生视频_1934598793851510785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1934598793851510785.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（16 个）：
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `ImageResizeKJ`
- `WanVideoImageToVideoEncode`
- `PreviewImage`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeSingle`
- `LoadImage`
- `WanVideoModelLoader`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadImage`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、ImageResizeKJ

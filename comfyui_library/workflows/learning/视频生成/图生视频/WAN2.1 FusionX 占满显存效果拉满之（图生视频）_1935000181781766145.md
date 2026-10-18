---
key: 视频生成/图生视频/WAN2.1 FusionX 占满显存效果拉满之（图生视频）_1935000181781766145.json
name: WAN2.1 FusionX 占满显存效果拉满之（图生视频）_1935000181781766145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1 FusionX 占满显存效果拉满之（图生视频）_1935000181781766145.json
hash: 42b7095788b8700c
coverage: 0.9375
learned_at: 2026-10-15 22:30:20
nodes: [INTConstant, WanVideoTextEncode, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoDecode, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoVAELoader, PreviewImage, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1 FusionX 占满显存效果拉满之（图生视频）_1935000181781766145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935000181781766145.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（16 个）：
- `INTConstant`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `PreviewImage`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`INTConstant`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`ImageResizeKJ`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

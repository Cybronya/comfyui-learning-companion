---
key: 视频生成/图生视频/wanvideo_WanMove_I2V_example_1998599416028258305.json
name: wanvideo_WanMove_I2V_example_1998599416028258305.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998599416028258305.json
hash: fd6301260537dd84
coverage: 0.846154
learned_at: 2026-10-15 22:33:32
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, LoadImage, PrimitiveNode, PrimitiveNode, WanVideoTextEncode, easy showAnything, RepeatImageBatch, WanVideoDecode, PrimitiveNode, WanVideoSampler, VHS_VideoCombine, WanVideoWanDrawWanMoveTracks, WanVideoWanDrawWanMoveTracks, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SplineEditor, ImageResizeKJv2, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoAddWanMoveTracks, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo_WanMove_I2V_example_1998599416028258305.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998599416028258305.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoTextEncode`
- `easy showAnything`
- `RepeatImageBatch`
- `WanVideoDecode`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoWanDrawWanMoveTracks`
- `WanVideoWanDrawWanMoveTracks`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SplineEditor`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoAddWanMoveTracks`
- `VHS_VideoCombine`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LoadImage`、`WanVideoTextEncode`、`RepeatImageBatch`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoWanDrawWanMoveTracks`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`SplineEditor`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoAddWanMoveTracks`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

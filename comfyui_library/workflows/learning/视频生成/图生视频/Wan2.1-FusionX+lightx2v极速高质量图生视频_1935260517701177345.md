---
key: 视频生成/图生视频/Wan2.1-FusionX+lightx2v极速高质量图生视频_1935260517701177345.json
name: Wan2.1-FusionX+lightx2v极速高质量图生视频_1935260517701177345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935260517701177345.json
hash: 634332ff2e639e11
coverage: 0.884615
learned_at: 2026-10-15 22:30:21
nodes: [WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadImage, WanVideoSampler, GetImageRangeFromBatch, SaveImage, PreviewImage, WanVideoSLG, WanVideoExperimentalArgs, Fast Groups Bypasser (rgthree), WanVideoEnhanceAVideo, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoLoraSelect, Fast Bypasser (rgthree), WanVideoLoraSelect, WanVideoTextEncode, LayerUtility: ImageScaleByAspectRatio V2, easy int, PreviewImage, WanVideoBlockSwap, VHS_VideoCombine, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1-FusionX+lightx2v极速高质量图生视频_1935260517701177345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935260517701177345.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（26 个）：
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadImage`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `SaveImage`
- `PreviewImage`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoLoraSelect`
- `Fast Bypasser (rgthree)`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `PreviewImage`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `easy int`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadImage`、`WanVideoSampler`、`GetImageRangeFromBatch`、`SaveImage`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`Fast Bypasser (rgthree)`、`WanVideoTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`WanVideoBlockSwap`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

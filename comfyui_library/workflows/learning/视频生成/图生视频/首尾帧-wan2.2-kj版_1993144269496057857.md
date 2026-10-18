---
key: 视频生成/图生视频/首尾帧-wan2.2-kj版_1993144269496057857.json
name: 首尾帧-wan2.2-kj版_1993144269496057857.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧-wan2.2-kj版_1993144269496057857.json
hash: 874514be8694f67e
coverage: 1
learned_at: 2026-10-15 22:33:17
nodes: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, JWInteger, WanVideoLoraSelect, INTConstant, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, JWInteger, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, ImageLoader, ImageLoader, LayerUtility: ImageScaleByAspectRatio V2, ImageResize+, WanVideoImageToVideoEncode, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧-wan2.2-kj版_1993144269496057857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993144269496057857.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（31 个）：
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `JWInteger`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `JWInteger`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `ImageLoader`
- `ImageLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResize+`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（31/31）

**有卡**：`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`JWInteger`、`INTConstant`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`ImageLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResize+`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

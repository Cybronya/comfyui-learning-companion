---
key: 视频生成/图生视频/ani，ani全能视频S自选这些的的wan2.1自用加速7步_1944806594343522306.json
name: ani，ani全能视频S自选这些的的wan2.1自用加速7步_1944806594343522306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ani，ani全能视频S自选这些的的wan2.1自用加速7步_1944806594343522306.json
hash: 5c1c3ba71a3ca181
coverage: 1
learned_at: 2026-10-15 22:30:40
nodes: [WanVideoLoraSelect, WanVideoBlockSwap, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoExperimentalArgs, WanVideoFreeInitArgs, LayerUtility: PurgeVRAM, CR Value, WanVideoDecode, VHS_VideoCombine, LoadImage, WanVideoTextEncode, Text Multiline, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoVAELoader, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoEasyCache, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/ani，ani全能视频S自选这些的的wan2.1自用加速7步_1944806594343522306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1944806594343522306.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoExperimentalArgs`
- `WanVideoFreeInitArgs`
- `LayerUtility: PurgeVRAM`
- `CR Value`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoTextEncode`
- `Text Multiline`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoEasyCache`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（22/22）

**有卡**：`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoExperimentalArgs`、`WanVideoFreeInitArgs`、`LayerUtility: PurgeVRAM`、`CR Value`、`WanVideoDecode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTextEncode`、`Text Multiline`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoEasyCache`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

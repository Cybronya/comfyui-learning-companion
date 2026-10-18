---
key: 视频生成/图生视频/KJ版WAN2.1 GGUF Q8 LightX2V加速图生视频高质量版V1_1942759645448744961.json
name: KJ版WAN2.1 GGUF Q8 LightX2V加速图生视频高质量版V1_1942759645448744961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/KJ版WAN2.1 GGUF Q8 LightX2V加速图生视频高质量版V1_1942759645448744961.json
hash: 40bc72df213b484c
coverage: 0.774194
learned_at: 2026-10-15 22:30:37
nodes: [CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoVRAMManagement, WanVideoEnhanceAVideo, JWInteger, Note, Note, Note, Text Multiline, WanVideoLoraSelect, JWInteger, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, Note, VHS_VideoCombine, VHS_VideoCombine, Note, WanVideoSampler, Note, VHS_VideoCombine, VHS_VideoCombine, Note, WanVideoDecode, LayerUtility: PurgeVRAM V2, LoadImage, WanVideoImageToVideoEncode, WanVideoTextEncode, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ版WAN2.1 GGUF Q8 LightX2V加速图生视频高质量版V1_1942759645448744961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1942759645448744961.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoVRAMManagement`
- `WanVideoEnhanceAVideo`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Text Multiline`
- `WanVideoLoraSelect`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `WanVideoSampler` ★核心
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `WanVideoModelLoader`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVRAMManagement`、`WanVideoEnhanceAVideo`、`JWInteger`、`Text Multiline`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

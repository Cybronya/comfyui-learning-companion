---
key: 视频生成/图生视频/Wan2.1最高质量30秒长视频加速稳定版V1（图生视频）_1948954040869761026.json
name: Wan2.1最高质量30秒长视频加速稳定版V1（图生视频）_1948954040869761026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1948954040869761026.json
hash: d4a55ed8564ca861
coverage: 0.851852
learned_at: 2026-10-15 22:30:48
nodes: [CLIPVisionLoader, WanVideoVRAMManagement, Note, Note, Note, JWInteger, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoTextEncode, Note, LayerUtility: PurgeVRAM V2, WanVideoDecode, WanVideoSLG, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelect, LoadImage, WanVideoVAELoader, Text Multiline, JWInteger, WanVideoFreeInitArgs, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1最高质量30秒长视频加速稳定版V1（图生视频）_1948954040869761026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948954040869761026.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `CLIPVisionLoader`
- `WanVideoVRAMManagement`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoVAELoader`
- `Text Multiline`
- `JWInteger`
- `WanVideoFreeInitArgs`
- `VHS_VideoCombine`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`CLIPVisionLoader`、`WanVideoVRAMManagement`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoVAELoader`、`Text Multiline`、`WanVideoFreeInitArgs`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

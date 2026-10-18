---
key: 视频生成/图生视频/ani全能视频S动漫特化3.0模型版图生视频加速版v1_1961656258828943362.json
name: ani全能视频S动漫特化3.0模型版图生视频加速版v1_1961656258828943362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ani全能视频S动漫特化3.0模型版图生视频加速版v1_1961656258828943362.json
hash: 455accc74b4cafda
coverage: 0.851852
learned_at: 2026-10-15 22:31:29
nodes: [CLIPVisionLoader, WanVideoVRAMManagement, JWInteger, Note, Note, Note, JWInteger, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoTextEncode, WanVideoSLG, WanVideoEnhanceAVideo, LayerUtility: PurgeVRAM V2, WanVideoDecode, VHS_VideoCombine, WanVideoExperimentalArgs, WanVideoSampler, WanVideoModelLoader, LoadImage, Text Multiline, WanVideoFreeInitArgs, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/ani全能视频S动漫特化3.0模型版图生视频加速版v1_1961656258828943362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961656258828943362.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `CLIPVisionLoader`
- `WanVideoVRAMManagement`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `LoadImage`
- `Text Multiline`
- `WanVideoFreeInitArgs`
- `Note`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`CLIPVisionLoader`、`WanVideoVRAMManagement`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadImage`、`Text Multiline`、`WanVideoFreeInitArgs`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

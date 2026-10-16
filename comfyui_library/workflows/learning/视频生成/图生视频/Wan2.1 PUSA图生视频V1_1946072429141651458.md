---
key: 视频生成/图生视频/Wan2.1 PUSA图生视频V1_1946072429141651458.json
name: Wan2.1 PUSA图生视频V1_1946072429141651458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1946072429141651458.json
hash: a26b1fd0fb4a7dca
coverage: 0.846154
learned_at: 2026-10-15 22:30:43
nodes: [CLIPVisionLoader, WanVideoVRAMManagement, JWInteger, Note, Note, Note, JWInteger, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, Text Multiline, LoadImage, WanVideoClipVisionEncode, WanVideoTextEncode, Note, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, WanVideoLoraSelect, WanVideoDecode, WanVideoModelLoader, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoImageToVideoEncode, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 PUSA图生视频V1_1946072429141651458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1946072429141651458.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
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
- `Text Multiline`
- `LoadImage`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **85%**（22/26）

**有卡**：`CLIPVisionLoader`、`WanVideoVRAMManagement`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`Text Multiline`、`LoadImage`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoImageToVideoEncode`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode

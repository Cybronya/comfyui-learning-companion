---
key: 视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json
name: 首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json
hash: 0daf4c03114a3e83
coverage: 0.939394
learned_at: 2026-10-15 22:49:06
nodes: [WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, SetNode, LoadWanVideoT5TextEncoder, JWInteger, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoTextEncode, GetNode, VHS_VideoCombine, ImageResize+, ImageLoader, ImageLoader, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/首尾帧 wan2.2 kj加速版 万相4步加速视频 Rapid AllInOne 2图生视频_2028398849848516609.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `JWInteger`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageResize+`
- `ImageLoader`
- `ImageLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`VHS_VideoCombine`、`ImageResize+`、`ImageLoader`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

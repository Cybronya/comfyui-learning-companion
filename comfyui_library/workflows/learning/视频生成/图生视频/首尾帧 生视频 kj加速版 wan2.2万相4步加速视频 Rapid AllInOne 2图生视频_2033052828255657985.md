---
key: 视频生成/图生视频/首尾帧 生视频 kj加速版 wan2.2万相4步加速视频 Rapid AllInOne 2图生视频_2033052828255657985.json
name: 首尾帧 生视频 kj加速版 wan2.2万相4步加速视频 Rapid AllInOne 2图生视频_2033052828255657985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033052828255657985.json
hash: 28aae7b830ba687a
coverage: 0.939394
learned_at: 2026-10-15 22:35:38
nodes: [WanVideoVAELoader, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, JWInteger, WanVideoSampler, WanVideoSampler, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, SetNode, LoadWanVideoT5TextEncoder, JWInteger, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoImageToVideoEncode, GetNode, VHS_VideoCombine, ImageResize+, LayerUtility: ImageScaleByAspectRatio V2, ImageLoader, WanVideoTextEncode, ImageLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧 生视频 kj加速版 wan2.2万相4步加速视频 Rapid AllInOne 2图生视频_2033052828255657985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033052828255657985.json`

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
- `GetNode`
- `VHS_VideoCombine`
- `ImageResize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageLoader`
- `WanVideoTextEncode`
- `ImageLoader`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`INTConstant`、`JWInteger`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`ImageResize+`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageLoader`、`WanVideoTextEncode`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

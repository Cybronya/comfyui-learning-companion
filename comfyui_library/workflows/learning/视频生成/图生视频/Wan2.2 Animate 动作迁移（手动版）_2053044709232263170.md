---
key: 视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json
name: Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json
hash: 7632cc278f24272c
coverage: 1
learned_at: 2026-10-15 22:37:35
nodes: [JWInteger, JWInteger, WanVideoClipVisionEncode, ImageResizeKJv2, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, WanVideoSetBlockSwap, WanVideoBlockSwap, VHS_VideoInfo, WanVideoSampler, SaveImage, VHS_VideoCombine, VHS_LoadVideo, VHS_LoadVideo, LoadImage, VHS_LoadVideo, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoModelLoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053044709232263170.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（24 个）：
- `JWInteger`
- `JWInteger`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `VHS_VideoInfo`
- `WanVideoSampler` ★核心
- `SaveImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`JWInteger`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`VHS_VideoInfo`、`WanVideoSampler`、`SaveImage`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

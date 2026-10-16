---
key: 视频生成/图生视频/【遇见AI】wan2.1 Uni3c视频运镜模型_2071441193522778114.json
name: 【遇见AI】wan2.1 Uni3c视频运镜模型_2071441193522778114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2071441193522778114.json
hash: ec0f918f61625969
coverage: 1
learned_at: 2026-10-15 22:40:45
nodes: [WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoBlockSwap, WanVideoExperimentalArgs, ImageResizeKJv2, WanVideoVAELoader, CLIPVisionLoader, WanVideoModelLoader, LoadImage, WanVideoDecode, VHS_VideoCombine, WanVideoLoraSelect, WanVideoSampler, WanVideoEncode, ImageResizeKJv2, WanVideoUni3C_embeds, WanVideoTextEncodeCached, VHS_LoadVideo, WanVideoUni3C_ControlnetLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】wan2.1 Uni3c视频运镜模型_2071441193522778114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2071441193522778114.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoExperimentalArgs`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `WanVideoTextEncodeCached`
- `VHS_LoadVideo`
- `WanVideoUni3C_ControlnetLoader`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoExperimentalArgs`、`ImageResizeKJv2`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoModelLoader`、`LoadImage`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`WanVideoUni3C_ControlnetLoader`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached

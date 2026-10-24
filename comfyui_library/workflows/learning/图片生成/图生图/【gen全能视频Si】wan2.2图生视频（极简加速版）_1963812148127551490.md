---
key: 图片生成/图生图/【gen全能视频Si】wan2.2图生视频（极简加速版）_1963812148127551490.json
name: 【gen全能视频Si】wan2.2图生视频（极简加速版）_1963812148127551490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【gen全能视频Si】wan2.2图生视频（极简加速版）_1963812148127551490.json
hash: 85025680de863260
coverage: 1
learned_at: 2026-10-23 11:49:09
nodes: [WanVideoModelLoader, PurgeVRAM_UTK, WanVideoSampler, WanVideoSampler, WanVideoVAELoader, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoImageToVideoEncode, WanVideoDecode, INTConstant, VHS_VideoCombine, ImageScaleByAspectRatio_UTK, LoadImage, WanVideoTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/【gen全能视频Si】wan2.2图生视频（极简加速版）_1963812148127551490.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【gen全能视频Si】wan2.2图生视频（极简加速版）_1963812148127551490.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（23 个）：
- `WanVideoModelLoader`
- `PurgeVRAM_UTK`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageScaleByAspectRatio_UTK`
- `LoadImage`
- `WanVideoTextEncode`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`WanVideoModelLoader`、`PurgeVRAM_UTK`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`INTConstant`、`VHS_VideoCombine`、`ImageScaleByAspectRatio_UTK`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect

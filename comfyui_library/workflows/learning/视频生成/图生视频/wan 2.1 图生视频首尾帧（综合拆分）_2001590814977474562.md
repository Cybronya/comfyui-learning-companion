---
key: 视频生成/图生视频/wan 2.1 图生视频首尾帧（综合拆分）_2001590814977474562.json
name: wan 2.1 图生视频首尾帧（综合拆分）_2001590814977474562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2001590814977474562.json
hash: db225d2693b539aa
coverage: 1
learned_at: 2026-10-15 22:33:46
nodes: [WanVideoBlockSwap, CLIPVisionLoader, LoadImage, WanVideoTorchCompileSettings, WanVideoImageToVideoEncode, WanVideoDecode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, WanVideoClipVisionEncode, ImageResizeKJv2, VHS_VideoCombine, WanVideoModelLoader, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/wan 2.1 图生视频首尾帧（综合拆分）_2001590814977474562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001590814977474562.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（16 个）：
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoBlockSwap`、`CLIPVisionLoader`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs

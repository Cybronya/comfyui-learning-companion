---
key: 视频生成/图生视频/【遇见AI】wan2.1 Skyreels V2 图生视频，支持超过81帧_2067521044533039105.json
name: 【遇见AI】wan2.1 Skyreels V2 图生视频，支持超过81帧_2067521044533039105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067521044533039105.json
hash: 889192ff68b298b8
coverage: 0.954545
learned_at: 2026-10-15 22:40:03
nodes: [WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, VHS_VideoCombine, LoadImage, MarkdownNote, LoadImage, LoadImage, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader, CLIPVisionLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】wan2.1 Skyreels V2 图生视频，支持超过81帧_2067521044533039105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067521044533039105.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（22 个）：
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `CLIPVisionLoader`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect

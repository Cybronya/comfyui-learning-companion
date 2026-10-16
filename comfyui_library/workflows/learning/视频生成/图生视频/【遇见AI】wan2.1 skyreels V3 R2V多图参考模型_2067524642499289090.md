---
key: 视频生成/图生视频/【遇见AI】wan2.1 skyreels V3 R2V多图参考模型_2067524642499289090.json
name: 【遇见AI】wan2.1 skyreels V3 R2V多图参考模型_2067524642499289090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067524642499289090.json
hash: 6b53b9840d5d9694
coverage: 0.888889
learned_at: 2026-10-15 22:40:04
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoBlockSwap, WanVideoSampler, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, MarkdownNote, LoadImage, LoadImage, WanVideoLoraSelect, easy imageRemBg, WanVideoEncode, PreviewImage, WanVideoEncode, easy imageRemBg, ImageResizeKJ, PreviewImage, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, easy imageRemBg, WanVideoEncode, ImageResizeKJ, ImageResizeKJ, WanVideoPhantomEmbeds, LoadImage, LoadImage, LoadImage, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/【遇见AI】wan2.1 skyreels V3 R2V多图参考模型_2067524642499289090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067524642499289090.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `WanVideoLoraSelect`
- `easy imageRemBg`
- `WanVideoEncode`
- `PreviewImage`
- `WanVideoEncode`
- `easy imageRemBg`
- `ImageResizeKJ`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `easy imageRemBg`
- `WanVideoEncode`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `WanVideoPhantomEmbeds`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`LoadImage`、`WanVideoLoraSelect`、`easy imageRemBg`、`WanVideoEncode`、`ImageResizeKJ`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoPhantomEmbeds`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、WanVideoSetLoRAs

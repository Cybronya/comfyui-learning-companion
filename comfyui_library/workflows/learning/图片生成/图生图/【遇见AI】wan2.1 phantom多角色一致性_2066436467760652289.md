---
key: 图片生成/图生图/【遇见AI】wan2.1 phantom多角色一致性_2066436467760652289.json
name: 【遇见AI】wan2.1 phantom多角色一致性_2066436467760652289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 phantom多角色一致性_2066436467760652289.json
hash: e1c6538b61a0426b
coverage: 0.888889
learned_at: 2026-10-23 11:52:26
nodes: [WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoBlockSwap, WanVideoSampler, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, PreviewImage, WanVideoEncode, MarkdownNote, LoadImage, LoadImage, VHS_VideoCombine, LoadImage, WanVideoPhantomEmbeds, LoadImage, ImageResizeKJ, WanVideoEncode, ImageResizeKJ, PreviewImage, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVAELoader, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】wan2.1 phantom多角色一致性_2066436467760652289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 phantom多角色一致性_2066436467760652289.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（27 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `PreviewImage`
- `WanVideoEncode`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoPhantomEmbeds`
- `LoadImage`
- `ImageResizeKJ`
- `WanVideoEncode`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoEncode`、`LoadImage`、`VHS_VideoCombine`、`WanVideoPhantomEmbeds`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、WanVideoSetLoRAs

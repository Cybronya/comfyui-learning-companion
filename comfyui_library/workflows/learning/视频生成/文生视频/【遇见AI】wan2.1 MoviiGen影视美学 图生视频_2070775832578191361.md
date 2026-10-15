---
key: 视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json
name: 【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json
hash: 4682fd5f1cd7e35f
coverage: 0.888889
learned_at: 2026-10-15 22:47:43
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoSampler, WanVideoBlockSwap, GetImageSize+, LoadImage, MarkdownNote, LoadImage, WanVideoVAELoader, WanVideoModelLoader, WanVideoTextEncodeCached, LoadImage, PreviewImage, MaskPreview+, PreviewImage, VHS_VideoCombine, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoLoraSelect, ImageResizeKJv2, WanVideoVACEStartToEndFrame]
patterns: []
missing: []
---

# 视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（27 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `GetImageSize+`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `LoadImage`
- `PreviewImage`
- `MaskPreview+`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `ImageResizeKJv2`
- `WanVideoVACEStartToEndFrame`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoBlockSwap`、`GetImageSize+`、`LoadImage`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`MaskPreview+`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`WanVideoVACEStartToEndFrame`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs

---
key: 视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json
name: 【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json
hash: 4682fd5f1cd7e35f
coverage: 0.814815
learned_at: 2026-10-11 20:21:33
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoSampler, WanVideoBlockSwap, GetImageSize+, LoadImage, MarkdownNote, LoadImage, WanVideoVAELoader, WanVideoModelLoader, WanVideoTextEncodeCached, LoadImage, PreviewImage, MaskPreview+, PreviewImage, VHS_VideoCombine, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoLoraSelect, ImageResizeKJv2, WanVideoVACEStartToEndFrame]
patterns: []
missing: [GetImageSize+, MaskPreview+]
discoveries: [次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
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

覆盖率 **81%**（22/27）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`WanVideoVACEStartToEndFrame`

**缺卡**（2）：`GetImageSize+`、`MaskPreview+`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明

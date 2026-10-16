---
key: 视频生成/图生视频/Wan2.1_FusionX-VACE_Live2D动态壁纸_1980164711092228097.json
name: Wan2.1_FusionX-VACE_Live2D动态壁纸_1980164711092228097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980164711092228097.json
hash: aca559320af5bc53
coverage: 0.587302
learned_at: 2026-10-15 22:32:28
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, Note, MarkdownNote, VHS_VideoCombine, ImageUpscaleWithModel, VHS_VideoCombine, RIFE VFI, easy negative, SimpleMath+, WanVideoBlockSwap, Note, easy int, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, Note, WanVideoSampler, ImageResizeKJv2, easy int, SimpleMath+, SimpleMath+, Note, easy float, ImageResizeKJv2, LoadImage, LoadImage, easy int, SetNode, SetNode, UpscaleModelLoader, GetNode, GetNode, WanVideoVACEEncode, WanVideoTeaCache, WanVideoEasyCache, WanVideoExperimentalArgs, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoTextEncode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetRadialAttention, Note, SetNode, Note, WanVideoDecode, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoLoraSelect, easy positive, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1_FusionX-VACE_Live2D动态壁纸_1980164711092228097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980164711092228097.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（63 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `MarkdownNote`
- `VHS_VideoCombine`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `RIFE VFI`
- `easy negative`
- `SimpleMath+`
- `WanVideoBlockSwap`
- `Note`
- `easy int`
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `easy int`
- `SimpleMath+`
- `SimpleMath+`
- `Note`
- `easy float`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `easy int`
- `SetNode`
- `SetNode`
- `UpscaleModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoTeaCache`
- `WanVideoEasyCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetRadialAttention`
- `Note`
- `SetNode`
- `Note`
- `WanVideoDecode`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `easy positive`
- `WanVideoLoraSelect`

## 知识

覆盖率 **59%**（37/63）

**有卡**：`VHS_VideoCombine`、`ImageUpscaleWithModel`、`RIFE VFI`、`easy negative`、`SimpleMath+`、`WanVideoBlockSwap`、`easy int`、`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`WanVideoSampler`、`ImageResizeKJv2`、`easy float`、`LoadImage`、`UpscaleModelLoader`、`WanVideoVACEEncode`、`WanVideoTeaCache`、`WanVideoEasyCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSetRadialAttention`、`WanVideoDecode`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`easy positive`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect

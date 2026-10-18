---
key: 视频生成/图生视频/万相视频Wan2.1超级首尾帧控制_1905171860894437377.json
name: 万相视频Wan2.1超级首尾帧控制_1905171860894437377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相视频Wan2.1超级首尾帧控制_1905171860894437377.json
hash: dc242022cd49dc81
coverage: 0.891892
learned_at: 2026-10-15 22:29:25
nodes: [GetNode, AddLabel, AddLabel, WanVideoVRAMManagement, WanVideoModelLoader, LoadWanVideoT5TextEncoder, LoadWanVideoClipTextEncoder, WanVideoImageToVideoEncode, WanVideoTeaCache, WanVideoSampler, WanVideoExperimentalArgs, WanVideoSLG, WanVideoBlockSwap, CLIPVisionLoader, GetNode, EmptyImage, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, WanVideoDecode, GetImageSizeAndCount, WanVideoEnhanceAVideo, WanVideoTextEncode, LoadImage, LoadImage, ImageResize+, SetNode, Note Plus (mtb), VHS_VideoCombine, Text Multiline, ImageUpscaleWithModel, LayerUtility: PurgeVRAM, Upscale Model Loader, ImageResize+, WanVideoClipVisionEncode, WanVideoVAELoader, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/万相视频Wan2.1超级首尾帧控制_1905171860894437377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1905171860894437377.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（37 个）：
- `GetNode`
- `AddLabel`
- `AddLabel`
- `WanVideoVRAMManagement`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `GetNode`
- `EmptyImage`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncode`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `SetNode`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `Text Multiline`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `Upscale Model Loader`
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `SetNode`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`AddLabel`、`WanVideoVRAMManagement`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`LoadWanVideoClipTextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`EmptyImage`、`VHS_VideoCombine`、`ImageConcatMulti`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`LoadImage`、`ImageResize+`、`Note Plus (mtb)`、`Text Multiline`、`ImageUpscaleWithModel`、`LayerUtility: PurgeVRAM`、`Upscale Model Loader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

---
key: 视频生成/图生视频/最新Wan2.1+Vace首尾帧  极速运行 中文注释_1912169450282647553.json
name: 最新Wan2.1+Vace首尾帧  极速运行 中文注释_1912169450282647553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新Wan2.1+Vace首尾帧  极速运行 中文注释_1912169450282647553.json
hash: 1555ee9984f63f2d
coverage: 0.6
learned_at: 2026-10-15 22:29:32
nodes: [Note, WanVideoBlockSwap, Note, SetNode, SetNode, LoadWanVideoT5TextEncoder, Note, MarkdownNote, WanVideoVAELoader, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, Note, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, AddLabel, GetImageSizeAndCount, GetImageSizeAndCount, WanVideoExperimentalArgs, WanVideoSLG, WanVideoTeaCache, WanVideoSampler, WanVideoDecode, AddLabel, ImageConcatMulti, EmptyImage, LoadImage, MaskPreview+, WanVideoVACEEncode, SetNode, GetNode, SetNode, GetNode, LoadImage, ImageResizeKJ, ImageResizeKJ, ImageConcatMulti, VHS_VideoCombine, WanVideoTextEncode, WanVideoVACEStartToEndFrame, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/最新Wan2.1+Vace首尾帧  极速运行 中文注释_1912169450282647553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1912169450282647553.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（45 个）：
- `Note`
- `WanVideoBlockSwap`
- `Note`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `MarkdownNote`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `AddLabel`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `AddLabel`
- `ImageConcatMulti`
- `EmptyImage`
- `LoadImage`
- `MaskPreview+`
- `WanVideoVACEEncode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`

## 知识

覆盖率 **60%**（27/45）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`AddLabel`、`GetImageSizeAndCount`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`EmptyImage`、`LoadImage`、`MaskPreview+`、`WanVideoVACEEncode`、`ImageResizeKJ`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoVACEStartToEndFrame`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount

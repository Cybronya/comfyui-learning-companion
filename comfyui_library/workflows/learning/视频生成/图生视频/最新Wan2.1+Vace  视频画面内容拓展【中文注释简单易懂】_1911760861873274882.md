---
key: 视频生成/图生视频/最新Wan2.1+Vace  视频画面内容拓展【中文注释简单易懂】_1911760861873274882.json
name: 最新Wan2.1+Vace  视频画面内容拓展【中文注释简单易懂】_1911760861873274882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1911760861873274882.json
hash: 4e411b72d7e17042
coverage: 0.590909
learned_at: 2026-10-15 22:29:31
nodes: [Note, WanVideoBlockSwap, Note, SetNode, SetNode, LoadWanVideoT5TextEncoder, Note, MarkdownNote, WanVideoVAELoader, GetNode, GetNode, WanVideoDecode, EmptyImage, AddLabel, GetImageSizeAndCount, ImageConcatMulti, GetNode, GetNode, WanVideoExperimentalArgs, GetNode, GetNode, GetImageRangeFromBatch, GetImageRangeFromBatch, WanVideoTeaCache, GetImageSizeAndCount, WanVideoModelLoader, WanVideoVACEModelSelect, SetNode, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoTextEncode, PreviewImage, MaskPreview+, SetNode, WanVideoVACEEncode, INTConstant, Note, ImagePadKJ, VHS_LoadVideo, ImageResizeKJ, VHS_VideoCombine, Note, Note, WanVideoSLG]
patterns: []
missing: []
---

# 视频生成/图生视频/最新Wan2.1+Vace  视频画面内容拓展【中文注释简单易懂】_1911760861873274882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1911760861873274882.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `Note`
- `WanVideoBlockSwap`
- `Note`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `MarkdownNote`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `EmptyImage`
- `AddLabel`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoExperimentalArgs`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `WanVideoTeaCache`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `PreviewImage`
- `MaskPreview+`
- `SetNode`
- `WanVideoVACEEncode`
- `INTConstant`
- `Note`
- `ImagePadKJ`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoSLG`

## 知识

覆盖率 **59%**（26/44）

**有卡**：`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoDecode`、`EmptyImage`、`AddLabel`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoExperimentalArgs`、`GetImageRangeFromBatch`、`WanVideoTeaCache`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoTextEncode`、`MaskPreview+`、`WanVideoVACEEncode`、`INTConstant`、`ImagePadKJ`、`VHS_LoadVideo`、`ImageResizeKJ`、`VHS_VideoCombine`、`WanVideoSLG`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSizeAndCount、ImageResizeKJ

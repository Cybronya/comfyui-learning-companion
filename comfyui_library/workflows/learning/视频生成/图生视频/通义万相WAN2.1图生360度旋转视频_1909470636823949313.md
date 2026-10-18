---
key: 视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1909470636823949313.json
name: 通义万相WAN2.1图生360度旋转视频_1909470636823949313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1909470636823949313.json
hash: faf6b639a9ccea33
coverage: 0.869565
learned_at: 2026-10-15 22:29:29
nodes: [WanVideoBlockSwap, WanVideoSampler, easy imageSize, TextInput_, LayerUtility: ImageScaleByAspectRatio V2, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, ImageUpscaleWithModel, VHS_VideoCombine, LoadImage, LayerUtility: PurgeVRAM, Note, WanVideoTeaCache, Select Image Indices, PreviewImage, WanVideoImageClipEncode, WanVideoTextEncode, UpscaleModelLoader, WanVideoDecode, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/通义万相WAN2.1图生360度旋转视频_1909470636823949313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1909470636823949313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（23 个）：
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `easy imageSize`
- `TextInput_`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `Note`
- `WanVideoTeaCache`
- `Select Image Indices`
- `PreviewImage`
- `WanVideoImageClipEncode`
- `WanVideoTextEncode`
- `UpscaleModelLoader`
- `WanVideoDecode`
- `PreviewImage`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`WanVideoBlockSwap`、`WanVideoSampler`、`easy imageSize`、`TextInput_`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`ImageUpscaleWithModel`、`VHS_VideoCombine`、`LoadImage`、`LayerUtility: PurgeVRAM`、`WanVideoTeaCache`、`Select Image Indices`、`WanVideoImageClipEncode`、`WanVideoTextEncode`、`UpscaleModelLoader`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

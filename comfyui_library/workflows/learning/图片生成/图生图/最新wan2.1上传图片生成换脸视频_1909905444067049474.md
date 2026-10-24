---
key: 图片生成/图生图/最新wan2.1上传图片生成换脸视频_1909905444067049474.json
name: 最新wan2.1上传图片生成换脸视频_1909905444067049474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最新wan2.1上传图片生成换脸视频_1909905444067049474.json
hash: 4bb9d6f3cdb9e9c7
coverage: 0.962963
learned_at: 2026-10-23 13:07:22
nodes: [WanVideoEnhanceAVideo, WanVideoDecode, WanVideoBlockSwap, UpscaleModelLoader, WanVideoImageClipEncode, StringConstantMultiline, LayerUtility: PurgeVRAM, WanVideoTextEncode, ImageUpscaleWithModel, Int, WanVideoSampler, workflow>instnatID, VAEEncode, workflow>模型, PreviewImage, CropFace, DZ_Face_Detailer, ConstrainImage|pysssss, LoadImage, LoadImage, VHS_VideoCombine, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadWanVideoT5TextEncoder, ImageResizeKJ, VAEDecode]
patterns: []
missing: []
---

# 图片生成/图生图/最新wan2.1上传图片生成换脸视频_1909905444067049474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最新wan2.1上传图片生成换脸视频_1909905444067049474.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `UpscaleModelLoader`
- `WanVideoImageClipEncode`
- `StringConstantMultiline`
- `LayerUtility: PurgeVRAM`
- `WanVideoTextEncode`
- `ImageUpscaleWithModel`
- `Int`
- `WanVideoSampler` ★核心
- `workflow>instnatID`
- `VAEEncode` ★核心
- `workflow>模型`
- `PreviewImage`
- `CropFace`
- `DZ_Face_Detailer`
- `ConstrainImage|pysssss`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeKJ`
- `VAEDecode` ★核心

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoBlockSwap`、`UpscaleModelLoader`、`WanVideoImageClipEncode`、`StringConstantMultiline`、`LayerUtility: PurgeVRAM`、`WanVideoTextEncode`、`ImageUpscaleWithModel`、`Int`、`WanVideoSampler`、`workflow>instnatID`、`VAEEncode`、`workflow>模型`、`CropFace`、`DZ_Face_Detailer`、`ConstrainImage|pysssss`、`LoadImage`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJ`、`VAEDecode`

**用到的条目**：VAEDecode、LoadImage、WanVideoSampler、VAEEncode、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode

---
key: 图片生成/图生图/【遇见AI】wan2.1 VACE 视频重绘，换脸，修改任何东西_2065246575059886081.json
name: 【遇见AI】wan2.1 VACE 视频重绘，换脸，修改任何东西_2065246575059886081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 VACE 视频重绘，换脸，修改任何东西_2065246575059886081.json
hash: d1df56fc72624ede
coverage: 0.896552
learned_at: 2026-10-23 11:52:26
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoBlockSwap, MarkdownNote, LoadImage, LoadImage, WanVideoTeaCache, WanVideoVACEEncode, VHS_VideoCombine, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, PreviewImage, MaskPreview+, ImageResizeKJv2, PreviewImage, InpaintPreprocessor, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoVACEModelSelect, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】wan2.1 VACE 视频重绘，换脸，修改任何东西_2065246575059886081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 VACE 视频重绘，换脸，修改任何东西_2065246575059886081.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `WanVideoTeaCache`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `PreviewImage`
- `MaskPreview+`
- `ImageResizeKJv2`
- `PreviewImage`
- `InpaintPreprocessor`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoTeaCache`、`WanVideoVACEEncode`、`VHS_VideoCombine`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`MaskPreview+`、`ImageResizeKJv2`、`InpaintPreprocessor`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs

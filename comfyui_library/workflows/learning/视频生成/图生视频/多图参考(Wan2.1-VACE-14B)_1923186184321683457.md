---
key: 视频生成/图生视频/多图参考(Wan2.1-VACE-14B)_1923186184321683457.json
name: 多图参考(Wan2.1-VACE-14B)_1923186184321683457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多图参考(Wan2.1-VACE-14B)_1923186184321683457.json
hash: c6e7f236008f08e2
coverage: 0.921053
learned_at: 2026-10-15 22:29:47
nodes: [WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVACEEncode, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, WanVideoTextEncode, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, VHS_VideoCombine, PreviewImage, GetImageSize, Image Blank, ImageConcanate, WanVideoVAELoader, String Literal, LoadImage, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSampler, INTConstant, ImageCompositeMasked, PreviewImage, INTConstant, ImageResizeKJ, INTConstant, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/多图参考(Wan2.1-VACE-14B)_1923186184321683457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1923186184321683457.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（38 个）：
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVACEEncode`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoTextEncode`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetImageSize`
- `Image Blank`
- `ImageConcanate`
- `WanVideoVAELoader`
- `String Literal`
- `LoadImage`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSampler` ★核心
- `INTConstant`
- `ImageCompositeMasked`
- `PreviewImage`
- `INTConstant`
- `ImageResizeKJ`
- `INTConstant`
- `LoadImage`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVACEEncode`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`LayerMask: ObjectDetectorFL2`、`WanVideoTextEncode`、`GetImageSize`、`Image Blank`、`ImageCompositeMasked`、`VHS_VideoCombine`、`ImageConcanate`、`WanVideoVAELoader`、`String Literal`、`LoadImage`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoSampler`、`INTConstant`、`ImageResizeKJ`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、GetImageSize

---
key: 视频生成/图生视频/wan2.2动态壁纸无缝循环_1985985160506159105.json
name: wan2.2动态壁纸无缝循环_1985985160506159105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1985985160506159105.json
hash: c4cfac12186f290b
coverage: 0.96
learned_at: 2026-10-15 22:32:53
nodes: [mxSlider, mxSlider, Int, Note, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSEImageClipEncode, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoSEModelLoader, CR Upscale Image, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, mxSlider, RHHiddenNodes, VHS_VideoCombine, WanVideoSESampler, WanVideoSEDecode, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2动态壁纸无缝循环_1985985160506159105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985985160506159105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（25 个）：
- `mxSlider`
- `mxSlider`
- `Int`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSEImageClipEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoSEModelLoader`
- `CR Upscale Image`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `mxSlider`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `WanVideoSESampler` ★核心
- `WanVideoSEDecode`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`mxSlider`、`Int`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSEImageClipEncode`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoSEModelLoader`、`CR Upscale Image`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`RHHiddenNodes`、`VHS_VideoCombine`、`WanVideoSESampler`、`WanVideoSEDecode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSESampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoTextEncode、WanVideoVAELoader、WanVideoSEDecode、WanVideoSEImageClipEncode

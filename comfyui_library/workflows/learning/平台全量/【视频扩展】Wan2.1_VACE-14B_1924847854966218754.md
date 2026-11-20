---
key: 平台全量/【视频扩展】Wan2.1_VACE-14B_1924847854966218754.json
name: 【视频扩展】Wan2.1_VACE-14B_1924847854966218754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【视频扩展】Wan2.1_VACE-14B_1924847854966218754.json
hash: 070e4af49b9a7474
coverage: 0.823529
learned_at: 2026-11-14 01:25:10
nodes: [WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, VHS_LoadVideo, SetNode, Anything Everywhere, VHS_VideoCombine, RH_Captioner, WanVideoSampler, WanVideoDecode, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoVACEEncode, WanVideoVACEModelSelect, Anything Everywhere, Anything Everywhere, ImageResize+, GetNode, RepeatImageBatch, MaskToImage, InpaintPreprocessor, GetImageSizeAndCount, PreviewImage, ImageResize+, ImageResize+, Int, Int, ImageToMask, WanVideoTextEncode, ImagePadForOutpaint, LoadWanVideoT5TextEncoder, WanVideoVAELoader]
patterns: []
missing: []
---

# 平台全量/【视频扩展】Wan2.1_VACE-14B_1924847854966218754.json

> 来源文件 `comfyui_library/workflows/平台全量/【视频扩展】Wan2.1_VACE-14B_1924847854966218754.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（34 个）：
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `VHS_LoadVideo`
- `SetNode`
- `Anything Everywhere`
- `VHS_VideoCombine`
- `RH_Captioner`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `Anything Everywhere`
- `Anything Everywhere`
- `ImageResize+`
- `GetNode`
- `RepeatImageBatch`
- `MaskToImage`
- `InpaintPreprocessor`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageResize+`
- `ImageResize+`
- `Int`
- `Int`
- `ImageToMask`
- `WanVideoTextEncode`
- `ImagePadForOutpaint`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`VHS_VideoCombine`、`RH_Captioner`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`ImageResize+`、`RepeatImageBatch`、`MaskToImage`、`InpaintPreprocessor`、`GetImageSizeAndCount`、`Int`、`ImageToMask`、`WanVideoTextEncode`、`ImagePadForOutpaint`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageSizeAndCount

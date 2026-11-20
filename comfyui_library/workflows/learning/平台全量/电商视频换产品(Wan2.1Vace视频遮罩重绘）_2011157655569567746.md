---
key: 平台全量/电商视频换产品(Wan2.1Vace视频遮罩重绘）_2011157655569567746.json
name: 电商视频换产品(Wan2.1Vace视频遮罩重绘）_2011157655569567746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/电商视频换产品(Wan2.1Vace视频遮罩重绘）_2011157655569567746.json
hash: 88c7870b56fd1202
coverage: 0.83871
learned_at: 2026-11-14 02:25:19
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTeaCache, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, PreviewImage, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, VHS_VideoCombine, ImageResizeKJ, GrowMaskWithBlur, InpaintPreprocessor, ImageResizeKJ, LayerMask: SegmentAnythingUltra V2, VHS_VideoInfo, easy compare, JWInteger, JWInteger, easy ifElse, easy ifElse, JjkText, VHS_LoadVideo, Note, WanVideoDecode, LoadImage]
patterns: []
missing: []
---

# 平台全量/电商视频换产品(Wan2.1Vace视频遮罩重绘）_2011157655569567746.json

> 来源文件 `comfyui_library/workflows/平台全量/电商视频换产品(Wan2.1Vace视频遮罩重绘）_2011157655569567746.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（31 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `PreviewImage`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `GrowMaskWithBlur`
- `InpaintPreprocessor`
- `ImageResizeKJ`
- `LayerMask: SegmentAnythingUltra V2`
- `VHS_VideoInfo`
- `easy compare`
- `JWInteger`
- `JWInteger`
- `easy ifElse`
- `easy ifElse`
- `JjkText`
- `VHS_LoadVideo`
- `Note`
- `WanVideoDecode`
- `LoadImage`

## 知识

覆盖率 **84%**（26/31）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`ImageResizeKJ`、`GrowMaskWithBlur`、`InpaintPreprocessor`、`LayerMask: SegmentAnythingUltra V2`、`VHS_VideoInfo`、`easy compare`、`JWInteger`、`VHS_LoadVideo`、`WanVideoDecode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、ImageResizeKJ

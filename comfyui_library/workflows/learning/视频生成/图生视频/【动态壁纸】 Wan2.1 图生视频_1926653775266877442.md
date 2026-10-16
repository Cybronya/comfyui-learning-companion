---
key: 视频生成/图生视频/【动态壁纸】 Wan2.1 图生视频_1926653775266877442.json
name: 【动态壁纸】 Wan2.1 图生视频_1926653775266877442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1926653775266877442.json
hash: e3d3ffa04ea35522
coverage: 0.96
learned_at: 2026-10-15 22:29:53
nodes: [VHS_VideoCombine, WanVideoDecode, Int, MathExpression|pysssss, WanVideoModelLoader, LoadWanVideoT5TextEncoder, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, WanVideoImageClipEncode, WanVideoSampler, WanVideoTeaCache, WanVideoSLG, WanVideoEnhanceAVideo, LayerUtility: PurgeVRAM V2, DownloadAndLoadFlorence2Model, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoTorchCompileSettings, Florence2Run, StringFunction|pysssss, WanVideoTextEncode, LoadWanVideoClipTextEncoder, Bjornulf_ShowInt]
patterns: []
missing: []
---

# 视频生成/图生视频/【动态壁纸】 Wan2.1 图生视频_1926653775266877442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1926653775266877442.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（25 个）：
- `VHS_VideoCombine`
- `WanVideoDecode`
- `Int`
- `MathExpression|pysssss`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `LayerUtility: PurgeVRAM V2`
- `DownloadAndLoadFlorence2Model`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `Florence2Run`
- `StringFunction|pysssss`
- `WanVideoTextEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `Bjornulf_ShowInt`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`VHS_VideoCombine`、`WanVideoDecode`、`Int`、`MathExpression|pysssss`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadFlorence2Model`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`Florence2Run`、`StringFunction|pysssss`、`WanVideoTextEncode`、`LoadWanVideoClipTextEncoder`、`Bjornulf_ShowInt`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

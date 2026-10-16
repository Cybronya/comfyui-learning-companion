---
key: 视频生成/文生视频/Wan2.1 最新 FusionX 电商模特主播讲解产品视频 风格一致性_1943186431659425794.json
name: Wan2.1 最新 FusionX 电商模特主播讲解产品视频 风格一致性_1943186431659425794.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1943186431659425794.json
hash: 7f358a031cfe64e9
coverage: 1
learned_at: 2026-10-15 22:43:30
nodes: [WanVideoDecode, WanVideoTeaCache, WanVideoVAELoader, WanVideoBlockSwap, LoadImage, LoadImage, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoModelLoader, ImageResizeKJv2, LayerUtility: ImageMaskScaleAs, WanVideoEnhanceAVideo, WanVideoEncode, WanVideoEncode, WanVideoPhantomEmbeds, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1 最新 FusionX 电商模特主播讲解产品视频 风格一致性_1943186431659425794.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1943186431659425794.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（17 个）：
- `WanVideoDecode`
- `WanVideoTeaCache`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `LoadImage`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `LayerUtility: ImageMaskScaleAs`
- `WanVideoEnhanceAVideo`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LayerUtility: ImageMaskScaleAs`、`WanVideoEnhanceAVideo`、`WanVideoEncode`、`WanVideoPhantomEmbeds`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、ImageResizeKJv2

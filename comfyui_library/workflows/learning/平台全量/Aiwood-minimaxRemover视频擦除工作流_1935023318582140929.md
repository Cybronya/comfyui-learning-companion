---
key: 平台全量/Aiwood-minimaxRemover视频擦除工作流_1935023318582140929.json
name: Aiwood-minimaxRemover视频擦除工作流_1935023318582140929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Aiwood-minimaxRemover视频擦除工作流_1935023318582140929.json
hash: b88eb654f0d86706
coverage: 1
learned_at: 2026-11-14 00:17:35
nodes: [WanVideoDecode, WanVideoEncode, SolidMask, WanVideoEncode, ImageCompositeMasked, MaskToImage, DownloadAndLoadSAM2Model, ImageCompositeMasked, ImageResizeKJv2, GrowMaskWithBlur, WanVideoModelLoader, WanVideoVAELoader, Sam2Segmentation, WanVideoMiniMaxRemoverEmbeds, MaskToImage, WanVideoSampler, LoadWanVideoT5TextEncoder, MaskPreview+, WanVideoTextEncode, easy imageRemBg, PointsEditor, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Aiwood-minimaxRemover视频擦除工作流_1935023318582140929.json

> 来源文件 `comfyui_library/workflows/平台全量/Aiwood-minimaxRemover视频擦除工作流_1935023318582140929.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
- `WanVideoDecode`
- `WanVideoEncode`
- `SolidMask`
- `WanVideoEncode`
- `ImageCompositeMasked`
- `MaskToImage`
- `DownloadAndLoadSAM2Model`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `GrowMaskWithBlur`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `Sam2Segmentation`
- `WanVideoMiniMaxRemoverEmbeds`
- `MaskToImage`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `MaskPreview+`
- `WanVideoTextEncode`
- `easy imageRemBg`
- `PointsEditor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`WanVideoDecode`、`WanVideoEncode`、`SolidMask`、`ImageCompositeMasked`、`MaskToImage`、`DownloadAndLoadSAM2Model`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`WanVideoModelLoader`、`WanVideoVAELoader`、`Sam2Segmentation`、`WanVideoMiniMaxRemoverEmbeds`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`MaskPreview+`、`WanVideoTextEncode`、`easy imageRemBg`、`PointsEditor`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJv2、MaskPreview+

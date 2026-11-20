---
key: 平台全量/Qwen2.5VL+MinMax 水印_字幕消除_1949690862814023681.json
name: Qwen2.5VL+MinMax 水印_字幕消除_1949690862814023681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen2.5VL+MinMax 水印_字幕消除_1949690862814023681.json
hash: 4ae52a0ad71d36b2
coverage: 0.85
learned_at: 2026-11-14 00:52:25
nodes: [LoadImage, LayerMask: LoadSAM2Model, LoadWanVideoT5TextEncoder, WanVideoModelLoader, SolidMask, MaskToImage, WanVideoSampler, MaskListToMaskBatch, WanVideoTextEncode, MaskToImage, BBoxesToSAM2, QwenVLDetection, LayerMask: MaskPreview, PreviewImage, ImageListToBatch+, VHS_VideoCombine, VHS_VideoInfo, DownloadAndLoadQwenModel, Reroute, WanVideoDecode, ImageBatchToList+, LayerUtility: PurgeVRAM, ImageCompositeMasked, PreviewImage, WanVideoEncode, WanVideoEncode, WanVideoVAELoader, WanVideoMiniMaxRemoverEmbeds, VHS_VideoCombine, easy showAnything, ImageConcanate, GrowMaskWithBlur, LayerMask: SAM2UltraV2, VHS_VideoCombine, LayerMask: MaskPreview, VHS_LoadVideo, JjkText, Int, RHHiddenNodes, PreviewImage]
patterns: []
missing: []
---

# 平台全量/Qwen2.5VL+MinMax 水印_字幕消除_1949690862814023681.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen2.5VL+MinMax 水印_字幕消除_1949690862814023681.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `LoadImage`
- `LayerMask: LoadSAM2Model`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `SolidMask`
- `MaskToImage`
- `WanVideoSampler` ★核心
- `MaskListToMaskBatch`
- `WanVideoTextEncode`
- `MaskToImage`
- `BBoxesToSAM2`
- `QwenVLDetection`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `ImageListToBatch+`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `DownloadAndLoadQwenModel`
- `Reroute`
- `WanVideoDecode`
- `ImageBatchToList+`
- `LayerUtility: PurgeVRAM`
- `ImageCompositeMasked`
- `PreviewImage`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoMiniMaxRemoverEmbeds`
- `VHS_VideoCombine`
- `easy showAnything`
- `ImageConcanate`
- `GrowMaskWithBlur`
- `LayerMask: SAM2UltraV2`
- `VHS_VideoCombine`
- `LayerMask: MaskPreview`
- `VHS_LoadVideo`
- `JjkText`
- `Int`
- `RHHiddenNodes`
- `PreviewImage`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`LoadImage`、`LayerMask: LoadSAM2Model`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`SolidMask`、`MaskToImage`、`WanVideoSampler`、`MaskListToMaskBatch`、`WanVideoTextEncode`、`BBoxesToSAM2`、`QwenVLDetection`、`LayerMask: MaskPreview`、`ImageListToBatch+`、`VHS_VideoCombine`、`VHS_VideoInfo`、`DownloadAndLoadQwenModel`、`WanVideoDecode`、`ImageBatchToList+`、`LayerUtility: PurgeVRAM`、`ImageCompositeMasked`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoMiniMaxRemoverEmbeds`、`ImageConcanate`、`GrowMaskWithBlur`、`LayerMask: SAM2UltraV2`、`VHS_LoadVideo`、`Int`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、LayerMask: MaskPreview

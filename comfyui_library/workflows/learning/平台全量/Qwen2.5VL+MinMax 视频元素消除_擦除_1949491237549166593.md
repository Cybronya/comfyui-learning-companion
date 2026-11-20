---
key: 平台全量/Qwen2.5VL+MinMax 视频元素消除_擦除_1949491237549166593.json
name: Qwen2.5VL+MinMax 视频元素消除_擦除_1949491237549166593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen2.5VL+MinMax 视频元素消除_擦除_1949491237549166593.json
hash: c7d0c4e414d864b6
coverage: 0.837838
learned_at: 2026-11-14 00:52:26
nodes: [LoadImage, LayerMask: LoadSAM2Model, LoadWanVideoT5TextEncoder, WanVideoModelLoader, SolidMask, MaskToImage, WanVideoSampler, LayerMask: SAM2UltraV2, MaskListToMaskBatch, WanVideoTextEncode, MaskToImage, BBoxesToSAM2, QwenVLDetection, LayerMask: MaskPreview, PreviewImage, ImageListToBatch+, VHS_VideoCombine, VHS_VideoInfo, DownloadAndLoadQwenModel, Reroute, WanVideoDecode, VHS_VideoCombine, ImageBatchToList+, LayerUtility: PurgeVRAM, GrowMaskWithBlur, ImageCompositeMasked, PreviewImage, WanVideoEncode, WanVideoEncode, WanVideoVAELoader, WanVideoMiniMaxRemoverEmbeds, VHS_VideoCombine, ImageConcanate, PreviewImage, easy showAnything, VHS_LoadVideo, JjkText]
patterns: []
missing: []
---

# 平台全量/Qwen2.5VL+MinMax 视频元素消除_擦除_1949491237549166593.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen2.5VL+MinMax 视频元素消除_擦除_1949491237549166593.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `LoadImage`
- `LayerMask: LoadSAM2Model`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `SolidMask`
- `MaskToImage`
- `WanVideoSampler` ★核心
- `LayerMask: SAM2UltraV2`
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
- `VHS_VideoCombine`
- `ImageBatchToList+`
- `LayerUtility: PurgeVRAM`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `PreviewImage`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `WanVideoMiniMaxRemoverEmbeds`
- `VHS_VideoCombine`
- `ImageConcanate`
- `PreviewImage`
- `easy showAnything`
- `VHS_LoadVideo`
- `JjkText`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`LoadImage`、`LayerMask: LoadSAM2Model`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`SolidMask`、`MaskToImage`、`WanVideoSampler`、`LayerMask: SAM2UltraV2`、`MaskListToMaskBatch`、`WanVideoTextEncode`、`BBoxesToSAM2`、`QwenVLDetection`、`LayerMask: MaskPreview`、`ImageListToBatch+`、`VHS_VideoCombine`、`VHS_VideoInfo`、`DownloadAndLoadQwenModel`、`WanVideoDecode`、`ImageBatchToList+`、`LayerUtility: PurgeVRAM`、`GrowMaskWithBlur`、`ImageCompositeMasked`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoMiniMaxRemoverEmbeds`、`ImageConcanate`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、LayerMask: MaskPreview

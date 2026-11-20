---
key: 平台全量/MinimaxRemover+Qwen 2.5万物视频消除工作流V1_1935379256069521409.json
name: MinimaxRemover+Qwen 2.5万物视频消除工作流V1_1935379256069521409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MinimaxRemover+Qwen 2.5万物视频消除工作流V1_1935379256069521409.json
hash: 85643def7ef064bd
coverage: 0.857143
learned_at: 2026-11-14 00:46:12
nodes: [WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, BBoxesToSAM2, LayerUtility: PurgeVRAM, WanVideoSampler, LayerMask: LoadSAM2Model, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, Note, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, ImageBatchToList+, GrowMaskWithBlur, LayerMask: SAM2UltraV2, ImageListToBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VHS_VideoInfo, WanVideoMiniMaxRemoverEmbeds, MaskListToMaskBatch, VHS_LoadVideo, WanVideoTextEncode, Note, MaskToImage, WanVideoEncode, WanVideoEncode, preview_mask, PreviewImage, PreviewImage, PreviewImage, CR Prompt Text, PreviewImage, MaskToImage, ImageCompositeMasked, SolidMask, ImageConcanate, QwenVLDetection, DownloadAndLoadQwenModel, CR Prompt Text]
patterns: []
missing: []
---

# 平台全量/MinimaxRemover+Qwen 2.5万物视频消除工作流V1_1935379256069521409.json

> 来源文件 `comfyui_library/workflows/平台全量/MinimaxRemover+Qwen 2.5万物视频消除工作流V1_1935379256069521409.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `BBoxesToSAM2`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `LayerMask: LoadSAM2Model`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `Note`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageBatchToList+`
- `GrowMaskWithBlur`
- `LayerMask: SAM2UltraV2`
- `ImageListToBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VHS_VideoInfo`
- `WanVideoMiniMaxRemoverEmbeds`
- `MaskListToMaskBatch`
- `VHS_LoadVideo`
- `WanVideoTextEncode`
- `Note`
- `MaskToImage`
- `WanVideoEncode`
- `WanVideoEncode`
- `preview_mask`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `CR Prompt Text`
- `PreviewImage`
- `MaskToImage`
- `ImageCompositeMasked`
- `SolidMask`
- `ImageConcanate`
- `QwenVLDetection`
- `DownloadAndLoadQwenModel`
- `CR Prompt Text`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`BBoxesToSAM2`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`LayerMask: LoadSAM2Model`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageBatchToList+`、`GrowMaskWithBlur`、`LayerMask: SAM2UltraV2`、`ImageListToBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`VHS_VideoInfo`、`WanVideoMiniMaxRemoverEmbeds`、`MaskListToMaskBatch`、`VHS_LoadVideo`、`WanVideoTextEncode`、`MaskToImage`、`WanVideoEncode`、`preview_mask`、`CR Prompt Text`、`ImageCompositeMasked`、`SolidMask`、`ImageConcanate`、`QwenVLDetection`、`DownloadAndLoadQwenModel`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、CR Prompt Text、preview_mask

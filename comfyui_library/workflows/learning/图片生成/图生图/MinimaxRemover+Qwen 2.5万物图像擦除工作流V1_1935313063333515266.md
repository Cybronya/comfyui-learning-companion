---
key: 图片生成/图生图/MinimaxRemover+Qwen 2.5万物图像擦除工作流V1_1935313063333515266.json
name: MinimaxRemover+Qwen 2.5万物图像擦除工作流V1_1935313063333515266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/MinimaxRemover+Qwen 2.5万物图像擦除工作流V1_1935313063333515266.json
hash: 249174151f7c070d
coverage: 0.85
learned_at: 2026-10-23 11:09:36
nodes: [WanVideoModelLoader, WanVideoVAELoader, DownloadAndLoadQwenModel, ImageBatchToList+, WanVideoTextEncode, LoadWanVideoT5TextEncoder, BBoxesToSAM2, LayerUtility: PurgeVRAM, WanVideoSampler, LayerMask: LoadSAM2Model, LayerUtility: PurgeVRAM V2, QwenVLDetection, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, PreviewImage, WanVideoMiniMaxRemoverEmbeds, preview_mask, LayerMask: SAM2UltraV2, PreviewImage, ImageListToBatch+, WanVideoEncode, GrowMaskWithBlur, WanVideoEncode, MaskToImage, ImageCompositeMasked, PreviewImage, PreviewImage, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, WanVideoDecode, SaveImage, ImageConcanate, SaveImage, LoadImage, JWInteger, Note, Note, CR Prompt Text, SolidMask]
patterns: []
missing: []
---

# 图片生成/图生图/MinimaxRemover+Qwen 2.5万物图像擦除工作流V1_1935313063333515266.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/MinimaxRemover+Qwen 2.5万物图像擦除工作流V1_1935313063333515266.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `DownloadAndLoadQwenModel`
- `ImageBatchToList+`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `BBoxesToSAM2`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `LayerMask: LoadSAM2Model`
- `LayerUtility: PurgeVRAM V2`
- `QwenVLDetection`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `WanVideoMiniMaxRemoverEmbeds`
- `preview_mask`
- `LayerMask: SAM2UltraV2`
- `PreviewImage`
- `ImageListToBatch+`
- `WanVideoEncode`
- `GrowMaskWithBlur`
- `WanVideoEncode`
- `MaskToImage`
- `ImageCompositeMasked`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `WanVideoDecode`
- `SaveImage`
- `ImageConcanate`
- `SaveImage`
- `LoadImage`
- `JWInteger`
- `Note`
- `Note`
- `CR Prompt Text`
- `SolidMask`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`WanVideoModelLoader`、`WanVideoVAELoader`、`DownloadAndLoadQwenModel`、`ImageBatchToList+`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`BBoxesToSAM2`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`LayerMask: LoadSAM2Model`、`LayerUtility: PurgeVRAM V2`、`QwenVLDetection`、`WanVideoMiniMaxRemoverEmbeds`、`preview_mask`、`LayerMask: SAM2UltraV2`、`ImageListToBatch+`、`WanVideoEncode`、`GrowMaskWithBlur`、`MaskToImage`、`ImageCompositeMasked`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`WanVideoDecode`、`ImageConcanate`、`LoadImage`、`JWInteger`、`CR Prompt Text`、`SolidMask`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、CR Prompt Text

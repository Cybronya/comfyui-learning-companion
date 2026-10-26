---
key: 图片生成/反推提示词/动态水印 去除 Seedance 2.0 豆包 即梦 小云雀_2024292706696044545.json
name: 动态水印 去除 Seedance 2.0 豆包 即梦 小云雀_2024292706696044545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/动态水印 去除 Seedance 2.0 豆包 即梦 小云雀_2024292706696044545.json
hash: 4b1a551d36ea5bfa
coverage: 1
learned_at: 2026-10-26 01:47:25
nodes: [LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, WanVideoSampler, WanVideoMiniMaxRemoverEmbeds, WanVideoEncode, WanVideoEncode, ImageCompositeMasked, MaskToImage, easy imageBatchToImageList, MaskToImage, GrowMaskWithBlur, SolidMask, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, UltralyticsDetectorProvider, VHS_VideoCombine, LayerUtility: ColorImage V2, BboxDetectorCombined_v2, MaskListToMaskBatch, ImageCompositeMasked, VHS_VideoInfo, WanVideoModelLoader, WanVideoVAELoader, WanVideoTextEncodeCached, VHS_LoadVideo]
patterns: []
missing: []
---

# 图片生成/反推提示词/动态水印 去除 Seedance 2.0 豆包 即梦 小云雀_2024292706696044545.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/动态水印 去除 Seedance 2.0 豆包 即梦 小云雀_2024292706696044545.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoEncode`
- `WanVideoEncode`
- `ImageCompositeMasked`
- `MaskToImage`
- `easy imageBatchToImageList`
- `MaskToImage`
- `GrowMaskWithBlur`
- `SolidMask`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `UltralyticsDetectorProvider`
- `VHS_VideoCombine`
- `LayerUtility: ColorImage V2`
- `BboxDetectorCombined_v2`
- `MaskListToMaskBatch`
- `ImageCompositeMasked`
- `VHS_VideoInfo`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoMiniMaxRemoverEmbeds`、`WanVideoEncode`、`ImageCompositeMasked`、`MaskToImage`、`easy imageBatchToImageList`、`GrowMaskWithBlur`、`SolidMask`、`ImageConcatMulti`、`VHS_VideoCombine`、`UltralyticsDetectorProvider`、`LayerUtility: ColorImage V2`、`BboxDetectorCombined_v2`、`MaskListToMaskBatch`、`VHS_VideoInfo`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ImageConcatMulti、UltralyticsDetectorProvider、VHS_LoadVideo

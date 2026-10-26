---
key: 数字人/数字人/Seedance 2.0 豆包 即梦 小云雀 动态水印 去除 无痕版_2026659905779802114.json
name: Seedance 2.0 豆包 即梦 小云雀 动态水印 去除 无痕版_2026659905779802114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Seedance 2.0 豆包 即梦 小云雀 动态水印 去除 无痕版_2026659905779802114.json
hash: 2f2fb8eddd5b5f00
coverage: 1
learned_at: 2026-10-26 01:57:23
nodes: [WanVideoDecode, WanVideoSampler, WanVideoMiniMaxRemoverEmbeds, WanVideoEncode, WanVideoEncode, ImageCompositeMasked, MaskToImage, MaskToImage, SolidMask, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoInfo, WanVideoModelLoader, WanVideoVAELoader, WanVideoTextEncodeCached, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, UltralyticsDetectorProvider, LayerUtility: ColorImage V2, easy imageBatchToImageList, BboxDetectorCombined_v2, ImageCompositeMasked, GrowMaskWithBlur]
patterns: []
missing: []
---

# 数字人/数字人/Seedance 2.0 豆包 即梦 小云雀 动态水印 去除 无痕版_2026659905779802114.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Seedance 2.0 豆包 即梦 小云雀 动态水印 去除 无痕版_2026659905779802114.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（25 个）：
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoEncode`
- `WanVideoEncode`
- `ImageCompositeMasked`
- `MaskToImage`
- `MaskToImage`
- `SolidMask`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `UltralyticsDetectorProvider`
- `LayerUtility: ColorImage V2`
- `easy imageBatchToImageList`
- `BboxDetectorCombined_v2`
- `ImageCompositeMasked`
- `GrowMaskWithBlur`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`WanVideoDecode`、`WanVideoSampler`、`WanVideoMiniMaxRemoverEmbeds`、`WanVideoEncode`、`ImageCompositeMasked`、`MaskToImage`、`SolidMask`、`ImageConcatMulti`、`VHS_VideoCombine`、`VHS_VideoInfo`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`UltralyticsDetectorProvider`、`LayerUtility: ColorImage V2`、`easy imageBatchToImageList`、`BboxDetectorCombined_v2`、`GrowMaskWithBlur`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoEncode、ImageConcatMulti、UltralyticsDetectorProvider、VHS_LoadVideo

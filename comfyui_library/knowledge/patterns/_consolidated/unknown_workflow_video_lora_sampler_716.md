---
name: unknown_workflow_video_lora_sampler_716
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.909
common_nodes: [CR Prompt Text, Float, INTConstant, ImageCompositeMasked, ImageConcatMulti, ImageRemoveBackground+, InvertMask, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskPreview, MaskToImage, PreviewImage, SolidMask, StringToFloatList, TransparentBGSession+, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Fun Vace视频主体参考替换_1967228508000935938.json, 视频生成/图生视频/Wan2.2 Fun Vace视频蒙版重绘V1_1966519907141791746.json, 视频生成/图生视频/Wan2.2 Fun Vace魔改版高质量视频主体参考替换V1_1966548561380978690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_716

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Fun Vace视频主体参考替换_1967228508000935938.json、视频生成/图生视频/Wan2.2 Fun Vace视频蒙版重绘V1_1966519907141791746.json、视频生成/图生视频/Wan2.2 Fun Vace魔改版高质量视频主体参考替换V1_1966548561380978690.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `Float`
- `INTConstant`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageRemoveBackground+`
- `InvertMask`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview`
- `MaskToImage`
- `PreviewImage`
- `SolidMask`
- `StringToFloatList`
- `TransparentBGSession+`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `PDIMAGE_LongerSize` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

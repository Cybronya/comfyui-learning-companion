---
name: unknown_workflow_video_lora_sampler_489
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.909167
common_nodes: [CR Prompt Text, Float, INTConstant, ImageCompositeMasked, InvertMask, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskPreview, MaskToImage, PreviewImage, SolidMask, StringToFloatList, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Video Subject Inpaint影片主體重繪 (WAN2.2 KJversion+Fun)_2087364991761608706.json, 平台全量/Wan2.2-Vace-主体替换_1983807545255075841.json, 平台全量/Wan2.2-Vace-局部编辑_1983813532632424449.json, 视频生成/图生视频/Wan2.2 Fun Vace视频主体参考替换_1967228508000935938.json, 视频生成/图生视频/Wan2.2 Fun Vace视频蒙版重绘V1_1966519907141791746.json, 视频生成/图生视频/Wan2.2 Fun Vace魔改版高质量视频主体参考替换V1_1966548561380978690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_489

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Video Subject Inpaint影片主體重繪 (WAN2.2 KJversion+Fun)_2087364991761608706.json、平台全量/Wan2.2-Vace-主体替换_1983807545255075841.json、平台全量/Wan2.2-Vace-局部编辑_1983813532632424449.json、视频生成/图生视频/Wan2.2 Fun Vace视频主体参考替换_1967228508000935938.json、视频生成/图生视频/Wan2.2 Fun Vace视频蒙版重绘V1_1966519907141791746.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CR Prompt Text`
- `Float`
- `INTConstant`
- `ImageCompositeMasked`
- `InvertMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview`
- `MaskToImage`
- `PreviewImage`
- `SolidMask`
- `StringToFloatList`
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
- `ImageConcatMulti` —— 5/6 个有
- `ImageRemoveBackground+` —— 5/6 个有
- `JWInteger` —— 5/6 个有
- `TransparentBGSession+` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `PDIMAGE_LongerSize` —— 3/6 个有
- `RH_Captioner` —— 3/6 个有
- `VHS_VideoInfo` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `GetImageSizeAndCount` —— 2/6 个有
- `BiRefNetRMBG` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SaveImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

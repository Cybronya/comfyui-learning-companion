---
name: unknown_workflow_video_lora_sampler_507
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95475
common_nodes: [CR Prompt Text, Float, INTConstant, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, StringToFloatList, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版动作迁移V1_1966542129269026818.json, 视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版首尾帧V1_1966523015905357825.json, 视频生成/图生视频/Wan2.2 Fun Vace视频扩图稳定版V1_1966560072405037057.json, 视频生成/图生视频/🦖Wan 2.2动作迁移（优化板）_1968976369134755842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_507

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版动作迁移V1_1966542129269026818.json、视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版首尾帧V1_1966523015905357825.json、视频生成/图生视频/Wan2.2 Fun Vace视频扩图稳定版V1_1966560072405037057.json、视频生成/图生视频/🦖Wan 2.2动作迁移（优化板）_1968976369134755842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Prompt Text`
- `Float`
- `INTConstant`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `StringToFloatList`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
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
- `ColorMatch` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `WanVideoVACEModelSelect` —— 3/4 个有
- `DWPreprocessor` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `ImageAndMaskPreview` —— 1/4 个有
- `ImagePadKJ` —— 1/4 个有
- `ImageResize` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `WanVideoExtraModelSelect` —— 1/4 个有
- `WanVideoVACEStartToEndFrame` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

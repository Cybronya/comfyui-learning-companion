---
name: unknown_workflow_video_upscale_lora_36
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.797
common_nodes: [Any Switch (rgthree), CreateCFGScheduleFloatList, Display Int (rgthree), Fast Groups Muter (rgthree), Fast Muter (rgthree), Float, Get resolution [Crystools], GetImageRangeFromBatch, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageAndMaskPreview, ImageConcatMulti, ImagePadKJ, ImageUpscaleWithModelBatched, ImpactInt, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskPreview+, MathExpression|pysssss, Mute / Bypass Repeater (rgthree), PreviewAny, PreviewImage, PrimitiveStringMultiline, RH_LLMAPI_NODE, RIFE VFI, Seed (rgthree), ShowText|pysssss, Upscale Model Loader, VHS_LoadVideo, VHS_SplitImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader, easy compare, easy ifElse, easy imageCount]
problems: []
missing: []
members: [平台全量/视频扩展（视频扩图）_2027033849053581314.json, 平台全量/视频扩展（视频扩图， 修改视频尺寸，横竖屏转换）_2043877815845658625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频扩展（视频扩图）_2027033849053581314.json、平台全量/视频扩展（视频扩图， 修改视频尺寸，横竖屏转换）_2043877815845658625.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CreateCFGScheduleFloatList`
- `Display Int (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Muter (rgthree)`
- `Float`
- `Get resolution [Crystools]`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageAndMaskPreview`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageUpscaleWithModelBatched`
- `ImpactInt`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview+`
- `MathExpression|pysssss`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RIFE VFI`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `Upscale Model Loader`
- `VHS_LoadVideo`
- `VHS_SplitImages`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy compare`
- `easy ifElse`
- `easy imageCount`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

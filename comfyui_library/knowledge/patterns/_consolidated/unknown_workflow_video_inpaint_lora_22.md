---
name: unknown_workflow_video_inpaint_lora_22
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.743
common_nodes: [GetImageSize+, GetImageSizeAndCount, GetNode, GrowMask, INPAINT_MaskedFill, ImageResize+, ImageResizeKJ, ImpactImageBatchToImageList, LoadImage, LoadWanVideoT5TextEncoder, MaskListToMaskBatch, Mask_image2mask, ResizeMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [平台全量/视频-局部替换修改（开关版）_1959964157468684289.json, 平台全量/视频P图，视频服装，人物替换_1955090336692387841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频-局部替换修改（开关版）_1959964157468684289.json、平台全量/视频P图，视频服装，人物替换_1955090336692387841.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INPAINT_MaskedFill`
- `ImageResize+`
- `ImageResizeKJ`
- `ImpactImageBatchToImageList`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskListToMaskBatch`
- `Mask_image2mask`
- `ResizeMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `Mute / Bypass Relay (rgthree)` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

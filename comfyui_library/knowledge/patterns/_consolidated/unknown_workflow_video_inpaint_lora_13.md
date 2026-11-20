---
name: unknown_workflow_video_inpaint_lora_13
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.536
common_nodes: [Any Switch (rgthree), ApplyFaceProcessor, ClothesSegment, DWPreprocessor, FaceProcessorLoader, Fast Groups Muter (rgthree), GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INPAINT_MaskedFill, Image Comparer (rgthree), ImageCompositeMasked, ImageResizeKJv2, ImageToMask, LayerUtility: CropByMask V2, LoadImage, LoadWanVideoT5TextEncoder, Mask Fill Holes, MaskToImage, MediaPipe-FaceMeshPreprocessor, PreviewAny, PreviewImage, PrimitiveInt, PrimitiveStringMultiline, RMBG, RepeatImageBatch, SaveImage, SetNode, StringLength, ToBinaryMask, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy cleanGpuUsed, easy compare, easy ifElse, easy int, easy isMaskEmpty, easy seed]
problems: []
missing: []
members: [图片生成/图生图/人物替换-图片编辑V1（支持多人，蒙版圈中角色替换）_2004118122019864578.json, 图片生成/图生图/人物替换-图片编辑V1（支持多人，蒙版圈中角色替换）_2026570441309032450.json, 图片生成/文生图/人物替换-图片编辑V1（偏参考图，不会改变风格）_1965710290023284737.json, 平台全量/人物替换【视频首帧】角色迁移图片编辑版Wan2.1 T2V-14B图生视频_2004220950633738241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_lora_13

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人物替换-图片编辑V1（支持多人，蒙版圈中角色替换）_2004118122019864578.json、图片生成/图生图/人物替换-图片编辑V1（支持多人，蒙版圈中角色替换）_2026570441309032450.json、图片生成/文生图/人物替换-图片编辑V1（偏参考图，不会改变风格）_1965710290023284737.json、平台全量/人物替换【视频首帧】角色迁移图片编辑版Wan2.1 T2V-14B图生视频_2004220950633738241.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `ApplyFaceProcessor`
- `ClothesSegment`
- `DWPreprocessor`
- `FaceProcessorLoader`
- `Fast Groups Muter (rgthree)`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INPAINT_MaskedFill`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `ImageToMask`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Mask Fill Holes`
- `MaskToImage`
- `MediaPipe-FaceMeshPreprocessor`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RMBG`
- `RepeatImageBatch`
- `SaveImage`
- `SetNode`
- `StringLength`
- `ToBinaryMask`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy isMaskEmpty`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `Mute / Bypass Relay (rgthree)` —— 3/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/4 个有
- `PrimitiveString` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `StringConcatenate` —— 3/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `Bookmark (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `Qwen2.5VL` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

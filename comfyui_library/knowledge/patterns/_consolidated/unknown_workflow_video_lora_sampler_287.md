---
name: unknown_workflow_video_lora_sampler_287
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.525857
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, EmptyImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetNode, ImageCompositeMasked, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PreviewImage, PrimitiveInt, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [图片生成/图生图/动作迁移2_2092576578264977410.json, 视频生成/图生视频/CG迷-Scail2超强角色替换工作流_2070766031924191234.json, 视频生成/图生视频/SCAIL2_人物转绘替换_打光_2079863299176484866.json, 视频生成/图生视频/Wan 视频编辑-Scail2 V1-支持长视频_2086402055798870018.json, 视频生成/图生视频/Wan 视频编辑-Scail2 V1-支持长视频！—转载阿硕_2092973975054934018.json, 视频生成/图生视频/练习舞蹈工作流_2081699626717114369.json, 视频生成/文生视频/Wan 视频编辑-Scail2 V1-支持长视频_2095009418013405186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_287

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/动作迁移2_2092576578264977410.json、视频生成/图生视频/CG迷-Scail2超强角色替换工作流_2070766031924191234.json、视频生成/图生视频/SCAIL2_人物转绘替换_打光_2079863299176484866.json、视频生成/图生视频/Wan 视频编辑-Scail2 V1-支持长视频_2086402055798870018.json、视频生成/图生视频/Wan 视频编辑-Scail2 V1-支持长视频！—转载阿硕_2092973975054934018.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyImage`
- `GIMMVFI_interpolate`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveInt`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `TensorLoopClose`
- `TensorLoopOpen`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoInfo` —— 6/7 个有
- `Bookmark (rgthree)` —— 5/7 个有
- `GetImageSizeAndCount` —— 5/7 个有
- `LayerUtility: CropByMask V2` —— 5/7 个有
- `Mask Fill Holes` —— 5/7 个有
- `PlaySound|pysssss` —— 5/7 个有
- `PrimitiveBoolean` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `Switch any [Crystools]` —— 5/7 个有
- `ToBinaryMask` —— 5/7 个有
- `easy ifElse` —— 5/7 个有
- `easy int` —— 5/7 个有
- `easy isMaskEmpty` —— 5/7 个有
- `Label (rgthree)` —— 3/7 个有
- `GetImageSize` —— 2/7 个有
- `ResizeImageMaskNode` —— 2/7 个有
- `Int` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/7 个有
- `ShowAnything|Mie` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

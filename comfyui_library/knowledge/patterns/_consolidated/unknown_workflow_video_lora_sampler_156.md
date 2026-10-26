---
name: unknown_workflow_video_lora_sampler_156
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.491833
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageRangeFromBatch, GetNode, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PrimitiveInt, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [图片生成/图生图/动作迁移2_2092576578264977410.json, 数字人/数字人/Scail2循环动作迁移（爱屋流）_2066466150837473282.json, 数字人/数字人/Scail2视频动作迁移-KJ流-自动循环_2067926791343403009.json, 数字人/数字人/Scail2视频角色替换-KJ流-自动循环_2067782830385618946.json, 数字人/数字人/Wan Scail2 无限时长视频外循环角色替换动作迁移_2074324688473518081.json, 数字人/数字人/动作运镜最强迁移 角色替换-视频换人换角色 动作迁移 指定人替换-电商带货_2068881167440498690.json, 视频生成/图生视频/CG迷-Scail2超强角色替换工作流_2070766031924191234.json, 视频生成/图生视频/SCAIL2_人物转绘替换_打光_2079863299176484866.json, 视频生成/图生视频/Wan 视频编辑-Scail2 V1-支持长视频_2086402055798870018.json, 视频生成/图生视频/Wan 视频编辑-Scail2 V1-支持长视频！—转载阿硕_2092973975054934018.json, 视频生成/图生视频/练习舞蹈工作流_2081699626717114369.json, 视频生成/文生视频/Wan 视频编辑-Scail2 V1-支持长视频_2095009418013405186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_156

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/动作迁移2_2092576578264977410.json、数字人/数字人/Scail2循环动作迁移（爱屋流）_2066466150837473282.json、数字人/数字人/Scail2视频动作迁移-KJ流-自动循环_2067926791343403009.json、数字人/数字人/Scail2视频角色替换-KJ流-自动循环_2067782830385618946.json、数字人/数字人/Wan Scail2 无限时长视频外循环角色替换动作迁移_2074324688473518081.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 12 个 workflow 都包含：
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
- `GIMMVFI_interpolate`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PrimitiveInt`
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
- `EmptyImage` —— 11/12 个有
- `ImageCompositeMasked` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `SAM3_TrackToMask` —— 11/12 个有
- `VHS_VideoInfo` —— 8/12 个有
- `GetImageSize` —— 6/12 个有
- `GetImageSizeAndCount` —— 6/12 个有
- `LayerUtility: CropByMask V2` —— 6/12 个有
- `Mask Fill Holes` —— 6/12 个有
- `PlaySound|pysssss` —— 6/12 个有
- `PrimitiveBoolean` —— 6/12 个有
- `PrimitiveStringMultiline` —— 6/12 个有
- `ResizeImageMaskNode` —— 6/12 个有
- `Switch any [Crystools]` —— 6/12 个有
- `ToBinaryMask` —— 6/12 个有
- `easy ifElse` —— 6/12 个有
- `easy int` —— 6/12 个有
- `easy isMaskEmpty` —— 6/12 个有
- `Bookmark (rgthree)` —— 5/12 个有
- `Label (rgthree)` —— 3/12 个有
- `Int` —— 2/12 个有
- `JjkText` —— 2/12 个有
- `ShowAnything|Mie` —— 2/12 个有
- `ImageStitch` —— 1/12 个有
- `Note Plus (mtb)` —— 1/12 个有
- `PrimitiveFloat` —— 1/12 个有
- `RH_LLMAPI_NODE` —— 1/12 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/12 个有
- `RH_Translator` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `Text` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

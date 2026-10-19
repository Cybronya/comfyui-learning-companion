---
name: unknown_workflow_video_lora_sampler_104
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.5045
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, EmptyImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetNode, ImageCompositeMasked, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: [Bookmark (rgthree), LayerUtility: CropByMask V2, Mask Fill Holes, PlaySound|pysssss, Switch any [Crystools], easy int, easy isMaskEmpty]
members: [图片生成/图生图/2092576578264977410.json, 数字人/数字人/多人 动作迁移 Scail2循环 长视频 插帧_2097249659348672514.json, 数字人/数字人/数字人舞蹈动作+服装展示Scail2循环动作迁移 超长视频 人物角色替换 动作迁移 高清长视频_2100056881053126657.json, 数字人/数字人/数字人舞蹈动作Scail2循环动作迁移 超长视频 人物角色替换 动作迁移 高清长视频_2100047823772409858.json, 视频生成/图生视频/2070766031924191234.json, 视频生成/图生视频/Scail-2.5_2094612201767268354.json, 视频生成/图生视频/Scail2 人物角色替换 超长视频  动作迁移 循环动作迁移 高清长视频_2082827837156970498.json, 视频生成/图生视频/2077364440512688130.json, 视频生成/图生视频/Wan 视频编辑-Scail2 V1-支持长视频_2086402055798870018.json, 视频生成/图生视频/Wan 视频编辑-Scail2 V1-支持长视频！—转载阿硕_2092973975054934018.json, 视频生成/图生视频/2074789088183537665.json, 视频生成/图生视频/2081699626717114369.json, 视频生成/图生视频/长视频循环Scail-2最终完成版_2093359415452852225.json, 视频生成/文生视频/Wan 视频编辑-Scail2 V1-支持长视频_2095009418013405186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_104

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/2092576578264977410.json、数字人/数字人/多人 动作迁移 Scail2循环 长视频 插帧_2097249659348672514.json、数字人/数字人/数字人舞蹈动作+服装展示Scail2循环动作迁移 超长视频 人物角色替换 动作迁移 高清长视频_2100056881053126657.json、数字人/数字人/数字人舞蹈动作Scail2循环动作迁移 超长视频 人物角色替换 动作迁移 高清长视频_2100047823772409858.json、视频生成/图生视频/2070766031924191234.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `DiffusionModelLoaderKJ`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyImage`
- `GIMMVFI_interpolate`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 13/14 个有
- `ComfyMathExpression` —— 12/14 个有
- `ImageConcatMulti` —— 12/14 个有
- `PreviewAny` —— 12/14 个有
- `TensorLoopClose` —— 12/14 个有
- `TensorLoopOpen` —— 12/14 个有
- `GetImageSize` —— 9/14 个有
- `Bjornulf_ShowInt` —— 7/14 个有
- `CR Text` —— 7/14 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 7/14 个有
- `MathExpression|pysssss` —— 7/14 个有
- `ResizeImageMaskNode` —— 7/14 个有
- `Bookmark (rgthree)` —— 5/14 个有
- `GetImageSizeAndCount` —— 5/14 个有
- `ImageStitch` —— 5/14 个有
- `LayerUtility: CropByMask V2` —— 5/14 个有
- `Mask Fill Holes` —— 5/14 个有
- `PlaySound|pysssss` —— 5/14 个有
- `PrimitiveBoolean` —— 5/14 个有
- `PrimitiveStringMultiline` —— 5/14 个有
- `Switch any [Crystools]` —— 5/14 个有
- `ToBinaryMask` —— 5/14 个有
- `VHS_VideoInfo` —— 5/14 个有
- `easy ifElse` —— 5/14 个有
- `easy int` —— 5/14 个有
- `easy isMaskEmpty` —— 5/14 个有
- `Label (rgthree)` —— 3/14 个有
- `AutoCropFaces` —— 2/14 个有
- `easy forLoopEnd` —— 2/14 个有
- `easy forLoopStart` —— 2/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `PrimitiveFloat` —— 1/14 个有
- `Wav2Lip` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Bookmark (rgthree)、LayerUtility: CropByMask V2、Mask Fill Holes、PlaySound|pysssss、Switch any [Crystools]

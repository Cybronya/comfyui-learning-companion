---
name: unknown_workflow_video_lora_sampler_43
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.459
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, EmptyImage, GetImageRangeFromBatch, ImageCompositeMasked, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, ResizeImageMaskNode, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [图片生成/图生图/10秒直出scail2动作迁移_2065436546555277314.json, 图片生成/图生图/Scail2动作模仿 循环长视频版_2086769009139208194.json, 图片生成/图生图/Scail2动作迁移 循环长视频版_2068484521166725122.json, 图片生成/图生图/Scail2动作迁移无限时长_2098341241476964354.json, 图片生成/图生图/Scail2角色替换 循环长视频版 天运子_2080732152978829313.json, 图片生成/图生图/动作迁移Extremely Long Videos + Character Replacement_2092790825444012034.json, 图片生成/图生图/动作迁移双人跳舞之两单人图片版_SCAIL2_2072659617250893826.json, 图片生成/图生图/高配2k_迁移无阉割纯血统_长续航版_2100562120453742593.json, 数字人/数字人/动作迁移  wan scail2_2081659467623657473.json, 数字人/数字人/多人 动作迁移 Scail2循环 长视频 插帧_2097249659348672514.json, 数字人/数字人/数字人舞蹈动作+服装展示Scail2循环动作迁移 超长视频 人物角色替换 动作迁移 高清长视频_2100056881053126657.json, 数字人/数字人/数字人舞蹈动作Scail2循环动作迁移 超长视频 人物角色替换 动作迁移 高清长视频_2100047823772409858.json, 数字人/数字人/（高质量循环版）Scail2多人角色替换V1_2065296848927150081.json, 视频生成/图生视频/HLL-Scail2动作迁移_2070484357101473794.json, 视频生成/图生视频/Scail2动作迁移 单人跳舞 双人跳舞循环长视频版_2077721960137707521.json, 视频生成/图生视频/Scail2动作迁移 单人跳舞 双人跳舞循环长视频版_2077728210632134658.json, 视频生成/图生视频/Scail2动作迁移 循环长视频版 （天运子)_2071186712600072193.json, 视频生成/图生视频/Scail2动作迁移 循环长视频版_2068526463132979202.json, 视频生成/图生视频/Scail2动作迁移 循环长视频版_2068583873969217538.json, 视频生成/图生视频/Scail2动作迁移 循环长视频版_2069607269846839298.json, 视频生成/图生视频/Scail2角色替换 循环长视频版_2069261444784418817.json, 视频生成/图生视频/scail2大模型sam抠人像动作迁移长视频动作迁移舞蹈复刻性感网红扭臀复刻动作复制快速版_2092834091065503746.json, 视频生成/图生视频/虚拟IP打造专用工作流_2087539753280434177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/10秒直出scail2动作迁移_2065436546555277314.json、图片生成/图生图/Scail2动作模仿 循环长视频版_2086769009139208194.json、图片生成/图生图/Scail2动作迁移 循环长视频版_2068484521166725122.json、图片生成/图生图/Scail2动作迁移无限时长_2098341241476964354.json、图片生成/图生图/Scail2角色替换 循环长视频版 天运子_2080732152978829313.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `EmptyImage`
- `GetImageRangeFromBatch`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 22/23 个有
- `GetImageSize` —— 22/23 个有
- `GetNode` —— 22/23 个有
- `PreviewAny` —— 22/23 个有
- `SetNode` —— 22/23 个有
- `TensorLoopClose` —— 22/23 个有
- `TensorLoopOpen` —— 22/23 个有
- `CR Text` —— 21/23 个有
- `PreviewImage` —— 21/23 个有
- `UNETLoader` —— 16/23 个有
- `DapaoImageAspectRatioResizeNode` —— 11/23 个有
- `ImpactInt` —— 11/23 个有
- `RIFE VFI` —— 11/23 个有
- `SimpleMath+` —— 11/23 个有
- `easy int` —— 11/23 个有
- `DownloadAndLoadGIMMVFIModel` —— 10/23 个有
- `GIMMVFI_interpolate` —— 10/23 个有
- `孤海注释` —— 9/23 个有
- `DiffusionModelLoaderKJ` —— 7/23 个有
- `JWInteger` —— 7/23 个有
- `Bjornulf_ShowInt` —— 5/23 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 5/23 个有
- `MathExpression|pysssss` —— 5/23 个有
- `ImageStitch` —— 3/23 个有
- `Label (rgthree)` —— 2/23 个有
- `MemoryCleaner` —— 1/23 个有
- `Note Plus (mtb)` —— 1/23 个有
- `RH_RhartImageG2ImageToImage` —— 1/23 个有
- `RunningHub Deepcleaner` —— 1/23 个有
- `SaveImage` —— 1/23 个有
- `SaveVideoRGBA` —— 1/23 个有
- `Vignette` —— 1/23 个有
- `ZhipuAPIConfig` —— 1/23 个有
- `easy cleanGpuUsed` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

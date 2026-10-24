---
name: unknown_workflow_video_lora_sampler_28
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.443667
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, EmptyImage, GetImageRangeFromBatch, GetNode, ImageCompositeMasked, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PrimitiveInt, ResizeImageMaskNode, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [图片生成/图生图/10秒直出scail2动作迁移_2065436546555277314.json, 图片生成/图生图/Scail2动作模仿 循环长视频版_2086769009139208194.json, 图片生成/图生图/Scail2动作迁移 循环长视频版_2068484521166725122.json, 图片生成/图生图/Scail2动作迁移无限时长_2098341241476964354.json, 图片生成/图生图/Scail2角色替换 循环长视频版 天运子_2080732152978829313.json, 图片生成/图生图/动作迁移Extremely Long Videos + Character Replacement_2092790825444012034.json, 图片生成/图生图/动作迁移双人跳舞之两单人图片版_SCAIL2_2072659617250893826.json, 图片生成/图生图/高配2k_迁移无阉割纯血统_长续航版_2100562120453742593.json, 数字人/数字人/多人 动作迁移 Scail2循环 长视频 插帧_2097249659348672514.json, 数字人/数字人/数字人舞蹈动作+服装展示Scail2循环动作迁移 超长视频 人物角色替换 动作迁移 高清长视频_2100056881053126657.json, 数字人/数字人/数字人舞蹈动作Scail2循环动作迁移 超长视频 人物角色替换 动作迁移 高清长视频_2100047823772409858.json, 视频生成/图生视频/HLL-Scail2动作迁移_2070484357101473794.json, 视频生成/图生视频/Scail2 人物角色替换 超长视频  动作迁移 循环动作迁移 高清长视频_2082827837156970498.json, 视频生成/图生视频/Scail2动作迁移 单人跳舞 双人跳舞循环长视频版_2077721960137707521.json, 视频生成/图生视频/Scail2动作迁移 单人跳舞 双人跳舞循环长视频版_2077728210632134658.json, 视频生成/图生视频/Scail2动作迁移 复刻动作（无限时长）_2098356016508391426.json, 视频生成/图生视频/Scail2动作迁移 复刻动作（无限时长）_2098383871367798785.json, 视频生成/图生视频/Scail2动作迁移 复刻跳舞动作-无限循环任意时长版_2078427819096494082.json, 视频生成/图生视频/Scail2动作迁移 循环长视频版 （天运子)_2071186712600072193.json, 视频生成/图生视频/Scail2动作迁移 循环长视频版_2068526463132979202.json, 视频生成/图生视频/Scail2动作迁移 循环长视频版_2068583873969217538.json, 视频生成/图生视频/Scail2动作迁移 循环长视频版_2069607269846839298.json, 视频生成/图生视频/Scail2循环动作迁移_2079918971205279746.json, 视频生成/图生视频/Scail2循环角色替换_2064684111977082882.json, 视频生成/图生视频/Scail2视频动作迁移_2064673674170560513.json, 视频生成/图生视频/Scail2角色替换 循环长视频版_2069261444784418817.json, 视频生成/图生视频/虚拟IP打造专用工作流_2087539753280434177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/10秒直出scail2动作迁移_2065436546555277314.json、图片生成/图生图/Scail2动作模仿 循环长视频版_2086769009139208194.json、图片生成/图生图/Scail2动作迁移 循环长视频版_2068484521166725122.json、图片生成/图生图/Scail2动作迁移无限时长_2098341241476964354.json、图片生成/图生图/Scail2角色替换 循环长视频版 天运子_2080732152978829313.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 27 个 workflow 都包含：
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
- `GetNode`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PrimitiveInt`
- `ResizeImageMaskNode`
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
- `ComfyMathExpression` —— 26/27 个有
- `GetImageSize` —— 26/27 个有
- `PreviewImage` —— 26/27 个有
- `TensorLoopClose` —— 26/27 个有
- `TensorLoopOpen` —— 26/27 个有
- `CR Text` —— 23/27 个有
- `UNETLoader` —— 18/27 个有
- `DownloadAndLoadGIMMVFIModel` —— 13/27 个有
- `GIMMVFI_interpolate` —— 13/27 个有
- `RIFE VFI` —— 12/27 个有
- `DapaoImageAspectRatioResizeNode` —— 11/27 个有
- `ImpactInt` —— 11/27 个有
- `SimpleMath+` —— 11/27 个有
- `easy int` —— 11/27 个有
- `DiffusionModelLoaderKJ` —— 9/27 个有
- `孤海注释` —— 8/27 个有
- `JWInteger` —— 7/27 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 6/27 个有
- `MathExpression|pysssss` —— 6/27 个有
- `Bjornulf_ShowInt` —— 5/27 个有
- `ImageStitch` —— 5/27 个有
- `SaveImage` —— 4/27 个有
- `FlashVSRNode` —— 3/27 个有
- `Sleep` —— 3/27 个有
- `Label (rgthree)` —— 2/27 个有
- `Int` —— 1/27 个有
- `MemoryCleaner` —— 1/27 个有
- `Note Plus (mtb)` —— 1/27 个有
- `RH_RhartImageG2ImageToImage` —— 1/27 个有
- `RunningHub Deepcleaner` —— 1/27 个有
- `ZhipuAPIConfig` —— 1/27 个有
- `easy clearCacheAll` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

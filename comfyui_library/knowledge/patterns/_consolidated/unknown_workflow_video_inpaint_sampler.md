---
name: unknown_workflow_video_inpaint_sampler
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.642429
common_nodes: [Any Switch (rgthree), Fast Groups Muter (rgthree), GetImageSize, GetImageSize+, GetImageSizeAndCount, GetNode, INPAINT_MaskedFill, ImageCompositeMasked, ImageFromBatch, Label (rgthree), MaskToImage, Mute / Bypass Repeater (rgthree), PrimitiveInt, PrimitiveString, RepeatImageBatch, ResizeMask, SetNode, StringConcatenate, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVAELoader, easy compare, easy ifElse, easy int, easy seed]
problems: []
missing: []
members: [图片生成/图生图/【CQ808】视频去字幕_水印_2020782485591822338.json, 图片生成/图生图/完美去水印、字幕、全能视频S水印-高质量_2033787300122992641.json, 图片生成/文生图/完美去水印、字幕、全能视频S水印-高质量_2045437255841488898.json, 平台全量/DB最强去水印 浮云3.9_2030894175620698113.json, 平台全量/DB最强去水印+VSR高清放大_2032699050771881986.json, 平台全量/JM最强去水印 浮云3.9_2030936851959259138.json, 平台全量/seedance2 去水印_字幕工作流_2031977822096465922.json, 平台全量/区域遮罩视频去水印-视频去字幕-自动_手动遮罩识别-自动去除_2054795786281603074.json, 平台全量/去水印、字幕_2031558021377167361.json, 平台全量/完美去水印、字幕、全能视频S水印-效率版_1985450156919300097.json, 平台全量/完美去水印、字幕、全能视频S水印-效率版_2016870824736722945.json, 平台全量/完美去水印、字幕、全能视频S水印-高质量_1984827631017279489.json, 平台全量/完美去水印、字幕、全能视频S水印-高质量_2036739613099823106.json, 平台全量/完美去水印、字幕、全能视频去水印-效率版_2007358917168336897.json, 平台全量/视频去水印-视频去字幕-自动_手动遮罩识别-自动去除_2052188126805798913.json, 平台全量/视频去水印-视频去字幕-自动识别-自动去除_2047859646211297282.json, 平台全量/视频完美一键去水印、字幕_2043600327944970242.json, 平台全量/视频完美一键去水印、字幕、全能视频S水印_1999045780545658881.json, 数字人/数字人/完美去水印、字幕、全能视频S水印-添加deepclener版本_2034261875877220354.json, 数字人/数字人/完美去水印、字幕、全能视频S水印-阿浩_2026924085489438721.json, 视频生成/图生视频/完美去水印、字幕、全能视频S水印-高效率版_2033794775064776706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/【CQ808】视频去字幕_水印_2020782485591822338.json、图片生成/图生图/完美去水印、字幕、全能视频S水印-高质量_2033787300122992641.json、图片生成/文生图/完美去水印、字幕、全能视频S水印-高质量_2045437255841488898.json、平台全量/DB最强去水印 浮云3.9_2030894175620698113.json、平台全量/DB最强去水印+VSR高清放大_2032699050771881986.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 21 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImageSize`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GetNode`
- `INPAINT_MaskedFill`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `Label (rgthree)`
- `MaskToImage`
- `Mute / Bypass Repeater (rgthree)`
- `PrimitiveInt`
- `PrimitiveString`
- `RepeatImageBatch`
- `ResizeMask`
- `SetNode`
- `StringConcatenate`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AddMask` —— 20/21 个有
- `BboxDetectorCombined_v2` —— 20/21 个有
- `ImageToMask` —— 20/21 个有
- `LoadImage` —— 20/21 个有
- `PreviewBridge` —— 20/21 个有
- `SaveImage` —— 20/21 个有
- `UltralyticsDetectorProvider` —— 20/21 个有
- `VHS_DuplicateMasks` —— 20/21 个有
- `easy imageBatchToImageList` —— 20/21 个有
- `easy imageListToImageBatch` —— 20/21 个有
- `Bookmark (rgthree)` —— 18/21 个有
- `WanVideoContextOptions` —— 17/21 个有
- `GetImageRangeFromBatch` —— 13/21 个有
- `ImageBatch` —— 13/21 个有
- `ImageResizeKJv2` —— 13/21 个有
- `LoadWanVideoT5TextEncoder` —— 13/21 个有
- `Mute / Bypass Relay (rgthree)` —— 13/21 个有
- `PreviewAny` —— 13/21 个有
- `SimpleMath+` —— 13/21 个有
- `WanVideoLoraSelect` —— 13/21 个有
- `WanVideoTextEncode` —— 13/21 个有
- `WanVideoTorchCompileSettings` —— 13/21 个有
- `WanVideoVACEEncode` —— 13/21 个有
- `WanVideoVACEModelSelect` —— 13/21 个有
- `easy showAnything` —— 13/21 个有
- `WanVideoEnhanceAVideo` —— 11/21 个有
- `WanVideoExperimentalArgs` —— 11/21 个有
- `GrowMask` —— 9/21 个有
- `ImageResizeKJ` —— 8/21 个有
- `WanVideoTeaCache` —— 3/21 个有
- `CreateVideo` —— 1/21 个有
- `FlashVSR_SM_KSampler` —— 1/21 个有
- `FlashVSR_SM_Model` —— 1/21 个有
- `GetVideoComponents` —— 1/21 个有
- `ImageFromBatch+` —— 1/21 个有
- `JWInteger` —— 1/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/21 个有
- `RHHiddenNodes` —— 1/21 个有
- `RunningHub Deepcleaner` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.82102e+09 | - | 1 | 100% |
| Prompt 约束强度(CFG) | randomize | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 1.82102e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）

---
name: text_to_image_video_lora_sampler_31
type: Text To Image
frequency: 21
level: strong
coverage: 0.665286
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, EmptyLatentImage, GetImageRangeFromBatch, GetImageSize, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PreviewImage, PrimitiveInt, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SCAIL2动作迁移不限时长复刻跳舞动作，单人跳舞图生视频方案_2103987283769774081.json, 视频生成/图生视频/SCAIL2动作迁移不限时长复刻跳舞动作，单人跳舞视频生视频方案_2103947994725965825.json, 视频生成/图生视频/SCAIL2动作迁移不限时长｜国内版视频生成_2095242789704527874.json, 视频生成/图生视频/SCAIL2动作迁移不限时长｜视频生视频图生视频_2100826652468137986.json, 视频生成/图生视频/SCAIL2动作迁移单人跳舞版｜复刻舞蹈不限时长视频直出_2103689612811132930.json, 视频生成/图生视频/SCAIL2循环动作迁移高清长视频版，人物动作无缝复刻流畅自然_2114473450915065857.json, 视频生成/图生视频/SCAIL2舞蹈动作复刻版｜单人跳舞视频不限时长超稳迁移_2103695977902329858.json, 视频生成/图生视频/SCAIL2跳舞动作不限时长复刻 单人图生视频迁移方案_2104700736683732993.json, 视频生成/图生视频/Scail 2单人电商带货人物产品替换图生视频处理工具_2101736999525896194.json, 视频生成/图生视频/Scail 2双人互动替换工作流｜视频里两个人物随心互换｜图生视频_2099119654894657538.json, 视频生成/图生视频/Scail 2双人互动替换｜视频图生视频一键生成_2090883066775556098.json, 视频生成/图生视频/Scail2人物角色替换 超长视频循环动作迁移处理工具_2114127248419803137.json, 视频生成/图生视频/Scail2人物角色替换超长视频｜循环动作迁移高清长视频版_2113575535904382978.json, 视频生成/图生视频/Scail2低显存动作复刻｜视频动作迁移加长无限时长_2106645828902408193.json, 视频生成/图生视频/Scail2动作迁移lite版｜复刻跳舞动作无限时长低显存_2106596717176123393.json, 视频生成/图生视频/scail 2 电商带货｜单人出镜人物产品随意替换视频生视频_2097516340285362178.json, 视频生成/图生视频/scail 2单人电商带货｜人物产品替换自动版_2097926408709427201.json, 视频生成/图生视频/scail 2电商带货利器｜单人视频里人物产品一键替换_2101491690153533442.json, 视频生成/图生视频/人物产品替换｜scail 2单人电商带货视频生成_2094004023534907393.json, 视频生成/图生视频/单人电商带货自动版｜Scail 2人物产品替换视频_2093764609831424001.json, 视频生成/图生视频/单人电商带货自动版｜scail 2人物产品替换视频生成_2093994662599155714.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/SCAIL2动作迁移不限时长复刻跳舞动作，单人跳舞图生视频方案_2103987283769774081.json、视频生成/图生视频/SCAIL2动作迁移不限时长复刻跳舞动作，单人跳舞视频生视频方案_2103947994725965825.json、视频生成/图生视频/SCAIL2动作迁移不限时长｜国内版视频生成_2095242789704527874.json、视频生成/图生视频/SCAIL2动作迁移不限时长｜视频生视频图生视频_2100826652468137986.json、视频生成/图生视频/SCAIL2动作迁移单人跳舞版｜复刻舞蹈不限时长视频直出_2103689612811132930.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveInt`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `TensorLoopClose`
- `TensorLoopOpen`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 19/21 个有
- `JWInteger` —— 18/21 个有
- `SetNode` —— 15/21 个有
- `DownloadAndLoadGIMMVFIModel` —— 14/21 个有
- `EmptyImage` —— 14/21 个有
- `GIMMVFI_interpolate` —— 14/21 个有
- `GetNode` —— 14/21 个有
- `ImageCompositeMasked` —— 14/21 个有
- `SAM3_TrackToMask` —— 14/21 个有
- `easy showAnything` —— 10/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/21 个有
- `VHS_VideoInfoSource` —— 9/21 个有
- `easy imageCount` —— 9/21 个有
- `1hew_MaskMathOps` —— 7/21 个有
- `CR Prompt Text` —— 7/21 个有
- `ColorPickerMW` —— 7/21 个有
- `DrawMaskOnImage` —— 7/21 个有
- `FillMaskWithColor` —— 7/21 个有
- `ImageConcatMulti` —— 7/21 个有
- `InvertMask` —— 7/21 个有
- `RH_Captioner` —— 7/21 个有
- `RH_RhartImageG2OfficialImageToImage` —— 7/21 个有
- `ResizeImageMaskNode` —— 7/21 个有
- `Seed (rgthree)` —— 7/21 个有
- `ShowAnything|Mie` —— 7/21 个有
- `Switch` —— 7/21 个有
- `Text` —— 7/21 个有
- `VHS_VideoInfo` —— 7/21 个有
- `WanChunkFeedForward` —— 7/21 个有
- `easy indexAnything` —— 7/21 个有
- `SaveImage` —— 6/21 个有
- `CR Text` —— 5/21 个有
- `ImageFromBatch` —— 4/21 个有
- `MathExpression|pysssss` —— 4/21 个有
- `PointsEditor` —— 4/21 个有
- `SeCModelLoader` —— 4/21 个有
- `SeCVideoSegmentation` —— 4/21 个有
- `Bjornulf_ShowInt` —— 3/21 个有
- `ImageStitch` —— 3/21 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 3/21 个有
- `ToFloat` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高发问题（23/21 个样本）：Steps较低可能导致细节不足

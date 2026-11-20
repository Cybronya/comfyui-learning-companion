---
name: text_to_image_video_lora_sampler_17
type: Text To Image
frequency: 27
level: strong
coverage: 0.561407
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DownloadAndLoadGIMMVFIModel, EmptyImage, EmptyLatentImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSize, ImageCompositeMasked, ImageResizeKJv2, JWInteger, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, PrimitiveInt, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Scail 2单人电商带货人物产品替换图生视频处理工具_2101736999525896194.json, 视频生成/图生视频/Scail 2双人互动替换工作流｜视频里两个人物随心互换｜图生视频_2099119654894657538.json, 视频生成/图生视频/Scail 2双人互动替换｜视频图生视频一键生成_2090883066775556098.json, 视频生成/图生视频/Scail2低显存动作复刻｜视频动作迁移加长无限时长_2106645828902408193.json, 视频生成/图生视频/Scail2动作迁移lite版｜复刻跳舞动作无限时长低显存_2106596717176123393.json, 视频生成/图生视频/Scail2动作迁移低配置长续航版工作流，数字人图生视频写实风格处理方案_2107981765909499905.json, 视频生成/图生视频/Scail2动作迁移复刻动作视频图片复制跳舞动作无限时长低显存版，图生视频_2106898397432213506.json, 视频生成/图生视频/Scail2动作迁移复刻动作视频图片复制跳舞动作无限时长低显存版，图生视频_2106912137393303553.json, 视频生成/图生视频/Scail2动作迁移复刻动作视频图片复制跳舞动作无限时长低显存版，图生视频_2107576153123942401.json, 视频生成/图生视频/Scail2动作迁移复刻动作视频图片复制跳舞动作无限时长低显存版，图生视频_2108372496239128578.json, 视频生成/图生视频/Scail2动作迁移无限时长版｜视频动作完整复刻_2098721885197524993.json, 视频生成/图生视频/Scail2复刻动作无限时长｜视频生视频动作迁移_2098747334107680770.json, 视频生成/图生视频/Scail2角色替换动作迁移 高清补帧图生视频处理工具_2114113214412836866.json, 视频生成/图生视频/Scail2角色替换动作迁移高清补帧｜视频三合一套餐_2114076412540973057.json, 视频生成/图生视频/lite无限时长低显存｜Scail2动作迁移复刻跳舞视频_2093792459687026690.json, 视频生成/图生视频/lite无限时长低显存｜Scail2跳舞动作复刻迁移视频_2094015557204008961.json, 视频生成/图生视频/scail 2 电商带货｜单人出镜人物产品随意替换视频生视频_2097516340285362178.json, 视频生成/图生视频/scail 2单人电商带货｜人物产品替换自动版_2097926408709427201.json, 视频生成/图生视频/scail 2电商带货利器｜单人视频里人物产品一键替换_2101491690153533442.json, 视频生成/图生视频/人物产品替换｜scail 2单人电商带货视频生成_2094004023534907393.json, 视频生成/图生视频/单人电商带货自动版｜Scail 2人物产品替换视频_2093764609831424001.json, 视频生成/图生视频/单人电商带货自动版｜scail 2人物产品替换视频生成_2093994662599155714.json, 视频生成/图生视频/双人互动一键替换｜Scail 2视频图生视频生成_2091161243632627714.json, 视频生成/图生视频/双人互动替换｜Scail 2视频生视频图生视频生成_2095067096408481794.json, 视频生成/图生视频/跳舞动作复刻视频lite无限时长低显存 Scail2动作迁移图片复制方案_2094026121233920002.json, 视频生成/图生视频/跳舞动作复刻视频lite无限时长低显存 Scail2动作迁移图片复制方案_2097105682641285121.json, 视频生成/图生视频/高配2k迁移无阉割纯血统长续航版｜图生视频不降规格，长片一跑到底_2100489274977251330.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/Scail 2单人电商带货人物产品替换图生视频处理工具_2101736999525896194.json、视频生成/图生视频/Scail 2双人互动替换工作流｜视频里两个人物随心互换｜图生视频_2099119654894657538.json、视频生成/图生视频/Scail 2双人互动替换｜视频图生视频一键生成_2090883066775556098.json、视频生成/图生视频/Scail2低显存动作复刻｜视频动作迁移加长无限时长_2106645828902408193.json、视频生成/图生视频/Scail2动作迁移lite版｜复刻跳舞动作无限时长低显存_2106596717176123393.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：56%

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
- `ComfyMathExpression`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyImage`
- `EmptyLatentImage`
- `GIMMVFI_interpolate`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `JWInteger`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveInt`
- `SAM3_TrackToMask`
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 26/27 个有
- `GetNode` —— 25/27 个有
- `PreviewAny` —— 25/27 个有
- `SetNode` —— 25/27 个有
- `ImageConcatMulti` —— 20/27 个有
- `ResizeImageMaskNode` —— 20/27 个有
- `CR Text` —— 16/27 个有
- `DiffusionModelLoaderKJ` —— 11/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/27 个有
- `VHS_VideoInfoSource` —— 11/27 个有
- `easy imageCount` —— 11/27 个有
- `easy showAnything` —— 11/27 个有
- `1hew_MaskMathOps` —— 7/27 个有
- `ColorPickerMW` —— 7/27 个有
- `DrawMaskOnImage` —— 7/27 个有
- `FillMaskWithColor` —— 7/27 个有
- `InvertMask` —— 7/27 个有
- `RH_Captioner` —— 7/27 个有
- `RH_RhartImageG2OfficialImageToImage` —— 7/27 个有
- `SaveImage` —— 7/27 个有
- `Switch` —— 7/27 个有
- `Text` —— 7/27 个有
- `easy indexAnything` —— 7/27 个有
- `ImageFromBatch` —— 4/27 个有
- `PointsEditor` —— 4/27 个有
- `SeCModelLoader` —— 4/27 个有
- `SeCVideoSegmentation` —— 4/27 个有
- `easy cleanGpuUsed` —— 2/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高发问题（28/27 个样本）：Steps较低可能导致细节不足

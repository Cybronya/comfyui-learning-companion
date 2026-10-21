---
name: text_to_image_video_lora_sampler_34
type: Text To Image
frequency: 15
level: strong
coverage: 0.7766
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, DiffusionModelLoaderKJ, EmptyLatentImage, GetNode, ImageResizeKJv2, Int, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2SimpleVideo, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/S2动作迁移工作流｜数字人动作复刻视频生成_2097520692454576129.json, 视频生成/图生视频/SCAIL2超快超长视频｜动作迁移加速生成_2095244285921812482.json, 视频生成/图生视频/Scail2一键表情迁移复刻 AI表情模仿图生视频_2098867038323298306.json, 视频生成/图生视频/Scail2数字人视频换人 图生视频支持跳舞唱歌的角色替换动作迁移_2095066924060332034.json, 视频生成/图生视频/Scail2数字人视频换人 图生视频支持跳舞唱歌的角色替换动作迁移_2097463724142587905.json, 视频生成/图生视频/Scail2数字人视频换人 图生视频支持跳舞唱歌的角色替换动作迁移_2106523439917002753.json, 视频生成/图生视频/Scail2数字人视频换人唱歌跳舞 图生视频角色替换动作迁移方案_2094356341321195522.json, 视频生成/图生视频/Scail2视频换人动作迁移角色替换图生视频处理工具_2101359118161367042.json, 视频生成/图生视频/Scail2视频换人单人双人角色替换动物迁移动作复刻跳舞模仿_2109339405835132930.json, 视频生成/图生视频/Scail2视频换人单人双人角色替换动物迁移动作复刻跳舞模仿_2109768730392752130.json, 视频生成/图生视频/Scail2视频换人单双人都行｜动作迁移换脸不崩戏_2103716490397700098.json, 视频生成/图生视频/Scail2视频换人绝了｜跳舞唱歌数字人角色替换动作迁移_2101141456789528577.json, 视频生成/图生视频/Scail2视频换人｜动作迁移跳舞唱歌数字人角色替换_2094330368626348034.json, 视频生成/图生视频/scail2一键AI表情复刻模仿｜表情迁移让照片活起来｜图生视频_2099123625453510658.json, 视频生成/图生视频/全新AI表情迁移上线｜scail2表情复刻加模仿一气呵成｜视频生视频_2099130899462971393.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_34

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（数字人/数字人/S2动作迁移工作流｜数字人动作复刻视频生成_2097520692454576129.json、视频生成/图生视频/SCAIL2超快超长视频｜动作迁移加速生成_2095244285921812482.json、视频生成/图生视频/Scail2一键表情迁移复刻 AI表情模仿图生视频_2098867038323298306.json、视频生成/图生视频/Scail2数字人视频换人 图生视频支持跳舞唱歌的角色替换动作迁移_2095066924060332034.json、视频生成/图生视频/Scail2数字人视频换人 图生视频支持跳舞唱歌的角色替换动作迁移_2097463724142587905.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `EmptyLatentImage`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2SimpleVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 14/15 个有
- `LayerUtility: PurgeVRAM` —— 14/15 个有
- `PrimitiveInt` —— 14/15 个有
- `SCAIL2FitVideo` —— 14/15 个有
- `SCAIL2ReferencePack` —— 14/15 个有
- `SCAIL2ReferenceSAMBuilder` —— 14/15 个有
- `ShowText|pysssss` —— 14/15 个有
- `SimpleMath+` —— 14/15 个有
- `WanChunkFeedForward` —— 14/15 个有
- `PreviewImage` —— 10/15 个有
- `CLIPVisionLoader` —— 8/15 个有
- `RHHiddenNodes` —— 7/15 个有
- `SaveImage` —— 5/15 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/15 个有
- `GIMMVFI_interpolate` —— 3/15 个有
- `INTConstant` —— 3/15 个有
- `ImageConcatMulti` —— 3/15 个有
- `easy compare` —— 3/15 个有
- `easy ifElse` —— 3/15 个有
- `ImageColorMatch+` —— 2/15 个有
- `GetImageSizeAndCount` —— 1/15 个有
- `GetVideoComponents` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `OverlayVideos` —— 1/15 个有
- `PreviewAny` —— 1/15 个有
- `VHS_VideoInfoLoaded` —— 1/15 个有
- `VideoToPath` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足

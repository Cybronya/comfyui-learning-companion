---
name: text_to_image_video_lora_sampler_16
type: Text To Image
frequency: 28
level: strong
coverage: 0.557143
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, EmptyLatentImage, GetNode, ImageResizeKJv2, Int, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PlaySound|pysssss, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SCAIL_2 TwoPhase Settings, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader, WanVideoTextEncodeCached, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Scail2高阶工作流Plus V4.1版人物替换长视频动作迁移背景替换_2100677048300818433.json, 视频生成/图生视频/AI舞蹈动作模仿神器｜上传视频一键复刻同款舞姿｜图生视频视频生视频_2099092870555848706.json, 视频生成/图生视频/Scail 2高阶工作流Plus V4版长视频加多图参考加动作迁移，图生视频方案_2107921047751315457.json, 视频生成/图生视频/Scail-2人物替换 简单几步换掉视频中的人_2096740903728803841.json, 视频生成/图生视频/Scail-2人物替换 简单几步换掉视频中的人_2098648284570144770.json, 视频生成/图生视频/Scail-2人物替换 简单几步换掉视频中的人_2100363189539131393.json, 视频生成/图生视频/Scail-2人物替换高阶工作流Plus V4.1｜动作迁移背景替换_2100820014902366210.json, 视频生成/图生视频/Scail-2动作复刻神器｜长视频迁移与背景替换实测_2097204671491428354.json, 视频生成/图生视频/Scail-2动作迁移动作复刻｜长视频背景替换图生视频_2091729594511609858.json, 视频生成/图生视频/Scail-2动作迁移动作复刻｜长视频背景替换处理_2095571202466209793.json, 视频生成/图生视频/Scail-2动作迁移复刻工作流｜长视频背景替换视频生成_2097075469312159745.json, 视频生成/图生视频/Scail-2动作迁移复刻｜长视频背景替换一步搞定_2097200849033453569.json, 视频生成/图生视频/Scail-2动作迁移复刻｜长视频背景替换生成_2095572428113145857.json, 视频生成/图生视频/Scail-2经典动作迁移 视频动作复刻剪辑利器_2096739586310492162.json, 视频生成/图生视频/Scail-2经典动作迁移 视频动作复刻剪辑利器_2098647045899898882.json, 视频生成/图生视频/Scail-2经典动作迁移 视频动作复刻剪辑利器_2100373797672148994.json, 视频生成/图生视频/Scail-2高阶Plus_V4.1版_长视频动作迁移背景替换人物替换_2109092542255026177.json, 视频生成/图生视频/动作复刻长视频背景替换｜Scail-2视频动作迁移生成_2095821509133692929.json, 视频生成/图生视频/舞蹈动作模仿 图生视频人物动态跟随 动作迁移工具_2098867114407972865.json, 视频生成/图生视频/跳舞_2110885441183502337.json, 视频生成/图生视频/跳舞女孩动态视频 图生视频人物动作生成 舞蹈特效_2098865375722172418.json, 视频生成/图生视频/跳舞的女孩第1弹｜图生视频一键让静态人像舞动起来_2099113102162878465.json, 视频生成/图生视频/跳舞视频一键生成｜视频生视频舞姿跟着节奏走_2111336759203291138.json, 视频生成/图生视频/长视频动作复刻背景替换｜Scail-2动作迁移视频生视频_2095815237009240066.json, 视频生成/图生视频/长视频动作复刻｜Scail-2背景替换人物特效迁移_2091777063823953922.json, 视频生成/图生视频/长视频背景替换 Scail-2动作复刻迁移全都能做_2096745184041197569.json, 视频生成/图生视频/长视频背景替换 Scail-2动作复刻迁移全都能做_2098652089533681665.json, 视频生成/图生视频/长视频背景替换 Scail-2动作复刻迁移全都能做_2100367372585623553.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（数字人/数字人/Scail2高阶工作流Plus V4.1版人物替换长视频动作迁移背景替换_2100677048300818433.json、视频生成/图生视频/AI舞蹈动作模仿神器｜上传视频一键复刻同款舞姿｜图生视频视频生视频_2099092870555848706.json、视频生成/图生视频/Scail 2高阶工作流Plus V4版长视频加多图参考加动作迁移，图生视频方案_2107921047751315457.json、视频生成/图生视频/Scail-2人物替换 简单几步换掉视频中的人_2096740903728803841.json、视频生成/图生视频/Scail-2人物替换 简单几步换掉视频中的人_2098648284570144770.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PlaySound|pysssss`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode V2`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SCAIL_2 TwoPhase Settings`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus VAELoader`
- `WanVideoTextEncodeCached`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 26/28 个有
- `Fast Groups Bypasser (rgthree)` —— 24/28 个有
- `FastGroupsBypassSwitch` —— 24/28 个有
- `INTConstant` —— 24/28 个有
- `Image Blank` —— 24/28 个有
- `ImageCompositeMasked` —— 24/28 个有
- `RepeatImageBatch` —— 24/28 个有
- `SAM3_TrackToMask` —— 24/28 个有
- `Seed (rgthree)` —— 24/28 个有
- `VHS_LoadVideo` —— 24/28 个有
- `WanAnimatePlus ContextOptions` —— 24/28 个有
- `WanAnimatePlus LoraSelect` —— 24/28 个有
- `PrimitiveStringMultiline` —— 6/28 个有
- `SaveImage` —— 5/28 个有
- `BatchImagesNode` —— 4/28 个有
- `ImageBatchMulti` —— 4/28 个有
- `ImageBatchMultiV2` —— 4/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/28 个有
- `LayerUtility: PurgeVRAM` —— 4/28 个有
- `PrimitiveBoolean` —— 4/28 个有
- `SimpleMath+` —— 4/28 个有
- `VHS_LoadVideoFFmpeg` —— 4/28 个有
- `WanVideoEncode` —— 4/28 个有
- `WanVideoTorchCompileSettings` —— 4/28 个有
- `WanVideoUni3C_ControlnetLoader` —— 4/28 个有
- `WanVideoUni3C_embeds` —— 4/28 个有
- `easy cleanGpuUsed` —— 4/28 个有
- `easy clearCacheAll` —— 4/28 个有
- `easy mathInt` —— 4/28 个有
- `EmptyImage` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 28 | 100% |
| 采样算法 | er_sde | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |
| 宽度 | 80 | 80 - 80 | 28 | 100% |
| 高度 | 80 | 80 - 80 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高发问题（29/28 个样本）：Steps较低可能导致细节不足

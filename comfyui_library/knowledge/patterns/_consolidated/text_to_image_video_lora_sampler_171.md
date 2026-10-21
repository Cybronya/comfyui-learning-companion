---
name: text_to_image_video_lora_sampler_171
type: Text To Image
frequency: 3
level: strong
coverage: 0.696667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CM_IntToFloat, CR Text, CheckpointLoaderSimple, EmptyLatentImage, GetNode, INTConstant, ImageBatchMulti, ImageResizeKJv2, Int, InvertBoolean, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveBoolean, RH_Translator, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SaveImage, SetNode, Switch any [Crystools], Text, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, easy boolean, easy imageRemBg, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Scail 2替换视频人物和背景专用流，支持人物多参图生视频方案_2106111390447656961.json, 视频生成/图生视频/单人动作迁移替换视频人物可多参高质量极简版，动作迁移图生视频_2106856823751004162.json, 视频生成/图生视频/单人动作迁移替换视频人物可多参高质量极简版，动作迁移图生视频_2110161325371514882.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_171

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Scail 2替换视频人物和背景专用流，支持人物多参图生视频方案_2106111390447656961.json、视频生成/图生视频/单人动作迁移替换视频人物可多参高质量极简版，动作迁移图生视频_2106856823751004162.json、视频生成/图生视频/单人动作迁移替换视频人物可多参高质量极简版，动作迁移图生视频_2110161325371514882.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `InvertBoolean`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveBoolean`
- `RH_Translator`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `SaveImage`
- `SetNode`
- `Switch any [Crystools]`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `easy boolean`
- `easy imageRemBg`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `WanAnimatePlus LoraSelect` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LoadVideoUI` —— 1/3 个有
- `RH_RhartImageG2ImageToImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

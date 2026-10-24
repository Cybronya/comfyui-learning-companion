---
name: text_to_image_video_lora_sampler_128
type: Text To Image
frequency: 5
level: strong
coverage: 0.699
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CM_IntToFloat, CR Text, CheckpointLoaderSimple, EmptyLatentImage, GetNode, INTConstant, ImageBatchMulti, ImageResizeKJv2, Int, InvertBoolean, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveBoolean, RH_Translator, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SaveImage, SetNode, Switch any [Crystools], Text, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, easy boolean, easy imageRemBg, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Scail 2单人动作迁移替换视频人物新王，支持多参图生视频方案_2105715425505013762.json, 图片生成/图生图/单人动作迁移新王驾到｜Scail 2 替换视频人物 支持多参 20260930更新_2105485524852101122.json, 视频生成/图生视频/Scail 2替换视频人物和背景专用流，支持人物多参图生视频方案_2106111390447656961.json, 视频生成/图生视频/单人动作迁移替换视频人物可多参高质量极简版，动作迁移图生视频_2106856823751004162.json, 视频生成/图生视频/单人动作迁移替换视频人物可多参高质量极简版，动作迁移图生视频_2110161325371514882.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Scail 2单人动作迁移替换视频人物新王，支持多参图生视频方案_2105715425505013762.json、图片生成/图生图/单人动作迁移新王驾到｜Scail 2 替换视频人物 支持多参 20260930更新_2105485524852101122.json、视频生成/图生视频/Scail 2替换视频人物和背景专用流，支持人物多参图生视频方案_2106111390447656961.json、视频生成/图生视频/单人动作迁移替换视频人物可多参高质量极简版，动作迁移图生视频_2106856823751004162.json、视频生成/图生视频/单人动作迁移替换视频人物可多参高质量极简版，动作迁移图生视频_2110161325371514882.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
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
- `孤海注释` —— 4/5 个有
- `GetImageRangeFromBatch` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `LoadVideoUI` —— 3/5 个有
- `RH_RhartImageG2ImageToImage` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有
- `WanAnimatePlus LoraSelect` —— 2/5 个有
- `EmptyImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_70
type: Text To Image
frequency: 16
level: strong
coverage: 0.891375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/视频超分工作流_2101989284810153986.json, 数字人/数字人/AI视频换人动作迁移 角色替换数字人视频生成_2094258030903906306.json, 数字人/数字人/AI视频换人神器｜动作迁移加角色替换一键完成_2106586431224377346.json, 数字人/数字人/DLSS5视频图片超分辨率 Video Image Super Resolution增强_2098709137747169282.json, 数字人/数字人/数字人口播Pro高清形象视频｜专业级形象生成工作流_2097037549385633794.json, 数字人/数字人/数字人口播Pro高清版｜形象视频清晰度再上一档_2097216696036708353.json, 视频生成/图生视频/Seedance 2.0支持留空真人全参视频处理工作流_2102163252150099970.json, 视频生成/图生视频/Seedance2.0全参工作流支持留空支持真人视频生成_2100302038222598146.json, 视频生成/图生视频/Seedance2.0全参工作流支持留空真人，图生视频视频生视频全能力覆盖_2103230482023538689.json, 视频生成/图生视频/Seedance2.0全参工作流｜支持留空真人视频生视频生成_2097408085110386689.json, 视频生成/图生视频/地表最强Seedance2.0全参工作流｜支持提示词留空与真人视频生成_2108012548770582530.json, 视频生成/图生视频/地表最强Seedance2.0支持留空支持真人全参工作流，视频生视频图生视频方案_2108261699794063362.json, 视频生成/图生视频/留空真人全参工作流｜Seedance2.0地表最强视频生成_2093481519183654913.json, 视频生成/文生视频/MiniMax H3多模态视频生成 超低成本每秒两毛钱_2098276360841162754.json, 视频生成/文生视频/Seedance2.5多模态满血版 超低价格视频生成_2098267753768636418.json, 视频生成/文生视频/Seedance2.5多模态满血版_2099730054174560257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/视频超分工作流_2101989284810153986.json、数字人/数字人/AI视频换人动作迁移 角色替换数字人视频生成_2094258030903906306.json、数字人/数字人/AI视频换人神器｜动作迁移加角色替换一键完成_2106586431224377346.json、数字人/数字人/DLSS5视频图片超分辨率 Video Image Super Resolution增强_2098709137747169282.json、数字人/数字人/数字人口播Pro高清形象视频｜专业级形象生成工作流_2097037549385633794.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 15/16 个有
- `LoadVideo` —— 14/16 个有
- `孤海注释` —— 14/16 个有
- `LoadAudio` —— 12/16 个有
- `PreviewAny` —— 10/16 个有
- `SaveImage` —— 10/16 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 7/16 个有
- `CR Prompt Text` —— 3/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `RHBerniniFullReferenceVideoToVideo` —— 2/16 个有
- `RH_BytedanceSeedance25GlobalTokenMultimodalVideo` —— 2/16 个有
- `RH_KlingV2AiAvatarProImageAudioToVideo` —— 2/16 个有
- `Image Comparer (rgthree)` —— 1/16 个有
- `JWInteger` —— 1/16 个有
- `RH_Astra` —— 1/16 个有
- `RH_DLSS5Enhance` —— 1/16 个有
- `RH_MinimaxHailuoH3MultimodalToVideo` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足

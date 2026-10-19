---
name: text_to_image_lora_sampler_clip_66
type: Text To Image
frequency: 12
level: strong
coverage: 0.893917
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/AI视频换人动作迁移 角色替换数字人视频生成_2094258030903906306.json, 数字人/数字人/AI视频换人神器｜动作迁移加角色替换一键完成_2106586431224377346.json, 数字人/数字人/DLSS5视频图片超分辨率 Video Image Super Resolution增强_2098709137747169282.json, 数字人/数字人/HeyGem视频换声工作流｜语音迁移保留原画面_2106623816477794305.json, 数字人/数字人/HeyGem语音迁移换声｜视频配音一键替换原声_2097222877983625217.json, 数字人/数字人/Heygem真人对口型数字人｜口播长视频快速生成书评国学情感_2110692840987783169.json, 视频生成/图生视频/Seedance 2.0支持留空真人全参视频处理工作流_2102163252150099970.json, 视频生成/图生视频/地表最强Seedance2.0全参工作流｜支持提示词留空与真人视频生成_2108012548770582530.json, 视频生成/图生视频/地表最强Seedance2.0支持留空支持真人全参工作流，视频生视频图生视频方案_2108261699794063362.json, 视频生成/图生视频/留空真人全参工作流｜Seedance2.0地表最强视频生成_2093481519183654913.json, 视频生成/图生视频/真人对口型口播｜Heygem书评国学情感数字人超长视频_2091209074963730434.json, 视频生成/文生视频/Seedance2.0 Fast全能参考视频 图片音频视频三参考输入_2104694435845070849.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/AI视频换人动作迁移 角色替换数字人视频生成_2094258030903906306.json、数字人/数字人/AI视频换人神器｜动作迁移加角色替换一键完成_2106586431224377346.json、数字人/数字人/DLSS5视频图片超分辨率 Video Image Super Resolution增强_2098709137747169282.json、数字人/数字人/HeyGem视频换声工作流｜语音迁移保留原画面_2106623816477794305.json、数字人/数字人/HeyGem语音迁移换声｜视频配音一键替换原声_2097222877983625217.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 10/12 个有
- `LoadAudio` —— 9/12 个有
- `LoadImage` —— 8/12 个有
- `PreviewAny` —— 4/12 个有
- `RH_HeyGemNode` —— 4/12 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 4/12 个有
- `SaveImage` —— 4/12 个有
- `AudioCrop` —— 2/12 个有
- `CreateVideo` —— 2/12 个有
- `RHBerniniFullReferenceVideoToVideo` —— 2/12 个有
- `VHS_LoadVideo` —— 2/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `RH_DLSS5Enhance` —— 1/12 个有
- `RH_RhartVideoSparkvideo20FastMultimodalVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足

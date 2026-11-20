---
name: text_to_image_lora_sampler_clip_88
type: Text To Image
frequency: 14
level: strong
coverage: 0.887786
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/火山引擎视频去字幕流｜一键擦除画面字幕文字_2098751317052313601.json, 图片生成/图生图/越南饰品海报快速生成｜图生图东南亚风格电商海报一步到位_2099162981023182849.json, 图片生成/图生图/软装搭配分析工作流 室内设计方案辅助生成_2105427749509881858.json, 图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图一键出图_2093788695898968066.json, 图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图直出_2093455106091077633.json, 图片生成/文生图/Cc-MJ影视柔光｜Krea2文生图一键生成工作流_2094792236109221890.json, 图片生成/文生图/Flux3_Klein图像编辑工作流，文生图图生图双修_2111904655876911106.json, 图片生成/文生图/Krea2影视柔光效果｜文生图MJ风格质感_2094546613636255746.json, 图片生成/文生图/丰盈美女写真生成｜文生图人像一键高清出图工作流_2094808157049671682.json, 视频生成/图生视频/Seedance 2.5动作迁移，人物场景特效图生视频_2111225027298414593.json, 视频生成/文生视频/30秒长视频多模态生成｜seedance2.5文生图生视频_2093081229213126657.json, 视频生成/文生视频/30秒长视频多模态｜seedance2.5文生图生视频生成_2093245885135286273.json, 视频生成/文生视频/Seedance2.5多模态满血版 超低价格视频生成_2098267753768636418.json, 视频生成/文生视频/Seedance2.5多模态满血版_2099730054174560257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/火山引擎视频去字幕流｜一键擦除画面字幕文字_2098751317052313601.json、图片生成/图生图/越南饰品海报快速生成｜图生图东南亚风格电商海报一步到位_2099162981023182849.json、图片生成/图生图/软装搭配分析工作流 室内设计方案辅助生成_2105427749509881858.json、图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图一键出图_2093788695898968066.json、图片生成/文生图/6宫格图片生成｜全能图片G IMAGE2文生图直出_2093455106091077633.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 13/14 个有
- `LoadImage` —— 12/14 个有
- `SaveImage` —— 11/14 个有
- `Fast Groups Bypasser (rgthree)` —— 7/14 个有
- `LoadVideo` —— 6/14 个有
- `SaveVideo` —— 6/14 个有
- `CR Prompt Text` —— 5/14 个有
- `ConditioningZeroOut` —— 4/14 个有
- `LoadAudio` —— 4/14 个有
- `RH_RhartImageG2ImageToImage` —— 4/14 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 3/14 个有
- `ResolutionSelector` —— 3/14 个有
- `CR Text` —— 2/14 个有
- `PreviewAny` —— 2/14 个有
- `RH_BytedanceSeedance25GlobalTokenMultimodalVideo` —— 2/14 个有
- `RH_VolcSubtitleEraseProVideo` —— 1/14 个有
- `ReferenceMultiLatent` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（17/14 个样本）：Steps较低可能导致细节不足

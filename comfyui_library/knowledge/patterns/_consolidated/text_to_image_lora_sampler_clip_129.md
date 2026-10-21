---
name: text_to_image_lora_sampler_clip_129
type: Text To Image
frequency: 9
level: strong
coverage: 0.884444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json, 视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频生成_2093247372666167298.json, 视频生成/文生视频/30秒长视频多模态生成｜seedance2.5文生图生视频_2093081229213126657.json, 视频生成/文生视频/30秒长视频多模态｜seedance2.5文生图生视频生成_2093245885135286273.json, 视频生成/文生视频/H3 Max Turbo图生视频首尾帧生成 全节点注释_2099926302546550786.json, 视频生成/文生视频/MiniMax H3多模态视频生成 超低成本每秒两毛钱_2098276360841162754.json, 视频生成/文生视频/Seedance 2.5图生视频处理生成工具_2102525837089263617.json, 视频生成/文生视频/Seedance2.5多模态满血版 超低价格视频生成_2098267753768636418.json, 视频生成/文生视频/Seedance2.5多模态满血版_2099730054174560257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频人物场景特效_2093082741544939522.json、视频生成/图生视频/首尾帧图生视频｜seedance2.5支持30秒长视频生成_2093247372666167298.json、视频生成/文生视频/30秒长视频多模态生成｜seedance2.5文生图生视频_2093081229213126657.json、视频生成/文生视频/30秒长视频多模态｜seedance2.5文生图生视频生成_2093245885135286273.json、视频生成/文生视频/H3 Max Turbo图生视频首尾帧生成 全节点注释_2099926302546550786.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `CR Text` —— 5/9 个有
- `LoadAudio` —— 5/9 个有
- `LoadVideo` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `CR Prompt Text` —— 3/9 个有
- `PreviewAny` —— 3/9 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `RH_BytedanceSeedance25GlobalTokenMultimodalVideo` —— 2/9 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 2/9 个有
- `RH_MinimaxH3MaxTurboImageToVideo` —— 1/9 个有
- `RH_MinimaxHailuoH3MultimodalToVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

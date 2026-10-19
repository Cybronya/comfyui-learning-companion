---
name: text_to_image_lora_sampler_clip_143
type: Text To Image
frequency: 7
level: strong
coverage: 0.901857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoadVideo, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Seedance2.0 Mini多模态｜文生图生视频全都能跑_2106629854375534594.json, 视频生成/图生视频/Seedance2.0全参工作流支持留空支持真人视频生成_2100302038222598146.json, 视频生成/图生视频/Seedance2.0全参工作流支持留空真人，图生视频视频生视频全能力覆盖_2103230482023538689.json, 视频生成/图生视频/Seedance2.0全参工作流｜支持留空真人视频生视频生成_2097408085110386689.json, 视频生成/图生视频/Seedance_2.5多模态全能参考视频｜图生视频视频生视频双支持_2101899070481719297.json, 视频生成/图生视频/Wan3多模态全参工作流，视频生视频图生视频全覆盖方案_2110206029798662146.json, 视频生成/图生视频/动作迁移角色替换AI视频换人｜免改骨架直接换主角｜图生视频_2101892897812606978.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Seedance2.0 Mini多模态｜文生图生视频全都能跑_2106629854375534594.json、视频生成/图生视频/Seedance2.0全参工作流支持留空支持真人视频生成_2100302038222598146.json、视频生成/图生视频/Seedance2.0全参工作流支持留空真人，图生视频视频生视频全能力覆盖_2103230482023538689.json、视频生成/图生视频/Seedance2.0全参工作流｜支持留空真人视频生视频生成_2097408085110386689.json、视频生成/图生视频/Seedance_2.5多模态全能参考视频｜图生视频视频生视频双支持_2101899070481719297.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 6/7 个有
- `LoadAudio` —— 5/7 个有
- `SaveImage` —— 4/7 个有
- `EmptyImage` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 3/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `RHBerniniFullReferenceVideoToVideo` —— 1/7 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 1/7 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 1/7 个有
- `RH_RhartVideoSparkvideo20MiniMultimodalVideo` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足

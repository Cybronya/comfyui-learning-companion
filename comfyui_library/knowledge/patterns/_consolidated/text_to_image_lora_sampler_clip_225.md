---
name: text_to_image_lora_sampler_clip_225
type: Text To Image
frequency: 5
level: strong
coverage: 0.8774
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Text]
members: [图片生成/图生图/2102571193546133506.json, 图片生成/文生图/Image2.5全能图像文生图 高品质文本到图像生成_2098269388993548289.json, 图片生成/文生图/Krea2-turbo超写实真人摄影｜文生图人像写真写实风格_2089715224533360641.json, 图片生成/文生图/全能图片G2.5 G-Image-2.5 Flare经济版文生图处理工具_2102168275445702657.json, 图片生成/文生图/全能图片G2.5语义拟真文生图 细腻光影复杂构图生成_2099228349863391233.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_225

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102571193546133506.json、图片生成/文生图/Image2.5全能图像文生图 高品质文本到图像生成_2098269388993548289.json、图片生成/文生图/Krea2-turbo超写实真人摄影｜文生图人像写真写实风格_2089715224533360641.json、图片生成/文生图/全能图片G2.5 G-Image-2.5 Flare经济版文生图处理工具_2102168275445702657.json、图片生成/文生图/全能图片G2.5语义拟真文生图 细腻光影复杂构图生成_2099228349863391233.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 4/5 个有
- `RH_RhartImageG25FlareTextToImage` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `ConditioningKrea2Rebalance` —— 1/5 个有
- `FishS2VoiceCloneTTS` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `LoadWhisperModel_` —— 1/5 个有
- `SaveAudio` —— 1/5 个有
- `Text` —— 1/5 个有
- `WhisperTranscribe_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text

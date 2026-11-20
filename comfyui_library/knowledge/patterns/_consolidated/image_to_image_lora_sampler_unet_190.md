---
name: image_to_image_lora_sampler_unet_190
type: Image To Image
frequency: 4
level: strong
coverage: 0.731
common_nodes: [CLIPLoader, CR Prompt Text, JWStringConcat, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Qwen3_VQA, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片无限素材流 — 支持多分镜 _ 多角度 _ 多场景_1993296418674769922.json, 图片生成/图生图/应用级：写真写意+多角度，千问编辑模型，和风整理。_2008029412943466498.json, 图片生成/图生图/超级分镜2511_2004558868975939585.json, 图片生成/图生图/超级分镜动漫版_2016459672915550209.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_190

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图片无限素材流 — 支持多分镜 _ 多角度 _ 多场景_1993296418674769922.json、图片生成/图生图/应用级：写真写意+多角度，千问编辑模型，和风整理。_2008029412943466498.json、图片生成/图生图/超级分镜2511_2004558868975939585.json、图片生成/图生图/超级分镜动漫版_2016459672915550209.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `JWStringConcat`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `CFGNorm` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `ProcessString` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 12 | 4 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 75% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 12，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 75%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

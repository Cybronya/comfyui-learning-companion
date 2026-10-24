---
name: image_to_image_lora_sampler_unet_132
type: Image To Image
frequency: 5
level: strong
coverage: 0.7212
common_nodes: [CLIPLoader, CR Prompt Text, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-2511多角度批量生图_2031310962111811586.json, 图片生成/图生图/图片无限素材流 — 支持多分镜 _ 多角度 _ 多场景_1993296418674769922.json, 图片生成/图生图/最强分镜_2015319873622122498.json, 图片生成/图生图/超级分镜2511_2004558868975939585.json, 图片生成/图生图/超级分镜动漫版_2016459672915550209.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_132

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/qwen-2511多角度批量生图_2031310962111811586.json、图片生成/图生图/图片无限素材流 — 支持多分镜 _ 多角度 _ 多场景_1993296418674769922.json、图片生成/图生图/最强分镜_2015319873622122498.json、图片生成/图生图/超级分镜2511_2004558868975939585.json、图片生成/图生图/超级分镜动漫版_2016459672915550209.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `JWStringConcat` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ProcessString` —— 3/5 个有
- `Qwen3_VQA` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `CFGNorm` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `图像缩放V2_孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 12 | 5 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 80% |
| 调度器 | beta | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 12，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足

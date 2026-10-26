---
name: unknown_workflow_lora_clip_unet_3
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.995214
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-2511+Zimage人像转夸张画风_2069970171485315074.json, 图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2067163925694734338.json, 图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2069224963105714177.json, 图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2069701534362980354.json, 图片生成/图生图/Qwen-2511+Zimage人像转抽象画风图生图_2069734160117362689.json, 图片生成/图生图/Qwen-2511+Zimage抽象画风_2041336947678908417.json, 图片生成/图生图/Qwen-2511+Zimage抽象画风_2064238909428682753.json, 图片生成/图生图/Qwen-Image-Edit-2511 放大2k_2005875871875563521.json, 图片生成/图生图/Qwen-Image-Edit-2511-Upscale2K_2005851095861788673.json, 图片生成/图生图/z-image-t控油+高清放大+增强细节_2022814596637134850.json, 图片生成/图生图/人物荒诞抽象特写_2034543447280984065.json, 图片生成/图生图/美式卡通肖像漫画-荒诞特写_2049022001309814786.json, 图片生成/图生图/荒诞特写：造物主_2032835612440535042.json, 视频生成/图生视频/一键荒诞特写_2034914535194238977.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen-2511+Zimage人像转夸张画风_2069970171485315074.json、图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2067163925694734338.json、图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2069224963105714177.json、图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2069701534362980354.json、图片生成/图生图/Qwen-2511+Zimage人像转抽象画风图生图_2069734160117362689.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/14 个有
- `ModelSamplingAuraFlow` —— 13/14 个有
- `TextEncodeQwenImageEditPlus` —— 13/14 个有
- `KSamplerAdvanced` —— 12/14 个有
- `VAEEncode` —— 12/14 个有
- `CR SDXL Aspect Ratio` —— 2/14 个有
- `ImageConcanate` —— 2/14 个有
- `KSampler` —— 2/14 个有
- `Seed (rgthree)` —— 2/14 个有
- `scale` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 86% |
| Prompt 约束强度(CFG) | 5 | 1 - 9 | 14 | 59% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler | - | 14 | 86% |
| 重绘幅度 | simple | - | 14 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 9，14 个样本
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，14 个样本，一致性 86%
- 重绘幅度 最常用 simple，14 个样本，一致性 79%

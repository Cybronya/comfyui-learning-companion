---
name: text_to_image_sampler_clip_unet_129
type: Text To Image
frequency: 6
level: moderate
coverage: 0.933167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/建筑和室内-文生图-z_image_turbo_2039276421989797890.json, 图片生成/文生图/徽派建筑klein_2063615144353165314.json, 图片生成/文生图/怀旧农村写实风格工作流_2000925300957605889.json, 图片生成/文生图/文生图 KREA 2 Turbo_2070092265502105601.json, 图片生成/文生图/文生图+KREA+2+Turbo_2085275912530124802.json, 图片生成/文生图/红衣女子生成_2015933896071847938.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_129

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/建筑和室内-文生图-z_image_turbo_2039276421989797890.json、图片生成/文生图/徽派建筑klein_2063615144353165314.json、图片生成/文生图/怀旧农村写实风格工作流_2000925300957605889.json、图片生成/文生图/文生图 KREA 2 Turbo_2070092265502105601.json、图片生成/文生图/文生图+KREA+2+Turbo_2085275912530124802.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `LoraLoader` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `PreviewImage` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `ConditioningNoiseInjection` —— 1/6 个有
- `SeedVarianceEnhancer` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 6 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 0% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 512 - 1920 | 6 | 62% |
| 高度 | 1024 | 512 - 1600 | 6 | 70% |
| LoRA 模型强度 | 1 | 0.9 - 1 | 3 | 95% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，6 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1920，6 个样本
- 高度 中位数 1024，观测区间 512 - 1600，6 个样本
- LoRA 模型强度 中位数 1，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

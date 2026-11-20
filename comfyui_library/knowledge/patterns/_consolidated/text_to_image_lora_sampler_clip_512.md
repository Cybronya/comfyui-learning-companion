---
name: text_to_image_lora_sampler_clip_512
type: Text To Image
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/2D艺术动漫风格_2006360008132399106.json, 平台全量/Anima_distilled细节加强工作流_2097509487342088194.json, 平台全量/Krea2 漆金水墨武侠｜红黑金女侠·桃花仕女_2121150889779089410.json, 平台全量/Krea2 蒂法 · 8 步四套造型 16 场景_2114575951559487489.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_512

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/2D艺术动漫风格_2006360008132399106.json、平台全量/Anima_distilled细节加强工作流_2097509487342088194.json、平台全量/Krea2 漆金水墨武侠｜红黑金女侠·桃花仕女_2121150889779089410.json、平台全量/Krea2 蒂法 · 8 步四套造型 16 场景_2114575951559487489.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 3/4 个有
- `CompressImages` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `JWImageResizeByFactor` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 768 - 1024 | 4 | 86% |
| 高度 | 1024 | 1024 - 1368 | 4 | 87% |
| 采样步数 | 8.5 | 8 - 12 | 4 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 896，观测区间 768 - 1024，4 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1368，4 个样本，取值集中（一致性 87%）
- 采样步数 中位数 8.5，观测区间 8 - 12，4 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

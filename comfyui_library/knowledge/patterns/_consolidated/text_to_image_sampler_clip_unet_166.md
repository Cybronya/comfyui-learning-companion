---
name: text_to_image_sampler_clip_unet_166
type: Text To Image
frequency: 4
level: strong
coverage: 0.83925
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069683043954151426.json, 图片生成/文生图/Krea-2-Turbo 文生图_2071991072359796737.json, 图片生成/文生图/Krea2 MJ风格图片生成_2113335543516979201.json, 图片生成/文生图/Z-image-turbo文生图_2055253303348482049.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_166

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069683043954151426.json、图片生成/文生图/Krea-2-Turbo 文生图_2071991072359796737.json、图片生成/文生图/Krea2 MJ风格图片生成_2113335543516979201.json、图片生成/文生图/Z-image-turbo文生图_2055253303348482049.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ClipLoaderGGUF` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1280 | 4 | 80% |
| 高度 | 1152 | 720 - 1920 | 4 | 64% |
| 采样步数 | 8 | 8 - 10 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1280，4 个样本，取值集中（一致性 80%）
- 高度 中位数 1152，观测区间 720 - 1920，4 个样本
- 采样步数 中位数 8，观测区间 8 - 10，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_sampler_clip_unet_12
type: Text To Image
frequency: 18
level: moderate
coverage: 0.9295
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea-2 全官方 LoRA 风格集成_2069797124136595458.json, 图片生成/文生图/Krea-2-Turbo 文生图_2071991072359796737.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2075851087260766210.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084089644026781698.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084098279272439810.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084123057798598658.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084159014056841218.json, 图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084160465382494209.json, 图片生成/文生图/krea2-turbo-极简极速文生图小说用_2103827094890434561.json, 图片生成/文生图/krea2-多风格手动文生图_2072150661021659138.json, 图片生成/文生图/krea2-多风格手动文生图_2085615556467716097.json, 图片生成/文生图/krea2-多风格手动文生图_2085620387404140546.json, 图片生成/文生图/krea2-多风格手动文生图_2085623883734020097.json, 图片生成/文生图/krea2-多风格手动文生图_2086705686548926466.json, 图片生成/文生图/krea2-多风格手动文生图_2086707015786786817.json, 图片生成/文生图/krea2-多风格手动文生图_2086728368371884033.json, 图片生成/文生图/krea2-多风格手动文生图_2086731072540336130.json, 图片生成/文生图/▶▷Krea2-标准生图)_2077775542920769537.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Krea-2 全官方 LoRA 风格集成_2069797124136595458.json、图片生成/文生图/Krea-2-Turbo 文生图_2071991072359796737.json、图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2075851087260766210.json、图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084089644026781698.json、图片生成/文生图/Krea2 MuseByStable 单图文生图+批量文生图_2084098279272439810.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 17/18 个有
- `Fast Groups Bypasser (rgthree)` —— 17/18 个有
- `LoraLoaderModelOnly` —— 17/18 个有
- `Label (rgthree)` —— 15/18 个有
- `TTResolutionSelector` —— 14/18 个有
- `Seed (rgthree)` —— 8/18 个有
- `PreviewImage` —— 7/18 个有
- `HAIGC_SaveImagesToZip` —— 6/18 个有
- `TextInputNode` —— 6/18 个有
- `easy promptList` —— 6/18 个有
- `Anything Everywhere` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 10 | 18 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 764 | 512 - 1024 | 18 | 75% |
| 高度 | 1280 | 512 - 1920 | 18 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 10，18 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 764，观测区间 512 - 1024，18 个样本
- 高度 中位数 1280，观测区间 512 - 1920，18 个样本
- 高发问题（22/18 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_sampler_clip_vae_2
type: Text To Image
frequency: 26
level: weak
coverage: 0.845308
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1982417831478345730.json, 图片生成/文生图/Boogu-Image 0.1 Turbo 极速文生图_2067853157933338626.json, 图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json, 图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json, 图片生成/文生图/Boogu-Image Turbo 文生图 极速版_2068190168858841090.json, 图片生成/文生图/Boogu_Turbo 文生图_2069444653648273409.json, 图片生成/文生图/Boogu_Turbo_文生图工作流_2069274849616416770.json, 图片生成/文生图/Boogu文生图标准版_2068941708238352385.json, 图片生成/文生图/ERNIE-Image文生图工作流_2077952838453514242.json, 图片生成/文生图/Krea2 Turbo 基础文生图_2070831897437097985.json, 图片生成/文生图/Krea2 Turbo文生图（双采版）_2070485457284190209.json, 图片生成/文生图/Krea2 Turbo文生图（双采版）_2070846138026119169.json, 图片生成/文生图/Krea2-红潮_写实人像（双采版）_2070682832741163010.json, 图片生成/文生图/Krea2_写实人像_2083068524297277442.json, 图片生成/文生图/Krea2_写实人像（双采版）_2071137932169269249.json, 图片生成/文生图/Krea2_写实人像（双采版）_2077640931263737858.json, 图片生成/文生图/Krea2_写实人像（双采版）_2079377240273547266.json, 图片生成/文生图/Krea2_写实人像（双采版）_2087070012069736450.json, 图片生成/文生图/Krea2_写实人像（双采版）_2087380793143422978.json, 图片生成/文生图/Krea2文生图_2095904097835765761.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2066049562531418114.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2075535526135947265.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2078810535986032641.json, 图片生成/文生图/boogu 文生图工作流_2072977078944886785.json, 图片生成/文生图/文生图 KREA 2 Turbo_2070092265502105601.json, 图片生成/文生图/文生图+KREA+2+Turbo_2085275912530124802.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_2

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/1982417831478345730.json、图片生成/文生图/Boogu-Image 0.1 Turbo 极速文生图_2067853157933338626.json、图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json、图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json、图片生成/文生图/Boogu-Image Turbo 文生图 极速版_2068190168858841090.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 25/26 个有
- `PrimitiveStringMultiline` —— 14/26 个有
- `PreviewImage` —— 13/26 个有
- `ResolutionSelector` —— 12/26 个有
- `Int` —— 4/26 个有
- `Label (rgthree)` —— 3/26 个有
- `NunchakuQwenImageDiTLoader` —— 1/26 个有
- `NunchakuQwenImageLoraLoader` —— 1/26 个有
- `NunchakuQwenImageLoraStack` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 26 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 26 | 48% |
| 采样算法 | euler | - | 26 | 81% |
| 调度器 | sgm_uniform | - | 26 | 46% |
| 重绘幅度 | 1 | 0.4 - 1 | 26 | 83% |
| 宽度 | 1024 | 512 - 1536 | 26 | 80% |
| 高度 | 1024 | 512 - 1920 | 26 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 32/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，26 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，26 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，26 个样本，一致性 81%
- 调度器 最常用 sgm_uniform，26 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，26 个样本，取值集中（一致性 83%）
- 宽度 中位数 1024，观测区间 512 - 1536，26 个样本，取值集中（一致性 80%）
- 高度 中位数 1024，观测区间 512 - 1920，26 个样本
- 高发问题（32/26 个样本）：Steps较低可能导致细节不足

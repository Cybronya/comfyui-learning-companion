---
name: text_to_image_sampler_clip_vae_18
type: Text To Image
frequency: 8
level: weak
coverage: 0.932625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z_IMAGE_BACE_2026986655982297089.json, 图片生成/文生图/boogu_image_base 文生图_1900216622093840386.json, 图片生成/文生图/boogu_image_turbo 文生图_1911034174755799042.json, 图片生成/文生图/boogu_image_turbo 文生图_2074111380944408578.json, 图片生成/文生图/boogu_turbo_快速出图，支持复杂提示词_2069069696166612994.json, 图片生成/文生图/krea2 Lora文生图加英伟达rtx nodes高清放大_2074689431730221057.json, 图片生成/文生图/krea2+Lora文生图_2082750366432718849.json, 图片生成/文生图/失败作图工作流_2077959412047765506.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_18

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z_IMAGE_BACE_2026986655982297089.json、图片生成/文生图/boogu_image_base 文生图_1900216622093840386.json、图片生成/文生图/boogu_image_turbo 文生图_1911034174755799042.json、图片生成/文生图/boogu_image_turbo 文生图_2074111380944408578.json、图片生成/文生图/boogu_turbo_快速出图，支持复杂提示词_2069069696166612994.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 7/8 个有
- `ConditioningZeroOut` —— 6/8 个有
- `PreviewImage` —— 5/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `EnhancedLoadDiffusionModel` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 35 | 8 | 9% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 8 | 40% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 680 - 1920 | 8 | 70% |
| 高度 | 1536 | 1024 - 2048 | 8 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 35，8 个样本，取值分散，一致性仅 9%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 680 - 1920，8 个样本
- 高度 中位数 1536，观测区间 1024 - 2048，8 个样本
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足

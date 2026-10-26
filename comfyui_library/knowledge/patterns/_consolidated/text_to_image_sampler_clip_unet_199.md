---
name: text_to_image_sampler_clip_unet_199
type: Text To Image
frequency: 3
level: strong
coverage: 0.83
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图批量_1999442466036215810.json, 图片生成/文生图/krea2-turbo_2070710904806789122.json, 图片生成/文生图/国漫角色-2512文生图_2044754203783991298.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_199

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image文生图批量_1999442466036215810.json、图片生成/文生图/krea2-turbo_2070710904806789122.json、图片生成/文生图/国漫角色-2512文生图_2044754203783991298.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Int` —— 2/3 个有
- `ProcessString` —— 2/3 个有
- `easy forLoopEnd` —— 2/3 个有
- `easy forLoopStart` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `ImageSizeCalculator` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 928 - 1024 | 3 | 95% |
| 高度 | 1536 | 1536 - 1664 | 3 | 96% |
| 采样步数 | 8 | 4 - 9 | 3 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 928 - 1024，3 个样本，取值集中（一致性 95%）
- 高度 中位数 1536，观测区间 1536 - 1664，3 个样本，取值集中（一致性 96%）
- 采样步数 中位数 8，观测区间 4 - 9，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_sampler_clip_unet_160
type: Text To Image
frequency: 4
level: strong
coverage: 0.84025
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图批量_1999442466036215810.json, 图片生成/文生图/b-最新krea2文生图_2070050778475220994.json, 图片生成/文生图/boogu_turbo_2069417901609799682.json, 图片生成/文生图/国漫角色-2512文生图_2044754203783991298.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_160

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image文生图批量_1999442466036215810.json、图片生成/文生图/b-最新krea2文生图_2070050778475220994.json、图片生成/文生图/boogu_turbo_2069417901609799682.json、图片生成/文生图/国漫角色-2512文生图_2044754203783991298.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 3/4 个有
- `CR Prompt List` —— 2/4 个有
- `ProcessString` —— 2/4 个有
- `easy forLoopEnd` —— 2/4 个有
- `easy forLoopStart` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `Int` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 976 | 720 - 1024 | 4 | 87% |
| 高度 | 1536 | 1280 - 1664 | 4 | 91% |
| 采样步数 | 6 | 4 - 9 | 4 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 976，观测区间 720 - 1024，4 个样本，取值集中（一致性 87%）
- 高度 中位数 1536，观测区间 1280 - 1664，4 个样本，取值集中（一致性 91%）
- 采样步数 中位数 6，观测区间 4 - 9，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

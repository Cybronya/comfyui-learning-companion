---
name: text_to_image_sampler_clip_unet_169
type: Text To Image
frequency: 2
level: weak
coverage: 0.8535
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Int, JjkText, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图批量_1999442466036215810.json, 图片生成/文生图/krea2-turbo_2070710904806789122.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_169

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-image文生图批量_1999442466036215810.json、图片生成/文生图/krea2-turbo_2070710904806789122.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Int`
- `JjkText`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `ImageSizeCalculator` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 976 | - | 2 | 95% |
| 高度 | 1600 | - | 2 | 96% |
| 采样步数 | 8.5 | - | 2 | 94% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 976，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 高度 中位数 1600，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 采样步数 中位数 8.5，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

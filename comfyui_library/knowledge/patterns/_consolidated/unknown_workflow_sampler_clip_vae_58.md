---
name: unknown_workflow_sampler_clip_vae_58
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.865
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, ImpactInt, Int, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/≡文生图超越即梦-17秒极速≡_1989768191025008641.json, 图片生成/文生图/🥨Qwen 千问开源文生图【官方流 更快更稳更可控】🥨_1952916801829146626.json, 图片生成/文生图/🦖qwen文生图_1960272130506174465.json, 视频生成/图生视频/视频封面_2104049803217952770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_58

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/≡文生图超越即梦-17秒极速≡_1989768191025008641.json、图片生成/文生图/🥨Qwen 千问开源文生图【官方流 更快更稳更可控】🥨_1952916801829146626.json、图片生成/文生图/🦖qwen文生图_1960272130506174465.json、视频生成/图生视频/视频封面_2104049803217952770.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `ImpactInt`
- `Int`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `NunchakuQwenImageDiTLoader` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 4 | 81% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，4 个样本，取值集中（一致性 81%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

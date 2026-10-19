---
name: unknown_workflow_sampler_clip_vae_4
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.756625
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM, Text Multiline, CR SDXL Aspect Ratio]
members: [图片生成/文生图/1959414093880963073.json, 图片生成/文生图/1959689364051800066.json, 图片生成/文生图/1959849718341906433.json, 图片生成/文生图/1959965300433301506.json, 图片生成/文生图/1959997422854418434.json, 图片生成/文生图/1960003368511025153.json, 图片生成/文生图/1960120501131751425.json, 图片生成/文生图/1962382351810564097.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_4

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1959414093880963073.json、图片生成/文生图/1959689364051800066.json、图片生成/文生图/1959849718341906433.json、图片生成/文生图/1959965300433301506.json、图片生成/文生图/1959997422854418434.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 4/8 个有
- `EmptySD3LatentImage` —— 4/8 个有
- `Text Multiline` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 8 | 69% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 3.5 | 8 | 65% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 3.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、Text Multiline、CR SDXL Aspect Ratio

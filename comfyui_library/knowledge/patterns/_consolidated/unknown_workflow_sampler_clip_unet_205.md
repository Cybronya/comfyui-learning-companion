---
name: unknown_workflow_sampler_clip_unet_205
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.916
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/字体设计_qwen-image-2.0_2023648217132441602.json, 图片生成/文生图/完美中文海报生成_2002018843826503681.json, 图片生成/文生图/组件系列6-Z-image-turbo文生图_2058749993380569090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_205

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/字体设计_qwen-image-2.0_2023648217132441602.json、图片生成/文生图/完美中文海报生成_2002018843826503681.json、图片生成/文生图/组件系列6-Z-image-turbo文生图_2058749993380569090.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy promptList` —— 2/3 个有
- `CR Text Input Switch (4 way)` —— 1/3 个有
- `CR Text Replace` —— 1/3 个有
- `DoubaoSizePreset` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 50 | 3 | 32% |
| Prompt 约束强度(CFG) | 4 | 1 - 5 | 3 | 49% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 50，3 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 5，3 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

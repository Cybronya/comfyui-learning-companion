---
name: unknown_workflow_sampler_clip_unet_402
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.856
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2多风格生图_2089324174899765249.json, 图片生成/文生图/全能图片G-Image-2.5文生图工作流_2098372445806878721.json, 图片生成/文生图/玄幻壁纸_1950582399950327809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_402

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/krea2多风格生图_2089324174899765249.json、图片生成/文生图/全能图片G-Image-2.5文生图工作流_2098372445806878721.json、图片生成/文生图/玄幻壁纸_1950582399950327809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `easy stylesSelector` —— 2/3 个有
- `JjkText` —— 1/3 个有
- `Krea2SizePreset` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 24 | 3 | 61% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 24，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

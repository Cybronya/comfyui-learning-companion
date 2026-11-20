---
name: unknown_workflow_sampler_clip_unet_448
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.917
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image 双模型双采样非常版_2048543200930963458.json, 图片生成/文生图/【老金驿站】Z-imageBase两步采样高清出图工作流_2017100420610527233.json, 图片生成/文生图/墨沫白皙质感Z -Image工作流_2067629087857926145.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_448

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image 双模型双采样非常版_2048543200930963458.json、图片生成/文生图/【老金驿站】Z-imageBase两步采样高清出图工作流_2017100420610527233.json、图片生成/文生图/墨沫白皙质感Z -Image工作流_2067629087857926145.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CLIPLoaderGGUF` —— 1/3 个有
- `CompressImages` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 768 - 1280 | 3 | 78% |
| 高度 | 1152 | 1024 - 1856 | 3 | 73% |
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 9 | 3 - 12 | 3 | 53% |
| 采样算法 | 1 | 1 - 3 | 3 | 43% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 768 - 1280，3 个样本
- 高度 中位数 1152，观测区间 1024 - 1856，3 个样本
- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 9，观测区间 3 - 12，3 个样本
- 采样算法 中位数 1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 43%
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%

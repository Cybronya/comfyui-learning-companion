---
name: unknown_workflow_sampler_clip_unet_316
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.97725
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flex.2-preview-文生图_1917071528809136129.json, 图片生成/文生图/Flex.2-preview文生图演示_1916390487366762498.json, 图片生成/文生图/flux1_dev文生图_2059177447408627714.json, 图片生成/文生图/flux1_krea_dev 对比 flux dev_1950943932404400129.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_316

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flex.2-preview-文生图_1917071528809136129.json、图片生成/文生图/Flex.2-preview文生图演示_1916390487366762498.json、图片生成/文生图/flux1_dev文生图_2059177447408627714.json、图片生成/文生图/flux1_krea_dev 对比 flux dev_1950943932404400129.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `Flex2Conditioner` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `CR Multiline Text` —— 1/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `SDXLEmptyLatentSizePicker+` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 8 - 25 | 4 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | deis | - | 4 | 50% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 768x1280 (0.6) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 22.5，观测区间 8 - 25，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

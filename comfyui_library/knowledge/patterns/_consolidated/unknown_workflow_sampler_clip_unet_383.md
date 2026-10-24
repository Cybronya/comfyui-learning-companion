---
name: unknown_workflow_sampler_clip_unet_383
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.91
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image文生图（多批次增加随机性）_2000461485551779841.json, 图片生成/文生图/z_image二采_2093223736949432322.json, 图片生成/文生图/【老金驿站】Z-imageBase两步采样高清出图工作流_2017100420610527233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_383

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image文生图（多批次增加随机性）_2000461485551779841.json、图片生成/文生图/z_image二采_2093223736949432322.json、图片生成/文生图/【老金驿站】Z-imageBase两步采样高清出图工作流_2017100420610527233.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LatentColorMatch` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 10 | 3 - 20 | 3 | 37% |
| 采样算法 | 1 | 1 - 3 | 3 | 43% |
| 调度器 | gradient_estimation | - | 3 | 33% |
| 重绘幅度 | sgm_uniform | - | 3 | 67% |
| 宽度 | 896 | 720 - 1024 | 3 | 86% |
| 高度 | 1152 | 1024 - 1280 | 3 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 10，观测区间 3 - 20，3 个样本，取值分散，一致性仅 37%
- 采样算法 中位数 1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 43%
- 调度器 最常用 gradient_estimation，3 个样本，一致性 33%
- 重绘幅度 最常用 sgm_uniform，3 个样本，一致性 67%
- 宽度 中位数 896，观测区间 720 - 1024，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1152，观测区间 1024 - 1280，3 个样本，取值集中（一致性 91%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

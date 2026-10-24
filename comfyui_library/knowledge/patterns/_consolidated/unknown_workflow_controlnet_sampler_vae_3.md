---
name: unknown_workflow_controlnet_sampler_vae_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.906
common_nodes: [CFGNorm, CLIPLoader, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-Qwen-edit+CN控制加速工作流_2073059628220506114.json, 图片生成/文生图/Nunchaku-Qwen-edit+CN控制加速工作流_1966893817553149953.json, 图片生成/文生图/Qwen-Image的Edit&CN_1961483343902785537.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Nunchaku-Qwen-edit+CN控制加速工作流_2073059628220506114.json、图片生成/文生图/Nunchaku-Qwen-edit+CN控制加速工作流_1966893817553149953.json、图片生成/文生图/Qwen-Image的Edit&CN_1961483343902785537.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `SetUnionControlNetType` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `SDXLEmptyLatentSizePicker+` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | 1 - 512 | 3 | 29% |
| ControlNet 权重 | 1.2 | 1 - 2 | 3 | 69% |
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 6 | 3 | 55% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 1 - 512，3 个样本，取值分散，一致性仅 29%
- ControlNet 权重 中位数 1.2，观测区间 1 - 2，3 个样本
- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 6，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

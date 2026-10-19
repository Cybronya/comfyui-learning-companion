---
name: unknown_workflow_controlnet_sampler_vae
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [CFGNorm, CLIPLoader, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAELoader]
problems: []
missing: [SDXLEmptyLatentSizePicker+, GetImageSize+]
members: [图片生成/文生图/1961483343902785537.json, 图片生成/文生图/1966893817553149953.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_vae

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1961483343902785537.json、图片生成/文生图/1966893817553149953.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
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
- `EmptyLatentImage` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `NunchakuQwenImageDiTLoader` —— 1/2 个有
- `SDXLEmptyLatentSizePicker+` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 256.5 | - | 2 | 0% |
| ControlNet 权重 | 1.1 | - | 2 | 91% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.25 | - | 2 | 59% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 高度 中位数 256.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- ControlNet 权重 中位数 1.1，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.25，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：SDXLEmptyLatentSizePicker+、GetImageSize+
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

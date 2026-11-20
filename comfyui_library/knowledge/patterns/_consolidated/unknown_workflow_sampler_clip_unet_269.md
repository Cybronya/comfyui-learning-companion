---
name: unknown_workflow_sampler_clip_unet_269
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.83
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Beyond Reality Z-image人像写真文生图V1_2003169101386252290.json, 图片生成/文生图/Beyond Reality Z-image超现实人像写真文生图_2004848724062994434.json, 图片生成/文生图/DG_基础Zimage文生图+增强随机性_2011606529237065730.json, 图片生成/文生图/Krea2双采美感超强_文生图_2071509119319756801.json, 图片生成/文生图/Krea2文生图（双模型双采美感强化）_2071588892037443585.json, 图片生成/文生图/Z-Image 双重采样工作流_2043154035779313665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_269

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Beyond Reality Z-image人像写真文生图V1_2003169101386252290.json、图片生成/文生图/Beyond Reality Z-image超现实人像写真文生图_2004848724062994434.json、图片生成/文生图/DG_基础Zimage文生图+增强随机性_2011606529237065730.json、图片生成/文生图/Krea2双采美感超强_文生图_2071509119319756801.json、图片生成/文生图/Krea2文生图（双模型双采美感强化）_2071588892037443585.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `Int` —— 3/6 个有
- `ModelSamplingAuraFlow` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `TTResolutionSelector` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1280 | 6 | 92% |
| 高度 | 1800 | 1536 - 1920 | 6 | 90% |
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6.5 | 3 - 15 | 6 | 34% |
| 采样算法 | 1 | 1 - 2 | 6 | 65% |
| 调度器 | euler | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1280，6 个样本，取值集中（一致性 92%）
- 高度 中位数 1800，观测区间 1536 - 1920，6 个样本，取值集中（一致性 90%）
- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 3 - 15，6 个样本，取值分散，一致性仅 34%
- 采样算法 中位数 1，观测区间 1 - 2，6 个样本
- 调度器 最常用 euler，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

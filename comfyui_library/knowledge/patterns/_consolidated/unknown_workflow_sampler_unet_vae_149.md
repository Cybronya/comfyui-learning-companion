---
name: unknown_workflow_sampler_unet_vae_149
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8355
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/图生图/2102264547909390337.json, 图片生成/图生图/2102311506384867330.json, 图片生成/图生图/2102380656931196930.json, 数字人/数字人/千问工作流_2102229006685917186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_149

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2102264547909390337.json、图片生成/图生图/2102311506384867330.json、图片生成/图生图/2102380656931196930.json、数字人/数字人/千问工作流_2102229006685917186.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `EmptyImage` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 560 - 1024 | 4 | 78% |
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 560 - 1024，4 个样本
- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text

---
name: unknown_workflow_sampler_unet_vae_114
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.867833
common_nodes: [CLIPLoader, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/千问2.1文生图工作流｜官方原生架构一键出图_2104510217215111169.json, 图片生成/文生图/千问2.1白底商品图工作流｜纯白底商业摄影级_2104514790235402242.json, 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json, 数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json, 数字人/数字人/qwen_image_2_1_角色三视图生成(自定义服装)_2108073982967762946.json, 视频生成/文生视频/Qwen_image_2.1_文生图_2104447797318733826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/千问2.1文生图工作流｜官方原生架构一键出图_2104510217215111169.json、图片生成/文生图/千问2.1白底商品图工作流｜纯白底商业摄影级_2104514790235402242.json、图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json、数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json、数字人/数字人/qwen_image_2_1_角色三视图生成(自定义服装)_2108073982967762946.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `SaveImageAdvanced` —— 3/6 个有
- `TextGenerateLTX2Prompt` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 50 | 6 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 53% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 50，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）

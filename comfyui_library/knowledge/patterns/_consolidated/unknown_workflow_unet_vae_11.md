---
name: unknown_workflow_unet_vae_11
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9302
common_nodes: [DualCLIPLoader, EmptyLatentImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX1-DEV-FP16文生图_2032756063350562818.json, 图片生成/文生图/FLUX1-DEV-FP16文生图_2043001809165361153.json, 图片生成/文生图/Flux文生图_2041424074966044673.json, 图片生成/文生图/flux文生图_1988984318296985601.json, 图片生成/文生图/【汽水】Flux基础文生图工作流_1894635344313122817.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/FLUX1-DEV-FP16文生图_2032756063350562818.json、图片生成/文生图/FLUX1-DEV-FP16文生图_2043001809165361153.json、图片生成/文生图/Flux文生图_2041424074966044673.json、图片生成/文生图/flux文生图_1988984318296985601.json、图片生成/文生图/【汽水】Flux基础文生图工作流_1894635344313122817.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `DualCLIPLoader`
- `EmptyLatentImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `FluxSamplerParams+` —— 4/5 个有
- `LoraLoader` —— 3/5 个有
- `CLIPTextEncodeFlux` —— 2/5 个有
- `Int2String` —— 2/5 个有
- `Seed_` —— 2/5 个有
- `KSampler //Inspire` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `easy positive` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 768 - 1200 | 5 | 82% |
| 高度 | 1024 | 1024 - 1600 | 5 | 81% |
| LoRA 模型强度 | 0.9 | 0.8 - 1 | 3 | 91% |
| LoRA 文本强度 | 1 | 0.7 - 1 | 3 | 84% |
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | beta | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，观测区间 768 - 1200，5 个样本，取值集中（一致性 82%）
- 高度 中位数 1024，观测区间 1024 - 1600，5 个样本，取值集中（一致性 81%）
- LoRA 模型强度 中位数 0.9，观测区间 0.8 - 1，3 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）

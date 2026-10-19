---
name: unknown_workflow_sampler_unet_vae_133
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8358
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1文生图_2102442182849421314.json, 图片生成/文生图/Qwen image 2.1文生图_2103043092977905666.json, 图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json, 数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_133

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1文生图_2102442182849421314.json、图片生成/文生图/Qwen image 2.1文生图_2103043092977905666.json、图片生成/文生图/Qwen+image+2.1文生图_2102634572138762242.json、图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json、数字人/数字人/【尺素】Qwen_image_2.1文生图_2101923741793079298.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/5 个有
- `Text` —— 2/5 个有
- `TextGenerateLTX2Prompt` —— 2/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `QwenImage21Cache` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 25 - 50 | 5 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 25 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）

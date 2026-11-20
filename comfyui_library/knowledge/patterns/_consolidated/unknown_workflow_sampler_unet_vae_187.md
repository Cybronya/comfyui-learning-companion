---
name: unknown_workflow_sampler_unet_vae_187
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.675833
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, ResolutionSelector, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json, 图片生成/文生图/QWen2.1文生图_2102420206202216450.json, 图片生成/文生图/Qwen Image 2.1 文生图_2110596847675985921.json, 图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2111477762887348225.json, 图片生成/文生图/【qwen_image_2.1】文生图 角色资料卡_2109474485958172674.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_187

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json、图片生成/文生图/QWen2.1文生图_2102420206202216450.json、图片生成/文生图/Qwen Image 2.1 文生图_2110596847675985921.json、图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json、图片生成/文生图/image_qwen_image_2_1_t2i_2111477762887348225.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 5/6 个有
- `QwenImage21Cache` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `TextGenerate` —— 5/6 个有
- `SaveImageAdvanced` —— 3/6 个有
- `JjkText` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SaveText` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `TextGenerateLTX2Prompt` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 25 | 25 - 60 | 6 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 60，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）

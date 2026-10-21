---
name: unknown_workflow_sampler_unet_vae_143
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8584
common_nodes: [CLIPLoader, CR Text, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Text Load Line From File, easy forLoopEnd, easy forLoopStart]
members: [图片生成/图生图/2102141315575271426.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json, 图片生成/文生图/qwen-image-2.1_2101675550237614082.json, 图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_143

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102141315575271426.json、图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json、图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json、图片生成/文生图/qwen-image-2.1_2101675550237614082.json、图片生成/文生图/qwen-image-2.1多图编辑_2101799458202804226.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RHLLMChatNode` —— 1/5 个有
- `Text Load Line From File` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Text Load Line From File、easy forLoopEnd、easy forLoopStart

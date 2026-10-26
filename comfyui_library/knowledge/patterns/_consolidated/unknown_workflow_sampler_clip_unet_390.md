---
name: unknown_workflow_sampler_clip_unet_390
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.835333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, CR Text, EmptySD3LatentImage, JjkText, KSampler, ModelSamplingAuraFlow, PreviewImage, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen_Image千问详情页制作 电商产品 超长详情页生成 产品主图_海报__1973917651024130049.json, 图片生成/文生图/Qwen_Image千问详情页制作_1953326943464816642.json, 图片生成/文生图/千问Qwen批量自动润色出图_1953049037521022978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_390

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen_Image千问详情页制作 电商产品 超长详情页生成 产品主图_海报__1973917651024130049.json、图片生成/文生图/Qwen_Image千问详情页制作_1953326943464816642.json、图片生成/文生图/千问Qwen批量自动润色出图_1953049037521022978.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `CR Text`
- `EmptySD3LatentImage`
- `JjkText`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `easy imageListToImageBatch` —— 2/3 个有
- `easy convertAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

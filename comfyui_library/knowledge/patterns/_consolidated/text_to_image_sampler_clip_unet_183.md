---
name: text_to_image_sampler_clip_unet_183
type: Text To Image
frequency: 3
level: strong
coverage: 0.944667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, FluxResolutionNode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen文生图超美人像_2008785579265236993.json, 图片生成/文生图/Wan2.2 Magic Wan Image文生图_1970727639172476929.json, 图片生成/文生图/Wan2.2文生图：Magic Wan Image模型生图_1969671833953988610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_183

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen文生图超美人像_2008785579265236993.json、图片生成/文生图/Wan2.2 Magic Wan Image文生图_1970727639172476929.json、图片生成/文生图/Wan2.2文生图：Magic Wan Image模型生图_1969671833953988610.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `LoadImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 768 | 3 | 82% |
| 高度 | 1376 | 512 - 1376 | 3 | 63% |
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 4 | 3 | 86% |
| 采样算法 | deis | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 768，3 个样本，取值集中（一致性 82%）
- 高度 中位数 1376，观测区间 512 - 1376，3 个样本
- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 4，3 个样本，取值集中（一致性 86%）
- 采样算法 最常用 deis，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

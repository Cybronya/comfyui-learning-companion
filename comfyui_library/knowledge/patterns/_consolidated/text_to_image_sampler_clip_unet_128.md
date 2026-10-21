---
name: text_to_image_sampler_clip_unet_128
type: Text To Image
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, FluxResolutionNode, KSampler, SaveImage, Text, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen文生图超美人像_2008785579265236993.json, 图片生成/文生图/Z-Image-Base 文生图_2016324724057448450.json, 图片生成/文生图/万相z-Image-Base文生图工作流文本生图片最新发布万相基础模型_2016346347158380546.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_128

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen文生图超美人像_2008785579265236993.json、图片生成/文生图/Z-Image-Base 文生图_2016324724057448450.json、图片生成/文生图/万相z-Image-Base文生图工作流文本生图片最新发布万相基础模型_2016346347158380546.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `KSampler`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `easy promptList` —— 2/3 个有
- `LoadImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

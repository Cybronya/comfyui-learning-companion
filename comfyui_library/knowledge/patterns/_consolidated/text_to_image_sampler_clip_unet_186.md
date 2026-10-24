---
name: text_to_image_sampler_clip_unet_186
type: Text To Image
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, KSampler, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy promptList]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Base 文生图_2016324724057448450.json, 图片生成/文生图/Z-image 批量生图+SD放大_1994350300851019778.json, 图片生成/文生图/万相z-Image-Base文生图工作流文本生图片最新发布万相基础模型_2016346347158380546.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_186

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base 文生图_2016324724057448450.json、图片生成/文生图/Z-image 批量生图+SD放大_1994350300851019778.json、图片生成/文生图/万相z-Image-Base文生图工作流文本生图片最新发布万相基础模型_2016346347158380546.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptList`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 9 - 25 | 3 | 62% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 720 | 3 | 83% |
| 高度 | 512 | 512 - 1280 | 3 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 9 - 25，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 720，3 个样本，取值集中（一致性 83%）
- 高度 中位数 512，观测区间 512 - 1280，3 个样本

---
name: text_to_image_sampler_clip_unet_168
type: Text To Image
frequency: 4
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Base 文生图_2016324724057448450.json, 图片生成/文生图/Z-Image（文生图）工作流_1993963189358493697.json, 图片生成/文生图/qwen-image 文生图_1955085568910790658.json, 图片生成/文生图/万相z-Image-Base文生图工作流文本生图片最新发布万相基础模型_2016346347158380546.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_168

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base 文生图_2016324724057448450.json、图片生成/文生图/Z-Image（文生图）工作流_1993963189358493697.json、图片生成/文生图/qwen-image 文生图_1955085568910790658.json、图片生成/文生图/万相z-Image-Base文生图工作流文本生图片最新发布万相基础模型_2016346347158380546.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `easy promptList` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Text` —— 2/4 个有
- `CFGNorm` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `LatentSwitch` —— 1/4 个有
- `LoadImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17 | 4 - 25 | 4 | 40% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 40% |
| 采样算法 | res_multistep | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 616 | 512 - 1024 | 4 | 70% |
| 高度 | 896 | 512 - 1368 | 4 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，观测区间 4 - 25，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 res_multistep，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 616，观测区间 512 - 1024，4 个样本
- 高度 中位数 896，观测区间 512 - 1368，4 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足

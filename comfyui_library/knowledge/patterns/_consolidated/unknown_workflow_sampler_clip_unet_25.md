---
name: unknown_workflow_sampler_clip_unet_25
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.900444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1989200631200100353.json, 图片生成/文生图/1994260229521162241.json, 图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json, 图片生成/文生图/Z-Image-Turbo 文生图_2104866138722230274.json, 图片生成/文生图/Z-Image_turbo文生图-又快又好_2100172337105690626.json, 图片生成/文生图/Z-image-文生图工作流_2103815728557281281.json, 图片生成/文生图/ZIT基础文生图_2088289408716992513.json, 图片生成/文生图/全能图片G-Image-2.5文生图工作流_2098372445806878721.json, 视频生成/图生视频/1955581722751483906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1989200631200100353.json、图片生成/文生图/1994260229521162241.json、图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json、图片生成/文生图/Z-Image-Turbo 文生图_2104866138722230274.json、图片生成/文生图/Z-Image_turbo文生图-又快又好_2100172337105690626.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/9 个有
- `ConditioningZeroOut` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `TextEncodeQwenImageEditPlus` —— 2/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `LoraLoader` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 40 | 9 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 38% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 40，9 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足

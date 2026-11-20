---
name: unknown_workflow_sampler_clip_unet_243
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.953833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/造相 Z_image文生图123_2010647595311435778.json, 图片生成/文生图/阿里 Z-image 文生图 工作流 最强开源模型_2038257042820960257.json, 图片生成/文生图/阿里开源文生图模型Qwen-Image_1952836741905510402.json, 图片生成/文生图/（官方版）Qwen Image文生图V1_1952787828896952322.json, 图片生成/文生图/（官方版）Qwen Image文生图（媲美即梦）_1953287044091023361.json, 图片生成/文生图/（电商娱乐流）z image turbo 文生图基础工作流_2052286821991755777.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_243

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/造相 Z_image文生图123_2010647595311435778.json、图片生成/文生图/阿里 Z-image 文生图 工作流 最强开源模型_2038257042820960257.json、图片生成/文生图/阿里开源文生图模型Qwen-Image_1952836741905510402.json、图片生成/文生图/（官方版）Qwen Image文生图V1_1952787828896952322.json、图片生成/文生图/（官方版）Qwen Image文生图（媲美即梦）_1953287044091023361.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `CLIPLoaderGGUF` —— 1/6 个有
- `Int` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 9 - 50 | 6 | 48% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 6 | 65% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 9 - 50，6 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）

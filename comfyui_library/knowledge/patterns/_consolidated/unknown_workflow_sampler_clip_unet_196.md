---
name: unknown_workflow_sampler_clip_unet_196
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.896143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image 直出高清基础流 v1_2002028004870111233.json, 图片生成/文生图/Z image 直出高清基础流 v2_2003053873344462850.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042926754704134145.json, 图片生成/文生图/Z-image Tubro文生图工作流，没有AI味的模型！_2061058146243801090.json, 图片生成/文生图/Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817.json, 图片生成/文生图/工作流基础系列4-z image turbo文生图工作流-基础向讲解此工作流_2044389426284990466.json, 图片生成/文生图/组件系列6-Z-image-turbo文生图_2058749993380569090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_196

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Z image 直出高清基础流 v1_2002028004870111233.json、图片生成/文生图/Z image 直出高清基础流 v2_2003053873344462850.json、图片生成/文生图/Z-image  zimage  文生图  工作流_2042926754704134145.json、图片生成/文生图/Z-image Tubro文生图工作流，没有AI味的模型！_2061058146243801090.json、图片生成/文生图/Zimage图片加速生成（Zimage Quick Text-to-Image Generatio）_2029019962836258817.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `easy promptList` —— 3/7 个有
- `CFGNorm` —— 2/7 个有
- `Display Any (rgthree)` —— 2/7 个有
- `QwenImageEngineer` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `EmptyZImageLatentImage //ZImagePowerNodes` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 7 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足

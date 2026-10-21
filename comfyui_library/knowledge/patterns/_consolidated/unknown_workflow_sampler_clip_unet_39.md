---
name: unknown_workflow_sampler_clip_unet_39
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.973583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo高质量文生图_2021205123837468673.json, 图片生成/文生图/Z-ImageBase+4步加速+文生图_2021786374671704065.json, 图片生成/文生图/Z-ImageBase+8步加速+文生图_2021754201637916674.json, 图片生成/文生图/Z-ImageBase+文生图_2016327178299904002.json, 图片生成/文生图/Z-Image_BASE工作流_2066527774562668546.json, 图片生成/文生图/Z-Image_BASE造像完整版文生图_2019239958594199554.json, 图片生成/文生图/Z-Image基础文生图工作流_2016022338512359425.json, 图片生成/文生图/Z-Image文生图大模型：满血版的出图效果宣判封顶！_2016493247157243905.json, 图片生成/文生图/Z-image 文生图_2027351141612265474.json, 图片生成/文生图/Z-image-base+lora文生图工作流_2016716307059707905.json, 图片生成/文生图/Z-image-base+lora文生图工作流_2058729767695904769.json, 图片生成/文生图/Z-image-base加速lora文生图_2017613550671372290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_39

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo高质量文生图_2021205123837468673.json、图片生成/文生图/Z-ImageBase+4步加速+文生图_2021786374671704065.json、图片生成/文生图/Z-ImageBase+8步加速+文生图_2021754201637916674.json、图片生成/文生图/Z-ImageBase+文生图_2016327178299904002.json、图片生成/文生图/Z-Image_BASE工作流_2066527774562668546.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 11/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `Text` —— 4/12 个有
- `CFGZeroStar` —— 1/12 个有
- `EasyCache` —— 1/12 个有
- `JWInteger` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `Seed Generator` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 50 | 12 | 42% |
| Prompt 约束强度(CFG) | 3.25 | 1 - 5 | 12 | 46% |
| 采样算法 | res_multistep | - | 12 | 33% |
| 调度器 | simple | - | 12 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 50，12 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 3.25，观测区间 1 - 5，12 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 res_multistep，12 个样本，一致性 33%
- 调度器 最常用 simple，12 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）

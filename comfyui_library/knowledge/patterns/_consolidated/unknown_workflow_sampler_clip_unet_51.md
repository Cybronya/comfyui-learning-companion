---
name: unknown_workflow_sampler_clip_unet_51
type: Unknown Workflow
frequency: 17
level: weak
coverage: 0.964059
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo高质量文生图_2021205123837468673.json, 图片生成/文生图/Z-ImageBase+4步加速+文生图_2021786374671704065.json, 图片生成/文生图/Z-ImageBase+8步加速+文生图_2021754201637916674.json, 图片生成/文生图/Z-ImageBase+文生图_2016327178299904002.json, 图片生成/文生图/Z-Image_BASE工作流_2066527774562668546.json, 图片生成/文生图/Z-Image_BASE造像完整版文生图_2019239958594199554.json, 图片生成/文生图/Z-Image_BASE造像模型完整版开源工作流_2049377951891853314.json, 图片生成/文生图/Z-Image_turbo文生图-又快又好_2100172337105690626.json, 图片生成/文生图/Z-Image_turbo文生图工作流_1995022387781492737.json, 图片生成/文生图/Z-Image_turbo文生图工作流_2032095488664670209.json, 图片生成/文生图/Z-Image基础文生图工作流_2016022338512359425.json, 图片生成/文生图/Z-Image文生图大模型：满血版的出图效果宣判封顶！_2016493247157243905.json, 图片生成/文生图/Z-image 文生图_2027351141612265474.json, 图片生成/文生图/Z-image-base+lora文生图工作流_2016716307059707905.json, 图片生成/文生图/Z-image-base+lora文生图工作流_2058729767695904769.json, 图片生成/文生图/Z-image-base加速lora文生图_2017613550671372290.json, 图片生成/文生图/手把手教你训练LORA，配合Qwen Image大模型，生图一致性达到99%！_1981265802265616385.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_51

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo高质量文生图_2021205123837468673.json、图片生成/文生图/Z-ImageBase+4步加速+文生图_2021786374671704065.json、图片生成/文生图/Z-ImageBase+8步加速+文生图_2021754201637916674.json、图片生成/文生图/Z-ImageBase+文生图_2016327178299904002.json、图片生成/文生图/Z-Image_BASE工作流_2066527774562668546.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 13/17 个有
- `LoraLoaderModelOnly` —— 7/17 个有
- `Text` —— 4/17 个有
- `Label (rgthree)` —— 2/17 个有
- `CFGZeroStar` —— 1/17 个有
- `EasyCache` —— 1/17 个有
- `JWInteger` —— 1/17 个有
- `Seed Generator` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 50 | 17 | 38% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 17 | 41% |
| 采样算法 | euler | - | 17 | 35% |
| 调度器 | simple | - | 17 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 50，17 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，17 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，17 个样本，一致性 35%
- 调度器 最常用 simple，17 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）

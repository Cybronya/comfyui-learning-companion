---
name: unknown_workflow_sampler_clip_unet_13
type: Unknown Workflow
frequency: 32
level: weak
coverage: 0.953125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo高质量文生图_2021205123837468673.json, 图片生成/文生图/Z-ImageBase+4步加速+文生图_2021786374671704065.json, 图片生成/文生图/Z-ImageBase+8步加速+文生图_2021754201637916674.json, 图片生成/文生图/Z-ImageBase+文生图_2016327178299904002.json, 图片生成/文生图/Z-Image_BASE工作流_2066527774562668546.json, 图片生成/文生图/Z-Image_BASE造像完整版文生图_2019239958594199554.json, 图片生成/文生图/Z-Image_BASE造像模型完整版开源工作流_2049377951891853314.json, 图片生成/文生图/Z-Image_turbo文生图-又快又好_2100172337105690626.json, 图片生成/文生图/Z-Image_turbo文生图工作流_1995022387781492737.json, 图片生成/文生图/Z-Image_turbo文生图工作流_2032095488664670209.json, 图片生成/文生图/Z-Image基础文生图工作流_2016022338512359425.json, 图片生成/文生图/Z-Image文生图大模型：满血版的出图效果宣判封顶！_2016493247157243905.json, 图片生成/文生图/Z-image 文生图_2027351141612265474.json, 图片生成/文生图/Z-image-Turbo 文生图_2046797778214461441.json, 图片生成/文生图/comfyui教学第一期-文生图_2008024786936537089.json, 图片生成/文生图/qwen-image-2512工作流_2067229524982587394.json, 图片生成/文生图/qwen-文生图_2090010243379060737.json, 图片生成/文生图/qwen2512文生图工作流_2068284987354476546.json, 图片生成/文生图/qwen2512粗线条水墨_2082670662396760065.json, 图片生成/文生图/【Z-Image-Turbo LoRA 一站式炼丹教程】手把手教你训练自己的猫咪LoRA，让自家猫咪“出现”在世界各地！_2004888505304182785.json, 图片生成/文生图/千问Qwen_image文生图海报_fp8_官方版26125_2015389169786294274.json, 图片生成/文生图/手把手教你训练LORA，配合Qwen Image大模型，生图一致性达到99%！_1981265802265616385.json, 图片生成/文生图/批量文生图_2033573673789034498.json, 图片生成/文生图/文生图+LoRA_2014558730028851201.json, 图片生成/文生图/文生图-Q版森林_2087797265531498498.json, 图片生成/文生图/文生图-古瓷碗里的微景观_2114540826620678146.json, 图片生成/文生图/文生图-微景观-迷你朋克工坊_2084933542248804354.json, 图片生成/文生图/文生图-微景观桃园_2088147505304395778.json, 图片生成/文生图/文生图-微景观草莓园_2085177631280029697.json, 图片生成/文生图/文生图-手机里的微景观_2084940722343600130.json, 图片生成/文生图/文生图，中英文都可以，我自己用，出图快 且准确 质量高_2026835950390747137.json, 图片生成/文生图/超可爱的q版3d风格动画角色设计_2067581459497578498.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo高质量文生图_2021205123837468673.json、图片生成/文生图/Z-ImageBase+4步加速+文生图_2021786374671704065.json、图片生成/文生图/Z-ImageBase+8步加速+文生图_2021754201637916674.json、图片生成/文生图/Z-ImageBase+文生图_2016327178299904002.json、图片生成/文生图/Z-Image_BASE工作流_2066527774562668546.json…）

- **类型**：Unknown Workflow
- **样本数**：32
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 32 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 28/32 个有
- `LoraLoaderModelOnly` —— 22/32 个有
- `ConditioningZeroOut` —— 13/32 个有
- `Text` —— 4/32 个有
- `Label (rgthree)` —— 3/32 个有
- `LatentUpscaleBy` —— 2/32 个有
- `JWInteger` —— 1/32 个有
- `Seed Generator` —— 1/32 个有
- `easy promptList` —— 1/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 32 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 32 | 29% |
| 采样算法 | euler | - | 32 | 56% |
| 调度器 | simple | - | 32 | 97% |
| 重绘幅度 | 1 | 1 - 1 | 32 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，32 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，32 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，32 个样本，一致性 56%
- 调度器 最常用 simple，32 个样本，一致性 97%
- 重绘幅度 中位数 1，观测区间 1 - 1，32 个样本，取值集中（一致性 100%）
- 高发问题（21/32 个样本）：Steps较低可能导致细节不足

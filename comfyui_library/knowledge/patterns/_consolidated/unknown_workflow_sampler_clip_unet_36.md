---
name: unknown_workflow_sampler_clip_unet_36
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.744947
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux3_Klein_t2i_2111797746670854146.json, 图片生成/文生图/Moss-image Base Fixed文生图_2112185356295688193.json, 图片生成/文生图/Moss-image Base文生图_2112066738195091457.json, 图片生成/文生图/Moss-image Base文生图_2112122177809108994.json, 图片生成/文生图/Moss-image Base文生图_2112140955116728321.json, 图片生成/文生图/Moss-image Sft Fixed文生图_2112185347613487105.json, 图片生成/文生图/Moss-image Sft文生图_2112060921463001089.json, 图片生成/文生图/Moss-image Sft文生图_自动词优化版_2112493550918258689.json, 图片生成/文生图/Moss-image Sft文生图_自动词优化版_2112499136711979009.json, 图片生成/文生图/Moss-image 文生图_2113858245021491201.json, 图片生成/文生图/Moss-image(文生图）_2111701557262766082.json, 图片生成/文生图/Moss-image+Base+Fixed文生图_2112225720482226178.json, 图片生成/文生图/Moss-image+Base文生图_2112079816290816001.json, 图片生成/文生图/Moss-image+Sft+Fixed文生图_2112225707626680321.json, 图片生成/文生图/Moss-image+Sft文生图_2112079796443369473.json, 图片生成/文生图/Moss_Image_sft 无损加速工作流_2113974334170681345.json, 图片生成/文生图/Moss_Image_sft_turbo8步加速工作流_2113398897551958018.json, 图片生成/文生图/Moss_Image_sft_turbo加速工作流_2113109058533285889.json, 图片生成/文生图/Moss_Image_sft图像生产工作流_2112494670994567169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Flux3_Klein_t2i_2111797746670854146.json、图片生成/文生图/Moss-image Base Fixed文生图_2112185356295688193.json、图片生成/文生图/Moss-image Base文生图_2112066738195091457.json、图片生成/文生图/Moss-image Base文生图_2112122177809108994.json、图片生成/文生图/Moss-image Base文生图_2112140955116728321.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 17/19 个有
- `PrimitiveBoolean` —— 16/19 个有
- `SkipLayerGuidanceDiTSimple` —— 6/19 个有
- `LoraLoaderModelOnly` —— 3/19 个有
- `ComfyMathExpression` —— 1/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `LazyCache` —— 1/19 个有
- `ModelSamplingFlux` —— 1/19 个有
- `PrimitiveFloat` —— 1/19 个有
- `Seed (rgthree)` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 19 | 67% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 19 | 76% |
| 采样算法 | er_sde | - | 19 | 89% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，19 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，19 个样本
- 采样算法 最常用 er_sde，19 个样本，一致性 89%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）

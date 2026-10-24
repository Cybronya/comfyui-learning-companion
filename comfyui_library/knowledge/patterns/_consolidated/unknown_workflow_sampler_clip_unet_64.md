---
name: unknown_workflow_sampler_clip_unet_64
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.969538
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX 2 文生图_1993689182549770241.json, 图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json, 图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json, 图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json, 图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json, 图片生成/文生图/FLUX2文生图_2038528285033897986.json, 图片生成/文生图/FLUX板块：FLUX.2-Klein多模态文生图工作流_2049841830287687681.json, 图片生成/文生图/Flux 2 txt2img 2K Image Generation_2037040628390957058.json, 图片生成/文生图/Flux Klein 基础文生图工作流_2017056654767951874.json, 图片生成/文生图/Flux-2-klein-文生图_2081417549262184450.json, 图片生成/文生图/Flux2 Klein 9B 文生图_2012015496945737730.json, 图片生成/文生图/Flux2-4步文生图_2007026656766074882.json, 图片生成/文生图/flux-2-klein-文生图标准流_2040040486324408321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/FLUX 2 文生图_1993689182549770241.json、图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json、图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json、图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json、图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/13 个有
- `FluxGuidance` —— 4/13 个有
- `LoraLoaderModelOnly` —— 4/13 个有
- `CLIPLoaderGGUF` —— 2/13 个有
- `UnetLoaderGGUF` —— 2/13 个有
- `JWInteger` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `LoadImage` —— 1/13 个有
- `MuyeSizeSelector` —— 1/13 个有
- `TTResolutionSelector` —— 1/13 个有
- `Text` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 22 | 13 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 22，13 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（9/13 个样本）：Steps较低可能导致细节不足

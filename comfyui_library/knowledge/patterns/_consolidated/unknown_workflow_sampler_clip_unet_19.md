---
name: unknown_workflow_sampler_clip_unet_19
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.969067
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json, 图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json, 图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json, 图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json, 图片生成/文生图/Flux Klein 基础文生图工作流_2017056654767951874.json, 图片生成/文生图/Flux-2-klein-文生图_2081417549262184450.json, 图片生成/文生图/Flux2 Klein 文生图9B版_2012014139270500354.json, 图片生成/文生图/Flux2 Klein 文生图9B版_极速10秒出图_2012051332127006722.json, 图片生成/文生图/Flux2 Klein 文生图_2070321896603873281.json, 图片生成/文生图/Flux2 Klein 文生图_2070323795138801666.json, 图片生成/文生图/Flux2 Klein 文生图_2070331931929178114.json, 图片生成/文生图/Flux2_Klein 文生图9B版-官方版-4步_2012020314640748545.json, 图片生成/文生图/Flux2文生图工作流_1993530593369587713.json, 图片生成/文生图/Flux2文生图工作流_1993542491129446401.json, 图片生成/文生图/flux2.0_1995304483615858689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_19

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json、图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json、图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json、图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json、图片生成/文生图/Flux Klein 基础文生图工作流_2017056654767951874.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/15 个有
- `CR Text` —— 6/15 个有
- `FluxGuidance` —— 4/15 个有
- `LoraLoaderModelOnly` —— 2/15 个有
- `CLIPLoaderGGUF` —— 1/15 个有
- `Int` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 22 | 15 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 22，15 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（10/15 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_sampler_clip_unet_228
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.987
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux 2 txt2img 2K Image Generation_2037040628390957058.json, 图片生成/文生图/Flux Klein 基础文生图工作流_2017056654767951874.json, 图片生成/文生图/Flux-2-klein-文生图_2081417549262184450.json, 图片生成/文生图/Flux2 Klein 9B 文生图_2012015496945737730.json, 图片生成/文生图/Flux2-4步文生图_2007026656766074882.json, 图片生成/文生图/Flux2文生图工作流_1993542491129446401.json, 图片生成/文生图/flux2.0_1995304483615858689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_228

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Flux 2 txt2img 2K Image Generation_2037040628390957058.json、图片生成/文生图/Flux Klein 基础文生图工作流_2017056654767951874.json、图片生成/文生图/Flux-2-klein-文生图_2081417549262184450.json、图片生成/文生图/Flux2 Klein 9B 文生图_2012015496945737730.json、图片生成/文生图/Flux2-4步文生图_2007026656766074882.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `FluxGuidance` —— 4/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `CLIPLoaderGGUF` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `MuyeSizeSelector` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 22 | 7 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 22，7 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）

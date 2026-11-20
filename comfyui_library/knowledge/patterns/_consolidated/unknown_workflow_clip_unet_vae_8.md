---
name: unknown_workflow_clip_unet_vae_8
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.925625
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2 Klein 9B 文生图_2012015496945737730.json, 图片生成/文生图/Flux2 Klein 文生图 9B版，官方版_2015074255158910977.json, 图片生成/文生图/Flux2 Klein 文生图9B版_2012014139270500354.json, 图片生成/文生图/Flux2 Klein 文生图9B版_极速10秒出图_2012051332127006722.json, 图片生成/文生图/Flux2 Klein 文生图_2070321896603873281.json, 图片生成/文生图/Flux2 Klein 文生图_2070323795138801666.json, 图片生成/文生图/Flux2 Klein 文生图_2070331931929178114.json, 图片生成/文生图/Flux2-Klein-9B-True-bf16_2024822336939106306.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Flux2 Klein 9B 文生图_2012015496945737730.json、图片生成/文生图/Flux2 Klein 文生图 9B版，官方版_2015074255158910977.json、图片生成/文生图/Flux2 Klein 文生图9B版_2012014139270500354.json、图片生成/文生图/Flux2 Klein 文生图9B版_极速10秒出图_2012051332127006722.json、图片生成/文生图/Flux2 Klein 文生图_2070321896603873281.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `MuyeSizeSelector` —— 2/8 个有
- `Int` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `KSamplerAdvanced` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 25 | 8 | 0% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 25，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_sampler_clip_unet_37
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.942211
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2 Klein 文生图 9B版，官方版_2015074255158910977.json, 图片生成/文生图/Flux2 Klein 文生图9B_10秒出图_2012086959107219458.json, 图片生成/文生图/Flux2 Klein 文生图9B版_2012014139270500354.json, 图片生成/文生图/Flux2 Klein 文生图9B版_极速10秒出图_2012051332127006722.json, 图片生成/文生图/Flux2 Klein 文生图_2020763009353785346.json, 图片生成/文生图/Flux2 Klein 文生图_2025932476836749314.json, 图片生成/文生图/Flux2 Klein 文生图_2028304337616769026.json, 图片生成/文生图/Flux2 Klein 文生图_2070321896603873281.json, 图片生成/文生图/Flux2 Klein 文生图_2070323795138801666.json, 图片生成/文生图/Flux2 Klein 文生图_2070331931929178114.json, 图片生成/文生图/Flux2.0-Dev _ 文生图_1993501652189642754.json, 图片生成/文生图/Flux2_Klein 文生图9B版-官方版-4步_2012020314640748545.json, 图片生成/文生图/Flux2文生图_1993378851996844034.json, 图片生成/文生图/Flux2文生图官方版_1993503885006405633.json, 图片生成/文生图/Flux2文生图工作流_1993530593369587713.json, 图片生成/文生图/Z_image_turbo文生图原版工作流-B站UP主@好奇漫步_1995897359357919233.json, 图片生成/文生图/【遇见AI】ernie-image-turbo文生图_2046172974834786305.json, 图片生成/文生图/【遇见AI】ernie-image文生图_2046172899383447554.json, 图片生成/文生图/【遇见AI】longcat image 基础文生图_2059223196771110914.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Flux2 Klein 文生图 9B版，官方版_2015074255158910977.json、图片生成/文生图/Flux2 Klein 文生图9B_10秒出图_2012086959107219458.json、图片生成/文生图/Flux2 Klein 文生图9B版_2012014139270500354.json、图片生成/文生图/Flux2 Klein 文生图9B版_极速10秒出图_2012051332127006722.json、图片生成/文生图/Flux2 Klein 文生图_2020763009353785346.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 18/19 个有
- `EmptyFlux2LatentImage` —— 14/19 个有
- `CR Text` —— 11/19 个有
- `LoadImage` —— 6/19 个有
- `EmptySD3LatentImage` —— 5/19 个有
- `FluxGuidance` —— 2/19 个有
- `Int` —— 2/19 个有
- `LayerUtility: PurgeVRAM V2` —— 2/19 个有
- `CFGNorm` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 19 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 19 | 30% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，19 个样本，取值分散，一致性仅 30%
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（10/19 个样本）：Steps较低可能导致细节不足

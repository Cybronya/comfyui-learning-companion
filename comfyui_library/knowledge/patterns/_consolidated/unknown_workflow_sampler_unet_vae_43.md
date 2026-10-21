---
name: unknown_workflow_sampler_unet_vae_43
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.991667
common_nodes: [ConditioningZeroOut, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ERNIE-Image-Turbo 文生图_2044675520398368770.json, 图片生成/文生图/ERNIE-Image-Turbo文生图_2063975108284346370.json, 图片生成/文生图/ERNIE-Image-Turbo文生图艺术字设计_2052935133627465729.json, 图片生成/文生图/ERNIE-Image-Turbo（文生图）_2059103096625782786.json, 图片生成/文生图/F.1玄金金箔美学_2008505998876614657.json, 图片生成/文生图/FLUX 2 文生图_1993689182549770241.json, 图片生成/文生图/FLUX.1 LoRA模型工作流搭建_2014635794983555074.json, 图片生成/文生图/Flux2 Klein 文生图_2025932476836749314.json, 图片生成/文生图/Flux2-4步文生图_2007026656766074882.json, 图片生成/文生图/Flux2.0-Dev _ 文生图_1993501652189642754.json, 图片生成/文生图/Flux2文生图_1993378851996844034.json, 图片生成/文生图/Flux2文生图官方版_1993503885006405633.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_43

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/ERNIE-Image-Turbo 文生图_2044675520398368770.json、图片生成/文生图/ERNIE-Image-Turbo文生图_2063975108284346370.json、图片生成/文生图/ERNIE-Image-Turbo文生图艺术字设计_2052935133627465729.json、图片生成/文生图/ERNIE-Image-Turbo（文生图）_2059103096625782786.json、图片生成/文生图/F.1玄金金箔美学_2008505998876614657.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `ConditioningZeroOut`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 11/12 个有
- `CLIPLoader` —— 10/12 个有
- `EmptyFlux2LatentImage` —— 7/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `EmptySD3LatentImage` —— 5/12 个有
- `CR Text` —— 3/12 个有
- `DualCLIPLoader` —— 2/12 个有
- `FluxGuidance` —— 2/12 个有
- `LayerUtility: PurgeVRAM V2` —— 2/12 个有
- `CLIPTextEncodeFlux` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 6 - 22 | 12 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 6 - 22，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_sampler_clip_unet_393
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo 文生图_1994229361725423618.json, 图片生成/文生图/flux.2文生图_1993490185759424514.json, 图片生成/文生图/【老金驿站】FLUX2-dev文生图工作流_1993506834367660033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_393

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo 文生图_1994229361725423618.json、图片生成/文生图/flux.2文生图_1993490185759424514.json、图片生成/文生图/【老金驿站】FLUX2-dev文生图工作流_1993506834367660033.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `StringConstantMultiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

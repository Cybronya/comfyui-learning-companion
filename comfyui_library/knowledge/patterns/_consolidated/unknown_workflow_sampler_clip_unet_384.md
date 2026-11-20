---
name: unknown_workflow_sampler_clip_unet_384
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.868667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, FLS_SamplerV4, KSamplerAdvanced, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, 孤海注释]
problems: []
missing: []
members: [图片生成/文生图/Flux2-Klein9B V2版文生图工作流 增强采样器，实景般逼真体验_2071099547346100225.json, 图片生成/文生图/Klein9B  社区优质模型 真实感爆棚V2版_2060263775722364930.json, 图片生成/文生图/Klein9B V2版  硬核优质模型 观感宛若实景_2060280246104055810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_384

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein9B V2版文生图工作流 增强采样器，实景般逼真体验_2071099547346100225.json、图片生成/文生图/Klein9B  社区优质模型 真实感爆棚V2版_2060263775722364930.json、图片生成/文生图/Klein9B V2版  硬核优质模型 观感宛若实景_2060280246104055810.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `FLS_SamplerV4`
- `KSamplerAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DapaoImageRatioLimitNode` —— 2/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `Ratio to Size` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 3 | 100% |
| 采样算法 | 1 | 1 - 1.2 | 3 | 91% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.2，3 个样本，取值集中（一致性 91%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%

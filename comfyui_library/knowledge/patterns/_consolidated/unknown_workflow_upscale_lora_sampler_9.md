---
name: unknown_workflow_upscale_lora_sampler_9
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.737571
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, ImageScaleBy, ImageUpscaleWithModel, ImpactStringSelector, Int, JjkConcat, JjkText, KSampler, PrimitiveFloat, SaveImage, StringConcatenate, TextRandomMultiline, UpscaleModelLoader, VAEDecode, easy loraStack, easy loraStackApply, easy showAnything, easy textSwitch, math_calculate, workflow>MainLoad]
problems: []
missing: [CR Split String, easy textSwitch, workflow>MainLoad, easy loraStack, easy loraStackApply]
members: [图片生成/文生图/1950577025067175938.json, 图片生成/文生图/3D动漫Illustrious文生图_无限制_2026917188258500609.json, 图片生成/文生图/Illustrious文生图_无限制动漫_2026498379655684098.json, 图片生成/文生图/Illustrious科幻机甲_2050905003711311874.json, 图片生成/文生图/SDXL文生图_无限制_2026919557071376386.json, 图片生成/文生图/SDXL文生美图_2026534975964712961.json, 图片生成/文生图/WAI Illustrious文生瑟图_二次元_动漫_2023677640929972226.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1950577025067175938.json、图片生成/文生图/3D动漫Illustrious文生图_无限制_2026917188258500609.json、图片生成/文生图/Illustrious文生图_无限制动漫_2026498379655684098.json、图片生成/文生图/Illustrious科幻机甲_2050905003711311874.json、图片生成/文生图/SDXL文生图_无限制_2026919557071376386.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactStringSelector`
- `Int`
- `JjkConcat`
- `JjkText`
- `KSampler`
- `PrimitiveFloat`
- `SaveImage`
- `StringConcatenate`
- `TextRandomMultiline`
- `UpscaleModelLoader`
- `VAEDecode`
- `easy loraStack`
- `easy loraStackApply`
- `easy showAnything`
- `easy textSwitch`
- `math_calculate`
- `workflow>MainLoad`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 6/7 个有
- `DuckHideNode` —— 6/7 个有
- `RandomInt` —— 6/7 个有
- `easy batchAnything` —— 6/7 个有
- `easy forLoopEnd` —— 6/7 个有
- `easy forLoopStart` —— 6/7 个有
- `easy mathInt` —— 6/7 个有
- `CR Split String` —— 1/7 个有
- `PrimitiveString` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 100% |
| 调度器 | normal | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Split String、easy textSwitch、workflow>MainLoad、easy loraStack、easy loraStackApply

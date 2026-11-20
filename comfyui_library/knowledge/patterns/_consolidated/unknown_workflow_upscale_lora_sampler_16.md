---
name: unknown_workflow_upscale_lora_sampler_16
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.794308
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed‑Image‑Edit衣服替换_2098222393721446402.json, 图片生成/图生图/FireRed‑Image‑Edit衣服替换换装_2097171417648427010.json, 图片生成/图生图/FireRed‑Image‑Edit衣服替换换装_2097510318359535618.json, 图片生成/图生图/一键换装   换装   一键换衣  换衣   电商服装展示_2059835700102651906.json, 图片生成/图生图/心然·寻源-FireRed‑Image‑Edit衣服替换_2091484811545370625.json, 图片生成/图生图/换装 换衣  服装展示 电商模特_2063873263129944066.json, 图片生成/图生图/换装 换衣  服装展示 电商模特_2063975044883238914.json, 图片生成/图生图/换装 换衣  服装展示 电商模特_2064223586767958017.json, 图片生成/图生图/换装 换衣  服装展示 电商模特_2064244296605323266.json, 图片生成/图生图/换装 换衣  服装展示 电商模特_2064318549887377410.json, 图片生成/图生图/换装 换衣  服装展示 电商模特_2064419023038799873.json, 图片生成/图生图/换装 换衣  服装展示 电商模特_2064646568548069377.json, 图片生成/图生图/换装+换衣++服装展示+电商模特+_2066700930946527234.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/FireRed‑Image‑Edit衣服替换_2098222393721446402.json、图片生成/图生图/FireRed‑Image‑Edit衣服替换换装_2097171417648427010.json、图片生成/图生图/FireRed‑Image‑Edit衣服替换换装_2097510318359535618.json、图片生成/图生图/一键换装   换装   一键换衣  换衣   电商服装展示_2059835700102651906.json、图片生成/图生图/心然·寻源-FireRed‑Image‑Edit衣服替换_2091484811545370625.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 9/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `GetNode` —— 4/13 个有
- `SetNode` —— 4/13 个有
- `Text` —— 4/13 个有
- `easy imageSizeBySide` —— 4/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足

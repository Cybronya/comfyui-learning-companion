---
name: unknown_workflow_upscale_lora_sampler_7
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.771111
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, ImageScaleBy, ImageUpscaleWithModel, ImpactStringSelector, Int, JjkConcat, JjkText, KSampler, PrimitiveFloat, SaveImage, StringConcatenate, TextRandomMultiline, UpscaleModelLoader, VAEDecode, easy loraStack, easy loraStackApply, easy showAnything, easy textSwitch, math_calculate, workflow>MainLoad]
problems: []
missing: []
members: [图片生成/文生图/3D动漫Illustrious文生图_无限制_2026917188258500609.json, 图片生成/文生图/Illustrious一键生成清纯女友_2042810792273252354.json, 图片生成/文生图/Illustrious亚洲女性写实_2050896068455485442.json, 图片生成/文生图/Illustrious文生图_无限制_2042480186519719937.json, 图片生成/文生图/Illustrious文生图_无限制动漫_2026498379655684098.json, 图片生成/文生图/Illustrious文生瑟图_2035035529380634626.json, 图片生成/文生图/Illustrious新世界_2035673216508764161.json, 图片生成/文生图/Illustrious无限制动漫-3D-大雷_2037095349076103170.json, 图片生成/文生图/Illustrious混音文生图_一键生成美女_2039291235839512578.json, 图片生成/文生图/Illustrious科幻机甲_2050905003711311874.json, 图片生成/文生图/Illustrious超越2.5D_2031655086094557186.json, 图片生成/文生图/SDXL文生图_无限制_2026919557071376386.json, 图片生成/文生图/SDXL文生美图_2026534975964712961.json, 图片生成/文生图/SDXL文生美图_2033772089961877506.json, 图片生成/文生图/SDXL文生美图无限制_2040632487734419458.json, 图片生成/文生图/WAI Illustrious全元素随机工作流ver1.84 [SakuragiKiri]_1950577025067175938.json, 图片生成/文生图/WAI Illustrious文生瑟图_二次元_动漫_2023677640929972226.json, 图片生成/文生图/一键生成日本美女壁纸_2036112611254734850.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/3D动漫Illustrious文生图_无限制_2026917188258500609.json、图片生成/文生图/Illustrious一键生成清纯女友_2042810792273252354.json、图片生成/文生图/Illustrious亚洲女性写实_2050896068455485442.json、图片生成/文生图/Illustrious文生图_无限制_2042480186519719937.json、图片生成/文生图/Illustrious文生图_无限制动漫_2026498379655684098.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 18 个 workflow 都包含：
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
- `CompressImages` —— 17/18 个有
- `DuckHideNode` —— 17/18 个有
- `RandomInt` —— 17/18 个有
- `easy batchAnything` —— 17/18 个有
- `easy forLoopEnd` —— 17/18 个有
- `easy forLoopStart` —— 17/18 个有
- `easy mathInt` —— 17/18 个有
- `CR Split String` —— 1/18 个有
- `PrimitiveString` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 18 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 18 | 100% |
| 采样算法 | euler_ancestral | - | 18 | 94% |
| 调度器 | normal | - | 18 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，18 个样本，一致性 94%
- 调度器 最常用 normal，18 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）

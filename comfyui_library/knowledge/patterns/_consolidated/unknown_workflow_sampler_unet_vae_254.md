---
name: unknown_workflow_sampler_unet_vae_254
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6582
common_nodes: [Any Switch (rgthree), CLIPLoader, EmptyLatentImage, JsonExtractString, KSampler, PrimitiveStringMultiline, SaveImage, TextConcatenator, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/QwenImage2.1 I2I + 官方提示词助手_2102348928711741442.json, 图片生成/图生图/QwenImage2.1图片编辑+ 官方提示词助手_2102657855655600129.json, 图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json, 图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json, 图片生成/文生图/通用QwenImage2.1_2111083073197666306.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_254

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/QwenImage2.1 I2I + 官方提示词助手_2102348928711741442.json、图片生成/图生图/QwenImage2.1图片编辑+ 官方提示词助手_2102657855655600129.json、图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json、图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json、图片生成/文生图/通用QwenImage2.1_2111083073197666306.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `EmptyLatentImage`
- `JsonExtractString`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextConcatenator`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `SaveImageAdvanced` —— 4/5 个有
- `ComfySwitchNode` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `QwenImage21Cache` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `ImageBatchMulti` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `ShowAnything|Mie` —— 2/5 个有
- `easy isNone` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1560 | 5 | 79% |
| 高度 | 1024 | 1024 - 1080 | 5 | 97% |
| 采样步数 | 30 | 25 - 30 | 5 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1560，5 个样本
- 高度 中位数 1024，观测区间 1024 - 1080，5 个样本，取值集中（一致性 97%）
- 采样步数 中位数 30，观测区间 25 - 30，5 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

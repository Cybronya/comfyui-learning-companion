---
name: unknown_workflow_sampler_unet_vae_182
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.690333
common_nodes: [Any Switch (rgthree), CLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), JsonExtractString, KSampler, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SaveImageAdvanced, TextConcatenator, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2102348928711741442.json, 图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json, 图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2102348928711741442.json、图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json、图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JsonExtractString`
- `KSampler`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TextConcatenator`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowAnything|Mie` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `QwenImage21Cache` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1560 | 1024 - 1560 | 3 | 82% |
| 高度 | 1080 | 1024 - 1080 | 3 | 98% |
| 采样步数 | 30 | 25 - 30 | 3 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1560，观测区间 1024 - 1560，3 个样本，取值集中（一致性 82%）
- 高度 中位数 1080，观测区间 1024 - 1080，3 个样本，取值集中（一致性 98%）
- 采样步数 中位数 30，观测区间 25 - 30，3 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

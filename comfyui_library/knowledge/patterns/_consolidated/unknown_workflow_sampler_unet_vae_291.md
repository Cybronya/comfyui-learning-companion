---
name: unknown_workflow_sampler_unet_vae_291
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.766667
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json, 图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json, 图片生成/文生图/Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_291

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/QwenImage2.1-T2I + 官方提示词助手_2102343746745626625.json、图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json、图片生成/文生图/Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `JsonExtractString` —— 2/3 个有
- `ShowAnything|Mie` —— 2/3 个有
- `TextConcatenator` —— 2/3 个有
- `PreviewAny` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1560 | 1024 - 1560 | 3 | 82% |
| 高度 | 1080 | 1024 - 1080 | 3 | 98% |
| 采样步数 | 30 | 30 - 50 | 3 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1560，观测区间 1024 - 1560，3 个样本，取值集中（一致性 82%）
- 高度 中位数 1080，观测区间 1024 - 1080，3 个样本，取值集中（一致性 98%）
- 采样步数 中位数 30，观测区间 30 - 50，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

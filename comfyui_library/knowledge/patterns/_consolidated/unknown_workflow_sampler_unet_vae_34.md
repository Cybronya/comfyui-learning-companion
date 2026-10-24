---
name: unknown_workflow_sampler_unet_vae_34
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.894813
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen image 2.1 文生图_2101866858684174338.json, 图片生成/文生图/Qwen image 2.1 文生图_2101882676365062146.json, 图片生成/文生图/Qwen image 2.1 文生图_2101914351019061250.json, 图片生成/文生图/Qwen image 2.1 文生图_2101979658001666049.json, 图片生成/文生图/Qwen image 2.1 文生图_2102020778916147202.json, 图片生成/文生图/Qwen image 2.1 文生图_2102034495846305793.json, 图片生成/文生图/Qwen image 2.1 文生图_2102211603243556865.json, 图片生成/文生图/Qwen image 2.1 文生图_2102236635739017218.json, 图片生成/文生图/Qwen image 2.1 文生图_2102576053557485569.json, 图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json, 图片生成/文生图/Qwen image 2.1 文生图【自动提示词】_2101839874704891906.json, 图片生成/文生图/Qwen image 2.1 文生图提示词增强_2101911095622594562.json, 图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105104996953059329.json, 图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105485714585636866.json, 图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json, 图片生成/文生图/文生图_qwenimage2.1_2101826399211446273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_34

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1 文生图_2101866858684174338.json、图片生成/文生图/Qwen image 2.1 文生图_2101882676365062146.json、图片生成/文生图/Qwen image 2.1 文生图_2101914351019061250.json、图片生成/文生图/Qwen image 2.1 文生图_2101979658001666049.json、图片生成/文生图/Qwen image 2.1 文生图_2102020778916147202.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 14/16 个有
- `SaveImageAdvanced` —— 14/16 个有
- `PrimitiveStringMultiline` —— 5/16 个有
- `Int` —— 1/16 个有
- `JjkText` —— 1/16 个有
- `SeedGeneratorMira` —— 1/16 个有
- `StringToInt` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 16 | 100% |
| 高度 | 1024 | 1024 - 1024 | 16 | 100% |
| 采样步数 | 50 | 25 - 50 | 16 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 25 - 50，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）

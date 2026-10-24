---
name: unknown_workflow_sampler_unet_vae_148
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.716286
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json, 图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json, 图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json, 图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json, 图片生成/文生图/QWen2.1文生图_2102420206202216450.json, 图片生成/文生图/Qwen Image2.1 全能_2101873993291751425.json, 数字人/数字人/Qwen Image2.1 全能_2102320159447937026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_148

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json、图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json、图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json、图片生成/文生图/QWEN IMAGE 2.1 文生图，带提示词增强_2103073606212341761.json、图片生成/文生图/QWen2.1文生图_2102420206202216450.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `SaveImageAdvanced` —— 5/7 个有
- `TextGenerate` —— 5/7 个有
- `PreviewAny` —— 4/7 个有
- `PrimitiveBoolean` —— 3/7 个有
- `RegexExtract` —— 3/7 个有
- `StringConcatenate` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `JsonExtractString` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `QwenImage21Cache` —— 2/7 个有
- `RegexMatch` —— 2/7 个有
- `StringCompare` —— 2/7 个有
- `ComfyMathExpression` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `TextGenerateLTX2Prompt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 7 | 98% |
| 高度 | 1024 | 1024 - 1920 | 7 | 73% |
| 采样步数 | 25 | 25 - 50 | 7 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，7 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，7 个样本
- 采样步数 中位数 25，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）

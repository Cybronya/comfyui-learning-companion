---
name: unknown_workflow_sampler_unet_vae_89
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7845
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json, 图片生成/图生图/qwen2.1-image-图片编辑_2114193382485618689.json, 图片生成/图生图/【开源】Qwen image 2.1 图片编辑_2102011288636452865.json, 图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json, 图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json, 图片生成/文生图/Qwen Image2.1 全能_2101873993291751425.json, 图片生成/文生图/Qwen Image2.1文生图_2101668523557875714.json, 图片生成/文生图/Qwen Image2.1文生图_2101858341764034561.json, 图片生成/文生图/Qwen Image2.1文生图_2107782937193308162.json, 数字人/数字人/Qwen Image2.1 全能_2102320159447937026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_89

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/Qwen Image2.1文生图_2103745897376079874.json、图片生成/图生图/qwen2.1-image-图片编辑_2114193382485618689.json、图片生成/图生图/【开源】Qwen image 2.1 图片编辑_2102011288636452865.json、图片生成/文生图/(V2)-qwen-image2.1-文生图_2102577741005676545.json、图片生成/文生图/CGD_qwen-image-2.1-rh-t2i_2104813454950486018.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `SaveImageAdvanced` —— 9/10 个有
- `TextGenerate` —— 9/10 个有
- `JsonExtractString` —— 7/10 个有
- `PreviewAny` —— 7/10 个有
- `RegexExtract` —— 7/10 个有
- `StringCompare` —— 6/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `Text` —— 5/10 个有
- `LoadImage` —— 4/10 个有
- `StringConcatenate` —— 3/10 个有
- `BatchImagesNode` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `PrimitiveBoolean` —— 2/10 个有
- `RegexMatch` —— 2/10 个有
- `ComfyMathExpression` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `QwenImage21Cache` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 10 | 98% |
| 高度 | 1024 | 1024 - 1920 | 10 | 76% |
| 采样步数 | 40 | 25 - 40 | 10 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，10 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，10 个样本
- 采样步数 中位数 40，观测区间 25 - 40，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）

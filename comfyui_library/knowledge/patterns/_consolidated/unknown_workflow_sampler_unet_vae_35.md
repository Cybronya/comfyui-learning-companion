---
name: unknown_workflow_sampler_unet_vae_35
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.89625
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1-图生图-V1_2101853390769840130.json, 图片生成/图生图/Qwen image 2.1-图生图-V1_2114660896239874049.json, 图片生成/图生图/Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113.json, 图片生成/图生图/Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101800014677897217.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101884328585285634.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101946565576454146.json, 图片生成/图生图/Qwen image 2.1图片编辑_2101981525330976770.json, 图片生成/图生图/Qwen image 2.1图片编辑_2102013628437319682.json, 图片生成/图生图/Qwen image 2.1图片编辑_2102212076977606658.json, 图片生成/图生图/Qwen image 2.1图片编辑_2102302751672848386.json, 图片生成/图生图/Qwen image 2.1图片编辑_2111737939410640897.json, 图片生成/图生图/Qwen image 2.1图片编辑【自动提示词版】_2101837155051073537.json, 图片生成/图生图/Qwen image 2.1图片编辑（双图）_2101862560432746498.json, 图片生成/图生图/QwenImage2.1-图像编辑换头_2101872643862523905.json, 图片生成/图生图/Qwenimage2.1 图像编辑工作流_2101869615268847617.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_35

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1-图生图-V1_2101853390769840130.json、图片生成/图生图/Qwen image 2.1-图生图-V1_2114660896239874049.json、图片生成/图生图/Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113.json、图片生成/图生图/Qwen image 2.1-多宫格分镜图-V2.2_2101933499191222274.json、图片生成/图生图/Qwen image 2.1图片编辑_2101800014677897217.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 15/16 个有
- `easy showAnything` —— 15/16 个有
- `BatchImagesNode` —— 13/16 个有
- `SaveImageAdvanced` —— 12/16 个有
- `ImageConcatMulti` —— 9/16 个有
- `PrimitiveStringMultiline` —— 5/16 个有
- `StringConcatenate` —— 5/16 个有
- `ZNGB_ImageBatchMulti` —— 3/16 个有
- `PrimitiveBoolean` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `GetImageSize` —— 1/16 个有
- `Int` —— 1/16 个有
- `NanFengH3LimitImageLongEdge` —— 1/16 个有
- `RHLLMChatNode` —— 1/16 个有
- `Text` —— 1/16 个有
- `TextInput_` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 30 - 50 | 16 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 16 | 100% |
| 高度 | 1024 | 1024 - 1024 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 30 - 50，16 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）

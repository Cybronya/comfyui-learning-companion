---
name: unknown_workflow_sampler_unet_vae_157
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.883143
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889.json, 图片生成/图生图/一键扩图！电商必备！超快！_2103068831634771970.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105647767073935362.json, 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json, 图片生成/图生图/模特换装 Model Outfit Changes Qwen+Image+2.1+图片换装_2105094118673309698.json, 图片生成/文生图/AI换装丨Qwen-Image 2.1丨双图试穿·智能提示词_2108075858605993985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_157

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/【API】Qwen-Image2.1图像编辑（提示词反推）_2111987132129701889.json、图片生成/图生图/一键扩图！电商必备！超快！_2103068831634771970.json、图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json、图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105647767073935362.json、图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2105680844940734465.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 6/7 个有
- `TextGenerateLTX2Prompt` —— 6/7 个有
- `easy imageConcat` —— 3/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `TextGenerate` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 40 - 50 | 7 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1088 | 7 | 98% |
| 高度 | 1024 | 1024 - 1920 | 7 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 40 - 50，7 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1088，7 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，7 个样本

---
name: text_to_image_controlnet_sampler_clip_2
type: Text To Image
frequency: 6
level: moderate
coverage: 0.647
common_nodes: [CLIPTextEncode, CR Text Concatenate, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: [CR Text, CR Text Concatenate, easy imageSize]
members: [图片生成/文生图/1978394953720156161.json, 图片生成/文生图/1978737989356556290.json, 图片生成/文生图/1982352014791319553.json, 图片生成/文生图/1982688056933269506.json, 图片生成/文生图/1985325068840484866.json, 图片生成/文生图/SDXL文生图+Contronnet控制工作流_2106560364379987969.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1978394953720156161.json、图片生成/文生图/1978737989356556290.json、图片生成/文生图/1982352014791319553.json、图片生成/文生图/1982688056933269506.json、图片生成/文生图/1985325068840484866.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `LoraLoader` —— 5/6 个有
- `CannyEdgePreprocessor` —— 4/6 个有
- `ControlNetApplyAdvanced` —— 4/6 个有
- `DepthAnythingPreprocessor` —— 4/6 个有
- `OpenposePreprocessor` —— 4/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `ControlNetApplySD3` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `TextInputBasic` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `JjkText` —— 1/6 个有
- `VAEEncode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 5 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 776 | 768 - 1024 | 6 | 86% |
| 高度 | 1024 | 1024 - 2048 | 6 | 68% |
| 采样步数 | 25 | 20 - 30 | 6 | 87% |
| Prompt 约束强度(CFG) | 5.25 | 3.1 - 8 | 6 | 72% |
| 采样算法 | dpmpp_2m | - | 6 | 67% |
| 调度器 | karras | - | 6 | 50% |
| 重绘幅度 | 1 | 0.65 - 1 | 6 | 86% |
| ControlNet 权重 | 0.85 | 0.5 - 1 | 6 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 776，观测区间 768 - 1024，6 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 2048，6 个样本
- 采样步数 中位数 25，观测区间 20 - 30，6 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 5.25，观测区间 3.1 - 8，6 个样本
- 采样算法 最常用 dpmpp_2m，6 个样本，一致性 67%
- 调度器 最常用 karras，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.65 - 1，6 个样本，取值集中（一致性 86%）
- ControlNet 权重 中位数 0.85，观测区间 0.5 - 1，6 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、easy imageSize

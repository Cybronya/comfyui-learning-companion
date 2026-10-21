---
name: text_to_image_controlnet_sampler_clip_2
type: Text To Image
frequency: 8
level: moderate
coverage: 0.6765
common_nodes: [CLIPTextEncode, CR Text Concatenate, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: [CR Text, CR Text Concatenate, easy imageSize]
members: [图片生成/文生图/1978394953720156161.json, 图片生成/文生图/1978737989356556290.json, 图片生成/文生图/1982352014791319553.json, 图片生成/文生图/1982688056933269506.json, 图片生成/文生图/1985325068840484866.json, 图片生成/文生图/SDXL文生图+Controlnet控制工作流_1990346536599080961.json, 图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_2007712583985405954.json, 图片生成/文生图/SDXL文生图+Contronnet控制工作流_2106560364379987969.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1978394953720156161.json、图片生成/文生图/1978737989356556290.json、图片生成/文生图/1982352014791319553.json、图片生成/文生图/1982688056933269506.json、图片生成/文生图/1985325068840484866.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/8 个有
- `LoraLoader` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `CannyEdgePreprocessor` —— 6/8 个有
- `DepthAnythingPreprocessor` —— 6/8 个有
- `OpenposePreprocessor` —— 6/8 个有
- `ShowText|pysssss` —— 5/8 个有
- `ControlNetApplyAdvanced` —— 4/8 个有
- `ControlNetApplySD3` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `TextInputBasic` —— 4/8 个有
- `easy imageSize` —— 4/8 个有
- `AIO_Preprocessor` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `VAEEncode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 7 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 768 | 768 - 1024 | 8 | 87% |
| 高度 | 1024 | 1024 - 2048 | 8 | 71% |
| 采样步数 | 27.5 | 20 - 30 | 8 | 87% |
| Prompt 约束强度(CFG) | 5 | 3.1 - 8 | 8 | 75% |
| 采样算法 | dpmpp_2m | - | 8 | 75% |
| 调度器 | sgm_uniform | - | 8 | 50% |
| 重绘幅度 | 1 | 0.65 - 1 | 8 | 88% |
| ControlNet 权重 | 0.7 | 0.5 - 1 | 8 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，7 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1024，8 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 2048，8 个样本
- 采样步数 中位数 27.5，观测区间 20 - 30，8 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 3.1 - 8，8 个样本
- 采样算法 最常用 dpmpp_2m，8 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.65 - 1，8 个样本，取值集中（一致性 88%）
- ControlNet 权重 中位数 0.7，观测区间 0.5 - 1，8 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、easy imageSize

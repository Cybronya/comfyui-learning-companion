---
name: text_to_image_controlnet_lora_sampler_6
type: Text To Image
frequency: 5
level: strong
coverage: 0.731
common_nodes: [CLIPTextEncode, CR Text, CR Text Concatenate, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetLoader, DepthAnythingPreprocessor, EmptyLatentImage, KSampler, LoadImage, LoraLoader, OpenposePreprocessor, SaveImage, ShowText|pysssss, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/SDXL文生图+Controlnet控制工作流_1990346536599080961.json, 图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_1985325068840484866.json, 图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_2007712583985405954.json, 图片生成/文生图/SDXL文生图+Contronnet控制工作流_2106560364379987969.json, 图片生成/文生图/文生图+图生图（写实人像高度控制）_1978394953720156161.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/SDXL文生图+Controlnet控制工作流_1990346536599080961.json、图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_1985325068840484866.json、图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_2007712583985405954.json、图片生成/文生图/SDXL文生图+Contronnet控制工作流_2106560364379987969.json、图片生成/文生图/文生图+图生图（写实人像高度控制）_1978394953720156161.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `OpenposePreprocessor`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplySD3` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `TextInputBasic` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `ControlNetApplyAdvanced` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 5 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 30 | 25 - 30 | 5 | 93% |
| Prompt 约束强度(CFG) | 5 | 5 - 8 | 5 | 79% |
| 采样算法 | dpmpp_2m | - | 5 | 80% |
| 调度器 | sgm_uniform | - | 5 | 80% |
| 重绘幅度 | 1 | 0.65 - 1 | 5 | 85% |
| ControlNet 权重 | 0.7 | 0.7 - 1 | 5 | 84% |
| 宽度 | 768 | 768 - 1024 | 5 | 88% |
| 高度 | 1024 | 1024 - 2048 | 5 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，5 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 25 - 30，5 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 8，5 个样本
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.65 - 1，5 个样本，取值集中（一致性 85%）
- ControlNet 权重 中位数 0.7，观测区间 0.7 - 1，5 个样本，取值集中（一致性 84%）
- 宽度 中位数 768，观测区间 768 - 1024，5 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 2048，5 个样本

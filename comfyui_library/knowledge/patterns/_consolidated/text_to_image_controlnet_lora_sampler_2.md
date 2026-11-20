---
name: text_to_image_controlnet_lora_sampler_2
type: Text To Image
frequency: 9
level: strong
coverage: 0.728
common_nodes: [CLIPTextEncode, CR Text, CR Text Concatenate, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetLoader, DepthAnythingPreprocessor, EmptyLatentImage, KSampler, LoadImage, LoraLoader, OpenposePreprocessor, SaveImage, ShowText|pysssss, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/线稿、CAD绘图姿态深度多维度上色渲染-SZ_2115321385143848961.json, 图片生成/文生图/SDXL文生图+Controlnet控制工作流_1990346536599080961.json, 图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_1985325068840484866.json, 图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_2007712583985405954.json, 图片生成/文生图/SDXL文生图+Contronnet控制工作流_2106560364379987969.json, 图片生成/文生图/文生图+图生图（写实人像高度控制）_1978394953720156161.json, 图片生成/文生图/线稿、CAD绘图姿态深度多维度上色渲染-SZ_2044626375784538113.json, 平台全量/SDXL文生图+Controlnet控制工作流_1916037911018672129.json, 平台全量/工作流项目篇1-线稿上色-Controlnet控制工作流（合集）_2016406118397906945.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/线稿、CAD绘图姿态深度多维度上色渲染-SZ_2115321385143848961.json、图片生成/文生图/SDXL文生图+Controlnet控制工作流_1990346536599080961.json、图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_1985325068840484866.json、图片生成/文生图/SDXL文生图+Controlnet控制工作流（合集）_2007712583985405954.json、图片生成/文生图/SDXL文生图+Contronnet控制工作流_2106560364379987969.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ControlNetApplySD3` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `TextInputBasic` —— 8/9 个有
- `easy imageSize` —— 8/9 个有
- `ControlNetApplyAdvanced` —— 1/9 个有
- `VAEEncode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 9 | 92% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |
| ControlNet 权重 | 0.7 | 0.7 - 1 | 9 | 87% |
| 宽度 | 768 | 768 - 1024 | 9 | 90% |
| 高度 | 1024 | 1024 - 2048 | 9 | 72% |
| 采样步数 | 30 | 25 - 30 | 9 | 95% |
| Prompt 约束强度(CFG) | 5 | 5 - 8 | 9 | 82% |
| 采样算法 | dpmpp_2m | - | 9 | 89% |
| 调度器 | sgm_uniform | - | 9 | 89% |
| 重绘幅度 | 1 | 0.65 - 1 | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，9 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，观测区间 0.7 - 1，9 个样本，取值集中（一致性 87%）
- 宽度 中位数 768，观测区间 768 - 1024，9 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 1024 - 2048，9 个样本
- 采样步数 中位数 30，观测区间 25 - 30，9 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 8，9 个样本，取值集中（一致性 82%）
- 采样算法 最常用 dpmpp_2m，9 个样本，一致性 89%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.65 - 1，9 个样本，取值集中（一致性 89%）

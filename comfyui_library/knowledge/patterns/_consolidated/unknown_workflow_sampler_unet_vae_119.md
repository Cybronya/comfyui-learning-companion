---
name: unknown_workflow_sampler_unet_vae_119
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8956
common_nodes: [CLIPLoader, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑（单图_提示词增强)_2117158723134251010.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑（多图编辑)_2117177935034667010.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346.json, 图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2113099904515137538.json, 图片生成/图生图/Qwen2.1图像编辑_（无PE）_2103535325745336321.json, 图片生成/图生图/qwenimage2.0编辑图片_2101937853101076481.json, 平台全量/Qwen-Image-2.1 一键抠图｜透明背景｜人像抠图 _ 产品换背景_2117618388699795457.json, 平台全量/Qwen-Image-2.1_图像编辑单图_提示词增强)_2117407730624458754.json, 平台全量/Qwen-Image-2.1_图像编辑（单图_提示词增强)_2117483572968902657.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_119

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1 一键抠图｜透明背景｜自动识别主体 _ 电商产品照_2103702044094853121.json、图片生成/图生图/Qwen-Image-2.1 图像编辑（单图_提示词增强)_2117158723134251010.json、图片生成/图生图/Qwen-Image-2.1 图像编辑（多图编辑)_2117177935034667010.json、图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2112762662135353346.json、图片生成/图生图/Qwen-Image-2.1 图像编辑（最新模型）_2113099904515137538.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/10 个有
- `TextInput_` —— 6/10 个有
- `RHHiddenNodes` —— 4/10 个有
- `TextGenerate` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `easy seed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 10 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，10 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）

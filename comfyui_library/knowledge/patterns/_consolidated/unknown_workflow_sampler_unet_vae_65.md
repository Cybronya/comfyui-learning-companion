---
name: unknown_workflow_sampler_unet_vae_65
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.884077
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json, 图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json, 图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json, 图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json, 图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json, 图片生成/文生图/qwen-image2.1-文生图_2105500926474801154.json, 图片生成/文生图/qwen_image_2_1_t2i_2101938471274369025.json, 图片生成/文生图/qwen_image_2_1_文生图_2101842315596886018.json, 图片生成/文生图/qwen_image_2_1文生图_2101884688183947265.json, 图片生成/文生图/▶Qwen-image21-生图_2112039123488960513.json, 图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json, 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json, 数字人/数字人/Qwen Image 2.1 文生图 T2I_2101822255830495234.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_65

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json、图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json、图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json、图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json、图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 11/13 个有
- `SaveImageAdvanced` —— 8/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `TextGenerateLTX2Prompt` —— 4/13 个有
- `PreviewAny` —— 3/13 个有
- `Label (rgthree)` —— 1/13 个有
- `Seed (rgthree)` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 13 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 1024 - 2048 | 13 | 75% |
| 高度 | 1024 | 1024 - 2048 | 13 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，13 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2048，13 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，13 个样本

---
name: unknown_workflow_sampler_unet_vae_171
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.885667
common_nodes: [CLIPLoader, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: ["图片生成/图生图/qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826.json", 图片生成/图生图/qwen_image_2.1 _ 图像编辑_2103129784736903169.json, 图片生成/图生图/qwenimage2.0编辑图片_2101937853101076481.json, 图片生成/图生图/人物照片六种精修工具_2109075675494834178.json, 图片生成/图生图/六种风格_2108026478259691522.json, 图片生成/图生图/林茜数字人_Qwen 2.1换脸工作流_2112738971427106817.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_171

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/qwen 2.1 人像瘦脸祛痘磨皮美白 Face Slimming, Acne Removal, S_2109441353208909826.json、图片生成/图生图/qwen_image_2.1 _ 图像编辑_2103129784736903169.json、图片生成/图生图/qwenimage2.0编辑图片_2101937853101076481.json、图片生成/图生图/人物照片六种精修工具_2109075675494834178.json、图片生成/图生图/六种风格_2108026478259691522.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 40 | 6 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 43% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 40，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_lora_sampler_unet_137
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.845
common_nodes: [CLIPLoader, Image Comparer (rgthree), ImageScaleToMaxDimension, ImageScaleToTotalPixels, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, QwenImageIntegratedKSampler, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEEncode, VAELoader, easy cleanGpuUsed, easy int]
problems: []
missing: []
members: [图片生成/图生图/Qwen2511-丰胸神器（加强版）_2057705373263556610.json, 图片生成/图生图/Qwen2511丰胸神器，胸部增强编辑加强版_2054181669988519938.json, 图片生成/图生图/Qwen2511丰胸神器，胸部增强编辑加强版_2057650794018729985.json, 图片生成/图生图/qwen2511丰胸神器，胸部增强加强版变美！_2045056767100456962.json, 图片生成/图生图/qwen2511丰胸神器，胸部增强，即刻变美！_2036719881151848450.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_137

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen2511-丰胸神器（加强版）_2057705373263556610.json、图片生成/图生图/Qwen2511丰胸神器，胸部增强编辑加强版_2054181669988519938.json、图片生成/图生图/Qwen2511丰胸神器，胸部增强编辑加强版_2057650794018729985.json、图片生成/图生图/qwen2511丰胸神器，胸部增强加强版变美！_2045056767100456962.json、图片生成/图生图/qwen2511丰胸神器，胸部增强，即刻变美！_2036719881151848450.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToMaxDimension`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `QwenImageIntegratedKSampler`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | 0 | 0 - 0 | 5 | 100% |
| 调度器 | 0 | 0 - 0 | 5 | 100% |
| 重绘幅度 | 3.56016e+14 | 1.93667e+14 - 9.19984e+14 | 5 | 37% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 0，观测区间 0 - 0，5 个样本，取值集中（一致性 100%）
- 调度器 中位数 0，观测区间 0 - 0，5 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 3.56016e+14，观测区间 1.93667e+14 - 9.19984e+14，5 个样本，取值分散，一致性仅 37%
- 风险：重绘幅度 观测到 9.19984e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）

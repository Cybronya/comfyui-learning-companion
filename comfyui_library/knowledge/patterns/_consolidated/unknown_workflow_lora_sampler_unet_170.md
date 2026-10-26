---
name: unknown_workflow_lora_sampler_unet_170
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.6835
common_nodes: [CLIPLoader, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978.json, 图片生成/图生图/Qwen image2.1编辑，全能抠图去背景，PNG输出_2114598159891656706.json, 图片生成/图生图/抠图去背景-Qwen image2.1编辑_2110044236191191041.json, 图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_170

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978.json、图片生成/图生图/Qwen image2.1编辑，全能抠图去背景，PNG输出_2114598159891656706.json、图片生成/图生图/抠图去背景-Qwen image2.1编辑_2110044236191191041.json、图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `GetNode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `LoadSharpModel` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `SharpPredict` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `YCGaussianPreview` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 8 | 8 - 30 | 4 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 30，4 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足

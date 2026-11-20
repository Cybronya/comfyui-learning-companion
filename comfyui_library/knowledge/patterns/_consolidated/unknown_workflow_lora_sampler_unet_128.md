---
name: unknown_workflow_lora_sampler_unet_128
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.579333
common_nodes: [CLIPLoader, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978.json, 图片生成/图生图/Qwen image2.1编辑，全能抠图去背景，PNG输出_2114598159891656706.json, 图片生成/图生图/Qwen_image2.1编辑，全能抠图去背景，PNG输出_2115617232339431425.json, 图片生成/图生图/Qwen_image2.1编辑，全能抠图去背景，PNG输出_2115665186186158082.json, 图片生成/图生图/抠图去背景-Qwen image2.1编辑_2110044236191191041.json, 图片生成/图生图/抠图去背景-Qwen image2.1编辑_2111019839597932545.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_128

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 ｜图像转换角度（更精准｜高斯泼溅版）图像自由360°旋转角度｜+ QI2.1 AnyAngle LoRA_2113806870229118978.json、图片生成/图生图/Qwen image2.1编辑，全能抠图去背景，PNG输出_2114598159891656706.json、图片生成/图生图/Qwen_image2.1编辑，全能抠图去背景，PNG输出_2115617232339431425.json、图片生成/图生图/Qwen_image2.1编辑，全能抠图去背景，PNG输出_2115665186186158082.json、图片生成/图生图/抠图去背景-Qwen image2.1编辑_2110044236191191041.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
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
- `PrimitiveStringMultiline` —— 5/6 个有
- `GetNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `INTConstant` —— 1/6 个有
- `LoadSharpModel` —— 1/6 个有
- `SharpPredict` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `YCGaussianPreview` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 8 | 8 - 30 | 6 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 30，6 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足

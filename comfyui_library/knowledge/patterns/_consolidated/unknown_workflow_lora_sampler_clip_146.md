---
name: unknown_workflow_lora_sampler_clip_146
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8264
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler (Efficient), LayerFilter: HDREffects, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241.json, 图片生成/图生图/一键运行：z-image 局部重绘 图像控制最新CN_2002260940475252737.json, 平台全量/一键运行：qwen image   canny  控制 、图像编辑、上色、线稿_1959862756956647426.json, 平台全量/千问 qwen image inpaint 局部重绘，图像修改，洗图_1960168822827331585.json, 平台全量/千问深度_1960162318527180802.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_146

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241.json、图片生成/图生图/一键运行：z-image 局部重绘 图像控制最新CN_2002260940475252737.json、平台全量/一键运行：qwen image   canny  控制 、图像编辑、上色、线稿_1959862756956647426.json、平台全量/千问 qwen image inpaint 局部重绘，图像修改，洗图_1960168822827331585.json、平台全量/千问深度_1960162318527180802.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `QwenImageDiffsynthControlnet` —— 3/5 个有
- `Anything Everywhere` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ZImageFunControlnet` —— 2/5 个有
- `Prompts Everywhere` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 20 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

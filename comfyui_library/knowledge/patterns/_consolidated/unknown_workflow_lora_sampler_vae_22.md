---
name: unknown_workflow_lora_sampler_vae_22
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.554
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, GetNode, Image Comparer (rgthree), KSampler (Efficient), LayerFilter: HDREffects, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, NunchakuQwenImageLoraLoader, PreviewImage, SaveImage, SetNode, TextEncodeQwenImageEditPlus_lrzjason, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/edit-2509-lightningv2.0-8steps 单图编辑 一致性 便宜 图生图_1989150846225100801.json, 图片生成/图生图/一键运行：镜头转换，qwen图生图，角度转换_1994681338747817985.json, 平台全量/一键运行：QWEN产品换背景 局部重绘_1989160241793208321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/edit-2509-lightningv2.0-8steps 单图编辑 一致性 便宜 图生图_1989150846225100801.json、图片生成/图生图/一键运行：镜头转换，qwen图生图，角度转换_1994681338747817985.json、平台全量/一键运行：QWEN产品换背景 局部重绘_1989160241793208321.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `NunchakuQwenImageLoraLoader`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `BiRefNet_Hugo` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy promptLine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_inpaint_lora_sampler_38
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.870667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), InpaintCrop, InpaintStitch, KSampler, Kontext Inpainting Conditioning, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-dev局部重绘(中文版)_1954845295475605506.json, 图片生成/图生图/Kontext_局部重绘优化版_1943954881646563330.json, 图片生成/图生图/🍡Kontext_局部重绘优化版🥘_1943851109633101826.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext-dev局部重绘(中文版)_1954845295475605506.json、图片生成/图生图/Kontext_局部重绘优化版_1943954881646563330.json、图片生成/图生图/🍡Kontext_局部重绘优化版🥘_1943851109633101826.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `InpaintCrop`
- `InpaintStitch`
- `KSampler`
- `Kontext Inpainting Conditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `preview_mask` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 28 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 28，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

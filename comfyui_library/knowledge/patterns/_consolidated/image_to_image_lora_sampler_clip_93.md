---
name: image_to_image_lora_sampler_clip_93
type: Image To Image
frequency: 3
level: strong
coverage: 0.812
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, FluxKontextImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext LoRA _ 电商海报物品替换_1946544312379432962.json, 图片生成/图生图/Kontext 一键溶图、换头、换背景_1966380464816762882.json, 图片生成/图生图/Kontext产品溶图lora【基础流】_1946870484107714562.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext LoRA _ 电商海报物品替换_1946544312379432962.json、图片生成/图生图/Kontext 一键溶图、换头、换背景_1966380464816762882.json、图片生成/图生图/Kontext产品溶图lora【基础流】_1946870484107714562.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `InspyrenetRembgAdvanced` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/3 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `SDVN Any Show` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TextInputBasic` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

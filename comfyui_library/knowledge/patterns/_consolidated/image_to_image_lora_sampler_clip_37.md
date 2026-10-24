---
name: image_to_image_lora_sampler_clip_37
type: Image To Image
frequency: 7
level: strong
coverage: 0.798
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FastCanvas, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_LLMAPI_NODE, ReferenceLatent, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext图像参考追色_1946826407948218369.json, 图片生成/图生图/Kontext LoRA _ 电商海报物品替换_1946544312379432962.json, 图片生成/图生图/Kontext优化精准移除物体_1945338596477870082.json, 图片生成/图生图/kontext-dev创程式填充_1942603916720672769.json, 图片生成/图生图/kontext-dev填_1942841076824608770.json, 图片生成/图生图/kontext-dev红框标记新玩法_1942839973647159298.json, 图片生成/图生图/kontext-dev超越PS创程式填充_1942838696930381825.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux Kontext图像参考追色_1946826407948218369.json、图片生成/图生图/Kontext LoRA _ 电商海报物品替换_1946544312379432962.json、图片生成/图生图/Kontext优化精准移除物体_1945338596477870082.json、图片生成/图生图/kontext-dev创程式填充_1942603916720672769.json、图片生成/图生图/kontext-dev填_1942841076824608770.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FastCanvas`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `DeepTranslatorTextNode` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `CR Latent Batch Size` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `LayerMask: MaskPreview` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `FastCanvasTool` —— 2/7 个有
- `RMBG` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PDIMAGE_LongerSize` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `TeaCache` —— 1/7 个有
- `TextInputBasic` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 21 | 7 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 21，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）

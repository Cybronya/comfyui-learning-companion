---
name: image_to_image_sampler_clip_unet_4
type: Image To Image
frequency: 5
level: strong
coverage: 0.8472
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, ConstrainImage|pysssss]
members: [图片生成/图生图/2088607792931360770.json, 图片生成/文生图/1938493107786964994.json, 图片生成/文生图/1938509637782011905.json, 图片生成/文生图/1938830456097792001.json, 图片生成/文生图/1940231458583695361.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2088607792931360770.json、图片生成/文生图/1938493107786964994.json、图片生成/文生图/1938509637782011905.json、图片生成/文生图/1938830456097792001.json、图片生成/文生图/1940231458583695361.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `RH_Translator` —— 4/5 个有
- `ConstrainImage|pysssss` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_ComfyFluxKontext` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 20 | 20 - 25 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline、ConstrainImage|pysssss

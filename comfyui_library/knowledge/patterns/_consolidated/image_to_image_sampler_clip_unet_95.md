---
name: image_to_image_sampler_clip_unet_95
type: Image To Image
frequency: 5
level: strong
coverage: 0.8534
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Kontext奇技淫巧之高清放大（细节拉满效果逆天）_1940033039915421698.json, 图片生成/图生图/Kontext高清放大_1944620173674336258.json, 图片生成/图生图/flux_kontext_dev_一秒变自拍_1941803812078383105.json, 图片生成/图生图/千府AI-FLUX Kontext 图片去水印工作流_1929384205183041538.json, 图片生成/图生图/🔎kontext 🔍【一键】高清修复，人像专用保持人像完全一致_1960521386806734849.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_95

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext奇技淫巧之高清放大（细节拉满效果逆天）_1940033039915421698.json、图片生成/图生图/Kontext高清放大_1944620173674336258.json、图片生成/图生图/flux_kontext_dev_一秒变自拍_1941803812078383105.json、图片生成/图生图/千府AI-FLUX Kontext 图片去水印工作流_1929384205183041538.json、图片生成/图生图/🔎kontext 🔍【一键】高清修复，人像专用保持人像完全一致_1960521386806734849.json）

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
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `DF_Image_scale_to_side` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/5 个有
- `SUPIR_Upscale` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

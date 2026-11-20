---
name: image_to_image_sampler_clip_unet_32
type: Image To Image
frequency: 12
level: strong
coverage: 0.904833
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/老照片修复上色_1989170437110239233.json, 图片生成/图生图/老照片修复工作流_1974678865857613826.json, 图片生成/图生图/老照片修复应用版_1946064147912028161.json, 图片生成/图生图/老照片修复（最新版）_1985485008938876929.json, 图片生成/图生图/老照片修复｜人物版本_1952543895152463873.json, 图片生成/图生图/老照片废片修复_1942881233481478145.json, 图片生成/图生图/耳坠戒指万物穿戴_Kontext溶图V4_1947257451781443585.json, 图片生成/图生图/自己用：像素风转绘_1947475142944395266.json, 图片生成/文生图/人物换头写真工作流_1954452296111407106.json, 图片生成/文生图/电商手持商品 - Kontext-LORA_1953728095478009857.json, 图片生成/文生图/电商手持商品-_Kontext-LORA_1953730285512916993.json, 平台全量/003.首饰穿戴_2004254933476147201.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_32

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/老照片修复上色_1989170437110239233.json、图片生成/图生图/老照片修复工作流_1974678865857613826.json、图片生成/图生图/老照片修复应用版_1946064147912028161.json、图片生成/图生图/老照片修复（最新版）_1985485008938876929.json、图片生成/图生图/老照片修复｜人物版本_1952543895152463873.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 11/12 个有
- `Text Multiline` —— 11/12 个有
- `PreviewImage` —— 9/12 个有
- `RepeatLatentBatch` —— 9/12 个有
- `ShowText|pysssss` —— 9/12 个有
- `ImageStitch` —— 8/12 个有
- `GoogleTranslateTextNode` —— 7/12 个有
- `FastCanvas` —— 5/12 个有
- `FastCanvasTool` —— 5/12 个有
- `ImageConcatMulti` —— 5/12 个有
- `ImageScaleDownToSize` —— 4/12 个有
- `RMBG` —— 4/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `AILab_MaskPreview` —— 1/12 个有
- `CropByMask` —— 1/12 个有
- `DF_Text_Box` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `Image Rembg (Remove Background)` —— 1/12 个有
- `LayerMask: PersonMaskUltra V2` —— 1/12 个有
- `LayerUtility: CropByMask V2` —— 1/12 个有
- `RH_Translator` —— 1/12 个有
- `TTP_Expand_And_Mask` —— 1/12 个有
- `Text Concatenate` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）

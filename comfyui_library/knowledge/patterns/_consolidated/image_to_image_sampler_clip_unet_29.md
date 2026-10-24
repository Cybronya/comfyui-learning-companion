---
name: image_to_image_sampler_clip_unet_29
type: Image To Image
frequency: 11
level: strong
coverage: 0.915818
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/老照片修复上色_1989170437110239233.json, 图片生成/图生图/老照片修复应用版_1946064147912028161.json, 图片生成/图生图/老照片修复（最新版）_1985485008938876929.json, 图片生成/图生图/老照片修复｜人物版本_1952543895152463873.json, 图片生成/图生图/老照片废片修复_1942881233481478145.json, 图片生成/图生图/耳坠戒指万物穿戴_Kontext溶图V4_1947257451781443585.json, 图片生成/图生图/自己用：像素风转绘_1947475142944395266.json, 图片生成/图生图/超强老照片修复_1985490139109597185.json, 图片生成/图生图/超越IPAdapter风格迁移_Kontext-DEV开源ComfyUI官方版_1938278011328204801.json, 图片生成/图生图/风格转绘_Kontext-DEV_1938521459012599810.json, 图片生成/图生图/风格迁移_KontextComfyUI官方版_1958049410267623425.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_29

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/老照片修复上色_1989170437110239233.json、图片生成/图生图/老照片修复应用版_1946064147912028161.json、图片生成/图生图/老照片修复（最新版）_1985485008938876929.json、图片生成/图生图/老照片修复｜人物版本_1952543895152463873.json、图片生成/图生图/老照片废片修复_1942881233481478145.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 10/11 个有
- `ShowText|pysssss` —— 10/11 个有
- `ImageConcatMulti` —— 9/11 个有
- `GoogleTranslateTextNode` —— 8/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `PreviewImage` —— 8/11 个有
- `RepeatLatentBatch` —— 5/11 个有
- `LoaderGGUF` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `FastCanvas` —— 1/11 个有
- `FastCanvasTool` —— 1/11 个有
- `Image Rembg (Remove Background)` —— 1/11 个有
- `ImageScaleDownToSize` —— 1/11 个有
- `RH_Captioner` —— 1/11 个有
- `Text Concatenate` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）

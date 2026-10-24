---
name: image_to_image_sampler_clip_unet_37
type: Image To Image
frequency: 9
level: strong
coverage: 0.920333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GoogleTranslateTextNode, ImageConcatMulti, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext Dev二阶段换装工作流V1（提高成功率）_1939271936381992962.json, 图片生成/图生图/Kontext-DEV一键三视图_1939869541839052801.json, 图片生成/图生图/Kontext-DEV一键三视图_1951214560822931457.json, 图片生成/图生图/Kontext-DEV人物、产品换背景 产品一致性工作流   效果很不错_1967778723778932737.json, 图片生成/图生图/Kontext-Emoj风格转换_1951268420702646274.json, 图片生成/图生图/智能水印擦除_Kontext-DEV图像编辑_1938936115401252866.json, 图片生成/图生图/毛坯房精装方案设计图_Kontext-DEV图像编辑_1938944918020612098.json, 图片生成/图生图/电商服装加模特_Kontext-DEV开源ComfyUI官方版_1938390435477786625.json, 图片生成/图生图/线稿提取_Kontext-DEV图像编辑_1938971620017164289.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux Kontext Dev二阶段换装工作流V1（提高成功率）_1939271936381992962.json、图片生成/图生图/Kontext-DEV一键三视图_1939869541839052801.json、图片生成/图生图/Kontext-DEV一键三视图_1951214560822931457.json、图片生成/图生图/Kontext-DEV人物、产品换背景 产品一致性工作流   效果很不错_1967778723778932737.json、图片生成/图生图/Kontext-Emoj风格转换_1951268420702646274.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GoogleTranslateTextNode`
- `ImageConcatMulti`
- `ImageStitch`
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
- `LoraLoaderModelOnly` —— 8/9 个有
- `ShowText|pysssss` —— 8/9 个有
- `PreviewImage` —— 6/9 个有
- `LoaderGGUF` —— 5/9 个有
- `easy showAnything` —— 2/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `ImagePadForOutpaint` —— 1/9 个有
- `LoadLatent` —— 1/9 个有
- `MZ_Flux1PartialLoad_Patch` —— 1/9 个有
- `MagCache` —— 1/9 个有
- `PMRF` —— 1/9 个有
- `SaveLatent` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）

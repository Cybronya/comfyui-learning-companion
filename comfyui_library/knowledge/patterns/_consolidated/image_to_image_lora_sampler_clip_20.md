---
name: image_to_image_lora_sampler_clip_20
type: Image To Image
frequency: 11
level: strong
coverage: 0.908727
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键去人（去掉人物只留衣服）单图_1980916752647409665.json, 图片生成/图生图/一键精修_2076038023472566274.json, 图片生成/图生图/万物擦除_Kontext-DEV图像编辑_1938902253212520450.json, 图片生成/图生图/万物擦除之Kontext-DEV精准区域编辑_1940637803657015297.json, 图片生成/图生图/万物毛毡_Kontext-DEV-LORA_1940660615935586306.json, 图片生成/图生图/人物换背景_Kontext-DEV图像编辑_1938939080438636546.json, 图片生成/图生图/修复老照片（新版）_1988514615141253122.json, 图片生成/图生图/像素风转绘_Kontext-DEV-LORA_1940668432364843010.json, 图片生成/图生图/去人留衣服白底图(单图)_1980917486336000002.json, 平台全量/Kontext精准控制技巧_1940545879491375106.json, 平台全量/万物擦除_Kontext-DEV精准区域编辑_1940153094753701890.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/一键去人（去掉人物只留衣服）单图_1980916752647409665.json、图片生成/图生图/一键精修_2076038023472566274.json、图片生成/图生图/万物擦除_Kontext-DEV图像编辑_1938902253212520450.json、图片生成/图生图/万物擦除之Kontext-DEV精准区域编辑_1940637803657015297.json、图片生成/图生图/万物毛毡_Kontext-DEV-LORA_1940660615935586306.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 10/11 个有
- `ShowText|pysssss` —— 10/11 个有
- `Text Multiline` —— 10/11 个有
- `ImageConcatMulti` —— 8/11 个有
- `ImageStitch` —— 8/11 个有
- `PreviewImage` —— 7/11 个有
- `GoogleTranslateTextNode` —— 4/11 个有
- `ConstrainImage|pysssss` —— 3/11 个有
- `ImageAndMaskPreview` —— 3/11 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `Anything Everywhere3` —— 1/11 个有
- `GetImageSize+` —— 1/11 个有
- `ImageCompositeMasked` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `LayerUtility: ColorImage` —— 1/11 个有
- `LayerUtility: ExtendCanvas` —— 1/11 个有
- `LoaderGGUF` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 11 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，11 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）

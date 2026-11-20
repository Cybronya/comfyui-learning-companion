---
name: image_to_image_lora_sampler_clip_13
type: Image To Image
frequency: 13
level: strong
coverage: 0.910154
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/kontext电商服装展示工作流_1941300697810026498.json, 平台全量/动漫转绘真人_Kontext-DEV-LORA_1940709122679664642.json, 平台全量/取衣去人(只保留衣服)去人留衣_1991386512723935234.json, 平台全量/图像马赛克去除_Kontext-DEV_1940723813879541761.json, 平台全量/图像高清去模糊_Kontext-LORA_1940818126143700993.json, 平台全量/旧照片修复(超牛)_1949841545701801985.json, 平台全量/老照片修复2.0_1980082978510508033.json, 平台全量/老照片修复_1955485281317261314.json, 平台全量/老照片修复_2000106070825631745.json, 平台全量/虚拟穿衣_电商服装展示_kontext-tryon-LORA_1941107680213942273.json, 平台全量/高清真实照片_Kontext-dev_1944345547257860097.json, 数字人/数字人/kontext 真实人物照片转动漫卡通风格_1943493630646493185.json, 视频生成/图生视频/Flux 去除马赛克_1994289242960576513.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/kontext电商服装展示工作流_1941300697810026498.json、平台全量/动漫转绘真人_Kontext-DEV-LORA_1940709122679664642.json、平台全量/取衣去人(只保留衣服)去人留衣_1991386512723935234.json、平台全量/图像马赛克去除_Kontext-DEV_1940723813879541761.json、平台全量/图像高清去模糊_Kontext-LORA_1940818126143700993.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 12/13 个有
- `ShowText|pysssss` —— 12/13 个有
- `ImageConcatMulti` —— 10/13 个有
- `PreviewImage` —— 8/13 个有
- `EmptySD3LatentImage` —— 6/13 个有
- `GetImageSizeAndCount` —— 6/13 个有
- `RepeatLatentBatch` —— 6/13 个有
- `GoogleTranslateTextNode` —— 4/13 个有
- `ImageScaleDownToSize` —— 3/13 个有
- `RMBG` —— 2/13 个有
- `SaveLatent` —— 2/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `ImageAndMaskPreview` —— 1/13 个有
- `SetNode` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 13 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，13 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）

---
name: image_to_image_upscale_sampler_clip_5
type: Image To Image
frequency: 22
level: strong
coverage: 0.878545
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GoogleTranslateTextNode, ImageListToImageBatch, ImageScaleBy, ImageStitch, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LoadImage, PreviewImage, ReferenceLatent, RepeatLatentBatch, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/(工作流可4K高清)泛黄老照片一键修复，留住瞬间永恒，忘不了的记忆~更符合东方审美的老照片修复_2047510654663266305.json, 图片生成/图生图/Kontext老照片修复黑白上色，FULLHD还原_1989227539405090817.json, 图片生成/图生图/东方美学老照片修复(工作流可4K高清)_2029463740457947137.json, 图片生成/图生图/国人东方审美标准的老旧照片修复上色处理高清_2068601390448078849.json, 图片生成/图生图/更符合东方审美的老照片修复(工作流可4K高清)_1941993225135800322.json, 图片生成/图生图/更符合东方审美的老照片修复(工作流可4K高清)_1996012157898833921.json, 图片生成/图生图/更符合东方审美的老照片修复(工作流可4K高清)_2096174219745910786.json, 图片生成/图生图/更符合东方审美的老照片修复(工作流可4K高清)_2096411297209479170.json, 图片生成/图生图/泛黄老照片一键修复，留住瞬间永恒，忘不了的记忆~更符合东方审美的老照片修复(工作流可4K高清)_2013126773386518529.json, 图片生成/图生图/真实质感老照片修复上色-高清放大(超级还原)_1981738946306678785.json, 图片生成/图生图/老照片一键修复(工作流可4K高清)_2076849498273435649.json, 图片生成/图生图/老照片一键修复(工作流可4K高清)_2076851740254752769.json, 图片生成/图生图/老照片修复  4K高清_2087271082897272834.json, 图片生成/图生图/老照片修复(可4K高清)_2078127845821476865.json, 图片生成/图生图/老照片修复(工作流可4K高清)_2064978436887760897.json, 图片生成/图生图/老照片修复(工作流可4K高清)_2065336001261826049.json, 图片生成/图生图/老照片修复——可4K高清_2034202678267486209.json, 图片生成/图生图/老照片修复器（运行超快省币版）_2029359809782358017.json, 平台全量/泛黄老照片一键修复，留住瞬间永恒，忘不了的记忆~更符合东方审美的老照片修复(工作流可4K高清)_2075872579574915073.json, 平台全量/老照片+智能修复+黑白上色+4K放大_1957308014275522562.json, 平台全量/老照片修复上色+放大（适合10人以下合影）_1988598598428442626.json, 平台全量/老照片高清修复—更符合东方审美+4K高清_2032355572594511873.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/(工作流可4K高清)泛黄老照片一键修复，留住瞬间永恒，忘不了的记忆~更符合东方审美的老照片修复_2047510654663266305.json、图片生成/图生图/Kontext老照片修复黑白上色，FULLHD还原_1989227539405090817.json、图片生成/图生图/东方美学老照片修复(工作流可4K高清)_2029463740457947137.json、图片生成/图生图/国人东方审美标准的老旧照片修复上色处理高清_2068601390448078849.json、图片生成/图生图/更符合东方审美的老照片修复(工作流可4K高清)_1941993225135800322.json…）

- **类型**：Image To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GoogleTranslateTextNode`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageStitch`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 21/22 个有
- `Fast Groups Bypasser (rgthree)` —— 21/22 个有
- `ImageScaleDownToSize` —— 21/22 个有
- `RHHiddenNodes` —— 20/22 个有
- `Image Comparer (rgthree)` —— 3/22 个有
- `LoraLoaderModelOnly` —— 2/22 个有
- `Any Switch (rgthree)` —— 1/22 个有
- `ImageConcatMulti` —— 1/22 个有
- `PlaySound|pysssss` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 22 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | exponential | - | 22 | 86% |
| 重绘幅度 | 0.9 | 0.9 - 1 | 22 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 exponential，22 个样本，一致性 86%
- 重绘幅度 中位数 0.9，观测区间 0.9 - 1，22 个样本，取值集中（一致性 96%）

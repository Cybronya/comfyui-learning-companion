---
name: text_to_image_inpaint_lora_sampler
type: Text To Image
frequency: 9
level: strong
coverage: 0.807889
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, DrawMaskOnImage, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, InpaintCropImproved, InpaintStitchImproved, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, Seed (rgthree), SetLatentNoiseMask, SimpleMath+, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1局部重绘零色差零位移，换头换脸与商品替换高清重绘_2112244498993606658.json, 图片生成/图生图/Qwen image 2.1高分局部重绘｜换头换脸产品替换全能｜零色差零位移保真_2112036472307142658.json, 图片生成/图生图/Qwen image 2.1高分重绘神器｜产品替换零位移不跑偏｜无色差商用级_2112031799219154945.json, 图片生成/图生图/Qwen-Image-2.1遮罩局部重绘V1，指哪改哪精准编辑_2110480100507602946.json, 图片生成/图生图/Qwen-image21功能流｜高分辨率局部编辑加扩图，修图一步到位_2107372752343748609.json, 图片生成/图生图/高分局部重绘产品替换，Qwen image 2.1零位移零色差_2112323089873854465.json, 图片生成/文生图/Qwen Image 2.1黑鹤全功能流｜高分局部编辑+去水印+扩图一板全搞定_2108006501402112001.json, 图片生成/文生图/黑鹤Qwen Image 2.1全功能流高分局部编辑去水印扩图工作流文生图图生图方案_2108679390967197697.json, 图片生成/文生图/黑鹤Qwen Image 2.1全功能流高分局部编辑去水印扩图工作流，文生图图生图方案_2108304277868474369.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1局部重绘零色差零位移，换头换脸与商品替换高清重绘_2112244498993606658.json、图片生成/图生图/Qwen image 2.1高分局部重绘｜换头换脸产品替换全能｜零色差零位移保真_2112036472307142658.json、图片生成/图生图/Qwen image 2.1高分重绘神器｜产品替换零位移不跑偏｜无色差商用级_2112031799219154945.json、图片生成/图生图/Qwen-Image-2.1遮罩局部重绘V1，指哪改哪精准编辑_2110480100507602946.json、图片生成/图生图/Qwen-image21功能流｜高分辨率局部编辑加扩图，修图一步到位_2107372752343748609.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `PreviewImage` —— 5/9 个有
- `Anything Everywhere` —— 4/9 个有
- `GetNode` —— 4/9 个有
- `ImagePadForOutpaint` —— 4/9 个有
- `ImpactInt` —— 4/9 个有
- `JoinImageWithAlpha` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `MaskFillHoles` —— 4/9 个有
- `ResolutionSelector` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `SplitImageWithAlpha` —— 4/9 个有
- `easy imageColorMatch` —— 4/9 个有
- `Any Switch (rgthree)` —— 2/9 个有
- `Int` —— 1/9 个有
- `easy isNone` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足

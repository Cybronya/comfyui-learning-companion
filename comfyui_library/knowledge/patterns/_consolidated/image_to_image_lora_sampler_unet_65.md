---
name: image_to_image_lora_sampler_unet_65
type: Image To Image
frequency: 10
level: moderate
coverage: 0.736
common_nodes: [CLIPLoader, ComfySwitchNode, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/COS自动修图V2版_2114184059889999873.json, 图片生成/图生图/COS自动修图V2版_2114881794200915970.json, 图片生成/图生图/COS自动修图V2版_2115014798000873473.json, 图片生成/图生图/自动COS原图直出版局部重绘_2114641746079608833.json, 图片生成/图生图/自动COS原图直出版局部重绘_2115266941693816833.json, 图片生成/图生图/自动COS原图直出版局部重绘_2115278870340526081.json, 图片生成/图生图/自动COS原图直出版局部重绘_2115299209468538881.json, 图片生成/图生图/自动COS原图直出版（局部重绘）_2108747499723907074.json, 平台全量/Qwen-image2.1-高分局部——编辑_去水印_移除_2108473248110440450.json, 平台全量/自动COS原图直出（厚涂版）_2118241900410003458.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_65

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/COS自动修图V2版_2114184059889999873.json、图片生成/图生图/COS自动修图V2版_2114881794200915970.json、图片生成/图生图/COS自动修图V2版_2115014798000873473.json、图片生成/图生图/自动COS原图直出版局部重绘_2114641746079608833.json、图片生成/图生图/自动COS原图直出版局部重绘_2115266941693816833.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 9/10 个有
- `ConditioningZeroOut` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `KSamplerAdvanced` —— 9/10 个有
- `RH_RhartImageG25FlareImageToImage` —— 9/10 个有
- `ReferenceLatent` —— 9/10 个有
- `DrawMaskOnImage` —— 7/10 个有
- `INTConstant` —— 7/10 个有
- `InpaintCropImproved` —— 7/10 个有
- `InpaintStitchImproved` —— 7/10 个有
- `SetLatentNoiseMask` —— 7/10 个有
- `SimpleMath+` —— 7/10 个有
- `Node Collector (rgthree)` —— 6/10 个有
- `ImageScaleToTotalPixels` —— 4/10 个有
- `JoinImageWithAlpha` —— 3/10 个有
- `SplitImageWithAlpha` —— 3/10 个有
- `easy imageColorMatch` —— 3/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 9 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 31% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，9 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）

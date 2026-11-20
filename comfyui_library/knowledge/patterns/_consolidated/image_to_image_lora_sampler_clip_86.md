---
name: image_to_image_lora_sampler_clip_86
type: Image To Image
frequency: 3
level: strong
coverage: 0.727667
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageResizeKJv2, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, QwenImage21Cache, RH_RhartImageG25FlareImageToImage, ReferenceLatent, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/COS自动修图V2版_2114184059889999873.json, 图片生成/图生图/自动COS原图直出版局部重绘_2114641746079608833.json, 图片生成/图生图/自动COS原图直出版（局部重绘）_2108747499723907074.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/COS自动修图V2版_2114184059889999873.json、图片生成/图生图/自动COS原图直出版局部重绘_2114641746079608833.json、图片生成/图生图/自动COS原图直出版（局部重绘）_2108747499723907074.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `RH_RhartImageG25FlareImageToImage`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `InpaintCropImproved` —— 2/3 个有
- `InpaintStitchImproved` —— 2/3 个有
- `Node Collector (rgthree)` —— 2/3 个有
- `SetLatentNoiseMask` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `JoinImageWithAlpha` —— 1/3 个有
- `SplitImageWithAlpha` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

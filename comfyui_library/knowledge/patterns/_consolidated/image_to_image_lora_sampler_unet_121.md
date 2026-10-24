---
name: image_to_image_lora_sampler_unet_121
type: Image To Image
frequency: 5
level: strong
coverage: 0.7826
common_nodes: [CFGNorm, CLIPLoader, CR Text, ComfySwitchNode, DF_Integer, FluxKontextImageScale, Get Image Size, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactMinMax, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/FireRed-Image-Edit标题修改高清放大_2083847390989213697.json, 图片生成/图生图/P图改字-改标题-数字-高清放大_2081934306439680001.json, 图片生成/图生图/P图改字-改标题-数字-高清放大_2082013592689405954.json, 图片生成/图生图/标题，文字同风格修改！！！_2081574381783969794.json, 图片生成/文生图/标题修改高清放大【御川0710】_2070032013683412994.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_121

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-Edit标题修改高清放大_2083847390989213697.json、图片生成/图生图/P图改字-改标题-数字-高清放大_2081934306439680001.json、图片生成/图生图/P图改字-改标题-数字-高清放大_2082013592689405954.json、图片生成/图生图/标题，文字同风格修改！！！_2081574381783969794.json、图片生成/文生图/标题修改高清放大【御川0710】_2070032013683412994.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ComfySwitchNode`
- `DF_Integer`
- `FluxKontextImageScale`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `SUPIR_Upscale` —— 4/5 个有
- `忽略多组孤海` —— 4/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）

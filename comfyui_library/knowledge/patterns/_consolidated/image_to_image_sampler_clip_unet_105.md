---
name: image_to_image_sampler_clip_unet_105
type: Image To Image
frequency: 6
level: strong
coverage: 0.8755
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, ConstrainImage|pysssss, DetailerForEach, DualCLIPLoader, GrowMaskWithBlur, Image Comparer (rgthree), JjkText, KSampler, LayerMask: SegmentAnythingUltra V2, LoadImage, MaskPreview+, MaskToSEGS, PreviewImage, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, preview_mask]
problems: []
missing: []
members: [图片生成/图生图/【快捷应用】F.1 Fill 一键修手_1909484173021880321.json, 平台全量/FLUX 完美修手 手部修复_1934420907894992898.json, 平台全量/FLUX自动化完美修手_1973657179674816513.json, 平台全量/flux完美修手_1973655453173420034.json, 平台全量/flux自动化完美修复手部_1973652838037458945.json, 平台全量/flux自动化完美修手_1981578204211224577.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【快捷应用】F.1 Fill 一键修手_1909484173021880321.json、平台全量/FLUX 完美修手 手部修复_1934420907894992898.json、平台全量/FLUX自动化完美修手_1973657179674816513.json、平台全量/flux完美修手_1973655453173420034.json、平台全量/flux自动化完美修复手部_1973652838037458945.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `ConstrainImage|pysssss`
- `DetailerForEach`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `MaskPreview+`
- `MaskToSEGS`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `LayerColor: ColorAdapter` —— 1/6 个有
- `LayerUtility: CropByMask V2` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: RestoreCropBox` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 100% |
| 重绘幅度 | 0.75 | 0.75 - 0.75 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.75 - 0.75，6 个样本，取值集中（一致性 100%）

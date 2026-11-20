---
name: image_to_image_controlnet_ipadapter_upscale_10
type: Image To Image
frequency: 2
level: weak
coverage: 0.6295
common_nodes: [Any Switch (rgthree), Anything Everywhere, Anything Everywhere3, BNK_CLIPTextEncodeAdvanced, BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, Fast Groups Muter (rgthree), FloatSlider, GetImageSize+, GetNode, GrowMask, GrowMaskWithBlur, ICLightConditioning, IPAdapter, IPAdapterUnifiedLoader, Image Overlay, ImagePass, ImageScale, InspyrenetRembg, InvertMask (segment anything), KSampler, LoadAndApplyICLightUnet, LoadImage, SaveImage, SetNode, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [平台全量/一键换背景（保留人物服饰细节一致性，自带SD放大+IClight光影调节）_1892197406832812033.json, 平台全量/一键换背景（保留人物服饰细节），可改光影_1906300964171878401.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/一键换背景（保留人物服饰细节一致性，自带SD放大+IClight光影调节）_1892197406832812033.json、平台全量/一键换背景（保留人物服饰细节），可改光影_1906300964171878401.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere`
- `Anything Everywhere3`
- `BNK_CLIPTextEncodeAdvanced`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Fast Groups Muter (rgthree)`
- `FloatSlider`
- `GetImageSize+`
- `GetNode`
- `GrowMask`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `Image Overlay`
- `ImagePass`
- `ImageScale`
- `InspyrenetRembg`
- `InvertMask (segment anything)`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `SaveImage`
- `SetNode`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ConditioningCombine` —— 1/2 个有
- `DetailerForEach` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `MaskToSEGS` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `SubtractMask` —— 1/2 个有
- `easy imageBatchToImageList` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | ddim | - | 2 | 100% |
| 调度器 | ddim_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.4 | - | 2 | 75% |
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 0.5 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，2 个样本，一致性 100%
- 调度器 最常用 ddim_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.4，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: text_to_image_lora_sampler_clip_442
type: Text To Image
frequency: 4
level: strong
coverage: 0.726
common_nodes: [Anything Everywhere, ApplyPulid, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, GetImageSizeAndCount, GetNode, ImageDesaturate+, ImageRemoveBackground+, ImageScaleToMegapixels, KSampler, Label (rgthree), LayerUtility: ColorImage, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance V2, LoadAndResizeImage, LoadImage, LoraLoader, MergeLayers, NewLayer, PreviewImage, Prompts Everywhere, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, RH_Captioner, RemBGSession+, SaveImage, SeargeIntegerConstant, SeargePromptCombiner, Seed Generator, SetNode, ShowText|pysssss, VAEDecode, easy cleanGpuUsed, easy promptReplace]
problems: []
missing: []
members: [图片生成/图生图/3D皮克斯风格AI头像_1918120115290968066.json, 图片生成/图生图/[3D皮克斯风格]头像_1912802061514174466.json, 平台全量/[3D皮克斯风格]头像_1846797898284417026.json, 平台全量/儿童插画绘本风格头像_1846436310549413889.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_442

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/3D皮克斯风格AI头像_1918120115290968066.json、图片生成/图生图/[3D皮克斯风格]头像_1912802061514174466.json、平台全量/[3D皮克斯风格]头像_1846797898284417026.json、平台全量/儿童插画绘本风格头像_1846436310549413889.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `ApplyPulid`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageDesaturate+`
- `ImageRemoveBackground+`
- `ImageScaleToMegapixels`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlendAdvance V2`
- `LoadAndResizeImage`
- `LoadImage`
- `LoraLoader`
- `MergeLayers`
- `NewLayer`
- `PreviewImage`
- `Prompts Everywhere`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `RH_Captioner`
- `RemBGSession+`
- `SaveImage`
- `SeargeIntegerConstant`
- `SeargePromptCombiner`
- `Seed Generator`
- `SetNode`
- `ShowText|pysssss`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 3/4 个有
- `BasicGuider` —— 3/4 个有
- `BasicScheduler` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `FluxGuidance` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PulidFluxEvaClipLoader` —— 3/4 个有
- `PulidFluxInsightFaceLoader` —— 3/4 个有
- `PulidFluxModelLoader` —— 3/4 个有
- `RandomNoise` —— 3/4 个有
- `SamplerCustomAdvanced` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `VAELoader` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.6 | 4 | 92% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 6.5 | 6.5 - 6.5 | 4 | 100% |
| 采样算法 | dpmpp_sde | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.6，4 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 6.5 - 6.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）

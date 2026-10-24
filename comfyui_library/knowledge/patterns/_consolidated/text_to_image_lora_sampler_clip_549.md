---
name: text_to_image_lora_sampler_clip_549
type: Text To Image
frequency: 2
level: weak
coverage: 0.74
common_nodes: [Anything Everywhere, ApplyPulid, ApplyPulidFlux, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BasicGuider, BasicScheduler, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GetImageSizeAndCount, GetNode, ImageDesaturate+, ImageRemoveBackground+, ImageScaleToMegapixels, KSampler, KSamplerSelect, Label (rgthree), LayerUtility: ColorImage, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance V2, LoadAndResizeImage, LoadImage, LoraLoader, LoraLoaderModelOnly, MergeLayers, NewLayer, PreviewImage, Prompts Everywhere, PulidEvaClipLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, PulidInsightFaceLoader, PulidModelLoader, RH_Captioner, RandomNoise, RemBGSession+, SamplerCustomAdvanced, SaveImage, SeargeIntegerConstant, SeargePromptCombiner, Seed Generator, SetNode, ShowText|pysssss, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy promptReplace]
problems: []
missing: []
members: [图片生成/图生图/3D皮克斯风格AI头像_1918120115290968066.json, 图片生成/图生图/[3D皮克斯风格]头像_1912802061514174466.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_549

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/3D皮克斯风格AI头像_1918120115290968066.json、图片生成/图生图/[3D皮克斯风格]头像_1912802061514174466.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `ApplyPulid`
- `ApplyPulidFlux`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `BasicGuider`
- `BasicScheduler`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageDesaturate+`
- `ImageRemoveBackground+`
- `ImageScaleToMegapixels`
- `KSampler`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlendAdvance V2`
- `LoadAndResizeImage`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MergeLayers`
- `NewLayer`
- `PreviewImage`
- `Prompts Everywhere`
- `PulidEvaClipLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `RH_Captioner`
- `RandomNoise`
- `RemBGSession+`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeargeIntegerConstant`
- `SeargePromptCombiner`
- `Seed Generator`
- `SetNode`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy promptReplace`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.5 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

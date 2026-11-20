---
name: unknown_workflow_lora_sampler_clip_94
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.839143
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Florence2Run, FluxGuidance, KSamplerSelect, LoadImage, LoraLoader, ModelSamplingFlux, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SDXLAspectRatioSelector, SamplerCustomAdvanced, SaveImage, VAEDecode]
problems: []
missing: []
members: [平台全量/Bloom_1861108312556355586.json, 平台全量/Cartoon Portrait_1868847046596902913.json, 平台全量/Cute Doll (flux pulid)_1861110876681191426.json, 平台全量/Cute Doll (flux pulid)_1862407833454096386.json, 平台全量/Flux Pulid 盲盒，Blind Box Studio_1843560449970229249.json, 平台全量/Flux 创意贴纸 Creative Sticker(Flux Turbo)_1845100064808300545.json, 平台全量/Minimalist Portrait 极简风格头像_1868334978919710721.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Bloom_1861108312556355586.json、平台全量/Cartoon Portrait_1868847046596902913.json、平台全量/Cute Doll (flux pulid)_1861110876681191426.json、平台全量/Cute Doll (flux pulid)_1862407833454096386.json、平台全量/Flux Pulid 盲盒，Blind Box Studio_1843560449970229249.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Florence2Run`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SDXLAspectRatioSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 6/7 个有
- `Image Overlay` —— 6/7 个有
- `Image Size to Number` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `JWIntegerSub` —— 6/7 个有
- `easy int` —— 6/7 个有
- `MaskToSEGS` —— 5/7 个有
- `SEGSPreview` —— 5/7 个有
- `LayerUtility: LoadVQAModel` —— 3/7 个有
- `LayerUtility: VQAPrompt` —— 3/7 个有
- `BNK_Unsampler` —— 2/7 个有
- `Bounded Image Crop with Mask` —— 2/7 个有
- `CLIPTextEncodeFlux` —— 2/7 个有
- `DownloadAndLoadSAM2Model` —— 2/7 个有
- `Florence2toCoordinates` —— 2/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `Latent Upscale by Factor (WAS)` —— 2/7 个有
- `LatentInterpolate` —— 2/7 个有
- `Replace Text _O` —— 2/7 个有
- `Sam2Segmentation` —— 2/7 个有
- `String Literal` —— 2/7 个有
- `AegisFlow/aflogo` —— 1/7 个有
- `DisplayText_Zho` —— 1/7 个有
- `DownloadAndLoadFlorence2Model` —— 1/7 个有
- `LayerMask: RmBgUltra V2` —— 1/7 个有
- `LayerUtility: ColorImage V2` —— 1/7 个有
- `LayerUtility: ImageBlend V2` —— 1/7 个有
- `LayerUtility: JoyCaption2` —— 1/7 个有
- `LayerUtility: JoyCaption2ExtraOptions` —— 1/7 个有
- `LayerUtility: TextJoin` —— 1/7 个有
- `Text Prompt (JPS)` —— 1/7 个有
- `easy imageSize` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | 832 - 832 | 7 | 100% |
| 高度 | 1216 | 1216 - 1216 | 7 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 7 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，观测区间 832 - 832，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，观测区间 1216 - 1216，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，7 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）

---
name: unknown_workflow_upscale_lora_sampler_60
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.84
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/Fluxkontext 一句话改图P图_1929891445510148098.json, 图片生成/图生图/Flux分块放大极速版 _ 高清修复_1893683000184377346.json, 图片生成/图生图/New-Kontext-Gemini-api-换背景_1943851520276201474.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Fluxkontext 一句话改图P图_1929891445510148098.json、图片生成/图生图/Flux分块放大极速版 _ 高清修复_1893683000184377346.json、图片生成/图生图/New-Kontext-Gemini-api-换背景_1943851520276201474.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `RH_ComfyFluxKontext` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `Anything Everywhere` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ComflyGeminiAPI` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Load Image From Url (mtb)` —— 1/3 个有
- `Text Input [Dream]` —— 1/3 个有
- `easy ifElse` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

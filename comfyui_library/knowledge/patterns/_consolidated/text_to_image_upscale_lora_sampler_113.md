---
name: text_to_image_upscale_lora_sampler_113
type: Text To Image
frequency: 2
level: weak
coverage: 0.9085
common_nodes: [CFGGuider, CLIPLoader, CLIPLoaderGGUF, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, GetNode, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, ImageSharpen, KSampler, KSamplerAdvanced, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTResolutionSelector, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, easy imageSize, easy int]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/【Krea2洗图】邪修三采_K双采+Z-turbo+Klein放大_超高随机性洗图_抽卡机_图生图版_2072239556870623234.json, 图片生成/文生图/【Krea2】邪修三采_K双采+Z-turbo+Klein放大_超高随机性_抽卡机_文生图版_2072217954493755394.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【Krea2洗图】邪修三采_K双采+Z-turbo+Klein放大_超高随机性洗图_抽卡机_图生图版_2072239556870623234.json、图片生成/文生图/【Krea2】邪修三采_K双采+Z-turbo+Klein放大_超高随机性_抽卡机_文生图版_2072217954493755394.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 0.4 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

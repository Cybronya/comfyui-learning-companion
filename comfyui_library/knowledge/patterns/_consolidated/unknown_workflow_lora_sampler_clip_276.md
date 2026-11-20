---
name: unknown_workflow_lora_sampler_clip_276
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.734
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR SDXL Aspect Ratio, DownloadAndLoadFlorence2Model, DualCLIPLoader, Fast Groups Bypasser (rgthree), Florence2Run, FluxGuidance, GetImageSize+, GetNode, Image Comparer (rgthree), JWImageResizeByLongerSide, Joy_caption, Joy_caption_load, KSamplerSelect, LayerUtility: JoyCaption2, LayerUtility: JoyCaption2ExtraOptions, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, Molmo7BDbnb, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed Everywhere, SetNode, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy promptConcat]
problems: []
missing: []
members: [图片生成/反推提示词/对比：FLUX使用各种 LLM 打标重绘原图_1845764590582775809.json, 平台全量/FLUX洗图神器_1846229524215119873.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_276

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/对比：FLUX使用各种 LLM 打标重绘原图_1845764590582775809.json、平台全量/FLUX洗图神器_1846229524215119873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `JWImageResizeByLongerSide`
- `Joy_caption`
- `Joy_caption_load`
- `KSamplerSelect`
- `LayerUtility: JoyCaption2`
- `LayerUtility: JoyCaption2ExtraOptions`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `Molmo7BDbnb`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `SetNode`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `ApplyPulidFlux` —— 1/2 个有
- `BNK_Unsampler` —— 1/2 个有
- `CR Simple Image Compare` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Float` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `Latent Upscale by Factor (WAS)` —— 1/2 个有
- `LatentInterpolate` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `MiniCPM_VQA_Polished` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

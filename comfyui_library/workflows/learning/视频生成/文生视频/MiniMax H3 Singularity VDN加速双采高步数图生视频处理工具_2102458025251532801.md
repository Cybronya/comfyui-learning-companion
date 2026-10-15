---
key: 视频生成/文生视频/MiniMax H3 Singularity VDN加速双采高步数图生视频处理工具_2102458025251532801.json
name: MiniMax H3 Singularity VDN加速双采高步数图生视频处理工具_2102458025251532801
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Singularity VDN加速双采高步数图生视频处理工具_2102458025251532801.json
hash: 34a9a3aa3b29b519
coverage: 0.918919
learned_at: 2026-10-15 22:45:34
nodes: [DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, ShowAnything|Mie, ShowAnything|Mie, PrimitiveFloat, CLIPLoader, VAELoader, VAELoader, VAEEncodeAudio, ImpactSwitch, ImpactSwitch, KSamplerSelect, ResolutionSelector, LoadImage, LoadImage, LoadImage, GetVideoComponents, GetVideoComponents, LoadVideo, LoadVideo, LoadVideo, LoadAudio, LoadAudio, LoadAudio, LTXVConcatAVLatent, SamplerCustomAdvanced, BasicGuider, VAEDecode, UNETLoader, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, ComfyMathExpression, MiniMaxH3ReferenceToVideo, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, VAEEncode, RandomSeedNoise, ResolutionSelector, ImageResizeKJv2, PrimitiveFloat, GetVideoComponents, ModelPreviewOverrideKJ, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, ModelPreviewOverrideKJ, CreateVideo, CreateVideo, CreateVideo, Fast Groups Bypasser (rgthree), BasicScheduler, BasicScheduler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, EasyCache, MiniMaxH3VDNRuntimeAuditT8Advanced, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveVideo, SaveVideo, SaveVideo, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3 Singularity VDN加速双采高步数图生视频处理工具_2102458025251532801.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Singularity VDN加速双采高步数图生视频处理工具_2102458025251532801.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `PrimitiveFloat`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `VAEEncodeAudio` ★核心
- `ImpactSwitch`
- `ImpactSwitch`
- `KSamplerSelect` ★核心
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetVideoComponents`
- `GetVideoComponents`
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `VAEEncode` ★核心
- `RandomSeedNoise`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `PrimitiveFloat`
- `GetVideoComponents`
- `ModelPreviewOverrideKJ`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `ModelPreviewOverrideKJ`
- `CreateVideo`
- `CreateVideo`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `BasicScheduler`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `EasyCache`
- `MiniMaxH3VDNRuntimeAuditT8Advanced`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `SaveVideo`
- `SaveVideo`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（102/111）

**有卡**：`DF_Int_to_Float`、`ShowAnything|Mie`、`CLIPLoader`、`VAELoader`、`VAEEncodeAudio`、`KSamplerSelect`、`ResolutionSelector`、`LoadImage`、`GetVideoComponents`、`LoadVideo`、`LoadAudio`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`BasicGuider`、`VAEDecode`、`UNETLoader`、`RandomNoise`、`VAEDecodeAudio`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`VAEEncode`、`RandomSeedNoise`、`ImageResizeKJv2`、`ModelPreviewOverrideKJ`、`CR Prompt Text`、`CreateVideo`、`BasicScheduler`、`LoraLoaderModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`EasyCache`、`MiniMaxH3VDNRuntimeAuditT8Advanced`、`SaveVideo`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

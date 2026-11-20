---
key: 平台全量/Luomini._AI短剧制作全流程_2118008875579437058.json
name: Luomini._AI短剧制作全流程_2118008875579437058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Luomini._AI短剧制作全流程_2118008875579437058.json
hash: d0e2a47960be37aa
coverage: 0.822222
learned_at: 2026-11-14 00:39:40
nodes: [VAEDecodeAudio, VAEDecode, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, MiniMaxH3ReferenceToVideo, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, LoraLoaderBypassModelOnly, PrimitiveFloat, VAELoader, VAELoader, Reroute, Reroute, Reroute, Reroute, CLIPLoader, Reroute, UNETLoader, INTConstant, Reroute, ComfyMathExpression, ResolutionSelector, Reroute, Reroute, Reroute, MarkdownNote, EmptyLatentImage, ResolutionSelector, UNETLoader, VAEDecode, CLIPLoader, KSampler, TextEncodeQwenImage21, VAELoader, ComfySwitchNode, SaveImage, UNETLoader, CLIPTextEncode, Note, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Image Comparer (rgthree), SeedVR2LoadDiTModel, ImageScaleToTotalPixels, KSampler, VAEDecode, INTConstant, SaveImage, LoraLoaderModelOnly, SaveImage, PreviewImage, EmptyLatentImage, CLIPLoader, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, UNETLoader, CLIPTextEncode, KSampler, VAEDecode, LoraLoaderModelOnly, EmptyLatentImage, CLIPLoader, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, SaveImage, CR Text, CR Text, CR Prompt Text, LoadImage, LoadImage, PrimitiveStringMultiline, LoadImage, LoraLoaderBypassModelOnly, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s_ode", "scheduler": "kl_optimal", "seed": 837845668738225, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Luomini._AI短剧制作全流程_2118008875579437058.json

> 来源文件 `comfyui_library/workflows/平台全量/Luomini._AI短剧制作全流程_2118008875579437058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `PrimitiveFloat`
- `VAELoader`
- `VAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `Reroute`
- `UNETLoader` ★核心
- `INTConstant`
- `Reroute`
- `ComfyMathExpression`
- `ResolutionSelector`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `VAELoader`
- `ComfySwitchNode`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `SaveImage`
- `CR Text`
- `CR Text`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoraLoaderBypassModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `837845668738225`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s_ode`
- `scheduler` = `kl_optimal`
- `denoise` = `1`

## 知识

覆盖率 **82%**（74/90）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`LoraLoaderBypassModelOnly`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`ComfyMathExpression`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`SaveImage`、`CLIPTextEncode`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`CR Text`、`CR Prompt Text`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

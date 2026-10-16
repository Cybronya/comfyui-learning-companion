---
key: 视频生成/图生视频/lightx2v 4步加速｜MiniMax H3参考生视频自动提示词优化V1.3_2089847613943271425.json
name: lightx2v 4步加速｜MiniMax H3参考生视频自动提示词优化V1.3_2089847613943271425
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/lightx2v 4步加速｜MiniMax H3参考生视频自动提示词优化V1.3_2089847613943271425.json
hash: b87a1ebd494857e8
coverage: 0.696429
learned_at: 2026-10-16 22:02:18
nodes: [SetNode, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, llama_cpp_parameters, GetNode, SetNode, Any Switch (rgthree), PrimitiveFloat, ComfyMathExpression, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PurgeVRAM_UTK, llama_cpp_model_loader, llama_cpp_instruct_adv, VAELoader, SetNode, GetNode, SetNode, GetNode, UNETLoader, JoinStringMulti, StringConcatenate, GetNode, ToString, GetNode, CLIPLoader, RandomNoise, MiniMaxH3ReferenceToVideo, UNETLoader, UNETLoader, LoraLoaderModelOnly, BasicGuider, LoraLoaderModelOnly, easy showAnything, MiniMaxH3SigmaShift, LoraLoaderModelOnly, ModelAttentionBackend, SetNode, KSamplerSelect, SamplerCustomAdvanced, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ZNGB_ImageBatchMulti, LoadAudio, LoadAudio, LoadAudio, easy showAnything, easy showAnything, SetNode, SetNode, ComfyMathExpression, ComfyMathExpression, PDRatioSelector, ratio_selector, Int, GetNode, BasicScheduler, H3SigmaRefiner, VAELoader, VAELoader, UNETLoader, CLIPLoader, CLIPLoader, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/lightx2v 4步加速｜MiniMax H3参考生视频自动提示词优化V1.3_2089847613943271425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/lightx2v 4步加速｜MiniMax H3参考生视频自动提示词优化V1.3_2089847613943271425.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（112 个）：
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `llama_cpp_parameters`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `VAELoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `UNETLoader` ★核心
- `JoinStringMulti`
- `StringConcatenate`
- `GetNode`
- `ToString`
- `GetNode`
- `CLIPLoader`
- `RandomNoise`
- `MiniMaxH3ReferenceToVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `MiniMaxH3SigmaShift`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `SetNode`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ZNGB_ImageBatchMulti`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PDRatioSelector`
- `ratio_selector`
- `Int`
- `GetNode`
- `BasicScheduler`
- `H3SigmaRefiner`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

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

覆盖率 **70%**（78/112）

**有卡**：`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`llama_cpp_parameters`、`ComfyMathExpression`、`PurgeVRAM_UTK`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`VAELoader`、`UNETLoader`、`JoinStringMulti`、`StringConcatenate`、`ToString`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`BasicGuider`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`KSamplerSelect`、`SamplerCustomAdvanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`ZNGB_ImageBatchMulti`、`LoadAudio`、`PDRatioSelector`、`ratio_selector`、`Int`、`BasicScheduler`、`H3SigmaRefiner`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 视频生成/图生视频/两次采样1080P｜MiniMax H3参考生视频音频参考提示词优化V1.3_2089794956117495810.json
name: 两次采样1080P｜MiniMax H3参考生视频音频参考提示词优化V1.3_2089794956117495810
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/两次采样1080P｜MiniMax H3参考生视频音频参考提示词优化V1.3_2089794956117495810.json
hash: 6147c0ceb02be0f1
coverage: 0.666667
learned_at: 2026-10-16 22:02:24
nodes: [SetNode, llama_cpp_parameters, GetNode, SetNode, Any Switch (rgthree), SetNode, easy showAnything, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PurgeVRAM_UTK, llama_cpp_model_loader, llama_cpp_instruct_adv, VAELoader, SetNode, JoinStringMulti, GetNode, ToString, SetNode, PrimitiveFloat, VHS_VideoCombine, VAEDecodeAudio, GetNode, VAEDecode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, UNETLoader, ModelAttentionBackend, SetNode, VAELoader, UNETLoader, CLIPLoader, CLIPLoader, easy showAnything, LTXVSeparateAVLatent, LTXVConcatAVLatent, GetNode, BasicGuider, SamplerCustomAdvanced, RandomNoise, ComfyMathExpression, SetNode, SetNode, LoraLoaderModelOnly, SolAttnMiniMax, MiniMaxH3SigmaShift, ModelAttentionBackend, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, BasicGuider, VAELoader, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, BasicScheduler, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, KSamplerSelect, GetNode, SplitSigmas, MiniMaxH3SigmaShift, ModelAttentionBackend, LoraLoaderModelOnly, easy showAnything, easy showAnything, SetNode, ComfyMathExpression, MinimaxH3LatentUpscalerNode3D, GetNode, Fast Groups Bypasser (rgthree), StringConcatenate, GetNode, ZNGB_ImageBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadAudio, LoadAudio, LoadAudio, ConvertAny2Int, PDRatioSelector, ComfyMathExpression, SetNode, SetNode, ComfyMathExpression, easy showAnything, ratio_selector, H3SigmaRefiner, Int, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/两次采样1080P｜MiniMax H3参考生视频音频参考提示词优化V1.3_2089794956117495810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/两次采样1080P｜MiniMax H3参考生视频音频参考提示词优化V1.3_2089794956117495810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（135 个）：
- `SetNode`
- `llama_cpp_parameters`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `VAELoader`
- `SetNode`
- `JoinStringMulti`
- `GetNode`
- `ToString`
- `SetNode`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `SetNode`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `easy showAnything`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SolAttnMiniMax`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `KSamplerSelect` ★核心
- `GetNode`
- `SplitSigmas`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `ComfyMathExpression`
- `MinimaxH3LatentUpscalerNode3D`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `StringConcatenate`
- `GetNode`
- `ZNGB_ImageBatchMulti`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `ConvertAny2Int`
- `PDRatioSelector`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `easy showAnything`
- `ratio_selector`
- `H3SigmaRefiner`
- `Int`
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

覆盖率 **67%**（90/135）

**有卡**：`llama_cpp_parameters`、`PurgeVRAM_UTK`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`VAELoader`、`JoinStringMulti`、`ToString`、`VHS_VideoCombine`、`VAEDecodeAudio`、`VAEDecode`、`UNETLoader`、`ModelAttentionBackend`、`CLIPLoader`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`SolAttnMiniMax`、`MiniMaxH3SigmaShift`、`ModelPreviewOverrideKJ`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`KSamplerSelect`、`SplitSigmas`、`MinimaxH3LatentUpscalerNode3D`、`StringConcatenate`、`ZNGB_ImageBatchMulti`、`LoadImage`、`LoadAudio`、`ConvertAny2Int`、`PDRatioSelector`、`ratio_selector`、`H3SigmaRefiner`、`Int`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

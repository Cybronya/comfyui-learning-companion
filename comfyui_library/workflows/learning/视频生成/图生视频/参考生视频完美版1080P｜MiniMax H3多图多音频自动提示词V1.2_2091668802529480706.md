---
key: 视频生成/图生视频/参考生视频完美版1080P｜MiniMax H3多图多音频自动提示词V1.2_2091668802529480706.json
name: 参考生视频完美版1080P｜MiniMax H3多图多音频自动提示词V1.2_2091668802529480706
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/参考生视频完美版1080P｜MiniMax H3多图多音频自动提示词V1.2_2091668802529480706.json
hash: 927087eee54dd780
coverage: 0.661765
learned_at: 2026-10-16 22:31:02
nodes: [SetNode, llama_cpp_parameters, GetNode, SetNode, Any Switch (rgthree), SetNode, easy showAnything, PurgeVRAM_UTK, llama_cpp_instruct_adv, VAELoader, SetNode, JoinStringMulti, GetNode, ToString, SetNode, PrimitiveFloat, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, UNETLoader, ModelAttentionBackend, SetNode, VAELoader, CLIPLoader, CLIPLoader, LTXVSeparateAVLatent, LTXVConcatAVLatent, GetNode, BasicGuider, SamplerCustomAdvanced, RandomNoise, ComfyMathExpression, SetNode, LoraLoaderModelOnly, SolAttnMiniMax, MiniMaxH3SigmaShift, ModelAttentionBackend, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, BasicGuider, VAELoader, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, BasicScheduler, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, KSamplerSelect, GetNode, SplitSigmas, MiniMaxH3SigmaShift, ModelAttentionBackend, LoraLoaderModelOnly, easy showAnything, SetNode, ComfyMathExpression, StringConcatenate, GetNode, ZNGB_ImageBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, LoadAudio, ConvertAny2Int, PDRatioSelector, ComfyMathExpression, SetNode, SetNode, ComfyMathExpression, easy showAnything, H3SigmaRefiner, SetReserveVRAM, easy showAnything, llama_cpp_model_loader, GetNode, MinimaxH3LatentUpscaler3D, VAEDecodeAudio, VHS_VideoCombine, PrimitiveStringMultiline, ratio_selector, VAEDecode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Int, PrimitiveStringMultiline, SetNode, easy showAnything, PrimitiveStringMultiline, CreateVideo, SaveVideo, LoadImage, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/参考生视频完美版1080P｜MiniMax H3多图多音频自动提示词V1.2_2091668802529480706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/参考生视频完美版1080P｜MiniMax H3多图多音频自动提示词V1.2_2091668802529480706.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（136 个）：
- `SetNode`
- `llama_cpp_parameters`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `easy showAnything`
- `PurgeVRAM_UTK`
- `llama_cpp_instruct_adv`
- `VAELoader`
- `SetNode`
- `JoinStringMulti`
- `GetNode`
- `ToString`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
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
- `CLIPLoader`
- `CLIPLoader`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ComfyMathExpression`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SolAttnMiniMax`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
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
- `SetNode`
- `ComfyMathExpression`
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
- `H3SigmaRefiner`
- `SetReserveVRAM`
- `easy showAnything`
- `llama_cpp_model_loader`
- `GetNode`
- `MinimaxH3LatentUpscaler3D`
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `ratio_selector`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `PrimitiveStringMultiline`
- `SetNode`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
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

覆盖率 **66%**（90/136）

**有卡**：`llama_cpp_parameters`、`PurgeVRAM_UTK`、`llama_cpp_instruct_adv`、`VAELoader`、`JoinStringMulti`、`ToString`、`UNETLoader`、`ModelAttentionBackend`、`CLIPLoader`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`SolAttnMiniMax`、`MiniMaxH3SigmaShift`、`ModelPreviewOverrideKJ`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`KSamplerSelect`、`SplitSigmas`、`StringConcatenate`、`ZNGB_ImageBatchMulti`、`LoadImage`、`LoadAudio`、`ConvertAny2Int`、`PDRatioSelector`、`H3SigmaRefiner`、`SetReserveVRAM`、`llama_cpp_model_loader`、`MinimaxH3LatentUpscaler3D`、`VAEDecodeAudio`、`VHS_VideoCombine`、`ratio_selector`、`VAEDecode`、`Int`、`CreateVideo`、`SaveVideo`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

---
key: 视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json
name: 文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json
hash: dd220f285dbc03dd
coverage: 0.542857
learned_at: 2026-10-15 22:48:40
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, GetNode, SetNode, SetNode, GetNode, MiniMaxH3ImageToVideo, BasicGuider, BasicScheduler, RandomNoise, SolAttnPatch, KSamplerSelect, GetNode, MiniMaxLowVRAMAttention, MiniMaxH3SigmaShift, ModelAttentionBackend, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, Any Switch (rgthree), LTXVConcatAVLatent, GetNode, GetNode, Any Switch (rgthree), GetNode, SetNode, Fast Groups Bypasser (rgthree), VAEDecode, VAEDecodeAudio, CreateVideo, MiniMaxChunkFeedForward, GetNode, GetNode, PrimitiveStringMultiline, GetNode, GetNode, GetNode, SetNode, ResolutionSelector, SetNode, PrimitiveFloat, SaveVideo, SetNode, SetNode, GetNode, easy ifElse, SetNode, SetNode, SamplerCustomAdvanced, BasicGuider, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), VAEDecode, VAEDecodeAudio, CreateVideo, ModelPreviewOverrideKJ, SamplerCustomAdvanced, SetNode, GetNode, MiniMaxH3ReferenceToVideo, BasicScheduler, Int, SamplerCustomAdvanced, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, PathchSageAttentionKJ, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, BasicScheduler, BasicGuider, GetNode, Any Switch (rgthree), easy ifElse, SetNode, SetNode, LoadAudio, MinimaxH3LatentUpscaler3D, SaveVideo, easy boolean, VRGDG_MiniMaxH3AudioDrive, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（175 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MiniMaxH3ImageToVideo`
- `BasicGuider`
- `BasicScheduler`
- `RandomNoise`
- `SolAttnPatch`
- `KSamplerSelect` ★核心
- `GetNode`
- `MiniMaxLowVRAMAttention`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `Any Switch (rgthree)`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `MiniMaxChunkFeedForward`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `PrimitiveFloat`
- `SaveVideo`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy ifElse`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `ModelPreviewOverrideKJ`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `BasicScheduler`
- `Int`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `BasicScheduler`
- `BasicGuider`
- `GetNode`
- `Any Switch (rgthree)`
- `easy ifElse`
- `SetNode`
- `SetNode`
- `LoadAudio`
- `MinimaxH3LatentUpscaler3D`
- `SaveVideo`
- `easy boolean`
- `VRGDG_MiniMaxH3AudioDrive`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **54%**（95/175）

**有卡**：`ComfyMathExpression`、`LoadImage`、`VHS_LoadVideo`、`MiniMaxH3ImageToVideo`、`BasicGuider`、`BasicScheduler`、`RandomNoise`、`SolAttnPatch`、`KSamplerSelect`、`MiniMaxLowVRAMAttention`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`MiniMaxChunkFeedForward`、`ResolutionSelector`、`SaveVideo`、`SamplerCustomAdvanced`、`ModelPreviewOverrideKJ`、`MiniMaxH3ReferenceToVideo`、`Int`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadAudio`、`MinimaxH3LatentUpscaler3D`、`easy boolean`、`VRGDG_MiniMaxH3AudioDrive`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

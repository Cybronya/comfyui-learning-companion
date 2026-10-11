---
key: 视频生成/文生视频/文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298.json
name: 文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298.json
hash: 14bf059b0e2be27b
coverage: 0.512987
learned_at: 2026-10-11 21:42:00
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, MiniMaxLowVRAMAttention, SetNode, SetNode, VAEDecodeAudio, GetNode, SetNode, GetNode, CreateVideo, GetNode, GetNode, VAEDecode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, 忽略多组孤海, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, GetNode, SolAttnPatch, ResolutionSelector, PrimitiveFloat, 忽略多组孤海, GetNode, SetNode, Any Switch (rgthree), GetNode, BasicScheduler, KSamplerSelect, MiniMaxH3SigmaShift, GetNode, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, SetNode, RandomNoise, ModelAttentionBackend, GetNode, SetNode, GetNode, Int, PrimitiveStringMultiline, PrimitiveFloat, MiniMaxH3ImageToVideo, GetNode, GetNode, Any Switch (rgthree), Any Switch (rgthree), VAEDecodeAudio, MiniMaxH3ReferenceToVideo, SetNode, GetNode, GetNode, VAEDecode, BasicGuider, SetNode, BasicGuider, BasicScheduler, VAEDecode, VAEDecodeAudio, SetNode, SetNode, GetNode, GetNode, SaveVideo, GetNode, GetNode, Any Switch (rgthree), GetNode, BasicGuider, SamplerCustomAdvanced, CreateVideo, MinimaxH3LatentUpscaler3D, LTXVSeparateAVLatent, CreateVideo, LTXVConcatAVLatent, SamplerCustomAdvanced, BasicScheduler, Any Switch (rgthree), SaveVideo, SetNode, SetNode, VRGDG_MiniMaxH3AudioDrive, LoadAudio, UNETLoader, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: [忽略多组孤海, 忽略多组孤海]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（154 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MiniMaxLowVRAMAttention`
- `SetNode`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
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
- `忽略多组孤海`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `Fast Groups Bypasser (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SolAttnPatch`
- `ResolutionSelector`
- `PrimitiveFloat`
- `忽略多组孤海`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `MiniMaxH3SigmaShift`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `RandomNoise`
- `ModelAttentionBackend`
- `GetNode`
- `SetNode`
- `GetNode`
- `Int`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `MiniMaxH3ImageToVideo`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `VAEDecodeAudio` ★核心
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `BasicGuider`
- `SetNode`
- `BasicGuider`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SaveVideo`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `MinimaxH3LatentUpscaler3D`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `Any Switch (rgthree)`
- `SaveVideo`
- `SetNode`
- `SetNode`
- `VRGDG_MiniMaxH3AudioDrive`
- `LoadAudio`
- `UNETLoader` ★核心
- `LoadImage`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
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

覆盖率 **51%**（79/154）

**有卡**：`ComfyMathExpression`、`MiniMaxLowVRAMAttention`、`VAEDecodeAudio`、`CreateVideo`、`VAEDecode`、`LoadImage`、`VHS_LoadVideo`、`MiniMaxChunkFeedForward`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`SamplerCustomAdvanced`、`SolAttnPatch`、`ResolutionSelector`、`BasicScheduler`、`KSamplerSelect`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`ModelAttentionBackend`、`Int`、`MiniMaxH3ImageToVideo`、`MiniMaxH3ReferenceToVideo`、`BasicGuider`、`SaveVideo`、`MinimaxH3LatentUpscaler3D`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`VRGDG_MiniMaxH3AudioDrive`、`LoadAudio`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**缺卡**（2）：`忽略多组孤海`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

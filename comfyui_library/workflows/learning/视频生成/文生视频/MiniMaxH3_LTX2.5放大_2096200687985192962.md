---
key: 视频生成/文生视频/MiniMaxH3_LTX2.5放大_2096200687985192962.json
name: MiniMaxH3_LTX2.5放大_2096200687985192962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMaxH3_LTX2.5放大_2096200687985192962.json
hash: 075352824d7a96fa
coverage: 0.888889
learned_at: 2026-10-11 21:41:48
nodes: [VAELoader, VAELoader, VAEDecodeAudio, KSamplerSelect, BasicScheduler, BasicGuider, MarkdownNote, VAELoader, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, CreateVideo, UNETLoader, VAEDecode, LTXVImgToVideoInplace, LTXAddVideoICLoRAGuide, ImageFromBatch, CreateVideo, GetVideoComponents, RandomNoise, LoadImage, LTXVImgToVideoInplace, LTXVCropGuides, SamplerCustomAdvanced, SaveAudio, VAEDecodeTiled, ComfyMathExpression, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveFloat, LoraLoaderModelOnly, CLIPLoader, CLIPLoader, UNETLoader, LTXICLoRALoaderModelOnly, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, MarkdownNote, SaveVideo, SaveVideo, LoadAudio, MiniMaxH3MemoryEfficientSageAttentionPatch, PerturbedAttention, LoadImage, PrimitiveStringMultiline, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMaxH3_LTX2.5放大_2096200687985192962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMaxH3_LTX2.5放大_2096200687985192962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `MarkdownNote`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LTXVImgToVideoInplace`
- `LTXAddVideoICLoRAGuide`
- `ImageFromBatch`
- `CreateVideo`
- `GetVideoComponents`
- `RandomNoise`
- `LoadImage`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `SaveAudio`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `SaveVideo`
- `SaveVideo`
- `LoadAudio`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PerturbedAttention`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **89%**（56/63）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`CreateVideo`、`UNETLoader`、`VAEDecode`、`LTXVImgToVideoInplace`、`LTXAddVideoICLoRAGuide`、`ImageFromBatch`、`GetVideoComponents`、`LoadImage`、`LTXVCropGuides`、`SaveAudio`、`VAEDecodeTiled`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPLoader`、`LTXICLoRALoaderModelOnly`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`SaveVideo`、`LoadAudio`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PerturbedAttention`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader

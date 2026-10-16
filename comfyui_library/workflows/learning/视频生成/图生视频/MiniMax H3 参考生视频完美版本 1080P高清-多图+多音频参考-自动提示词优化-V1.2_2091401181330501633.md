---
key: 视频生成/图生视频/MiniMax H3 参考生视频完美版本 1080P高清-多图+多音频参考-自动提示词优化-V1.2_2091401181330501633.json
name: MiniMax H3 参考生视频完美版本 1080P高清-多图+多音频参考-自动提示词优化-V1.2_2091401181330501633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 参考生视频完美版本 1080P高清-多图+多音频参考-自动提示词优化-V1.2_2091401181330501633.json
hash: 5399c4be373e1e55
coverage: 0.590909
learned_at: 2026-10-16 22:30:36
nodes: [MarkdownNote, MarkdownNote, SetNode, llama_cpp_parameters, GetNode, SetNode, Any Switch (rgthree), MarkdownNote, SetNode, easy showAnything, PurgeVRAM_UTK, llama_cpp_instruct_adv, VAELoader, SetNode, JoinStringMulti, GetNode, ToString, SetNode, PrimitiveFloat, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, UNETLoader, ModelAttentionBackend, SetNode, VAELoader, CLIPLoader, CLIPLoader, LTXVSeparateAVLatent, LTXVConcatAVLatent, GetNode, BasicGuider, SamplerCustomAdvanced, RandomNoise, ComfyMathExpression, SetNode, LoraLoaderModelOnly, SolAttnMiniMax, MiniMaxH3SigmaShift, ModelAttentionBackend, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, BasicGuider, VAELoader, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, BasicScheduler, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, KSamplerSelect, GetNode, SplitSigmas, MiniMaxH3SigmaShift, ModelAttentionBackend, LoraLoaderModelOnly, easy showAnything, SetNode, ComfyMathExpression, StringConcatenate, GetNode, ZNGB_ImageBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, LoadAudio, ConvertAny2Int, PDRatioSelector, ComfyMathExpression, SetNode, SetNode, ComfyMathExpression, easy showAnything, H3SigmaRefiner, SetReserveVRAM, easy showAnything, llama_cpp_model_loader, GetNode, MinimaxH3LatentUpscaler3D, VAEDecodeAudio, VHS_VideoCombine, PrimitiveStringMultiline, ratio_selector, VAEDecode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Int, PrimitiveStringMultiline, SetNode, easy showAnything, PrimitiveStringMultiline, CreateVideo, SaveVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 参考生视频完美版本 1080P高清-多图+多音频参考-自动提示词优化-V1.2_2091401181330501633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 参考生视频完美版本 1080P高清-多图+多音频参考-自动提示词优化-V1.2_2091401181330501633.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（110 个）：
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `llama_cpp_parameters`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `MarkdownNote`
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

## 知识

覆盖率 **59%**（65/110）

**有卡**：`llama_cpp_parameters`、`PurgeVRAM_UTK`、`llama_cpp_instruct_adv`、`VAELoader`、`JoinStringMulti`、`ToString`、`UNETLoader`、`ModelAttentionBackend`、`CLIPLoader`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`SolAttnMiniMax`、`MiniMaxH3SigmaShift`、`ModelPreviewOverrideKJ`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`KSamplerSelect`、`SplitSigmas`、`StringConcatenate`、`ZNGB_ImageBatchMulti`、`LoadImage`、`LoadAudio`、`ConvertAny2Int`、`PDRatioSelector`、`H3SigmaRefiner`、`SetReserveVRAM`、`llama_cpp_model_loader`、`MinimaxH3LatentUpscaler3D`、`VAEDecodeAudio`、`VHS_VideoCombine`、`ratio_selector`、`VAEDecode`、`Int`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

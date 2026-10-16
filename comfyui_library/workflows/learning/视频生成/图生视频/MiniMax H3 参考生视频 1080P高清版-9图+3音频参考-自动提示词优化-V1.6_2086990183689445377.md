---
key: 视频生成/图生视频/MiniMax H3 参考生视频 1080P高清版-9图+3音频参考-自动提示词优化-V1.6_2086990183689445377.json
name: MiniMax H3 参考生视频 1080P高清版-9图+3音频参考-自动提示词优化-V1.6_2086990183689445377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 参考生视频 1080P高清版-9图+3音频参考-自动提示词优化-V1.6_2086990183689445377.json
hash: 8c41f967571e5aa5
coverage: 0.59633
learned_at: 2026-10-16 21:07:19
nodes: [MarkdownNote, MarkdownNote, SetNode, llama_cpp_parameters, GetNode, SetNode, Any Switch (rgthree), MarkdownNote, SetNode, easy showAnything, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PurgeVRAM_UTK, llama_cpp_instruct_adv, VAELoader, SetNode, JoinStringMulti, GetNode, ToString, SetNode, PrimitiveFloat, VHS_VideoCombine, VAEDecodeAudio, GetNode, VAEDecode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, UNETLoader, ModelAttentionBackend, SetNode, VAELoader, UNETLoader, CLIPLoader, CLIPLoader, easy showAnything, LTXVSeparateAVLatent, LTXVConcatAVLatent, GetNode, BasicGuider, SamplerCustomAdvanced, RandomNoise, ComfyMathExpression, SetNode, SetNode, LoraLoaderModelOnly, SolAttnMiniMax, MiniMaxH3SigmaShift, ModelAttentionBackend, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, BasicGuider, VAELoader, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, BasicScheduler, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, KSamplerSelect, GetNode, SplitSigmas, MiniMaxH3SigmaShift, ModelAttentionBackend, LoraLoaderModelOnly, easy showAnything, easy showAnything, SetNode, ComfyMathExpression, GetNode, Fast Groups Bypasser (rgthree), StringConcatenate, GetNode, ZNGB_ImageBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), LoadAudio, LoadAudio, LoadAudio, ConvertAny2Int, PDRatioSelector, ComfyMathExpression, SetNode, SetNode, ComfyMathExpression, easy showAnything, ratio_selector, H3SigmaRefiner, Int, llama_cpp_model_loader, MinimaxH3LatentUpscaler3D]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 参考生视频 1080P高清版-9图+3音频参考-自动提示词优化-V1.6_2086990183689445377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 参考生视频 1080P高清版-9图+3音频参考-自动提示词优化-V1.6_2086990183689445377.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（109 个）：
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
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
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
- `llama_cpp_model_loader`
- `MinimaxH3LatentUpscaler3D`

## 知识

覆盖率 **60%**（65/109）

**有卡**：`llama_cpp_parameters`、`PurgeVRAM_UTK`、`llama_cpp_instruct_adv`、`VAELoader`、`JoinStringMulti`、`ToString`、`VHS_VideoCombine`、`VAEDecodeAudio`、`VAEDecode`、`UNETLoader`、`ModelAttentionBackend`、`CLIPLoader`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`SolAttnMiniMax`、`MiniMaxH3SigmaShift`、`ModelPreviewOverrideKJ`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`KSamplerSelect`、`SplitSigmas`、`StringConcatenate`、`ZNGB_ImageBatchMulti`、`LoadImage`、`LoadAudio`、`ConvertAny2Int`、`PDRatioSelector`、`ratio_selector`、`H3SigmaRefiner`、`Int`、`llama_cpp_model_loader`、`MinimaxH3LatentUpscaler3D`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

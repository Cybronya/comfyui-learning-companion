---
key: 视频生成/图生视频/MiniMax H3 参考生视频-lightx2v 4步加速-自动提示词优化-V1.3_2085749432846479361.json
name: MiniMax H3 参考生视频-lightx2v 4步加速-自动提示词优化-V1.3_2085749432846479361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 参考生视频-lightx2v 4步加速-自动提示词优化-V1.3_2085749432846479361.json
hash: 7ff8aa6f37bc3195
coverage: 0.616279
learned_at: 2026-10-16 20:50:28
nodes: [MarkdownNote, MarkdownNote, SetNode, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, llama_cpp_parameters, GetNode, SetNode, Any Switch (rgthree), MarkdownNote, PrimitiveFloat, ComfyMathExpression, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, easy showAnything, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PurgeVRAM_UTK, llama_cpp_instruct_adv, VAELoader, SetNode, GetNode, SetNode, GetNode, UNETLoader, JoinStringMulti, StringConcatenate, GetNode, ToString, GetNode, CLIPLoader, RandomNoise, MiniMaxH3ReferenceToVideo, UNETLoader, UNETLoader, LoraLoaderModelOnly, BasicGuider, LoraLoaderModelOnly, easy showAnything, MiniMaxH3SigmaShift, LoraLoaderModelOnly, ModelAttentionBackend, SetNode, KSamplerSelect, SamplerCustomAdvanced, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ZNGB_ImageBatchMulti, LoadAudio, LoadAudio, LoadAudio, easy showAnything, easy showAnything, SetNode, SetNode, ComfyMathExpression, ComfyMathExpression, PDRatioSelector, ratio_selector, Int, GetNode, BasicScheduler, H3SigmaRefiner, VAELoader, VAELoader, UNETLoader, CLIPLoader, llama_cpp_model_loader, CLIPLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 参考生视频-lightx2v 4步加速-自动提示词优化-V1.3_2085749432846479361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 参考生视频-lightx2v 4步加速-自动提示词优化-V1.3_2085749432846479361.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（86 个）：
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `llama_cpp_parameters`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `MarkdownNote`
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
- `llama_cpp_model_loader`
- `CLIPLoader`

## 知识

覆盖率 **62%**（53/86）

**有卡**：`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`llama_cpp_parameters`、`ComfyMathExpression`、`PurgeVRAM_UTK`、`llama_cpp_instruct_adv`、`VAELoader`、`UNETLoader`、`JoinStringMulti`、`StringConcatenate`、`ToString`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`BasicGuider`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`KSamplerSelect`、`SamplerCustomAdvanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`ZNGB_ImageBatchMulti`、`LoadAudio`、`PDRatioSelector`、`ratio_selector`、`Int`、`BasicScheduler`、`H3SigmaRefiner`、`llama_cpp_model_loader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

---
name: unknown_workflow_video_upscale_latent_upscale_137
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.3925
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetImage, GetNode, ImageScale, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PreviewImage, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, ShowText|pysssss, SplitSigmas, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace, YuanAudioList, YuanAudioSplit, YuanMultiImage, YuanTool, easy float, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2108461705771708417.json, 视频生成/文生视频/MiniMax-H3 全栈式短剧 多图音频参考二采优化版V1.0_2096284114990223362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_137

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2108461705771708417.json、视频生成/文生视频/MiniMax-H3 全栈式短剧 多图音频参考二采优化版V1.0_2096284114990223362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：39%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetImage`
- `GetNode`
- `ImageScale`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `SplitSigmas`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTShotReplace`
- `YuanAudioList`
- `YuanAudioSplit`
- `YuanMultiImage`
- `YuanTool`
- `easy float`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `JoinStringMulti` —— 1/2 个有
- `PurgeVRAM_UTK` —— 1/2 个有
- `ToString` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

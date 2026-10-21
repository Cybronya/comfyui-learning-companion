---
name: unknown_workflow_video_lora_sampler_695
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.448
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Int, KSamplerSelect, KepStringLiteral, Label (rgthree), LoadAudioUI, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RTXVideoSuperResolution, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, String Literal, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy clearCacheAll, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009.json, 视频生成/文生视频/MiniMax H3 顶级舞蹈视频直出 I 新提示词增强 I 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速_2092699967201824769.json, 视频生成/文生视频/MiniMax H3 顶级舞蹈视频超频版 I 新提示词增强 I 全模态 v2.0 I 混合模型_2093521519069716482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_695

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009.json、视频生成/文生视频/MiniMax H3 顶级舞蹈视频直出 I 新提示词增强 I 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速_2092699967201824769.json、视频生成/文生视频/MiniMax H3 顶级舞蹈视频超频版 I 新提示词增强 I 全模态 v2.0 I 混合模型_2093521519069716482.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Int`
- `KSamplerSelect`
- `KepStringLiteral`
- `Label (rgthree)`
- `LoadAudioUI`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `LTXVConcatAVLatent` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `MinimaxH3LatentUpscaler3D` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `VHS_LoadAudioUpload` —— 2/3 个有
- `ExtendIntermediateSigmas` —— 1/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

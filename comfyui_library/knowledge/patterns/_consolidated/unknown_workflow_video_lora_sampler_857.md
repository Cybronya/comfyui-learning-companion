---
name: unknown_workflow_video_lora_sampler_857
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6925
common_nodes: [Any Switch (rgthree), BasicScheduler, CLIPLoader, CR Text Concatenate, ComfyMathExpression, ExtractAndCombineLines, Fast Groups Bypasser (rgthree), ImageBatchMulti, JWFloatToString, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaGetNode, PixaromaLabel, PixaromaSetNode, PreviewAny, PreviewImage, PrimitiveFloat, ProcessString, RHHiddenNodes, RHLLMChatNode, RHSettingsNode, ResolutionSelector, ShowText|pysssss, Text, UNETLoader, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 1键4连战斗镜头+SelfLite超高清工作流_2101876665247944706.json, 视频生成/图生视频/MiniMax H3 20+步战斗镜头SKILL一键4镜版工作流_2104665711493861378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_857

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 1键4连战斗镜头+SelfLite超高清工作流_2101876665247944706.json、视频生成/图生视频/MiniMax H3 20+步战斗镜头SKILL一键4镜版工作流_2104665711493861378.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text Concatenate`
- `ComfyMathExpression`
- `ExtractAndCombineLines`
- `Fast Groups Bypasser (rgthree)`
- `ImageBatchMulti`
- `JWFloatToString`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PixaromaGetNode`
- `PixaromaLabel`
- `PixaromaSetNode`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveFloat`
- `ProcessString`
- `RHHiddenNodes`
- `RHLLMChatNode`
- `RHSettingsNode`
- `ResolutionSelector`
- `ShowText|pysssss`
- `Text`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ExtendIntermediateSigmas` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `SelfLiftAvatarH3Sampler` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

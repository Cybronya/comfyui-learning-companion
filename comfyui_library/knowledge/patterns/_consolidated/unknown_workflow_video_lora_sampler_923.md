---
name: unknown_workflow_video_lora_sampler_923
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.794
common_nodes: [Any Switch (rgthree), BasicScheduler, CLIPLoader, CR Prompt Text, CR Text, CR Text Concatenate, ConditioningZeroOut, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaLabel, PlaySound|pysssss, PrimitiveFloat, ResolutionSelector, SelfLiftAvatarH3Sampler, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Fl2V 首尾帧生图 + SelfLift节点采样 低显存超高2K分辨率_2103934254332862466.json, 音频生成/音频生成/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2110557852694827010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_923

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Fl2V 首尾帧生图 + SelfLift节点采样 低显存超高2K分辨率_2103934254332862466.json、音频生成/音频生成/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2110557852694827010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PixaromaLabel`
- `PlaySound|pysssss`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `RHSettingsNode` —— 1/2 个有
- `SoundFlow_GetLength` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

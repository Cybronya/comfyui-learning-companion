---
name: unknown_workflow_video_lora_sampler_934
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.778
common_nodes: [Any Switch (rgthree), BasicScheduler, CLIPLoader, CR Prompt Text, CR Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaLabel, PlaySound|pysssss, PrimitiveFloat, ResolutionSelector, SelfLiftAvatarH3Sampler, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 Fl2V 首尾帧生图 + SelfLift节点采样 低显存超高2K分辨率_2103934254332862466.json, 视频生成/视频生视频/MiniMax H3  Ref多模态SelfLift节点采样 低显存超高2K分辨率生成工作流_2098521007643521026.json, 音频生成/音频生成/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2110557852694827010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_934

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Fl2V 首尾帧生图 + SelfLift节点采样 低显存超高2K分辨率_2103934254332862466.json、视频生成/视频生视频/MiniMax H3  Ref多模态SelfLift节点采样 低显存超高2K分辨率生成工作流_2098521007643521026.json、音频生成/音频生成/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2110557852694827010.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `CR Text Concatenate` —— 2/3 个有
- `ComfyMathExpression` —— 2/3 个有
- `ExtendIntermediateSigmas` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `MiniMaxH3ReferenceToVideo` —— 2/3 个有
- `MiniMaxLowVRAMAttention` —— 2/3 个有
- `RHLLMChatNode` —— 2/3 个有
- `RHSettingsNode` —— 2/3 个有
- `VAEDecodeAudio` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `AudioSeparation` —— 1/3 个有
- `BlockSparseAttention` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `H3SigmaRefiner` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoadVideoUI` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `MiniMaxH3ImageToVideo` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SoundFlow_GetLength` —— 1/3 个有
- `VRGDG_AudioCrop` —— 1/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

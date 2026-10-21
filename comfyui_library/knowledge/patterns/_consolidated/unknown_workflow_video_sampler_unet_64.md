---
name: unknown_workflow_video_sampler_unet_64
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8066
common_nodes: [Any Switch (rgthree), BasicScheduler, CLIPLoader, CR Prompt Text, CR Text, CR Text Concatenate, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadAudio, LoadImage, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaLabel, PrimitiveFloat, ResolutionSelector, ShowText|pysssss, UNETLoader, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3  Ref多模态SelfLift节点采样 低显存超高2K分辨率生成工作流_2098521007643521026.json, 视频生成/图生视频/MiniMax H3 海螺Ref 图片 视频 音频多模态原生视频生成工作流（20步）_2089317433478828034.json, 视频生成/图生视频/MiniMax-H3 单人音频驱动数字人+SelfLite 超高分2K高清工作流_2101010348101955585.json, 视频生成/图生视频/MiniMax-H3 双人音频驱动数字人 + SelfLite超分高清工作流_2101010365365702658.json, 视频生成/图生视频/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2108767431442395138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_64

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3  Ref多模态SelfLift节点采样 低显存超高2K分辨率生成工作流_2098521007643521026.json、视频生成/图生视频/MiniMax H3 海螺Ref 图片 视频 音频多模态原生视频生成工作流（20步）_2089317433478828034.json、视频生成/图生视频/MiniMax-H3 单人音频驱动数字人+SelfLite 超高分2K高清工作流_2101010348101955585.json、视频生成/图生视频/MiniMax-H3 双人音频驱动数字人 + SelfLite超分高清工作流_2101010365365702658.json、视频生成/图生视频/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2108767431442395138.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `CR Text`
- `CR Text Concatenate`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PixaromaLabel`
- `PrimitiveFloat`
- `ResolutionSelector`
- `ShowText|pysssss`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 4/5 个有
- `ConditioningZeroOut` —— 4/5 个有
- `ExtendIntermediateSigmas` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `PlaySound|pysssss` —— 4/5 个有
- `RHLLMChatNode` —— 4/5 个有
- `RHSettingsNode` —— 4/5 个有
- `VAEDecode` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `Fast Groups Muter (rgthree)` —— 3/5 个有
- `SelfLiftAvatarH3Sampler` —— 3/5 个有
- `SoundFlow_GetLength` —— 3/5 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/5 个有
- `AudioSeparation` —— 2/5 个有
- `CreateVideo` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `LoadVideoUI` —— 2/5 个有
- `AudioConcat` —— 1/5 个有
- `BasicGuider` —— 1/5 个有
- `ComfyMathExpression` —— 1/5 个有
- `EmptyAudio` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `MiniMaxH3AVDecodeT8` —— 1/5 个有
- `PixaromaGroupSwitch` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `RandomNoise` —— 1/5 个有
- `SamplerCustomAdvanced` —— 1/5 个有
- `SelfLiftH3Sampler` —— 1/5 个有
- `VAEDecodeAudio` —— 1/5 个有
- `VRGDG_AudioCrop` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

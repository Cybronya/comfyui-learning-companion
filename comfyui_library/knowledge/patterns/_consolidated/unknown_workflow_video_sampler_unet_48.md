---
name: unknown_workflow_video_sampler_unet_48
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.789111
common_nodes: [Any Switch (rgthree), BasicScheduler, CLIPLoader, CR Prompt Text, CR Text, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PixaromaLabel, PrimitiveFloat, ResolutionSelector, ShowText|pysssss, UNETLoader, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2115644440567177218.json, 图片生成/图生图/MiniMax_H3_Ref多模态SelfLift节点采样_低显存超高2K分辨率生成工作流_2115639423189737474.json, 视频生成/图生视频/MiniMax H3  Ref多模态SelfLift节点采样 低显存超高2K分辨率生成工作流_2098521007643521026.json, 视频生成/图生视频/MiniMax H3  战斗（高动态视频）+SelfLift双采高清低显专属工作流1_2115542479842922498.json, 视频生成/图生视频/MiniMax H3 海螺Ref 图片 视频 音频多模态原生视频生成工作流（20步）_2089317433478828034.json, 视频生成/图生视频/MiniMax-H3 单人音频驱动数字人+SelfLite 超高分2K高清工作流_2101010348101955585.json, 视频生成/图生视频/MiniMax-H3 双人音频驱动数字人 + SelfLite超分高清工作流_2101010365365702658.json, 视频生成/图生视频/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2108767431442395138.json, 视频生成/图生视频/MiniMax_H3_Ref多模态SelfLift节点采样_低显存超高2K分辨率生成工作流_2115586447087587329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_48

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/MiniMax-H3_单人音频驱动数字人+SelfLite_超高分2K高清工作流_2115644440567177218.json、图片生成/图生图/MiniMax_H3_Ref多模态SelfLift节点采样_低显存超高2K分辨率生成工作流_2115639423189737474.json、视频生成/图生视频/MiniMax H3  Ref多模态SelfLift节点采样 低显存超高2K分辨率生成工作流_2098521007643521026.json、视频生成/图生视频/MiniMax H3  战斗（高动态视频）+SelfLift双采高清低显专属工作流1_2115542479842922498.json、视频生成/图生视频/MiniMax H3 海螺Ref 图片 视频 音频多模态原生视频生成工作流（20步）_2089317433478828034.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
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
- `ConditioningZeroOut` —— 8/9 个有
- `LoadAudio` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `PlaySound|pysssss` —— 8/9 个有
- `RHLLMChatNode` —— 8/9 个有
- `RHSettingsNode` —— 8/9 个有
- `VAEDecode` —— 8/9 个有
- `SelfLiftAvatarH3Sampler` —— 7/9 个有
- `easy cleanGpuUsed` —— 7/9 个有
- `AudioCrop` —— 5/9 个有
- `CR Text Concatenate` —— 5/9 个有
- `ImageConcatMulti` —— 5/9 个有
- `LayerUtility: PurgeVRAM V2` —— 5/9 个有
- `MathExpression|pysssss` —— 5/9 个有
- `MiniMaxLowVRAMAttention` —— 5/9 个有
- `AudioSeparation` —— 4/9 个有
- `BlockSparseAttention` —— 4/9 个有
- `ComfyMathExpression` —— 4/9 个有
- `CreateVideo` —— 4/9 个有
- `ExtendIntermediateSigmas` —— 4/9 个有
- `Fast Groups Muter (rgthree)` —— 4/9 个有
- `H3SigmaRefiner` —— 4/9 个有
- `LoadVideoUI` —— 4/9 个有
- `RHHiddenNodes` —— 4/9 个有
- `SoundFlow_GetLength` —— 4/9 个有
- `VAEDecodeAudio` —— 4/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/9 个有
- `VRGDG_AudioCrop` —— 3/9 个有
- `AudioConcat` —— 1/9 个有
- `BasicGuider` —— 1/9 个有
- `EmptyAudio` —— 1/9 个有
- `ImageBatchMulti` —— 1/9 个有
- `MiniMaxH3AVDecodeT8` —— 1/9 个有
- `NineGridMosaicNode` —— 1/9 个有
- `PixaromaGroupSwitch` —— 1/9 个有
- `PreviewAudio` —— 1/9 个有
- `RandomNoise` —— 1/9 个有
- `SamplerCustomAdvanced` —— 1/9 个有
- `SelfLiftH3Sampler` —— 1/9 个有
- `VRAM_Debug` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

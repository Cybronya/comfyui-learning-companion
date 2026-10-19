---
name: text_to_image_video_lora_sampler_114
type: Text To Image
frequency: 6
level: strong
coverage: 0.839167
common_nodes: [Any Switch (rgthree), BasicScheduler, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptyLatentImage, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PlaySound|pysssss, PrimitiveFloat, ResolutionSelector, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3单人音频驱动数字人加SelfLite超高分2K高清工作流_2105707477986791426.json, 视频生成/图生视频/MiniMax H3双人音频驱动数字人加SelfLite超分高清工作流_2105705768849854465.json, 视频生成/图生视频/SelfLite超高分2K直出 MiniMax H3单人音频驱动数字人高清工作流_2104823013219848194.json, 视频生成/图生视频/低显存也能跑的MiniMax H3视频生成 Ref多模态SelfLift节点采样直出2K超分_2104255063316324353.json, 视频生成/文生视频/Fl2V首尾帧生图加SelfLift采样 MiniMax H3低显存直出2K_2104359186711801858.json, 视频生成/文生视频/Fl2V首尾帧生图加SelfLift采样 MiniMax H3低显存直出2K_2104699110237491202.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3单人音频驱动数字人加SelfLite超高分2K高清工作流_2105707477986791426.json、视频生成/图生视频/MiniMax H3双人音频驱动数字人加SelfLite超分高清工作流_2105705768849854465.json、视频生成/图生视频/SelfLite超高分2K直出 MiniMax H3单人音频驱动数字人高清工作流_2104823013219848194.json、视频生成/图生视频/低显存也能跑的MiniMax H3视频生成 Ref多模态SelfLift节点采样直出2K超分_2104255063316324353.json、视频生成/文生视频/Fl2V首尾帧生图加SelfLift采样 MiniMax H3低显存直出2K_2104359186711801858.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PlaySound|pysssss`
- `PrimitiveFloat`
- `ResolutionSelector`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RHLLMChatNode` —— 5/6 个有
- `RHSettingsNode` —— 5/6 个有
- `SelfLiftAvatarH3Sampler` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `MiniMaxH3ReferenceToVideo` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `AudioCrop` —— 3/6 个有
- `ComfyMathExpression` —— 3/6 个有
- `Fast Groups Muter (rgthree)` —— 3/6 个有
- `ImageConcatMulti` —— 3/6 个有
- `LayerUtility: PurgeVRAM V2` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `SoundFlow_GetLength` —— 3/6 个有
- `VAEDecodeAudio` —— 3/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `easy imageConcat` —— 2/6 个有
- `AudioConcat` —— 1/6 个有
- `AudioSeparation` —— 1/6 个有
- `EmptyAudio` —— 1/6 个有
- `ImageBatchMulti` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `SelfLiftH3Sampler` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `VRGDG_AudioCrop` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足

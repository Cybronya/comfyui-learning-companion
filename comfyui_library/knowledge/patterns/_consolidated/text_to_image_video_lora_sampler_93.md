---
name: text_to_image_video_lora_sampler_93
type: Text To Image
frequency: 8
level: strong
coverage: 0.9155
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Minimax参考生视频V3｜角色一致性视频生成_2094920140604403713.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速开源版｜MiniMax H3角色设计人物类特效图生视频_2088339977326383106.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速开源｜MiniMax H3人物类特效角色设计图生视频_2088325534035042306.json, 视频生成/图生视频/去油版数字人口播唱歌MV加速版MiniMax H3开源版图生视频_2088371949490761729.json, 视频生成/图生视频/参考生视频V3｜Minimax图生视频直出_2091659742254026753.json, 视频生成/文生视频/H3官流终极版工作流，文生视频视频生视频图生视频全覆盖方案_2105809880144769025.json, 视频生成/文生视频/MiniMax H3数字人单人版｜文生视频口播生成_2094854429622231041.json, 视频生成/文生视频/单人版数字人生成｜MiniMax H3文生视频0901版_2095072554628239362.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_93

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Minimax参考生视频V3｜角色一致性视频生成_2094920140604403713.json、视频生成/图生视频/去油版数字人口播唱歌MV加速开源版｜MiniMax H3角色设计人物类特效图生视频_2088339977326383106.json、视频生成/图生视频/去油版数字人口播唱歌MV加速开源｜MiniMax H3人物类特效角色设计图生视频_2088325534035042306.json、视频生成/图生视频/去油版数字人口播唱歌MV加速版MiniMax H3开源版图生视频_2088371949490761729.json、视频生成/图生视频/参考生视频V3｜Minimax图生视频直出_2091659742254026753.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AVDecodeT8` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `CreateVideo` —— 5/8 个有
- `KSamplerSelect` —— 5/8 个有
- `LTXVConcatAVLatent` —— 5/8 个有
- `LTXVSeparateAVLatent` —— 5/8 个有
- `LoraLoaderBypassModelOnly` —— 5/8 个有
- `ManualSigmas` —— 5/8 个有
- `MiniMaxH3AudioConditioningT8` —— 5/8 个有
- `MiniMaxH3DualClockSamplerT8` —— 5/8 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 5/8 个有
- `PreviewAny` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `SolAttnMiniMax` —— 4/8 个有
- `Any To String (mtb)` —— 3/8 个有
- `BasicScheduler` —— 3/8 个有
- `JoinStringMulti` —— 3/8 个有
- `MiniMaxH3PromptEnhancerT8` —— 3/8 个有
- `MiniMaxH3ReferenceToVideo` —— 3/8 个有
- `StringConcatenate` —— 3/8 个有
- `AudioCrop` —— 2/8 个有
- `BatchImagesNode` —— 2/8 个有
- `MiniMaxH3BlockCacheT8` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `Qwen3ASRLoader` —— 2/8 个有
- `Qwen3ASRTranscribe` —— 2/8 个有
- `RunningHub_VoxCPM_Generate` —— 2/8 个有
- `RunningHub_VoxCPM_LoadModel` —— 2/8 个有
- `SoundFlow_GetLength` —— 2/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/8 个有
- `llama_cpp_instruct_adv` —— 2/8 个有
- `llama_cpp_model_loader` —— 2/8 个有
- `llama_cpp_parameters` —— 2/8 个有
- `BlockSparseAttention` —— 1/8 个有
- `MiniMaxH3HybridLoader` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `VAEDecodeAudio` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_video_lora_sampler_70
type: Text To Image
frequency: 11
level: strong
coverage: 0.860091
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3 SelfLift数字人图生视频处理生成工具_2101771880951803906.json, 数字人/数字人/MiniMax H3数字人图生视频 王炸级角色一致性处理工具_2112978757391835137.json, 数字人/数字人/Minimax H3 Selflift数字人｜口播形象一键生成_2101562944806023170.json, 数字人/数字人/Minimax H3数字人唱歌MV 口型同步音乐视频生成_2105113389172355074.json, 数字人/数字人/Minimax H3数字人唱歌MV｜数字人对口型出片｜音乐视频一键生成_2104821290807939073.json, 数字人/数字人/Minimax H3王炸级数字人｜图生视频口播形象一步到位_2112834880622120962.json, 数字人/数字人/Minimax H3音频驱动数字人，神态口型自然双采加速出片_2112344906474807297.json, 数字人/数字人/Minimax H3音频驱动数字人｜神态口型自然双采加速｜口播带货数字人_2112103025178398721.json, 数字人/数字人/高阶双采加速不降质音频驱动数字人｜MiniMax H3新技术视频流_2111757289240743938.json, 数字人/数字人/高阶双采音频驱动数字人，不降质MiniMax H3新技术_2111963357199818754.json, 视频生成/图生视频/高阶双采加速音频驱动数字人，图生视频不降质方案_2111240854835916802.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_70

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/MiniMax H3 SelfLift数字人图生视频处理生成工具_2101771880951803906.json、数字人/数字人/MiniMax H3数字人图生视频 王炸级角色一致性处理工具_2112978757391835137.json、数字人/数字人/Minimax H3 Selflift数字人｜口播形象一键生成_2101562944806023170.json、数字人/数字人/Minimax H3数字人唱歌MV 口型同步音乐视频生成_2105113389172355074.json、数字人/数字人/Minimax H3数字人唱歌MV｜数字人对口型出片｜音乐视频一键生成_2104821290807939073.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Float` —— 7/11 个有
- `PreviewAudio` —— 7/11 个有
- `ComfyNumberConvert` —— 6/11 个有
- `PreviewAny` —— 6/11 个有
- `SaveImage` —— 6/11 个有
- `CR Prompt Text` —— 5/11 个有
- `Int` —— 5/11 个有
- `MelBandRoFormerModelLoader` —— 5/11 个有
- `MelBandRoFormerSampler` —— 5/11 个有
- `PrimitiveFloat` —— 5/11 个有
- `SelfLiftAvatarH3TST` —— 5/11 个有
- `easy showAnything` —— 5/11 个有
- `MuyeTextEditOutput` —— 4/11 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 4/11 个有
- `GetNode` —— 2/11 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/11 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/11 个有
- `Qwen3ASRLoader` —— 2/11 个有
- `Qwen3ASRTranscribe` —— 2/11 个有
- `QwenH3PromptLocal` —— 2/11 个有
- `RunningHub_VoxCPM_Generate` —— 2/11 个有
- `RunningHub_VoxCPM_LoadModel` —— 2/11 个有
- `SaveAudioMP3` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `easy positive` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足

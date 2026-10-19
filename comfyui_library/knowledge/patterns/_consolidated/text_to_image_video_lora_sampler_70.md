---
name: text_to_image_video_lora_sampler_70
type: Text To Image
frequency: 10
level: strong
coverage: 0.8403
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3 SelfLift数字人图生视频处理生成工具_2101771880951803906.json, 数字人/数字人/Minimax H3 Selflift数字人｜口播形象一键生成_2101562944806023170.json, 数字人/数字人/Minimax H3数字人唱歌MV 口型同步音乐视频生成_2105113389172355074.json, 数字人/数字人/Minimax H3数字人唱歌MV｜数字人对口型出片｜音乐视频一键生成_2104821290807939073.json, 数字人/数字人/Selflift数字人开口说话｜一张照片一段音频就开演_2111320781878808578.json, 数字人/数字人/数字人MV最新版｜高质量与中等质量1分钟MV双模式_2105238906471010305.json, 视频生成/图生视频/MV数字人最高质量版MMH3 SelfLift，精品数字人音乐MV专用工作流_2103927834841542657.json, 视频生成/图生视频/MV数字人最高质量版加中等质量1分钟MV 数字人音乐视频生成_2105042694014853121.json, 视频生成/图生视频/MiniMax H3高清数字人自动提示词图生视频处理工具_2101031617153290241.json, 视频生成/图生视频/全新Selflift商用MV工作流，12种组合可选完美数字人版_2110450459541590017.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_70

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/MiniMax H3 SelfLift数字人图生视频处理生成工具_2101771880951803906.json、数字人/数字人/Minimax H3 Selflift数字人｜口播形象一键生成_2101562944806023170.json、数字人/数字人/Minimax H3数字人唱歌MV 口型同步音乐视频生成_2105113389172355074.json、数字人/数字人/Minimax H3数字人唱歌MV｜数字人对口型出片｜音乐视频一键生成_2104821290807939073.json、数字人/数字人/Selflift数字人开口说话｜一张照片一段音频就开演_2111320781878808578.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 9/10 个有
- `SoundFlow_GetLength` —— 9/10 个有
- `TrimAudioDuration` —— 9/10 个有
- `PreviewAudio` —— 6/10 个有
- `SaveImage` —— 6/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 5/10 个有
- `CR Float To String` —— 4/10 个有
- `CR Text` —— 4/10 个有
- `CR Text Concatenate` —— 4/10 个有
- `CR Text Replace` —— 4/10 个有
- `ImageBatchMultiV2` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/10 个有
- `MelBandRoFormerModelLoader` —— 4/10 个有
- `MelBandRoFormerSampler` —— 4/10 个有
- `ShowAnything|Mie` —— 4/10 个有
- `llama_cpp_instruct_adv` —— 4/10 个有
- `llama_cpp_model_loader` —— 4/10 个有
- `llama_cpp_parameters` —— 4/10 个有
- `JWStringToFloat` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/10 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/10 个有
- `MuyeTextEditOutput` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `easy positive` —— 2/10 个有
- `Int` —— 1/10 个有
- `LoadAudioUI` —— 1/10 个有
- `PurgeVRAM_UTK` —— 1/10 个有
- `QwenH3PromptLocal` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

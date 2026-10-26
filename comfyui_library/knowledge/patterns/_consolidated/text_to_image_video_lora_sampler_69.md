---
name: text_to_image_video_lora_sampler_69
type: Text To Image
frequency: 11
level: strong
coverage: 0.857818
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CR Float To String, CR Text, CR Text Concatenate, CR Text Replace, EmptyLatentImage, ImageBatchMultiV2, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PreviewAny, PreviewAudio, ResolutionSelector, ShowAnything|Mie, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MMH3 Selflift数字人音乐MV 高质量1分钟图生视频工具_2113676396081008642.json, 数字人/数字人/MiniMax H3数字歌手字节4步，最高质量完美版_2111279715519655937.json, 数字人/数字人/Selflift数字人MV方案，最高质量中等质量1分钟图生视频_2112014983725932546.json, 数字人/数字人/larry4步MinimaxH3数字人，商用级数字歌手演唱视频完美版_2112249176011665410.json, 数字人/数字人/全新Selflift商用MV工作流，12种组合可选完美数字人版_2113810082411671553.json, 数字人/数字人/商用数字歌手larry4步工作流｜MinimaxH3高质量MV直出｜开源商用级完美版_2112062671280500737.json, 数字人/数字人/数字人MV最新版｜高质量与中等质量1分钟MV双模式_2105238906471010305.json, 视频生成/图生视频/MV数字人最高质量版MMH3 SelfLift，精品数字人音乐MV专用工作流_2103927834841542657.json, 视频生成/图生视频/MV数字人最高质量版加中等质量1分钟MV 数字人音乐视频生成_2105042694014853121.json, 视频生成/图生视频/Selflift商用MV工作流 12种组合完美数字人处理工具_2113678005636780033.json, 视频生成/图生视频/全新Selflift商用MV工作流，12种组合可选完美数字人版_2110450459541590017.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_69

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/MMH3 Selflift数字人音乐MV 高质量1分钟图生视频工具_2113676396081008642.json、数字人/数字人/MiniMax H3数字歌手字节4步，最高质量完美版_2111279715519655937.json、数字人/数字人/Selflift数字人MV方案，最高质量中等质量1分钟图生视频_2112014983725932546.json、数字人/数字人/larry4步MinimaxH3数字人，商用级数字歌手演唱视频完美版_2112249176011665410.json、数字人/数字人/全新Selflift商用MV工作流，12种组合可选完美数字人版_2113810082411671553.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Float To String`
- `CR Text`
- `CR Text Concatenate`
- `CR Text Replace`
- `EmptyLatentImage`
- `ImageBatchMultiV2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PreviewAny`
- `PreviewAudio`
- `ResolutionSelector`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `SaveImage` —— 9/11 个有
- `ComfyMathExpression` —— 8/11 个有
- `ComfyNumberConvert` —— 8/11 个有
- `ConditioningZeroOut` —— 8/11 个有
- `LoadAudio` —— 8/11 个有
- `MiniMaxChunkFeedForward` —— 8/11 个有
- `MiniMaxLowVRAMAttention` —— 8/11 个有
- `ModelPreviewOverrideKJ` —— 8/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `SelfLiftAvatarH3Sampler` —— 8/11 个有
- `LTXVSeparateAVLatent` —— 7/11 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 7/11 个有
- `Int` —— 6/11 个有
- `LTXVAudioVAEEncode` —— 6/11 个有
- `LTXVConcatAVLatent` —— 6/11 个有
- `SetLatentNoiseMask` —— 6/11 个有
- `SolidMask` —— 6/11 个有
- `AudioCrop` —— 5/11 个有
- `GetNode` —— 5/11 个有
- `SetNode` —— 5/11 个有
- `SoundFlow_GetLength` —— 5/11 个有
- `BasicGuider` —— 3/11 个有
- `Bjornulf_ShowFloat` —— 3/11 个有
- `Bjornulf_ShowInt` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `JWStringToFloat` —— 3/11 个有
- `LoadAudioUI` —— 3/11 个有
- `MathExpression|pysssss` —— 3/11 个有
- `PrimitiveFloat` —— 3/11 个有
- `PurgeVRAM_UTK` —— 3/11 个有
- `RH_GetAudioDuration` —— 3/11 个有
- `RH_Translator` —— 3/11 个有
- `RandomNoise` —— 3/11 个有
- `SamplerCustomAdvanced` —— 3/11 个有
- `TrimAudioDuration` —— 3/11 个有
- `BlockSparseAttention` —— 2/11 个有
- `MiniMaxH3SigmaShift` —— 2/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

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

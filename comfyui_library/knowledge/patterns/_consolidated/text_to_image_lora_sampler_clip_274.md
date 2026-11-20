---
name: text_to_image_lora_sampler_clip_274
type: Text To Image
frequency: 8
level: strong
coverage: 0.930125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SBAPI MinimaxH3三分镜参考生成视频工作流 多模态输入_2109723354918907905.json, 视频生成/图生视频/SBAPI_MinimaxH3三分镜参考，文生视频图生视频联动_2111195384482721793.json, 视频生成/图生视频/SBAPI_MinimaxH3三连分镜参考出片｜文生视频图生视频一条龙_2111053464666206209.json, 视频生成/图生视频/h3 r2v runninghub tts v2｜图生视频音频驱动生成_2091306513502654466.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema图生视频加速模型_2105146341893693442.json, 视频生成/图生视频/step600_ema_kitchen_attn｜图生视频专业增强模型工作流_2113888199780163585.json, 视频生成/文生视频/minmaxH3单采加速三连发｜文生视频图生视频 又快又稳出片神器_2105532532883283969.json, 视频生成/文生视频/minmaxH3单采加速多场景｜文生视频视频生视频图生视频全支持_2105530783984340993.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_274

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/SBAPI MinimaxH3三分镜参考生成视频工作流 多模态输入_2109723354918907905.json、视频生成/图生视频/SBAPI_MinimaxH3三分镜参考，文生视频图生视频联动_2111195384482721793.json、视频生成/图生视频/SBAPI_MinimaxH3三连分镜参考出片｜文生视频图生视频一条龙_2111053464666206209.json、视频生成/图生视频/h3 r2v runninghub tts v2｜图生视频音频驱动生成_2091306513502654466.json、视频生成/图生视频/minimax_h3_turbo_v4_step600_ema图生视频加速模型_2105146341893693442.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/8 个有
- `ExtendIntermediateSigmas` —— 4/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `DF_String_Concatenate` —— 3/8 个有
- `DF_Text_Box` —— 3/8 个有
- `JWStringGetLine` —— 3/8 个有
- `JjkConcat` —— 3/8 个有
- `JjkShowText` —— 3/8 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/8 个有
- `MiniMaxH3SigmaShift` —— 3/8 个有
- `ModelAttentionBackend` —— 3/8 个有
- `ReplaceString` —— 3/8 个有
- `StringConstant` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `MiniMaxH3AudioLatentControlT8` —— 1/8 个有
- `MiniMaxH3TurboLoRA` —— 1/8 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/8 个有
- `easy indexTTSAudioMerge` —— 1/8 个有
- `easy indexTTSGenerate` —— 1/8 个有

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

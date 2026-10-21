---
name: text_to_image_video_lora_sampler_23
type: Text To Image
frequency: 17
level: strong
coverage: 0.924
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品换文案替换原语音，图生视频方案_2107160853769449474.json, 数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品文案不换保持原语音，图生视频方案_2107159320273178626.json, 数字人/数字人/MiniMax H3视频复刻数字人｜换人换产品文案不换原声保留_2106922727604056065.json, 数字人/数字人/MiniMax H3视频复刻数字人｜视频换人换产品换文案语音替换_2106924252430684161.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具，数字人生成方案_2107223547927162882.json, 数字人/数字人/MiniMax H3音频驱动数字人多人对话｜加速版长视频处理工具_2106925731669438465.json, 数字人/数字人/Minimax参考生视频V3｜角色一致性视频生成_2094920140604403713.json, 数字人/数字人/加速版单采参考生视频｜MiniMax H3长视频直出_2105482904137719809.json, 视频生成/图生视频/MiniMax H3视频复刻数字人｜换人换产品换文案换语音_2111128408808845313.json, 视频生成/图生视频/MiniMax H3音频驱动数字人 语音口型同步多人对话一键实现_2110352465429352449.json, 视频生成/图生视频/MiniMax H3音频驱动数字人加速版｜参考图生长视频直出_2103697575655333890.json, 视频生成/图生视频/MiniMax H3音频驱动数字人参考生视频长视频直出加速版，图生视频方案_2103992154782789634.json, 视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json, 视频生成/图生视频/参考生视频V3｜Minimax图生视频直出_2091659742254026753.json, 视频生成/文生视频/H3官流终极版工作流，文生视频视频生视频图生视频全覆盖方案_2105809880144769025.json, 视频生成/文生视频/MiniMax H3数字人单人版｜文生视频口播生成_2094854429622231041.json, 视频生成/文生视频/单人版数字人生成｜MiniMax H3文生视频0901版_2095072554628239362.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品换文案替换原语音，图生视频方案_2107160853769449474.json、数字人/数字人/MiniMax H3视频复刻数字人视频换人换产品文案不换保持原语音，图生视频方案_2107159320273178626.json、数字人/数字人/MiniMax H3视频复刻数字人｜换人换产品文案不换原声保留_2106922727604056065.json、数字人/数字人/MiniMax H3视频复刻数字人｜视频换人换产品换文案语音替换_2106924252430684161.json、数字人/数字人/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具，数字人生成方案_2107223547927162882.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
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

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AVDecodeT8` —— 16/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 16/17 个有
- `SolAttnMiniMax` —— 16/17 个有
- `孤海注释` —— 15/17 个有
- `LoraLoaderBypassModelOnly` —— 14/17 个有
- `MiniMaxH3AudioConditioningT8` —— 14/17 个有
- `MiniMaxH3DualClockSamplerT8` —— 14/17 个有
- `LoadAudio` —— 12/17 个有
- `SaveImage` —— 8/17 个有
- `VHS_LoadVideo` —— 6/17 个有
- `CreateVideo` —— 5/17 个有
- `KSamplerSelect` —— 5/17 个有
- `LTXVConcatAVLatent` —— 5/17 个有
- `LTXVSeparateAVLatent` —— 5/17 个有
- `ManualSigmas` —— 5/17 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 5/17 个有
- `PreviewAny` —— 5/17 个有
- `SaveVideo` —— 5/17 个有
- `ModelPreviewOverrideKJ` —— 4/17 个有
- `Any To String (mtb)` —— 3/17 个有
- `BasicScheduler` —— 3/17 个有
- `JoinStringMulti` —— 3/17 个有
- `MiniMaxH3PromptEnhancerT8` —— 3/17 个有
- `MiniMaxH3ReferenceToVideo` —— 3/17 个有
- `StringConcatenate` —— 3/17 个有
- `AudioCrop` —— 2/17 个有
- `BatchImagesNode` —— 2/17 个有
- `MiniMaxH3BlockCacheT8` —— 2/17 个有
- `PathchSageAttentionKJ` —— 2/17 个有
- `Qwen3ASRLoader` —— 2/17 个有
- `Qwen3ASRTranscribe` —— 2/17 个有
- `RunningHub_VoxCPM_Generate` —— 2/17 个有
- `RunningHub_VoxCPM_LoadModel` —— 2/17 个有
- `SoundFlow_GetLength` —— 2/17 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/17 个有
- `llama_cpp_instruct_adv` —— 2/17 个有
- `llama_cpp_model_loader` —— 2/17 个有
- `llama_cpp_parameters` —— 2/17 个有
- `BlockSparseAttention` —— 1/17 个有
- `MiniMaxH3HybridLoader` —— 1/17 个有
- `VAEDecodeAudio` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（20/17 个样本）：Steps较低可能导致细节不足

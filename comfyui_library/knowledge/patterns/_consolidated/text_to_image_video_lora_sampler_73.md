---
name: text_to_image_video_lora_sampler_73
type: Text To Image
frequency: 11
level: strong
coverage: 0.696727
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多图参考带货视频｜MiniMax-H3数字人倾情出镜_2096572891126124546.json, 视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频_2090451614204252162.json, 视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频一键直出_2090274287373611010.json, 视频生成/图生视频/开源多参考优化版｜MiniMax H3角色一致性生视频_2094474289755021314.json, 视频生成/图生视频/数字人视频带货｜MiniMax-H3多图参考生视频制作_2096314183389372417.json, 视频生成/图生视频/深度视频参考动作迁移｜H3视频图生视频直出_2091029816312156162.json, 视频生成/图生视频/深度视频参考动作迁移｜H3视频生视频生成_2091213094801465345.json, 视频生成/图生视频/满血FP16+剪枝int8二采｜MinimaxH3浅空间放大v4_2093250532080185346.json, 视频生成/图生视频/满血FP16剪枝int8加速｜MinimaxH3浅空间放大二采v4_2093092897481650178.json, 视频生成/图生视频/潜空间放大二次优化｜MiniMax H3 双采样DSW图生视频_2096239277662363650.json, 视频生成/图生视频/音频驱动数字人｜MiniMax H3图生视频口播直出_2090205102572400642.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_73

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/多图参考带货视频｜MiniMax-H3数字人倾情出镜_2096572891126124546.json、视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频_2090451614204252162.json、视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频一键直出_2090274287373611010.json、视频生成/图生视频/开源多参考优化版｜MiniMax H3角色一致性生视频_2094474289755021314.json、视频生成/图生视频/数字人视频带货｜MiniMax-H3多图参考生视频制作_2096314183389372417.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 9/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/11 个有
- `SetNode` —— 9/11 个有
- `LTXVSeparateAVLatent` —— 8/11 个有
- `PrimitiveFloat` —— 8/11 个有
- `LTXVConcatAVLatent` —— 7/11 个有
- `MinimaxH3LatentUpscaler3D` —— 7/11 个有
- `Text` —— 7/11 个有
- `easy cleanGpuUsed` —— 6/11 个有
- `VHS_LoadVideo` —— 5/11 个有
- `Float` —— 4/11 个有
- `LoadAudio` —— 4/11 个有
- `SplitSigmas` —— 4/11 个有
- `Divide [DVB]` —— 3/11 个有
- `FlashVSRNode` —— 3/11 个有
- `H3SigmaRefiner` —— 3/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `Int` —— 3/11 个有
- `JWInteger` —— 3/11 个有
- `ModelAttentionBackend` —— 3/11 个有
- `SigmasGraph` —— 3/11 个有
- `Label (rgthree)` —— 2/11 个有
- `ManualSigmas` —— 2/11 个有
- `ModelPreviewOverrideKJ` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `Text Multiline` —— 2/11 个有
- `LoraLoaderBypassModelOnly` —— 1/11 个有
- `PT_H3ConcatAVLatent` —— 1/11 个有
- `PlaySound|pysssss` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有
- `SoundFlow_GetLength` —— 1/11 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/11 个有
- `ZNGB_AudioCrop` —— 1/11 个有
- `easy float` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足

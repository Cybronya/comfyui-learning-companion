---
name: text_to_image_video_lora_sampler_71
type: Text To Image
frequency: 10
level: strong
coverage: 0.6299
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json, 视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json, 视频生成/图生视频/AITUDOU-H3+SelfLift组合｜影视级情绪表达出片_2106620640190095361.json, 视频生成/图生视频/AI影视剧制作MiniMaxH3多参视频生成发布版 多模态输入_2109729477717741570.json, 视频生成/图生视频/Fused-MiniMax H3战斗增强双采｜图生视频火力全开_2097934793827766274.json, 视频生成/图生视频/H3动作迁移2.0进阶史诗强化，图生视频自带放大_2110857064611405825.json, 视频生成/图生视频/H3动作迁移2.0进阶版史诗强化工作流，图生视频动作迁移处理工具_2107948212886786049.json, 视频生成/图生视频/H3多参考双采5秒一致性版 Singularity精修短片_2098842004485664770.json, 视频生成/图生视频/H3多参考双采5秒一致性版｜多图参考短平快出片不跑脸_2099124913448767489.json, 视频生成/图生视频/MiniMax H3多参生视频 图生视频多模态参考创作_2099194857146376194.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json、视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json、视频生成/图生视频/AITUDOU-H3+SelfLift组合｜影视级情绪表达出片_2106620640190095361.json、视频生成/图生视频/AI影视剧制作MiniMaxH3多参视频生成发布版 多模态输入_2109729477717741570.json、视频生成/图生视频/Fused-MiniMax H3战斗增强双采｜图生视频火力全开_2097934793827766274.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 10 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `RandomNoise` —— 8/10 个有
- `SamplerCustomAdvanced` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `SplitSigmas` —— 8/10 个有
- `Text` —— 8/10 个有
- `MinimaxH3LatentUpscaler3D` —— 7/10 个有
- `SaveImage` —— 7/10 个有
- `VHS_LoadVideo` —— 6/10 个有
- `LTXVConcatAVLatent` —— 5/10 个有
- `LTXVSeparateAVLatent` —— 5/10 个有
- `ModelAttentionBackend` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `Float` —— 4/10 个有
- `LoadAudio` —— 4/10 个有
- `PrimitiveFloat` —— 4/10 个有
- `SolAttnMiniMax` —— 4/10 个有
- `easy float` —— 4/10 个有
- `CR Prompt Text` —— 2/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `H3SigmaRefiner` —— 2/10 个有
- `JWFloat` —— 2/10 个有
- `Lora Loader Stack (rgthree)` —— 2/10 个有
- `MiniMaxH3AVLatentSeparateT8` —— 2/10 个有
- `PT_H3ConcatAVLatent` —— 2/10 个有
- `SelfLiftH3Sampler` —— 2/10 个有
- `VHS_LoadAudioUpload` —— 2/10 个有
- `VRAM_Debug` —— 2/10 个有
- `AudioSeparation` —— 1/10 个有
- `GH_AudioVideoMerger` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `MiniMaxChunkFeedForward` —— 1/10 个有
- `MiniMaxLowVRAMAttention` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SeedVR2LoadDiTModel` —— 1/10 个有
- `SeedVR2LoadVAEModel` —— 1/10 个有
- `SeedVR2VideoUpscaler` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

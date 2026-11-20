---
name: text_to_image_video_lora_sampler_114
type: Text To Image
frequency: 8
level: strong
coverage: 0.558625
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ResolutionSelector, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json, 视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json, 视频生成/图生视频/AITUDOU MiniMax H3短剧公司版｜短剧批量制作团队方案_2113558862644203521.json, 视频生成/图生视频/AI影视剧制作MiniMaxH3多参视频生成发布版 多模态输入_2109729477717741570.json, 视频生成/图生视频/Fused-MiniMax H3战斗增强双采｜图生视频火力全开_2097934793827766274.json, 视频生成/图生视频/H3动作迁移2.0进阶史诗强化，图生视频自带放大_2110857064611405825.json, 视频生成/图生视频/H3电影LORA巅峰双采去油PRO版视频生成处理工具_2101017420696739841.json, 视频生成/图生视频/MiniMax H3多参生视频 图生视频多模态参考创作_2099194857146376194.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_114

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/AITUDOU MiniMax H3 SelfLift影视级情绪表达SKILL工作流_2105052149024645122.json、视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json、视频生成/图生视频/AITUDOU MiniMax H3短剧公司版｜短剧批量制作团队方案_2113558862644203521.json、视频生成/图生视频/AI影视剧制作MiniMaxH3多参视频生成发布版 多模态输入_2109729477717741570.json、视频生成/图生视频/Fused-MiniMax H3战斗增强双采｜图生视频火力全开_2097934793827766274.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 7/8 个有
- `RandomNoise` —— 7/8 个有
- `SamplerCustomAdvanced` —— 7/8 个有
- `SaveImage` —— 6/8 个有
- `SplitSigmas` —— 6/8 个有
- `Text` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `Float` —— 5/8 个有
- `MinimaxH3LatentUpscaler3D` —— 5/8 个有
- `LTXVConcatAVLatent` —— 3/8 个有
- `LTXVSeparateAVLatent` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `H3SigmaRefiner` —— 2/8 个有
- `JWFloat` —— 2/8 个有
- `MiniMaxH3AVLatentSeparateT8` —— 2/8 个有
- `ModelAttentionBackend` —— 2/8 个有
- `PT_H3ConcatAVLatent` —— 2/8 个有
- `SelfLiftH3Sampler` —— 2/8 个有
- `VHS_LoadAudioUpload` —— 2/8 个有
- `VRAM_Debug` —— 2/8 个有
- `AudioSeparation` —— 1/8 个有
- `GH_AudioVideoMerger` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `MiniMaxChunkFeedForward` —— 1/8 个有
- `MiniMaxH3VoiceLibraryLoadT8` —— 1/8 个有
- `MiniMaxLowVRAMAttention` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `SeedVR2LoadDiTModel` —— 1/8 个有
- `SeedVR2LoadVAEModel` —— 1/8 个有
- `SeedVR2VideoUpscaler` —— 1/8 个有
- `SolAttnMiniMax` —— 1/8 个有
- `easy float` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

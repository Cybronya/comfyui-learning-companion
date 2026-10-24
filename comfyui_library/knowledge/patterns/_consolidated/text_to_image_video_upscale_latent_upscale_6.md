---
name: text_to_image_video_upscale_latent_upscale_6
type: Text To Image
frequency: 15
level: strong
coverage: 0.764733
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3社区模型工作流｜高质量加速版图生视频_2095147029315018754.json, 视频生成/图生视频/MiniMax H3参考生视频｜10Eros turbo动态叙事_2095275498304790529.json, 视频生成/图生视频/MiniMax H3参考生视频｜Dasiwa v2叠加singularity双采_2099863444169248769.json, 视频生成/图生视频/MiniMax H3双采V2二采版｜音频驱动数字人电商带货直出_2103050202750996481.json, 视频生成/图生视频/MiniMax H3双采全能V2文戏不油武戏动态强，电商带货参考生视频方案_2103180413962383361.json, 视频生成/图生视频/MiniMax H3双采全能V2音频驱动数字人，电商带货二采图生视频工作流_2103182055260647425.json, 视频生成/图生视频/MiniMax H3双采全能V2｜文戏细腻武戏动态强电商带货参考生视频_2103048629668892674.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3语义桥，文戏不油武戏动态强参考生视频_2105749839286984706.json, 视频生成/图生视频/MiniMax H3超强商品视频展示｜电商产品图生视频带货神器_2108008108562931714.json, 视频生成/图生视频/MiniMax H3音频驱动数字人对口型唱歌说话口播Remix文戏版方案_2105744989383913473.json, 视频生成/图生视频/动态最强参考生视频｜MiniMax H3 V1版图生视频_2095050766850551809.json, 视频生成/图生视频/格莱美慢镜头质感 MiniMax H3双采参考生视频动态可控_2104360820577759233.json, 视频生成/图生视频/高质量加速版0902｜H3社区模型图生视频生成_2095103895356919810.json, 视频生成/图生视频/高质量加速版图生视频｜H3社区模型一键生成_2095492025532637185.json, 视频生成/图生视频/高质量加速版｜H3社区模型工作流图生视频_2092733195283423233.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_6

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/H3社区模型工作流｜高质量加速版图生视频_2095147029315018754.json、视频生成/图生视频/MiniMax H3参考生视频｜10Eros turbo动态叙事_2095275498304790529.json、视频生成/图生视频/MiniMax H3参考生视频｜Dasiwa v2叠加singularity双采_2099863444169248769.json、视频生成/图生视频/MiniMax H3双采V2二采版｜音频驱动数字人电商带货直出_2103050202750996481.json、视频生成/图生视频/MiniMax H3双采全能V2文戏不油武戏动态强，电商带货参考生视频方案_2103180413962383361.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 15 个 workflow 都包含：
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
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/15 个有
- `LoraLoaderBypassModelOnly` —— 11/15 个有
- `SetNode` —— 11/15 个有
- `Float` —— 7/15 个有
- `LoadAudio` —— 7/15 个有
- `Fast Groups Bypasser (rgthree)` —— 5/15 个有
- `PrimitiveInt` —— 5/15 个有
- `SaveImage` —— 5/15 个有
- `VAEDecodeAudio` —— 5/15 个有
- `BasicScheduler` —— 4/15 个有
- `ConcatTextOfUtils` —— 4/15 个有
- `KSamplerSelect` —— 4/15 个有
- `LoadVideo` —— 4/15 个有
- `MiniMaxH3Easy` —— 4/15 个有
- `MiniMaxH3EasyLoader` —— 4/15 个有
- `MiniMaxH3EasyOutput` —— 4/15 个有
- `MiniMaxH3ReferenceToVideo` —— 4/15 个有
- `PrimitiveStringMultiline` —— 4/15 个有
- `Lora Loader Stack (rgthree)` —— 3/15 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/15 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/15 个有
- `easy anythingIndexSwitch` —— 2/15 个有
- `CR Text Concatenate` —— 1/15 个有
- `Fast Muter (rgthree)` —— 1/15 个有
- `ImageCrop` —— 1/15 个有
- `ImageFromBatch` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `MuyeTextEditOutput` —— 1/15 个有
- `TrimAudioDuration` —— 1/15 个有
- `VHS_LoadVideo` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足

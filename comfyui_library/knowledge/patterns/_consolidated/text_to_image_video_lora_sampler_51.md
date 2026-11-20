---
name: text_to_image_video_lora_sampler_51
type: Text To Image
frequency: 15
level: strong
coverage: 0.863933
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3超级加速二阶段快速文戏视频工作流 高效生成_2099913692656787457.json, 图片生成/图生图/MiniMax H3超级加速工作流｜二阶段快速文戏视频生成_2097430777486204930.json, 图片生成/图生图/二阶段快速文戏｜MiniMax H3超级加速，热门IP视频快出_2099923443507617794.json, 图片生成/图生图/双时钟8步高质量极速图生视频V2｜Minimax图生图工作流_2088157021035126785.json, 视频生成/图生视频/H3双采参考生视频Dasiwa V2版本对白战斗动作戏_2100636081782874114.json, 视频生成/图生视频/H3双采参考生视频V2 文戏武戏低显存适配版_2098846488892887041.json, 视频生成/图生视频/MiniMax H3 参考生视频多图参考｜最强战斗特效效果拉满_2096865093039513601.json, 视频生成/图生视频/MiniMax H3不油文剧工作流｜图生视频剧情质感生成_2097099800738095105.json, 视频生成/图生视频/MiniMax H3参考生视频｜10Eros turbo动态叙事_2095275498304790529.json, 视频生成/图生视频/MiniMax H3参考生视频｜Dasiwa v2叠加singularity双采_2099863444169248769.json, 视频生成/图生视频/MiniMax H3双采全能V2文戏不油武戏动态强，电商带货参考生视频方案_2103180413962383361.json, 视频生成/图生视频/MiniMax H3双采全能V2音频驱动数字人，电商带货二采图生视频工作流_2103182055260647425.json, 视频生成/图生视频/MiniMax H3双采全能V2｜文戏细腻武戏动态强电商带货参考生视频_2103048629668892674.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3语义桥，文戏不油武戏动态强参考生视频_2105749839286984706.json, 视频生成/文生视频/10Eros Beta5+FL2VA Ref2VA小脸去油二采精修视频处理工具_2102108154879369218.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/H3超级加速二阶段快速文戏视频工作流 高效生成_2099913692656787457.json、图片生成/图生图/MiniMax H3超级加速工作流｜二阶段快速文戏视频生成_2097430777486204930.json、图片生成/图生图/二阶段快速文戏｜MiniMax H3超级加速，热门IP视频快出_2099923443507617794.json、图片生成/图生图/双时钟8步高质量极速图生视频V2｜Minimax图生图工作流_2088157021035126785.json、视频生成/图生视频/H3双采参考生视频Dasiwa V2版本对白战斗动作戏_2100636081782874114.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：86%

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
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/15 个有
- `SolAttnMiniMax` —— 14/15 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 11/15 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 11/15 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 11/15 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 11/15 个有
- `SaveImage` —— 9/15 个有
- `ConcatTextOfUtils` —— 8/15 个有
- `Float` —— 6/15 个有
- `CreateVideo` —— 4/15 个有
- `Fast Groups Bypasser (rgthree)` —— 4/15 个有
- `GetNode` —— 4/15 个有
- `GetVideoComponents` —— 4/15 个有
- `SaveVideo` —— 4/15 个有
- `SetNode` —— 4/15 个有
- `CFGGuider` —— 3/15 个有
- `LTXVConditioning` —— 3/15 个有
- `LTXVLatentUpsampler` —— 3/15 个有
- `LatentUpscaleModelLoader` —— 3/15 个有
- `MiniMaxH3OutputTrimT8` —— 3/15 个有
- `MiniMaxH3SolEngineDraftToLTXT8Advanced` —— 3/15 个有
- `MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced` —— 3/15 个有
- `MiniMaxH3SolEngineTAEHVDecodeT8Advanced` —— 3/15 个有
- `MiniMaxH3SolEngineTAEHVLoaderT8Advanced` —— 3/15 个有
- `VAEEncode` —— 3/15 个有
- `easy anythingIndexSwitch` —— 3/15 个有
- `LoadAudio` —— 2/15 个有
- `AudioCrop` —— 1/15 个有
- `LoadVideo` —— 1/15 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/15 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/15 个有
- `Video Slice` —— 1/15 个有

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

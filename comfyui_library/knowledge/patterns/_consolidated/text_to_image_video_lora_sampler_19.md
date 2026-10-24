---
name: text_to_image_video_lora_sampler_19
type: Text To Image
frequency: 27
level: strong
coverage: 0.905852
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3全能参考生视频加速版 多重加速高清输出_2098827453300039682.json, 视频生成/图生视频/MiniMax H3参考生视频电商带货｜创意产品展示新玩法_2108086527170531330.json, 视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json, 视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json, 视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json, 视频生成/图生视频/MiniMax H3双采参考生视频｜8步turbo分镜叙事_2095276866591608833.json, 视频生成/图生视频/MiniMax H3双采数字人口播 双Pass高清精修工作流_2098824235585200129.json, 视频生成/图生视频/MiniMax H3双采数字人口播｜双Pass高清精修视频生成_2097495644985446401.json, 视频生成/图生视频/MiniMax H3双采模式｜多图参考生视频画质更稳_2105138633752793090.json, 视频生成/图生视频/MiniMax H3多参双采参考长视频Pov第一视角 沉浸式视频生成_2105369174095785985.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜POV第一视角沉浸感｜参考生视频出新招_2104794146677551106.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜Pov第一视角沉浸体验_2105259470069784577.json, 视频生成/图生视频/MiniMax H3多图参考双采生视频｜HyperVae 2X高清图生视频_2111058302082830338.json, 视频生成/图生视频/MiniMax H3多图参考双采，HyperVae 2X高清图生视频_2111259409954459649.json, 视频生成/图生视频/MiniMax H3长视频POV第一视角｜多参考双采样图生视频｜人物特效角色设计_2104751091027103746.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参工作流，角色一致性图生视频方案_2107184502861819906.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参｜角色一致性运镜图生视频_2106998238581714946.json, 视频生成/图生视频/MiniMax_H3长视频直出双采多参工作流，角色一致性图生视频方案_2109461992850419714.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105001173613899778.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105078692375519233.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105444809631686658.json, 视频生成/文生视频/30秒长视频文武双修均衡版高清 视频生成方案_2105053597879848962.json, 视频生成/文生视频/H3长视频优化版｜文生视频视频生视频图生视频全支持_2106981562544902146.json, 视频生成/文生视频/MiniMax H3文武双修均衡版 20秒长视频双采多参考图生视频HyperVae 2X高清_2105117710463098882.json, 视频生成/文生视频/MiniMax H3文武双修均衡版｜20秒长视频双采多参考｜HyperVae 2X高清_2104829141102190593.json, 视频生成/文生视频/多参双采30秒直出 MiniMax H3参考生视频最强均衡版_2104298425591353346.json, 视频生成/文生视频/长视频优化版H3工作流，文生视频视频生视频图生视频方案_2107243300871827458.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3全能参考生视频加速版 多重加速高清输出_2098827453300039682.json、视频生成/图生视频/MiniMax H3参考生视频电商带货｜创意产品展示新玩法_2108086527170531330.json、视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json、视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json、视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 26/27 个有
- `孤海注释` —— 26/27 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 25/27 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 25/27 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 25/27 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 25/27 个有
- `LoraLoaderBypassModelOnly` —— 24/27 个有
- `Float` —— 21/27 个有
- `easy anythingIndexSwitch` —— 21/27 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 19/27 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 19/27 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 18/27 个有
- `RunningHub Deepcleaner` —— 18/27 个有
- `easy cleanGpuUsed` —— 18/27 个有
- `SaveImage` —— 15/27 个有
- `Astra` —— 13/27 个有
- `CreateVideo` —— 13/27 个有
- `SaveVideo` —— 13/27 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 4/27 个有
- `MiniMaxH3OutputTrimT8` —— 4/27 个有
- `ConcatTextOfUtils` —— 3/27 个有
- `GetNode` —— 3/27 个有
- `LoadAudio` —— 3/27 个有
- `SetNode` —— 3/27 个有
- `VHS_LoadVideo` —— 3/27 个有
- `VHS_LoadAudioUpload` —— 2/27 个有
- `CR Text` —— 1/27 个有
- `EmptyImage` —— 1/27 个有
- `ExtendIntermediateSigmas` —— 1/27 个有
- `IntToString` —— 1/27 个有
- `PathchSageAttentionKJ` —— 1/27 个有
- `PreviewAny` —— 1/27 个有
- `PreviewImage` —— 1/27 个有
- `Seed_` —— 1/27 个有
- `text-util-join-text` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高发问题（28/27 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_11
type: Text To Image
frequency: 30
level: strong
coverage: 0.908467
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json, 视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json, 视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json, 视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json, 视频生成/图生视频/MiniMax H3双采参考生视频低显存版｜图生视频小显卡也能跑_2104566495551516674.json, 视频生成/图生视频/MiniMax H3双采参考生视频｜8步turbo分镜叙事_2095276866591608833.json, 视频生成/图生视频/MiniMax H3双采数字人口播 双Pass高清精修工作流_2098824235585200129.json, 视频生成/图生视频/MiniMax H3双采数字人口播｜双Pass高清精修视频生成_2097495644985446401.json, 视频生成/图生视频/MiniMax H3双采模式｜多图参考生视频画质更稳_2105138633752793090.json, 视频生成/图生视频/MiniMax H3多参双采参考长视频Pov第一视角 沉浸式视频生成_2105369174095785985.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜POV第一视角沉浸感｜参考生视频出新招_2104794146677551106.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜Pov第一视角沉浸体验_2105259470069784577.json, 视频生成/图生视频/MiniMax H3多图参考双采生视频｜HyperVae 2X高清图生视频_2111058302082830338.json, 视频生成/图生视频/MiniMax H3多图参考双采，HyperVae 2X高清图生视频_2111259409954459649.json, 视频生成/图生视频/MiniMax H3长视频POV第一视角｜多参考双采样图生视频｜人物特效角色设计_2104751091027103746.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参工作流，角色一致性图生视频方案_2107184502861819906.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参｜角色一致性运镜图生视频_2106998238581714946.json, 视频生成/图生视频/MiniMax_H3长视频直出双采多参工作流，角色一致性图生视频方案_2109461992850419714.json, 视频生成/图生视频/低显存也能跑 MiniMax H3双采参考生视频方案_2104650144351346689.json, 视频生成/图生视频/低显存友好方案｜时间分块前馈分块MiniMax H3双采参考生视频_2101157041715900417.json, 视频生成/图生视频/时间分块前馈分块降显存｜MiniMax H3双采参考生视频_2101187630208737281.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105001173613899778.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105078692375519233.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105444809631686658.json, 视频生成/文生视频/30秒长视频文武双修均衡版高清 视频生成方案_2105053597879848962.json, 视频生成/文生视频/H3长视频优化版｜文生视频视频生视频图生视频全支持_2106981562544902146.json, 视频生成/文生视频/MiniMax H3文武双修均衡版 20秒长视频双采多参考图生视频HyperVae 2X高清_2105117710463098882.json, 视频生成/文生视频/MiniMax H3文武双修均衡版｜20秒长视频双采多参考｜HyperVae 2X高清_2104829141102190593.json, 视频生成/文生视频/多参双采30秒直出 MiniMax H3参考生视频最强均衡版_2104298425591353346.json, 视频生成/文生视频/长视频优化版H3工作流，文生视频视频生视频图生视频方案_2107243300871827458.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json、视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json、视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json、视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json、视频生成/图生视频/MiniMax H3双采参考生视频低显存版｜图生视频小显卡也能跑_2104566495551516674.json…）

- **类型**：Text To Image
- **样本数**：30
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 30 个 workflow 都包含：
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
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 29/30 个有
- `LoraLoaderBypassModelOnly` —— 28/30 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 25/30 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 25/30 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 25/30 个有
- `PrimitiveFloat` —— 25/30 个有
- `VHS_VideoCombine` —— 25/30 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 23/30 个有
- `easy cleanGpuUsed` —— 23/30 个有
- `Float` —— 21/30 个有
- `easy anythingIndexSwitch` —— 21/30 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 19/30 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 19/30 个有
- `CreateVideo` —— 18/30 个有
- `RunningHub Deepcleaner` —— 18/30 个有
- `SaveVideo` —— 18/30 个有
- `SaveImage` —— 16/30 个有
- `Astra` —— 13/30 个有
- `JWFloat` —— 5/30 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 5/30 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 5/30 个有
- `PreviewAny` —— 5/30 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 4/30 个有
- `MiniMaxH3OutputTrimT8` —— 4/30 个有
- `ConcatTextOfUtils` —— 3/30 个有
- `GetNode` —— 3/30 个有
- `SetNode` —— 3/30 个有
- `LoadAudio` —— 2/30 个有
- `VHS_LoadAudioUpload` —— 2/30 个有
- `VHS_LoadVideo` —— 2/30 个有
- `EmptyImage` —— 1/30 个有
- `PreviewImage` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 30 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 30 | 100% |
| 采样算法 | er_sde | - | 30 | 100% |
| 调度器 | beta | - | 30 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 30 | 100% |
| 宽度 | 80 | 80 - 80 | 30 | 100% |
| 高度 | 80 | 80 - 80 | 30 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/30 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，30 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，30 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，30 个样本，一致性 100%
- 调度器 最常用 beta，30 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，30 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，30 个样本，取值集中（一致性 100%）
- 高发问题（31/30 个样本）：Steps较低可能导致细节不足

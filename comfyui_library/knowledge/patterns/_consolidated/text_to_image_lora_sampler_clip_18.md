---
name: text_to_image_lora_sampler_clip_18
type: Text To Image
frequency: 29
level: strong
coverage: 0.904793
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json, 视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json, 视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json, 视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json, 视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json, 视频生成/图生视频/MiniMax H3双采参考生视频低显存版｜图生视频小显卡也能跑_2104566495551516674.json, 视频生成/图生视频/MiniMax H3双采参考生视频｜8步turbo分镜叙事_2095276866591608833.json, 视频生成/图生视频/MiniMax H3双采数字人口播 双Pass高清精修工作流_2098824235585200129.json, 视频生成/图生视频/MiniMax H3双采数字人口播｜双Pass高清精修视频生成_2097495644985446401.json, 视频生成/图生视频/MiniMax H3双采模式｜多图参考生视频画质更稳_2105138633752793090.json, 视频生成/图生视频/MiniMax H3双采生视频 动作优化微调图生视频工具_2113404250654076929.json, 视频生成/图生视频/MiniMax H3双采生视频Hybird+VBVR逻辑强化均衡版，长视频稳定直出_2114494390554157057.json, 视频生成/图生视频/MiniMax H3多参双采参考长视频Pov第一视角 沉浸式视频生成_2105369174095785985.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜POV第一视角沉浸感｜参考生视频出新招_2104794146677551106.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜Pov第一视角沉浸体验_2105259470069784577.json, 视频生成/图生视频/MiniMax H3超强商品视频展示｜电商产品图生视频带货神器_2108008108562931714.json, 视频生成/图生视频/MiniMax H3长视频POV第一视角｜多参考双采样图生视频｜人物特效角色设计_2104751091027103746.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参工作流，角色一致性图生视频方案_2107184502861819906.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参｜角色一致性运镜图生视频_2106998238581714946.json, 视频生成/图生视频/MiniMax H3音频驱动数字人对口型唱歌说话口播Remix文戏版方案_2105744989383913473.json, 视频生成/图生视频/MiniMax_H3长视频直出双采多参工作流，角色一致性图生视频方案_2109461992850419714.json, 视频生成/图生视频/双采V3图生视频工作流｜双倍采样画质更稳_2114176763180969986.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105001173613899778.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105078692375519233.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105444809631686658.json, 视频生成/文生视频/30秒长视频文武双修均衡版高清 视频生成方案_2105053597879848962.json, 视频生成/文生视频/H3长视频优化版｜文生视频视频生视频图生视频全支持_2106981562544902146.json, 视频生成/文生视频/多参双采30秒直出 MiniMax H3参考生视频最强均衡版_2104298425591353346.json, 视频生成/文生视频/长视频优化版H3工作流，文生视频视频生视频图生视频方案_2107243300871827458.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json、视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json、视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json、视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json、视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 29 个 workflow 都包含：
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DualClockSamplerT8` —— 28/29 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 28/29 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 28/29 个有
- `ModelAttentionBackend` —— 28/29 个有
- `孤海注释` —— 28/29 个有
- `PrimitiveFloat` —— 27/29 个有
- `LoraLoaderBypassModelOnly` —— 26/29 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 26/29 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 26/29 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 26/29 个有
- `VHS_VideoCombine` —— 26/29 个有
- `Float` —— 20/29 个有
- `easy anythingIndexSwitch` —— 20/29 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 19/29 个有
- `easy cleanGpuUsed` —— 19/29 个有
- `CreateVideo` —— 18/29 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 18/29 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 18/29 个有
- `SaveVideo` —— 18/29 个有
- `RunningHub Deepcleaner` —— 17/29 个有
- `SaveImage` —— 16/29 个有
- `Astra` —— 15/29 个有
- `ConcatTextOfUtils` —— 4/29 个有
- `GetNode` —— 4/29 个有
- `LoadAudio` —— 4/29 个有
- `SetNode` —— 4/29 个有
- `JWFloat` —— 2/29 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 2/29 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 2/29 个有
- `PreviewAny` —— 2/29 个有
- `VAEDecodeAudio` —— 2/29 个有
- `CR Text Concatenate` —— 1/29 个有
- `EmptyImage` —— 1/29 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/29 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/29 个有
- `MuyeTextEditOutput` —— 1/29 个有
- `PreviewImage` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 29 | 100% |
| 高度 | 80 | 80 - 80 | 29 | 100% |
| 采样步数 | 4 | 4 - 4 | 29 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 29 | 100% |
| 采样算法 | er_sde | - | 29 | 100% |
| 调度器 | beta | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，29 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，29 个样本，一致性 100%
- 调度器 最常用 beta，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 高发问题（30/29 个样本）：Steps较低可能导致细节不足

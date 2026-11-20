---
name: text_to_image_video_lora_sampler_32
type: Text To Image
frequency: 19
level: strong
coverage: 0.936947
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3全能参考生视频加速版 多重加速高清输出_2098827453300039682.json, 视频生成/图生视频/MiniMax H3参考生视频4步加速 6参考图图生视频处理工具_2113015406763003906.json, 视频生成/图生视频/MiniMax H3参考生视频电商带货｜创意产品展示新玩法_2108086527170531330.json, 视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json, 视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json, 视频生成/图生视频/MiniMax H3双采参考生视频V2｜文戏武戏低显存适配流畅跑_2099134658318524417.json, 视频生成/图生视频/MiniMax H3双采参考生视频｜8步turbo分镜叙事_2095276866591608833.json, 视频生成/图生视频/MiniMax H3双采数字人口播 双Pass高清精修工作流_2098824235585200129.json, 视频生成/图生视频/MiniMax H3双采数字人口播｜双Pass高清精修视频生成_2097495644985446401.json, 视频生成/图生视频/MiniMax H3双采模式｜多图参考生视频画质更稳_2105138633752793090.json, 视频生成/图生视频/MiniMax H3双采生视频 动作优化微调图生视频工具_2113404250654076929.json, 视频生成/图生视频/MiniMax H3双采生视频Hybird+VBVR逻辑强化均衡版，长视频稳定直出_2114494390554157057.json, 视频生成/图生视频/MiniMax H3多参双采参考长视频Pov第一视角 沉浸式视频生成_2105369174095785985.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜POV第一视角沉浸感｜参考生视频出新招_2104794146677551106.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜Pov第一视角沉浸体验_2105259470069784577.json, 视频生成/图生视频/MiniMax H3多图参考双采生视频｜HyperVae 2X高清图生视频_2111058302082830338.json, 视频生成/图生视频/MiniMax H3多图参考双采，HyperVae 2X高清图生视频_2111259409954459649.json, 视频生成/文生视频/MiniMax H3文武双修均衡版 20秒长视频双采多参考图生视频HyperVae 2X高清_2105117710463098882.json, 视频生成/文生视频/MiniMax H3文武双修均衡版｜20秒长视频双采多参考｜HyperVae 2X高清_2104829141102190593.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3全能参考生视频加速版 多重加速高清输出_2098827453300039682.json、视频生成/图生视频/MiniMax H3参考生视频4步加速 6参考图图生视频处理工具_2113015406763003906.json、视频生成/图生视频/MiniMax H3参考生视频电商带货｜创意产品展示新玩法_2108086527170531330.json、视频生成/图生视频/MiniMax H3双采参考 八步turbo分镜叙事视频生成_2098120649641381889.json、视频生成/图生视频/MiniMax H3双采参考生视频Dasiwa v2版｜图生视频二次采样画质更扎实_2100438094607634434.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 19 个 workflow 都包含：
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
- `CR Prompt Text` —— 18/19 个有
- `ModelAttentionBackend` —— 18/19 个有
- `LoraLoaderBypassModelOnly` —— 16/19 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 16/19 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 16/19 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 16/19 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 16/19 个有
- `Float` —— 12/19 个有
- `easy anythingIndexSwitch` —— 12/19 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 10/19 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 10/19 个有
- `SaveImage` —— 10/19 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 9/19 个有
- `RunningHub Deepcleaner` —— 9/19 个有
- `easy cleanGpuUsed` —— 9/19 个有
- `Astra` —— 4/19 个有
- `CreateVideo` —— 4/19 个有
- `LoadAudio` —— 4/19 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 4/19 个有
- `MiniMaxH3OutputTrimT8` —— 4/19 个有
- `SaveVideo` —— 4/19 个有
- `ConcatTextOfUtils` —— 3/19 个有
- `VHS_LoadVideo` —— 3/19 个有
- `VHS_LoadAudioUpload` —— 2/19 个有
- `CR Text` —— 1/19 个有
- `ExtendIntermediateSigmas` —— 1/19 个有
- `IntToString` —— 1/19 个有
- `MiniMaxH3BlockCacheT8` —— 1/19 个有
- `ModelPreviewOverrideKJ` —— 1/19 个有
- `PathchSageAttentionKJ` —— 1/19 个有
- `PreviewAny` —— 1/19 个有
- `Seed_` —— 1/19 个有
- `VAEDecodeAudio` —— 1/19 个有
- `text-util-join-text` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足

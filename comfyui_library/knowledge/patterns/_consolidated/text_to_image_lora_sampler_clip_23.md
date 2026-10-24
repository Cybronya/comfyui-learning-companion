---
name: text_to_image_lora_sampler_clip_23
type: Text To Image
frequency: 24
level: strong
coverage: 0.923458
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json, 视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json, 视频生成/图生视频/MiniMax H3双采参考生视频低显存版｜图生视频小显卡也能跑_2104566495551516674.json, 视频生成/图生视频/MiniMax H3视频复刻加速版，数字人参考生视频与长视频直出工作流_2102827221554651137.json, 视频生成/图生视频/MiniMax H3视频复刻数字人加速版｜参考生视频长视频直出｜口播福音_2102608437405372417.json, 视频生成/图生视频/MiniMax H3视频复刻数字人换人换产品文案不换原声保留_2108718797380218882.json, 视频生成/图生视频/MiniMax H3视频复刻数字人视频换人换产品换文案语音替换_2108676232131997697.json, 视频生成/图生视频/MiniMax H3视频复刻数字人｜换人换产品换文案换语音_2111128408808845313.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜换人换产品文案不换原声保留_2107986135334088706.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2107984724403777537.json, 视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话加速版长视频处理工具，数字人生成方案_2109462993590382594.json, 视频生成/图生视频/Minimax H3边跳边换装工作流｜图生视频动态效果生成_2097847006080356353.json, 视频生成/图生视频/Minimax H3边跳边换装｜舞蹈换装一镜到底_2097910210886197250.json, 视频生成/图生视频/Remix双采加速参考生视频｜MiniMax-H3 Latent Upscaler_2093484648100884482.json, 视频生成/图生视频/minimax商品视频展示 产品展示动态效果一键生成_2104643850022252545.json, 视频生成/图生视频/minimax商品视频展示｜图生视频电商产品动态主图制作_2104552227313639426.json, 视频生成/图生视频/低显存也能跑 MiniMax H3双采参考生视频方案_2104650144351346689.json, 视频生成/图生视频/低显存友好方案｜时间分块前馈分块MiniMax H3双采参考生视频_2101157041715900417.json, 视频生成/图生视频/参考生视频最强战斗效果｜MiniMax H3多图参考图生视频_2096673588765093890.json, 视频生成/图生视频/双时钟双采加速｜Latent Upscaler参考生视频H3版_2092746811000844289.json, 视频生成/图生视频/双时钟双采加速｜Minimax H3 Latent Upscaler图生视频_2091203656212373506.json, 视频生成/图生视频/时间分块前馈分块降显存｜MiniMax H3双采参考生视频_2101187630208737281.json, 视频生成/图生视频/最强Minimax商品视频展示工作流，图生视频电商产品展示处理工具_2108426664534433793.json, 视频生成/文生视频/10Eros Beta5+FL2VA Ref2VA小脸去油二采精修视频处理工具_2102108154879369218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json、视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json、视频生成/图生视频/MiniMax H3双采参考生视频低显存版｜图生视频小显卡也能跑_2104566495551516674.json、视频生成/图生视频/MiniMax H3视频复刻加速版，数字人参考生视频与长视频直出工作流_2102827221554651137.json、视频生成/图生视频/MiniMax H3视频复刻数字人加速版｜参考生视频长视频直出｜口播福音_2102608437405372417.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 24 个 workflow 都包含：
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
- `LoraLoaderBypassModelOnly` —— 23/24 个有
- `MiniMaxH3DualClockSamplerT8` —— 23/24 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 23/24 个有
- `ModelAttentionBackend` —— 23/24 个有
- `孤海注释` —— 21/24 个有
- `PrimitiveFloat` —— 19/24 个有
- `VHS_VideoCombine` —— 18/24 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 15/24 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 10/24 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 10/24 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 10/24 个有
- `SaveImage` —— 10/24 个有
- `CreateVideo` —— 7/24 个有
- `SaveVideo` —— 7/24 个有
- `VHS_LoadVideo` —— 7/24 个有
- `EmptyImage` —— 5/24 个有
- `JWFloat` —— 5/24 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 5/24 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 5/24 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 5/24 个有
- `PreviewAny` —— 5/24 个有
- `PreviewImage` —— 5/24 个有
- `easy cleanGpuUsed` —— 5/24 个有
- `ConcatTextOfUtils` —— 4/24 个有
- `VAEDecodeAudio` —— 3/24 个有
- `LoadAudio` —— 2/24 个有
- `StariAI-MiniMaxH3-Skill` —— 2/24 个有
- `AudioCrop` —— 1/24 个有
- `GetVideoComponents` —— 1/24 个有
- `LoadVideo` —— 1/24 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/24 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/24 个有
- `Video Slice` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 24 | 100% |
| 高度 | 80 | 80 - 80 | 24 | 100% |
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 100% |
| 调度器 | beta | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（28/24 个样本）：Steps较低可能导致细节不足

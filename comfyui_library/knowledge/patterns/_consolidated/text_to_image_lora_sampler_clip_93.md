---
name: text_to_image_lora_sampler_clip_93
type: Text To Image
frequency: 14
level: strong
coverage: 0.800929
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 导演台｜首尾帧生视频加速二采段间引导｜手机端可用_2096836369745268738.json, 视频生成/图生视频/MinimaxH3电商多参生视频｜数字人视频生成直出_2092376463248019457.json, 视频生成/图生视频/导演台首尾帧生视频加速二采｜MiniMax H3手机端可用_2091664862375141378.json, 视频生成/图生视频/首尾帧生视频导演台｜MiniMax H3加速二采段间引导手机可用_2096657470713327617.json, 视频生成/文生视频/MiniMax H3导演台多参主图生视频｜r2v多模生成_2095223469838524417.json, 视频生成/文生视频/MiniMax H3导演台多参主图｜图生视频r2v生成_2095209145090789377.json, 视频生成/文生视频/MiniMax H3导演台工作流｜加速二采段间引导手机可用_2097790692042039298.json, 视频生成/文生视频/Minimax H3多参二次采样加速lora-文生视频生视频图生视频_2087402636411760642.json, 视频生成/文生视频/rv2v参考素材改视频｜MinimaxH3导演台优化版三模生成_2092598806088077313.json, 视频生成/文生视频/多参主图文生视频生成｜MiniMax H3导演台r2v视频版_2095561044872749057.json, 视频生成/文生视频/导演台rv2v参考素材改视频｜MinimaxH3优化版本_2092346894843469826.json, 视频生成/文生视频/导演台加速二采段间引导｜MiniMax H3手机端可用文生视频_2091239932064002050.json, 视频生成/文生视频/导演台多参主图生视频｜MiniMax H3 r2v文生视频_2095487730972192769.json, 视频生成/文生视频/导演台手机端可用｜MiniMax H3文生图生视频_2090925240871374849.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 导演台｜首尾帧生视频加速二采段间引导｜手机端可用_2096836369745268738.json、视频生成/图生视频/MinimaxH3电商多参生视频｜数字人视频生成直出_2092376463248019457.json、视频生成/图生视频/导演台首尾帧生视频加速二采｜MiniMax H3手机端可用_2091664862375141378.json、视频生成/图生视频/首尾帧生视频导演台｜MiniMax H3加速二采段间引导手机可用_2096657470713327617.json、视频生成/文生视频/MiniMax H3导演台多参主图生视频｜r2v多模生成_2095223469838524417.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 13/14 个有
- `GetNode` —— 13/14 个有
- `ImageResizeKJv2` —— 13/14 个有
- `LTXVConcatAVLatent` —— 13/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/14 个有
- `PathchSageAttentionKJ` —— 13/14 个有
- `PreviewAny` —— 13/14 个有
- `SaveVideo` —— 13/14 个有
- `SetNode` —— 13/14 个有
- `VAEEncode` —— 13/14 个有
- `VAEEncodeAudio` —— 13/14 个有
- `CR Model Input Switch` —— 12/14 个有
- `GetImageSizeAndCount` —— 12/14 个有
- `LazySwitch1way` —— 12/14 个有
- `MiniMaxH3Director` —— 12/14 个有
- `VHS_VideoCombine` —— 12/14 个有
- `easy boolean` —— 12/14 个有
- `LayerUtility: PurgeVRAM` —— 11/14 个有
- `LoadImage` —— 2/14 个有
- `PrimitiveFloat` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有
- `RH_LLMAPI_Pro_Node` —— 2/14 个有
- `easy showAnything` —— 2/14 个有
- `GetVideoComponents` —— 1/14 个有
- `LoadVideo` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `StringFunction|pysssss` —— 1/14 个有
- `Switch` —— 1/14 个有
- `easy saveText` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足

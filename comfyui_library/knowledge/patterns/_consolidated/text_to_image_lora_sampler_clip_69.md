---
name: text_to_image_lora_sampler_clip_69
type: Text To Image
frequency: 13
level: strong
coverage: 0.870462
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/4步8步加速稳定MAX｜MiniMaxH3多合一自用版_2092748173281423361.json, 视频生成/文生视频/8步加速电影质感 Minimax H3 文生视频LoRA强化出片_2094165667820957697.json, 视频生成/文生视频/9图3视频3音频全能多参音视频生成开源加速版｜海螺H3文生图生视频工作流_2088148034331963394.json, 视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085422971736383489.json, 视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085791756154654721.json, 视频生成/文生视频/H3开源9宫视图片Minimax图生视频EasyCache+Sage Attention KJ加速_2086197329035616258.json, 视频生成/文生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086200437891485697.json, 视频生成/文生视频/Ref2VA剧本直出六段式自动生成校验9图参考成片｜H3原生音画同步文生图生视频_2088323034326331393.json, 视频生成/文生视频/h3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版MiniMax_2086205446850965505.json, 视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版_2085188692620177410.json, 视频生成/文生视频/满血无损全家桶文生单图多图生视频｜MiniMax H3视频生成工作流_2088218544206077953.json, 视频生成/文生视频/满血无损加速1.0｜MiniMax H3高清工作流 文生图生视频全能生成_2089417024777834497.json, 视频生成/文生视频/满血无损高清加速版｜MiniMax H3文生图生视频工作流_2088221162772975617.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/4步8步加速稳定MAX｜MiniMaxH3多合一自用版_2092748173281423361.json、视频生成/文生视频/8步加速电影质感 Minimax H3 文生视频LoRA强化出片_2094165667820957697.json、视频生成/文生视频/9图3视频3音频全能多参音视频生成开源加速版｜海螺H3文生图生视频工作流_2088148034331963394.json、视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085422971736383489.json、视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085791756154654721.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
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
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 11/13 个有
- `VHS_VideoCombine` —— 10/13 个有
- `CreateVideo` —— 8/13 个有
- `SaveVideo` —— 8/13 个有
- `EasyCache` —— 7/13 个有
- `Fast Groups Bypasser (rgthree)` —— 7/13 个有
- `孤海注释` —— 7/13 个有
- `LoadAudio` —— 6/13 个有
- `VHS_LoadVideo` —— 6/13 个有
- `ModelPatchTorchSettings` —— 5/13 个有
- `PainterVRAM` —— 3/13 个有
- `UniBlockSwap` —— 3/13 个有
- `MiniMaxH3BlockCacheT8` —— 2/13 个有
- `Int` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `LazySwitchKJ` —— 1/13 个有
- `MiniMaxH3ImageToVideo` —— 1/13 个有
- `MiniMaxH3SigmaShift` —— 1/13 个有
- `PrimitiveBoolean` —— 1/13 个有
- `RHLLMChatNode` —— 1/13 个有
- `SolAttnPatch` —— 1/13 个有
- `easy anythingIndexSwitch` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足

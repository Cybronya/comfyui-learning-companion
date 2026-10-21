---
name: text_to_image_video_lora_sampler_45
type: Text To Image
frequency: 14
level: strong
coverage: 0.708286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多图参考生视频｜MiniMax R2V 768分辨率8步极速出片_2103022962520707074.json, 视频生成/图生视频/打斗单采图生视频｜AITUDOU-MiniMax H3生成_2095847355185717249.json, 视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3剧情向图生视频_2093777220228702209.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2090555558922383362.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2095937261144731649.json, 视频生成/图生视频/文戏多图参考｜MINIMAX-H3图生视频生成_2094025328523042818.json, 视频生成/文生视频/15秒直出高清分辨率Mini Max H3漫剧工作流文生视频图生视频_2088391498671935489.json, 视频生成/文生视频/GSMiniMaxH3多参二次采样放大工作流ENGENG高尚ENG_2087137351121326082.json, 视频生成/文生视频/MiniMax-H3全能参考｜文生视频图生视频多模态_2089708328279695361.json, 视频生成/文生视频/全能参考工作流｜MiniMax-H3文生图生视频生成_2093477174438354945.json, 视频生成/文生视频/全能参考工作流｜MiniMax-H3文生图生视频直出_2090658700645191681.json, 视频生成/文生视频/全能参考生视频｜MiniMax H3图生文生二合一_2090839391815159809.json, 视频生成/文生视频/全能参考｜MiniMax-H3文生视频图生视频多模态生成_2089429895570083841.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_45

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/多图参考生视频｜MiniMax R2V 768分辨率8步极速出片_2103022962520707074.json、视频生成/图生视频/打斗单采图生视频｜AITUDOU-MiniMax H3生成_2095847355185717249.json、视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json、视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3剧情向图生视频_2093777220228702209.json、视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2090555558922383362.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：71%

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
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
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
- `LoadAudio` —— 13/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/14 个有
- `VAEDecodeAudio` —— 13/14 个有
- `PrimitiveFloat` —— 12/14 个有
- `PrimitiveStringMultiline` —— 12/14 个有
- `H3SigmaRefiner` —— 11/14 个有
- `ExtendIntermediateSigmas` —— 10/14 个有
- `INTConstant` —— 10/14 个有
- `Fast Groups Bypasser (rgthree)` —— 9/14 个有
- `ImageResizeKJv2` —— 9/14 个有
- `VAEEncode` —— 9/14 个有
- `VAEEncodeAudio` —— 9/14 个有
- `GetNode` —— 8/14 个有
- `PT_H3ConcatAVLatent` —— 8/14 个有
- `SetNode` —— 8/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `VHS_LoadVideo` —— 7/14 个有
- `ModelAttentionBackend` —— 6/14 个有
- `Seed (rgthree)` —— 6/14 个有
- `Any Switch (rgthree)` —— 5/14 个有
- `LTXVConcatAVLatent` —— 5/14 个有
- `LoraLoaderBypassModelOnly` —— 5/14 个有
- `MiniMaxH3ImageToVideo` —— 5/14 个有
- `ConditioningZeroOut` —— 4/14 个有
- `LTXVSeparateAVLatent` —— 4/14 个有
- `SplitSigmas` —— 4/14 个有
- `MiniMaxH3AVDecodeT8` —— 3/14 个有
- `MinimaxH3LatentUpscalerNode3D` —— 3/14 个有
- `ModelPreviewOverrideKJ` —— 3/14 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/14 个有
- `RunningHub Deepcleaner` —— 3/14 个有
- `SolAttnMiniMax` —— 3/14 个有
- `easy cleanGpuUsed` —— 3/14 个有
- `DisableNoise` —— 2/14 个有
- `H3LatentUpscaleByJingchen573` —— 2/14 个有
- `MiniMaxH3SigmaShift` —— 2/14 个有
- `Text` —— 2/14 个有
- `CM_IntToFloat` —— 1/14 个有
- `Float` —— 1/14 个有
- `Int` —— 1/14 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `SigmasGraph` —— 1/14 个有
- `TrimAudioDuration` —— 1/14 个有
- `easy clearCacheAll` —— 1/14 个有

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
| Steps较低可能导致细节不足 | 18/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（18/14 个样本）：Steps较低可能导致细节不足

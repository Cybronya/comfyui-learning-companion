---
name: text_to_image_video_lora_sampler_109
type: Text To Image
frequency: 8
level: strong
coverage: 0.741625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Minimax人物替换｜动作迁移视频处理生成_2094865846144421890.json, 图片生成/图生图/人物替换处理｜Minimax动作迁移视频一键生成_2095056732870496257.json, 平台全量/视频人物替换参考生视频动作迁移｜minimax h3模特产品展示视频生视频_2087202382835965954.json, 数字人/数字人/MinimaxH3 角色替换｜视频换脸动作迁移数字人一键搞定_2096845137870671874.json, 数字人/数字人/MinimaxH3角色替换工作流｜数字人换脸动作迁移生成_2096647400864706561.json, 视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json, 视频生成/图生视频/多图参考生视频｜MiniMax R2V 768分辨率8步极速出片_2103022962520707074.json, 视频生成/图生视频/数字人对口型生成｜H3视频生视频图生视频直出_2092730251368558593.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_109

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Minimax人物替换｜动作迁移视频处理生成_2094865846144421890.json、图片生成/图生图/人物替换处理｜Minimax动作迁移视频一键生成_2095056732870496257.json、平台全量/视频人物替换参考生视频动作迁移｜minimax h3模特产品展示视频生视频_2087202382835965954.json、数字人/数字人/MinimaxH3 角色替换｜视频换脸动作迁移数字人一键搞定_2096845137870671874.json、数字人/数字人/MinimaxH3角色替换工作流｜数字人换脸动作迁移生成_2096647400864706561.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `MiniMaxH3SigmaShift` —— 7/8 个有
- `ModelAttentionBackend` —— 7/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `VHS_VideoInfo` —— 5/8 个有
- `ComfyMathExpression` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `ResolutionSelector` —— 4/8 个有
- `VAEDecodeAudio` —— 4/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `Int` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 2/8 个有
- `ShowAnything|Mie` —— 2/8 个有
- `SoundFlow_GetLength` —— 2/8 个有
- `TrimAudioDuration` —— 2/8 个有
- `VideoCombineV2` —— 2/8 个有
- `easy int` —— 2/8 个有
- `CM_IntToFloat` —— 1/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

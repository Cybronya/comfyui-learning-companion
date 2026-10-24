---
name: text_to_image_video_lora_sampler_113
type: Text To Image
frequency: 6
level: strong
coverage: 0.682667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json, 视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json, 视频生成/图生视频/MiniMax H3 FastVideo极速多参 视频生成加速方案_2109013584503201793.json, 视频生成/图生视频/MiniMax H3 Ref2VA超级提速音频驱动数字人MV-不降质转场运镜图生视频_2087390946962001921.json, 视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json, 视频生成/图生视频/数字人对口型生成｜H3视频生视频图生视频直出_2092730251368558593.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json、视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json、视频生成/图生视频/MiniMax H3 FastVideo极速多参 视频生成加速方案_2109013584503201793.json、视频生成/图生视频/MiniMax H3 Ref2VA超级提速音频驱动数字人MV-不降质转场运镜图生视频_2087390946962001921.json、视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadAudio` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `SoundFlow_GetLength` —— 4/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `PreviewAudio` —— 3/6 个有
- `TrimAudioDuration` —— 3/6 个有
- `Float` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `ModelPreviewOverrideKJ` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `ShowAnything|Mie` —— 2/6 个有
- `VAEDecodeAudio` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `BlockSparseAttention` —— 1/6 个有
- `MelBandRoFormerModelLoader` —— 1/6 个有
- `MelBandRoFormerSampler` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `SigmasGraph` —— 1/6 个有
- `ZNGB_AudioCrop` —— 1/6 个有
- `easy float` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

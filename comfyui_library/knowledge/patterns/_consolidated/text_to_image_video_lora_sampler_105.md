---
name: text_to_image_video_lora_sampler_105
type: Text To Image
frequency: 8
level: strong
coverage: 0.87025
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 Ref2VA超级提速音频驱动数字人MV-不降质转场运镜图生视频_2087390946962001921.json, 视频生成/图生视频/MiniMax H3单人音频驱动数字人 最高15秒视频生成_2099176616411881474.json, 视频生成/图生视频/MiniMax H3双人音频驱动数字人视频生成处理工具_2100993902961577985.json, 视频生成/图生视频/MiniMax H3海螺Ref图片视频音频多模态原生视频生成工具_2101392045809164289.json, 视频生成/图生视频/MiniMax H3海螺Ref多模态原生视频生成20步｜动作迁移图生视频视频生视频_2089703443115106306.json, 视频生成/图生视频/MiniMax-H3音频数字人来了｜单人出镜最高15秒，口播带货省事_2099401548009918466.json, 视频生成/图生视频/多模态原生视频生成｜MiniMax H3海螺Ref 图片视频音频20步直出_2089426965655805953.json, 视频生成/文生视频/MiniMax H3双时钟采样Turbo LORA双采集多模态文生视频_2088198784831545345.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_105

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 Ref2VA超级提速音频驱动数字人MV-不降质转场运镜图生视频_2087390946962001921.json、视频生成/图生视频/MiniMax H3单人音频驱动数字人 最高15秒视频生成_2099176616411881474.json、视频生成/图生视频/MiniMax H3双人音频驱动数字人视频生成处理工具_2100993902961577985.json、视频生成/图生视频/MiniMax H3海螺Ref图片视频音频多模态原生视频生成工具_2101392045809164289.json、视频生成/图生视频/MiniMax H3海螺Ref多模态原生视频生成20步｜动作迁移图生视频视频生视频_2089703443115106306.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `LayerUtility: PurgeVRAM V2` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `MathExpression|pysssss` —— 6/8 个有
- `AudioCrop` —— 5/8 个有
- `ModelAttentionBackend` —— 5/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `LoadVideoUI` —— 4/8 个有
- `MiniMaxH3AVDecodeT8` —— 4/8 个有
- `SoundFlow_GetLength` —— 4/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `SaveImage` —— 3/8 个有
- `AudioConcat` —— 2/8 个有
- `ComfyMathExpression` —— 2/8 个有
- `MiniMaxChunkFeedForward` —— 2/8 个有
- `MiniMaxLowVRAMAttention` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 2/8 个有
- `PixaromaLabel` —— 2/8 个有
- `PreviewAudio` —— 2/8 个有
- `TrimAudioDuration` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `EmptyAudio` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `Float` —— 1/8 个有
- `MelBandRoFormerModelLoader` —— 1/8 个有
- `MelBandRoFormerSampler` —— 1/8 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/8 个有
- `PT_H3ConcatAVLatent` —— 1/8 个有
- `VAEEncode` —— 1/8 个有
- `VAEEncodeAudio` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

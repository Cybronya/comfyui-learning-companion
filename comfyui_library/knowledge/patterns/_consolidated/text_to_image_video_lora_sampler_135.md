---
name: text_to_image_video_lora_sampler_135
type: Text To Image
frequency: 5
level: strong
coverage: 0.8474
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多参分镜硬控流，空间人物一致性分镜制作短剧漫剧图生视频_2103531675861995521.json, 视频生成/图生视频/MiniMax H3多参短剧批量专用90角色场景道具视频处理工具_2101729336322781185.json, 视频生成/图生视频/MiniMax H3海螺Ref图片视频音频多模态原生视频生成工具_2101392045809164289.json, 视频生成/图生视频/MiniMax H3海螺Ref多模态原生视频生成20步｜动作迁移图生视频视频生视频_2089703443115106306.json, 视频生成/图生视频/多模态原生视频生成｜MiniMax H3海螺Ref 图片视频音频20步直出_2089426965655805953.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多参分镜硬控流，空间人物一致性分镜制作短剧漫剧图生视频_2103531675861995521.json、视频生成/图生视频/MiniMax H3多参短剧批量专用90角色场景道具视频处理工具_2101729336322781185.json、视频生成/图生视频/MiniMax H3海螺Ref图片视频音频多模态原生视频生成工具_2101392045809164289.json、视频生成/图生视频/MiniMax H3海螺Ref多模态原生视频生成20步｜动作迁移图生视频视频生视频_2089703443115106306.json、视频生成/图生视频/多模态原生视频生成｜MiniMax H3海螺Ref 图片视频音频20步直出_2089426965655805953.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `PrimitiveFloat`
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
- `LoadAudio` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `AudioCrop` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `LoadVideoUI` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `MiniMaxChunkFeedForward` —— 3/5 个有
- `MiniMaxH3AVDecodeT8` —— 3/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/5 个有
- `MiniMaxH3ReferenceToVideo` —— 3/5 个有
- `MiniMaxLowVRAMAttention` —— 3/5 个有
- `ModelPreviewOverrideKJ` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `ComfyMathExpression` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `VAEDecodeAudio` —— 2/5 个有
- `ki_MiniMaxH3ReferenceToVideo` —— 2/5 个有
- `ExtendIntermediateSigmas` —— 1/5 个有
- `ManualSigmas` —— 1/5 个有
- `MiniMaxH3TurboSampler` —— 1/5 个有
- `PixaromaLabel` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ki_宫格拼图高阶版` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_141
type: Text To Image
frequency: 12
level: strong
coverage: 0.7305
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2103271632474300417.json, 视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2105721669728956418.json, 视频生成/图生视频/H3打斗工作流，图生视频高动态动作场景创作工具_2106489548766269442.json, 视频生成/图生视频/H3打斗工作流｜图生视频 打造拳拳到肉的打斗名场面_2105501306726207490.json, 视频生成/图生视频/H3打斗特效视频生成 武打动作画面直出方案_2110369061031989249.json, 视频生成/图生视频/MiniMax H3全能参考正式版 真实电影质感视频处理工具_2113410728010014721.json, 视频生成/图生视频/MiniMax H3全能参考真实电影质感V2，图生视频胶片感运镜直出_2114442449908228097.json, 视频生成/图生视频/MiniMax H3全能参考｜真实电影质感V2文生视频图生视频三合一_2114262759729881089.json, 视频生成/图生视频/MiniMax H3单采工作流，文生视频图生视频轻量简洁快速上手_2114479769403346945.json, 视频生成/图生视频/高质量打斗视频专用双采无加速 文生图生视频处理工具_2112970802692972545.json, 视频生成/文生视频/MiniMax H3单采V2工作流，文生视频视频生视频图生视频方案_2103619711580856322.json, 视频生成/文生视频/MiniMax H3双采工作流，文生视频视频生视频图生视频方案_2103963966656573441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2103271632474300417.json、视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2105721669728956418.json、视频生成/图生视频/H3打斗工作流，图生视频高动态动作场景创作工具_2106489548766269442.json、视频生成/图生视频/H3打斗工作流｜图生视频 打造拳拳到肉的打斗名场面_2105501306726207490.json、视频生成/图生视频/H3打斗特效视频生成 武打动作画面直出方案_2110369061031989249.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/12 个有
- `SaveImage` —— 10/12 个有
- `SetNode` —— 10/12 个有
- `CreateVideo` —— 9/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/12 个有
- `MiniMaxH3SigmaShift` —— 9/12 个有
- `ModelAttentionBackend` —— 9/12 个有
- `SaveVideo` —— 9/12 个有
- `BasicScheduler` —— 8/12 个有
- `BlockSparseAttention` —— 8/12 个有
- `ExtendIntermediateSigmas` —— 8/12 个有
- `LoadAudio` —— 8/12 个有
- `ModelPreviewOverrideKJ` —— 8/12 个有
- `DisableNoise` —— 6/12 个有
- `SplitSigmasDenoise` —— 6/12 个有
- `easy cleanGpuUsed` —— 6/12 个有
- `ImageScaleToTotalPixels` —— 5/12 个有
- `ManualSigmas` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `INTConstant` —— 4/12 个有
- `ResizeShortestToNode` —— 4/12 个有
- `SolAttnMiniMax` —— 4/12 个有
- `GetVideoComponents` —— 3/12 个有
- `LoadVideo` —— 3/12 个有
- `PreviewAudio` —— 3/12 个有
- `ResizeImageMaskNode` —— 3/12 个有
- `Seed (rgthree)` —— 3/12 个有
- `TrimAudioDuration` —— 3/12 个有
- `VHS_VideoCombine` —— 3/12 个有
- `Fast Groups Muter (rgthree)` —— 2/12 个有
- `Text Concatenate` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `ComfySwitchNode` —— 1/12 个有
- `EmptyImage` —— 1/12 个有
- `LTXVConcatAVLatent` —— 1/12 个有
- `LTXVSeparateAVLatent` —— 1/12 个有
- `MinimaxH3LatentUpscaler3D` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `SplitSigmas` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足

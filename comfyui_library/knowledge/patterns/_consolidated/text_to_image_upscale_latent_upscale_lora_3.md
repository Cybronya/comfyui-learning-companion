---
name: text_to_image_upscale_latent_upscale_lora_3
type: Text To Image
frequency: 9
level: strong
coverage: 0.766222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/五分钟1080p高清 MiniMax H3 可视化全模态输出_2094229426480439297.json, 视频生成/图生视频/五分钟1080p高清生成｜MiniMax H3全模态可视化视频_2094576638112657410.json, 视频生成/图生视频/五分钟出1080p高清｜MiniMax H3全模态可视化视频_2094351180242710529.json, 视频生成/图生视频/全能参考二采放大｜MiniMax H3视频图生视频_2092362550968147969.json, 视频生成/图生视频/全能参考二采放大｜MiniMax H3视频生视频图生视频_2092619898299179010.json, 视频生成/图生视频/全能多模态二采放大｜H3加速sigma强化工作流_2092350860545314817.json, 视频生成/图生视频/单模型二采无编解码放大｜MiniMax-H3 ref2va超分_2093849774721167362.json, 视频生成/图生视频/双模双采小脸不崩｜Minimax H3高动态不崩脸视频_2093486007596437506.json, 视频生成/图生视频/双模双采资源面板短剧助手 MiniMax H3 全能参考生成视频_2094255084355022849.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/五分钟1080p高清 MiniMax H3 可视化全模态输出_2094229426480439297.json、视频生成/图生视频/五分钟1080p高清生成｜MiniMax H3全模态可视化视频_2094576638112657410.json、视频生成/图生视频/五分钟出1080p高清｜MiniMax H3全模态可视化视频_2094351180242710529.json、视频生成/图生视频/全能参考二采放大｜MiniMax H3视频图生视频_2092362550968147969.json、视频生成/图生视频/全能参考二采放大｜MiniMax H3视频生视频图生视频_2092619898299179010.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `ComfyMathExpression` —— 6/9 个有
- `H3SigmaRefiner` —— 6/9 个有
- `MiniMaxH3ReferenceToVideo` —— 6/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `GetNode` —— 5/9 个有
- `LoadImage` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `CreateVideo` —— 4/9 个有
- `SaveVideo` —— 4/9 个有
- `CR Prompt Text` —— 3/9 个有
- `ExtendIntermediateSigmas` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `MiniMaxH3Unified` —— 3/9 个有
- `MiniMaxLowVRAMAttention` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `DF_Integer` —— 1/9 个有
- `GetVideoComponents` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `LoadVideo` —— 1/9 个有
- `ManualSigmas` —— 1/9 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/9 个有
- `MiniMaxH3ReferenceSplitter` —— 1/9 个有
- `PixaromaDuration` —— 1/9 个有
- `PixaromaSizes` —— 1/9 个有
- `SolAttnMiniMax` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足

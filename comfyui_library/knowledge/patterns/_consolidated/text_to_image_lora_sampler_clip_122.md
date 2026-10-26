---
name: text_to_image_lora_sampler_clip_122
type: Text To Image
frequency: 13
level: strong
coverage: 0.787615
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json, 视频生成/图生视频/Minimax H3图生视频Lightx2v正式版生成工作流_2088211425947897858.json, 视频生成/图生视频/Minimax H3多图参考视频流｜全节点中文注释齐全，新手也能看懂_2099470227150032898.json, 视频生成/图生视频/Minimax H3电商带货参考生视频 8步加速版服装展示_2110352251444355074.json, 视频生成/图生视频/MinimaxH3高动态Singularity新分段采样进阶工作流 视频生成优化_2105351940963131393.json, 视频生成/图生视频/Ref2VA多参生视频进阶版 MiniMax H3服装展示图生视频_2104344870545608706.json, 视频生成/图生视频/h3双采样高清流｜图生视频超清画质一键生成_2092887311095783425.json, 视频生成/图生视频/minimax h3二采1080p工作流｜高清图生视频画质增强_2097485061024215042.json, 视频生成/图生视频/双采样高清画质流｜H3图生视频画质增强直出_2092695582556114946.json, 视频生成/图生视频/角色替换生成｜H3图生视频一键处理工作流_2095096657456226306.json, 视频生成/文生视频/Singularity模型双采放大 视频图片超分辨率增强_2098863700953362434.json, 视频生成/文生视频/台词优化正反打镜头Singularity双采放大｜文生视频视频生视频对话戏更带感_2100457358244798465.json, 视频生成/文生视频/台词优化正反打镜头Singularity模型双采放大处理_2100644227557445634.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_122

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json、视频生成/图生视频/Minimax H3图生视频Lightx2v正式版生成工作流_2088211425947897858.json、视频生成/图生视频/Minimax H3多图参考视频流｜全节点中文注释齐全，新手也能看懂_2099470227150032898.json、视频生成/图生视频/Minimax H3电商带货参考生视频 8步加速版服装展示_2110352251444355074.json、视频生成/图生视频/MinimaxH3高动态Singularity新分段采样进阶工作流 视频生成优化_2105351940963131393.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 12/13 个有
- `ComfyMathExpression` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `PrimitiveFloat` —— 12/13 个有
- `ResolutionSelector` —— 12/13 个有
- `LTXVConcatAVLatent` —— 10/13 个有
- `LTXVSeparateAVLatent` —— 10/13 个有
- `MinimaxH3LatentUpscaler3D` —— 10/13 个有
- `SaveImage` —— 10/13 个有
- `SplitSigmas` —— 10/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/13 个有
- `PrimitiveStringMultiline` —— 9/13 个有
- `MiniMaxLowVRAMAttention` —— 8/13 个有
- `CreateVideo` —— 7/13 个有
- `ModelAttentionBackend` —— 7/13 个有
- `SaveVideo` —— 7/13 个有
- `GetNode` —— 6/13 个有
- `LoadAudio` —— 6/13 个有
- `MiniMaxH3SigmaShift` —— 6/13 个有
- `SetNode` —— 6/13 个有
- `VHS_VideoCombine` —— 6/13 个有
- `VHS_LoadVideo` —— 5/13 个有
- `DisableNoise` —— 4/13 个有
- `H3SigmaRefiner` —— 4/13 个有
- `PathchSageAttentionKJ` —— 4/13 个有
- `easy float` —— 4/13 个有
- `BlockSparseAttention` —— 3/13 个有
- `ExtendIntermediateSigmas` —— 3/13 个有
- `FlashVSRNode` —— 3/13 个有
- `Lora Loader Stack (rgthree)` —— 3/13 个有
- `MiniMaxChunkFeedForward` —— 3/13 个有
- `Sleep` —— 3/13 个有
- `CFGGuider` —— 1/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `EasyCache` —— 1/13 个有
- `Int` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有
- `StringConcatenate` —— 1/13 个有
- `Text` —— 1/13 个有
- `VRAM_Debug` —— 1/13 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

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
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_182
type: Text To Image
frequency: 10
level: strong
coverage: 0.9007
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3角色替换简易版工作流，视频生视频换人换脸操作简单出片快_2117103311932444674.json, 视频生成/图生视频/H3高清快速出视频工作流，图生视频高效创作工具_2106126711132876801.json, 视频生成/图生视频/Kitchen Attention图生视频 600步EMA模型工具_2114139959656538113.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采单采，参考生视频提速版_2110810539428499457.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采参考生视频｜武戏动态强_2108458056047742978.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采武戏动态强参考生视频方案_2108644932058697730.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采｜武戏动态强的参考生视频_2111123791060496385.json, 视频生成/图生视频/MiniMax H3 SelfLift双采对比普通双采图生视频处理工具_2101770093456871425.json, 视频生成/文生视频/MiniMax H3 SelfLift加速双采文戏武戏参考生视频处理工具_2101730945995993089.json, 视频生成/文生视频/MiniMax H3-SelfLift加速双采｜文戏不油武戏动态强_2101550350955270145.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/H3角色替换简易版工作流，视频生视频换人换脸操作简单出片快_2117103311932444674.json、视频生成/图生视频/H3高清快速出视频工作流，图生视频高效创作工具_2106126711132876801.json、视频生成/图生视频/Kitchen Attention图生视频 600步EMA模型工具_2114139959656538113.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采单采，参考生视频提速版_2110810539428499457.json、视频生成/图生视频/MiniMax H3 SelfLift加速双采参考生视频｜武戏动态强_2108458056047742978.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
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
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `ModelAttentionBackend` —— 9/10 个有
- `ModelPreviewOverrideKJ` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `MiniMaxChunkFeedForward` —— 8/10 个有
- `MiniMaxLowVRAMAttention` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `BasicGuider` —— 7/10 个有
- `ConditioningZeroOut` —— 7/10 个有
- `ExtendIntermediateSigmas` —— 7/10 个有
- `RandomNoise` —— 7/10 个有
- `SamplerCustomAdvanced` —— 7/10 个有
- `SaveImage` —— 7/10 个有
- `SelfLiftH3Sampler` —— 7/10 个有
- `LoraLoaderBypassModelOnly` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `SolAttnMiniMax` —— 5/10 个有
- `ManualSigmas` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `VHS_VideoCombine` —— 3/10 个有
- `BlockSparseAttention` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `LoadAudio` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `Any Switch (rgthree)` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `H3SigmaRefiner` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `LTXVConcatAVLatent` —— 1/10 个有
- `LTXVSeparateAVLatent` —— 1/10 个有
- `MiniMaxH3TurboLoRA` —— 1/10 个有
- `MinimaxH3LatentUpscaler3D` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `SplitSigmas` —— 1/10 个有
- `TextGenerate` —— 1/10 个有
- `VHS_LoadVideoFFmpeg` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_video_lora_sampler_80
type: Text To Image
frequency: 11
level: strong
coverage: 0.712818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3官方工作流文生视频｜基础视频生成_2090428143353024513.json, 视频生成/文生视频/MiniMax H3手机取物换装文生视频工作流，文生视频图生视频处理方案_2107568456165056514.json, 视频生成/文生视频/MiniMax H3数字人视频带货 多图生视频口播工具_2098845262381932545.json, 视频生成/文生视频/MiniMax H3文生视频电商带货｜手机取物换装创意视频_2108095483951538177.json, 视频生成/文生视频/MiniMax H3武戏全能视频V3｜打斗高质量生成_2095598787678007297.json, 视频生成/文生视频/MiniMax H3活人感女友二采工作流 一键直出自然感视频_2098737048969633793.json, 视频生成/文生视频/MiniMaxH3数字人带货视频｜多图生视频批量产出带货素材_2099148701758484482.json, 视频生成/文生视频/Minimax H3全能导演台｜短剧分镜丝滑衔接生成_2094862928741756929.json, 视频生成/文生视频/Singularity模型双采放大 视频图片超分辨率增强_2098863700953362434.json, 视频生成/文生视频/台词优化正反打镜头Singularity双采放大｜文生视频视频生视频对话戏更带感_2100457358244798465.json, 视频生成/文生视频/台词优化正反打镜头Singularity模型双采放大处理_2100644227557445634.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3官方工作流文生视频｜基础视频生成_2090428143353024513.json、视频生成/文生视频/MiniMax H3手机取物换装文生视频工作流，文生视频图生视频处理方案_2107568456165056514.json、视频生成/文生视频/MiniMax H3数字人视频带货 多图生视频口播工具_2098845262381932545.json、视频生成/文生视频/MiniMax H3文生视频电商带货｜手机取物换装创意视频_2108095483951538177.json、视频生成/文生视频/MiniMax H3武戏全能视频V3｜打斗高质量生成_2095598787678007297.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
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
- `GetNode` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `VAEDecodeAudio` —— 10/11 个有
- `LTXVConcatAVLatent` —— 8/11 个有
- `LTXVSeparateAVLatent` —— 8/11 个有
- `LoadImage` —— 8/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/11 个有
- `MiniMaxH3ReferenceToVideo` —— 8/11 个有
- `MinimaxH3LatentUpscaler3D` —— 8/11 个有
- `ModelAttentionBackend` —— 7/11 个有
- `LoadAudio` —— 6/11 个有
- `VHS_LoadVideo` —— 6/11 个有
- `SaveImage` —— 5/11 个有
- `Text` —— 5/11 个有
- `easy float` —— 5/11 个有
- `ExtendIntermediateSigmas` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `SplitSigmas` —— 4/11 个有
- `BlockSparseAttention` —— 3/11 个有
- `DisableNoise` —— 3/11 个有
- `Lora Loader Stack (rgthree)` —— 3/11 个有
- `ManualSigmas` —— 3/11 个有
- `MiniMaxChunkFeedForward` —— 3/11 个有
- `MiniMaxH3ImageToVideo` —— 3/11 个有
- `MiniMaxLowVRAMAttention` —— 3/11 个有
- `忽略多组孤海` —— 2/11 个有
- `CS-MultiImageLoader` —— 1/11 个有
- `DiffusionModelLoaderKJ` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `H3SigmaRefiner` —— 1/11 个有
- `MiniMaxH3AVDecodeT8` —— 1/11 个有
- `RunningHub Deepcleaner` —— 1/11 个有
- `UniBlockSwap` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足

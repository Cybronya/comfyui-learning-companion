---
name: text_to_image_lora_sampler_clip_70
type: Text To Image
frequency: 13
level: strong
coverage: 0.581769
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ResolutionSelector, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/AITUDOU-H3+SelfLift组合｜影视级情绪表达出片_2106620640190095361.json, 视频生成/文生视频/H3电影级LORA双采去油PRO版 巅峰画质视频生成_2098288538583392257.json, 视频生成/文生视频/H3虚幻引擎赛璐璃风格漫画流双采FL2高清PRO处理_2100642569272254465.json, 视频生成/文生视频/H3言出法随至尊工作流｜文生图生视频全能生成_2097497018427072514.json, 视频生成/文生视频/Jason二采H3多参考生视频优化版V2｜三模式视频生成_2108420583481499650.json, 视频生成/文生视频/Jason二采H3多参考生视频优化版｜不油腻二采高清放大更耐看_2101906733156364290.json, 视频生成/文生视频/MINIMAX H3原本fl2va分布高低解码二采 视频生成优化方案_2104719643922493441.json, 视频生成/文生视频/MINIMAX H3原本fl2va分布高低解码二采 视频生成优化方案_2105066230074920961.json, 视频生成/文生视频/MINIMAX-H3原版fl2va高低解码二采｜视频画质精修方案_2104483718219001858.json, 视频生成/文生视频/MINImax-H3单人音乐MV制作｜文生视频音乐生成_2094927265846091778.json, 视频生成/文生视频/minimaxH3混合模型sigma强化｜潜空间放大高清直出_2094545098968227842.json, 视频生成/文生视频/sigma强化不油腻混合模型｜minimaxH3潜空间放大高清直出_2094790731905986562.json, 视频生成/文生视频/单人音乐MV制作｜MINImax-H3三模视频生成工作流_2095106732040220673.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/AITUDOU-H3+SelfLift组合｜影视级情绪表达出片_2106620640190095361.json、视频生成/文生视频/H3电影级LORA双采去油PRO版 巅峰画质视频生成_2098288538583392257.json、视频生成/文生视频/H3虚幻引擎赛璐璃风格漫画流双采FL2高清PRO处理_2100642569272254465.json、视频生成/文生视频/H3言出法随至尊工作流｜文生图生视频全能生成_2097497018427072514.json、视频生成/文生视频/Jason二采H3多参考生视频优化版V2｜三模式视频生成_2108420583481499650.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 12/13 个有
- `LTXVConcatAVLatent` —— 12/13 个有
- `LTXVSeparateAVLatent` —— 12/13 个有
- `MinimaxH3LatentUpscaler3D` —— 12/13 个有
- `RandomNoise` —— 12/13 个有
- `SamplerCustomAdvanced` —— 12/13 个有
- `PrimitiveFloat` —— 11/13 个有
- `VAEDecodeAudio` —— 11/13 个有
- `LoadAudio` —— 10/13 个有
- `SplitSigmas` —— 9/13 个有
- `VHS_VideoCombine` —— 9/13 个有
- `H3SigmaRefiner` —— 8/13 个有
- `ModelAttentionBackend` —— 8/13 个有
- `easy float` —— 8/13 个有
- `INTConstant` —— 7/13 个有
- `Fast Groups Bypasser (rgthree)` —— 6/13 个有
- `Text` —— 6/13 个有
- `SaveImage` —— 5/13 个有
- `SolAttnMiniMax` —— 5/13 个有
- `CreateVideo` —— 4/13 个有
- `ModelPreviewOverrideKJ` —— 4/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `ResizeShortestToNode` —— 4/13 个有
- `SaveVideo` —— 4/13 个有
- `VHS_LoadVideo` —— 4/13 个有
- `CR Prompt Text` —— 3/13 个有
- `ExtendIntermediateSigmas` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `PlaySound|pysssss` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `Float` —— 2/13 个有
- `MuyeTextEditOutput` —— 2/13 个有
- `PreviewAudio` —— 2/13 个有
- `RHLLMChatNode` —— 2/13 个有
- `SoundFlow_GetLength` —— 2/13 个有
- `TrimAudioDuration` —— 2/13 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/13 个有
- `easy showAnything` —— 2/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `SelfLiftH3Sampler` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足

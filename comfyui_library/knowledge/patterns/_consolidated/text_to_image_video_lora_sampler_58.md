---
name: text_to_image_video_lora_sampler_58
type: Text To Image
frequency: 14
level: strong
coverage: 0.596286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json, 视频生成/图生视频/MiniMax H3官方工作流首尾帧生成视频｜图生视频_2090425354019229697.json, 视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json, 视频生成/图生视频/MiniMax H3短剧公司版本 图生视频高效出片处理工具_2113715561371885570.json, 视频生成/图生视频/lightx2v 8step加速｜MiniMax H3图生视频快速出片_2088748531585736705.json, 视频生成/图生视频/全能参考数字人｜AITUDOU MiniMax H3 人物音频一致性_2089296635812737025.json, 视频生成/图生视频/打斗单采图生视频｜AITUDOU-MiniMax H3生成_2095847355185717249.json, 视频生成/图生视频/最强打斗武戏双采工作流｜MINIMAX-H3自动提示词图生视频_2096734559260995586.json, 视频生成/图生视频/最强文戏低配版｜MINIMAX-H3开源角色一致性生成_2095074002149662722.json, 视频生成/文生视频/MINIMAX H3原本fl2va分布高低解码二采 视频生成优化方案_2104719643922493441.json, 视频生成/文生视频/MINIMAX H3原本fl2va分布高低解码二采 视频生成优化方案_2105066230074920961.json, 视频生成/文生视频/MINIMAX-H3原版fl2va高低解码二采｜视频画质精修方案_2104483718219001858.json, 视频生成/文生视频/MiniMax H3打斗版二采视频生视频处理生成工具_2101749624259309569.json, 视频生成/文生视频/武戏专用参考｜MiniMax H3提示词手输自动可选_2096598519665750017.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_58

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json、视频生成/图生视频/MiniMax H3官方工作流首尾帧生成视频｜图生视频_2090425354019229697.json、视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json、视频生成/图生视频/MiniMax H3短剧公司版本 图生视频高效出片处理工具_2113715561371885570.json、视频生成/图生视频/lightx2v 8step加速｜MiniMax H3图生视频快速出片_2088748531585736705.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 13/14 个有
- `LoadAudio` —— 11/14 个有
- `H3SigmaRefiner` —— 10/14 个有
- `ExtendIntermediateSigmas` —— 9/14 个有
- `ModelAttentionBackend` —— 9/14 个有
- `CR Prompt Text` —— 8/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/14 个有
- `PreviewImage` —— 8/14 个有
- `PrimitiveFloat` —— 8/14 个有
- `Float` —— 6/14 个有
- `INTConstant` —— 6/14 个有
- `LTXVConcatAVLatent` —— 6/14 个有
- `LTXVSeparateAVLatent` —— 6/14 个有
- `MinimaxH3LatentUpscaler3D` —— 6/14 个有
- `Text` —— 6/14 个有
- `SaveImage` —— 5/14 个有
- `Fast Groups Bypasser (rgthree)` —— 4/14 个有
- `RH_LLMAPI_Pro_Node` —— 4/14 个有
- `PlaySound|pysssss` —— 3/14 个有
- `PreviewAny` —— 3/14 个有
- `SigmasGraph` —— 3/14 个有
- `ZNGB_AudioCrop` —— 2/14 个有
- `Any Switch (rgthree)` —— 1/14 个有
- `ConditioningZeroOut` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `MiniMaxH3AVDecodeT8` —— 1/14 个有
- `MuyeTextEditOutput` —— 1/14 个有
- `PreviewAudio` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `RunningHub Deepcleaner` —— 1/14 个有
- `SelfLiftH3Sampler` —— 1/14 个有
- `忽略多组孤海` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（15/14 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_video_lora_sampler_20
type: Text To Image
frequency: 20
level: strong
coverage: 0.60505
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json, 视频生成/图生视频/MiniMax H3官方工作流首尾帧生成视频｜图生视频_2090425354019229697.json, 视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json, 视频生成/图生视频/MiniMax H3打斗双采｜高质量图生视频生成_2095602888709066753.json, 视频生成/图生视频/MiniMax_H3多参考7P3A2V生视频优化版｜图生视频_2100805403243278338.json, 视频生成/图生视频/MiniMax_H3多参考生视频优化版，文生视频视频生视频图生视频方案_2109447215457587202.json, 视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json, 视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json, 视频生成/图生视频/Minimax H3动作迁移2.0进阶｜视频生视频史诗级强化_2103047047137021954.json, 视频生成/图生视频/Minimax H3多参考双采｜最强一致性Singularity出视频_2101538998190698498.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频多比例版_2104776734221627394.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频标准版_2104646935444549633.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采视频生成_2098283807588839426.json, 视频生成/图生视频/Singularity最强一致性多参考双采生视频处理工具_2101743307100610561.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频王牌版_2104560310488223746.json, 视频生成/文生视频/0906 万象AI+Singularity 新模型｜12秒横屏960分辨率_2096858352113512449.json, 视频生成/文生视频/0906 万象AI+Singularity 新模型｜12秒竖屏960分辨率_2096856463141588993.json, 视频生成/文生视频/MINIMAX H3原本fl2va分布高低解码二采 视频生成优化方案_2104719643922493441.json, 视频生成/文生视频/MINIMAX H3原本fl2va分布高低解码二采 视频生成优化方案_2105066230074920961.json, 视频生成/文生视频/MINIMAX-H3原版fl2va高低解码二采｜视频画质精修方案_2104483718219001858.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json、视频生成/图生视频/MiniMax H3官方工作流首尾帧生成视频｜图生视频_2090425354019229697.json、视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json、视频生成/图生视频/MiniMax H3打斗双采｜高质量图生视频生成_2095602888709066753.json、视频生成/图生视频/MiniMax_H3多参考7P3A2V生视频优化版｜图生视频_2100805403243278338.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 20 个 workflow 都包含：
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
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 19/20 个有
- `VAEDecodeAudio` —— 19/20 个有
- `孤海注释` —— 19/20 个有
- `LTXVConcatAVLatent` —— 17/20 个有
- `LTXVSeparateAVLatent` —— 17/20 个有
- `LoadAudio` —— 17/20 个有
- `MinimaxH3LatentUpscaler3D` —— 17/20 个有
- `PrimitiveFloat` —— 17/20 个有
- `Text` —— 16/20 个有
- `SplitSigmas` —— 14/20 个有
- `ModelAttentionBackend` —— 13/20 个有
- `VHS_LoadVideo` —— 13/20 个有
- `easy float` —— 13/20 个有
- `SaveImage` —— 9/20 个有
- `Lora Loader Stack (rgthree)` —— 8/20 个有
- `SolAttnMiniMax` —— 8/20 个有
- `PreviewImage` —— 6/20 个有
- `CR Prompt Text` —— 4/20 个有
- `ExtendIntermediateSigmas` —— 4/20 个有
- `H3SigmaRefiner` —— 4/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/20 个有
- `Fast Groups Bypasser (rgthree)` —— 3/20 个有
- `Float` —— 3/20 个有
- `INTConstant` —— 3/20 个有
- `PlaySound|pysssss` —— 3/20 个有
- `EmptyImage` —— 2/20 个有
- `MiniMaxH3AVDecodeT8` —— 1/20 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/20 个有
- `PreviewAudio` —— 1/20 个有
- `RunningHub Deepcleaner` —— 1/20 个有
- `SigmasGraph` —— 1/20 个有
- `ZNGB_AudioCrop` —— 1/20 个有
- `easy int` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（21/20 个样本）：Steps较低可能导致细节不足

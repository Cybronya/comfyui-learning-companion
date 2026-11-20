---
name: text_to_image_video_lora_sampler_20
type: Text To Image
frequency: 26
level: strong
coverage: 0.640346
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3数字人带货图生视频_2108450739797446658.json, 视频生成/图生视频/MiniMax-H3数字人带货视频｜模特产品展示图生视频_2108417540744638465.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars模特产品展示_2108393078053756930.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars电商好帮手_2111119123915821058.json, 视频生成/图生视频/MiniMaxH3 ref2va加速八步采样-图生视频工作流_2087367770194403330.json, 视频生成/图生视频/MiniMaxH3 ref2va四步加速V4版｜图生视频_2090101812916482049.json, 视频生成/图生视频/MiniMaxH38高动态加速流｜人物场景类特效图生视频_2092030919111692289.json, 视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json, 视频生成/图生视频/Minimax H3动作迁移2.0进阶｜视频生视频史诗级强化_2103047047137021954.json, 视频生成/图生视频/Minimax H3多参考双采｜最强一致性Singularity出视频_2101538998190698498.json, 视频生成/图生视频/MinimaxH3动作迁移+人物替换二合一｜图生视频完美优化版_2110680462313218050.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频多比例版_2104776734221627394.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频标准版_2104646935444549633.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采视频生成_2098283807588839426.json, 视频生成/图生视频/Singularity最强一致性多参考双采生视频处理工具_2101743307100610561.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2089456017561186306.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2091266588484923394.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速直出_2089807243888914434.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3图生视频1.0分辨率极速出片_2093095662807248897.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3支持1.0分辨率图生视频_2093253169697611778.json, 视频生成/图生视频/多参生视频优化版｜MiniMax H3支持9图3音3视频参考_2095857101267628033.json, 视频生成/图生视频/多参考生视频4步加速｜MiniMax H3一采二采双输出_2095968881948061697.json, 视频生成/图生视频/多参考生视频720p高清｜MiniMax H3场景特效生成_2096685620121919489.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频王牌版_2104560310488223746.json, 视频生成/文生视频/0906 万象AI+Singularity 新模型｜12秒横屏960分辨率_2096858352113512449.json, 视频生成/文生视频/0906 万象AI+Singularity 新模型｜12秒竖屏960分辨率_2096856463141588993.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3数字人带货图生视频_2108450739797446658.json、视频生成/图生视频/MiniMax-H3数字人带货视频｜模特产品展示图生视频_2108417540744638465.json、视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars模特产品展示_2108393078053756930.json、视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars电商好帮手_2111119123915821058.json、视频生成/图生视频/MiniMaxH3 ref2va加速八步采样-图生视频工作流_2087367770194403330.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 26 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 25/26 个有
- `ResolutionSelector` —— 25/26 个有
- `孤海注释` —— 25/26 个有
- `LoadAudio` —— 22/26 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 22/26 个有
- `KSamplerSelect` —— 20/26 个有
- `LTXVConcatAVLatent` —— 18/26 个有
- `LTXVSeparateAVLatent` —— 18/26 个有
- `MinimaxH3LatentUpscaler3D` —— 18/26 个有
- `VHS_LoadVideo` —— 15/26 个有
- `SplitSigmas` —— 14/26 个有
- `Text` —— 14/26 个有
- `easy float` —— 13/26 个有
- `Lora Loader Stack (rgthree)` —— 8/26 个有
- `ModelAttentionBackend` —— 8/26 个有
- `SolAttnMiniMax` —— 8/26 个有
- `Text Multiline` —— 8/26 个有
- `ModelPatchTorchSettings` —— 7/26 个有
- `ImageScale` —— 6/26 个有
- `MiniMaxH3TurboLoRA` —— 6/26 个有
- `MiniMaxH3TurboSampler` —— 6/26 个有
- `PrimitiveInt` —— 6/26 个有
- `easy compare` —— 6/26 个有
- `ManualSigmas` —— 4/26 个有
- `SaveImage` —— 4/26 个有
- `Label (rgthree)` —— 2/26 个有
- `忽略多组孤海` —— 2/26 个有
- `Fast Groups Bypasser (rgthree)` —— 1/26 个有
- `FloatConstant` —— 1/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/26 个有
- `PreviewImage` —— 1/26 个有
- `PrimitiveBoolean` —— 1/26 个有
- `easy clearCacheAll` —— 1/26 个有
- `easy int` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 26 | 100% |
| 高度 | 80 | 80 - 80 | 26 | 100% |
| 采样步数 | 4 | 4 - 4 | 26 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 26 | 100% |
| 采样算法 | er_sde | - | 26 | 100% |
| 调度器 | beta | - | 26 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，26 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，26 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，26 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，26 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，26 个样本，一致性 100%
- 调度器 最常用 beta，26 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 高发问题（26/26 个样本）：Steps较低可能导致细节不足

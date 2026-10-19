---
name: text_to_image_lora_sampler_clip_22
type: Text To Image
frequency: 19
level: strong
coverage: 0.717684
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3数字人带货视频｜多图直生成模特产品展示_2103033669408608258.json, 视频生成/图生视频/MiniMax H3最强二采工作流｜音画俱佳战斗特效人物视频_2108009547691544578.json, 视频生成/图生视频/MiniMax H3电影感引擎｜人物场景特效加持，帧帧都是大片质感_2099408061910835201.json, 视频生成/图生视频/MiniMax H3电影感视频生成 每一帧电影级画面质感_2099207360228184066.json, 视频生成/图生视频/MiniMax h3开源加速版 海螺多参文生视频图生视频音频参考_2085303974785273857.json, 视频生成/图生视频/MiniMax+H3二采多参考生视频，图片视频音频混合输入_2110487892341641217.json, 视频生成/图生视频/MiniMax+H3多参考生视频二采，9图片3视频3音频全兼容_2110467435626319874.json, 视频生成/图生视频/MiniMax-H3开源多图生视频｜数字人视频带货电商口播好帮手_2104534112320180225.json, 视频生成/图生视频/MiniMax-H3开源数字人视频带货｜多图生视频电商口播神器_2104495131775815681.json, 视频生成/图生视频/MiniMax-H3数字人带货图生视频_2108450739797446658.json, 视频生成/图生视频/MiniMax-H3数字人带货视频｜模特产品展示图生视频_2108417540744638465.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars模特产品展示_2108393078053756930.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars电商好帮手_2111119123915821058.json, 视频生成/图生视频/MiniMax-H3高速大动态，无劣化抗形变模糊文生视频_2111233041338298369.json, 视频生成/图生视频/参考生视频提示词优化二阶高清｜MiniMax H3动作迁移图生视频_2091319533301747713.json, 视频生成/图生视频/文生图生首尾帧视频｜MiniMax_H3二阶高清直出_2090558225891553281.json, 视频生成/文生视频/H3二采去油不爆音加速工作流 视频生成处理_2100647828073832450.json, 视频生成/文生视频/H3全能视频｜vibex文生图生首尾帧通吃，二阶高清更细腻_2099860995895291906.json, 视频生成/文生视频/MiniMax-H3 极限复杂大动态｜16G显存人脸去油腻方案_2096876860767563778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3数字人带货视频｜多图直生成模特产品展示_2103033669408608258.json、视频生成/图生视频/MiniMax H3最强二采工作流｜音画俱佳战斗特效人物视频_2108009547691544578.json、视频生成/图生视频/MiniMax H3电影感引擎｜人物场景特效加持，帧帧都是大片质感_2099408061910835201.json、视频生成/图生视频/MiniMax H3电影感视频生成 每一帧电影级画面质感_2099207360228184066.json、视频生成/图生视频/MiniMax h3开源加速版 海螺多参文生视频图生视频音频参考_2085303974785273857.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 19 个 workflow 都包含：
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
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 18/19 个有
- `BasicScheduler` —— 17/19 个有
- `LTXVConcatAVLatent` —— 17/19 个有
- `LTXVSeparateAVLatent` —— 17/19 个有
- `MiniMaxH3ReferenceToVideo` —— 17/19 个有
- `GetNode` —— 16/19 个有
- `MinimaxH3LatentUpscaler3D` —— 16/19 个有
- `SetNode` —— 16/19 个有
- `ManualSigmas` —— 12/19 个有
- `VHS_VideoCombine` —— 12/19 个有
- `SplitSigmas` —— 11/19 个有
- `LoadAudio` —— 9/19 个有
- `VHS_LoadVideo` —— 9/19 个有
- `CreateVideo` —— 8/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/19 个有
- `SaveVideo` —— 7/19 个有
- `MiniMaxChunkFeedForward` —— 6/19 个有
- `PrimitiveStringMultiline` —— 6/19 个有
- `Text` —— 6/19 个有
- `easy float` —— 6/19 个有
- `MiniMaxH3SigmaShift` —— 5/19 个有
- `MiniMaxLowVRAMAttention` —— 5/19 个有
- `ModelPreviewOverrideKJ` —— 5/19 个有
- `SaveImage` —— 5/19 个有
- `ComfySwitchNode` —— 4/19 个有
- `Fast Groups Bypasser (rgthree)` —— 4/19 个有
- `PathchSageAttentionKJ` —— 4/19 个有
- `ModelAttentionBackend` —— 3/19 个有
- `PrimitiveBoolean` —— 3/19 个有
- `SpectrumApplyMiniMaxH3` —— 3/19 个有
- `Label (rgthree)` —— 2/19 个有
- `MiniMaxH3ImageToVideo` —— 2/19 个有
- `VRAM_Debug` —— 2/19 个有
- `布尔孤海` —— 2/19 个有
- `BlockSparseAttention` —— 1/19 个有
- `ConditioningZeroOut` —— 1/19 个有
- `Fast Bypasser (rgthree)` —— 1/19 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/19 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/19 个有
- `MiniMaxH3TurboSampler` —— 1/19 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/19 个有
- `UniBlockSwap` —— 1/19 个有
- `easy ifElse` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_upscale_latent_upscale_lora_2
type: Text To Image
frequency: 18
level: strong
coverage: 0.543222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多参考生视频｜字节DMAD加速双倍高清放大_2107644291471466498.json, 视频生成/图生视频/MiniMax H3打斗双采｜高质量图生视频生成_2095602888709066753.json, 视频生成/图生视频/MiniMax H3最强二采工作流｜音画俱佳战斗特效人物视频_2108009547691544578.json, 视频生成/图生视频/MiniMax H3电影感引擎｜人物场景特效加持，帧帧都是大片质感_2099408061910835201.json, 视频生成/图生视频/MiniMax H3电影感视频生成 每一帧电影级画面质感_2099207360228184066.json, 视频生成/图生视频/MiniMax+H3二采多参考生视频，图片视频音频混合输入_2110487892341641217.json, 视频生成/图生视频/MiniMax+H3多参考生视频二采，9图片3视频3音频全兼容_2110467435626319874.json, 视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json, 视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json, 视频生成/图生视频/Minimax H3动作迁移2.0进阶｜视频生视频史诗级强化_2103047047137021954.json, 视频生成/图生视频/双倍高清放大MiniMax H3多参考生视频字节DMAD加速版工作流，图生视频_2107922679855669249.json, 视频生成/图生视频/多参生视频优化版｜MiniMax H3支持9图3音3视频参考_2095857101267628033.json, 视频生成/图生视频/多参考生视频4步加速｜MiniMax H3一采二采双输出_2095968881948061697.json, 视频生成/图生视频/多参考生视频720p高清｜MiniMax H3场景特效生成_2096685620121919489.json, 视频生成/文生视频/H3二采去油不爆音加速工作流 视频生成处理_2100647828073832450.json, 视频生成/文生视频/MiniMax H3 二采加速｜多参考图生视频效率翻倍实用工作流_2097500273798369281.json, 视频生成/文生视频/MiniMax H3二采去油不爆音加速工作流，文生视频图生视频制作级方案_2103555034809192449.json, 视频生成/文生视频/MiniMax H3二采去油不爆音加速工作流｜视频生视频不糊脸，音画同步更高级_2100506185672781826.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多参考生视频｜字节DMAD加速双倍高清放大_2107644291471466498.json、视频生成/图生视频/MiniMax H3打斗双采｜高质量图生视频生成_2095602888709066753.json、视频生成/图生视频/MiniMax H3最强二采工作流｜音画俱佳战斗特效人物视频_2108009547691544578.json、视频生成/图生视频/MiniMax H3电影感引擎｜人物场景特效加持，帧帧都是大片质感_2099408061910835201.json、视频生成/图生视频/MiniMax H3电影感视频生成 每一帧电影级画面质感_2099207360228184066.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 18 个 workflow 都包含：
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
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 17/18 个有
- `PrimitiveFloat` —— 17/18 个有
- `VHS_LoadVideo` —— 17/18 个有
- `easy float` —— 16/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/18 个有
- `VHS_VideoCombine` —— 14/18 个有
- `SaveImage` —— 7/18 个有
- `SaveVideo` —— 6/18 个有
- `CreateVideo` —— 5/18 个有
- `Fast Groups Bypasser (rgthree)` —— 5/18 个有
- `ModelAttentionBackend` —— 5/18 个有
- `MiniMaxChunkFeedForward` —— 4/18 个有
- `MiniMaxH3TurboSampler` —— 4/18 个有
- `MiniMaxLowVRAMAttention` —— 4/18 个有
- `Astra` —— 2/18 个有
- `ImageFromBatch` —— 2/18 个有
- `Int` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/18 个有
- `LoadVideo` —— 2/18 个有
- `MiniMaxH3AVDecodeT8` —— 2/18 个有
- `easy showAnything` —— 2/18 个有
- `忽略多组孤海` —— 2/18 个有
- `获取视频信息` —— 2/18 个有
- `Float` —— 1/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/18 个有
- `PrimitiveBoolean` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足

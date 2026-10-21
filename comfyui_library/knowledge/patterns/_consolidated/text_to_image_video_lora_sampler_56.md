---
name: text_to_image_video_lora_sampler_56
type: Text To Image
frequency: 12
level: strong
coverage: 0.923583
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3全能参考生视频加速版 多重加速高清输出_2098827453300039682.json, 视频生成/图生视频/MiniMax H3打戏战斗特效图生视频处理工作流_2102501974091583489.json, 视频生成/图生视频/MiniMax H3数字人加速版V1｜音频驱动打造音乐MV_2105223015419170818.json, 视频生成/图生视频/MiniMax H3视频复刻加速版，数字人参考生视频与长视频直出工作流_2102827221554651137.json, 视频生成/图生视频/MiniMax H3视频复刻数字人加速版｜参考生视频长视频直出｜口播福音_2102608437405372417.json, 视频生成/图生视频/MiniMax H3视频复刻数字人换人换产品文案不换原声保留_2108718797380218882.json, 视频生成/图生视频/MiniMax H3视频复刻数字人视频换人换产品换文案语音替换_2108676232131997697.json, 视频生成/图生视频/MiniMax H3音频驱动数字人多人对话加速版长视频处理工具，数字人图生视频方案_2108327431890366466.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜换人换产品文案不换原声保留_2107986135334088706.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2107984724403777537.json, 视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话加速版长视频处理工具，数字人生成方案_2109462993590382594.json, 视频生成/图生视频/minimax h3多参工作流｜多参考图生视频高质量生成_2097060954776367106.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3全能参考生视频加速版 多重加速高清输出_2098827453300039682.json、视频生成/图生视频/MiniMax H3打戏战斗特效图生视频处理工作流_2102501974091583489.json、视频生成/图生视频/MiniMax H3数字人加速版V1｜音频驱动打造音乐MV_2105223015419170818.json、视频生成/图生视频/MiniMax H3视频复刻加速版，数字人参考生视频与长视频直出工作流_2102827221554651137.json、视频生成/图生视频/MiniMax H3视频复刻数字人加速版｜参考生视频长视频直出｜口播福音_2102608437405372417.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 11/12 个有
- `ModelAttentionBackend` —— 11/12 个有
- `SolAttnMiniMax` —— 11/12 个有
- `CR Prompt Text` —— 10/12 个有
- `孤海注释` —— 9/12 个有
- `SaveImage` —— 8/12 个有
- `VHS_LoadVideo` —— 8/12 个有
- `PreviewImage` —— 6/12 个有
- `EmptyImage` —— 5/12 个有
- `LoadAudio` —— 5/12 个有
- `CR Text` —— 2/12 个有
- `ExtendIntermediateSigmas` —— 2/12 个有
- `H3SigmaRefiner` —— 1/12 个有
- `IntToString` —— 1/12 个有
- `MiniMaxChunkFeedForward` —— 1/12 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 1/12 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 1/12 个有
- `MiniMaxLowVRAMAttention` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `Seed_` —— 1/12 个有
- `text-util-join-text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（17/12 个样本）：Steps较低可能导致细节不足

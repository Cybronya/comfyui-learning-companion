---
name: text_to_image_video_lora_sampler_74
type: Text To Image
frequency: 10
level: strong
coverage: 0.889
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax h3电商带货视频自动提示词模特产品展示_2088181792762318849.json, 视频生成/图生视频/全能参考加速版图生视频｜AIGC短剧视频生成工作流_2087223105965084673.json, 视频生成/图生视频/全能参考工作流｜MiniMax H3图生视频一键生成_2090270213274165249.json, 视频生成/图生视频/全能视频生成｜MiniMax H3开源图生视频直出_2089796312794488834.json, 视频生成/图生视频/加速工作流多图参考短剧制作Minimax_H3图生视频_2088378063548669954.json, 视频生成/图生视频/加速版MiniMax H3图文一键生视频 快速出片方案_2109082909939429378.json, 视频生成/图生视频/动作镜头参考洗稿｜MiniMax-H3视频运镜生成_2093772942814572545.json, 视频生成/图生视频/多图参考短剧制作加速工作流｜Minimax_H3图生视频_2088347597277843458.json, 视频生成/图生视频/镜头动作参考洗稿｜MiniMax-H3视频运镜图生视频_2093442197000646657.json, 视频生成/文生视频/Minimax H3多图参考加速文生视频图生视频工作流_2088178522983587841.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_74

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/minimax h3电商带货视频自动提示词模特产品展示_2088181792762318849.json、视频生成/图生视频/全能参考加速版图生视频｜AIGC短剧视频生成工作流_2087223105965084673.json、视频生成/图生视频/全能参考工作流｜MiniMax H3图生视频一键生成_2090270213274165249.json、视频生成/图生视频/全能视频生成｜MiniMax H3开源图生视频直出_2089796312794488834.json、视频生成/图生视频/加速工作流多图参考短剧制作Minimax_H3图生视频_2088378063548669954.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 9/10 个有
- `BasicGuider` —— 7/10 个有
- `LoraLoaderBypassModelOnly` —— 7/10 个有
- `MiniMaxH3AVDecodeT8` —— 7/10 个有
- `MiniMaxH3AudioConditioningT8` —— 7/10 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 7/10 个有
- `ResolutionSelector` —— 7/10 个有
- `LoadAudio` —— 5/10 个有
- `CFGGuider` —— 3/10 个有
- `ConditioningZeroOut` —— 3/10 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/10 个有
- `MiniMaxH3ReferenceToVideo` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `VAEDecodeAudio` —— 3/10 个有
- `easy int` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ImageConcanate` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `MiniMaxH3BlockCacheT8` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `RHLLMChatNode` —— 1/10 个有
- `SaveImage` —— 1/10 个有

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

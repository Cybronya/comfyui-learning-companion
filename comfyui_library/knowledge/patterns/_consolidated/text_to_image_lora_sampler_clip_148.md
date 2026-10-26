---
name: text_to_image_lora_sampler_clip_148
type: Text To Image
frequency: 11
level: strong
coverage: 0.866909
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3双人对话 文生音频图生图处理生成工具_2100316663001477121.json, 视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094250837928407041.json, 视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094271866994257922.json, 视频生成/图生视频/导演台双采样全能工作流｜MiniMax H3图生视频_2092388355215552514.json, 视频生成/图生视频/高质量加速图生视频 Minimax H3 画质与速度兼顾快速出片_2094180356353249281.json, 视频生成/图生视频/高质量加速版图生视频｜Minimax H3一键高清生成_2094316328000778241.json, 视频生成/文生视频/24GB通用版6倍加速参考生视频｜MiniMax H3文生图生视频生视频工作流_2087179601289236482.json, 视频生成/文生视频/48GB高配版6倍加速参考生视频｜MiniMax H3文生图生视频工作流_2087157477258383362.json, 视频生成/文生视频/4步8步加速稳定MAX｜MiniMaxH3多合一自用版_2092748173281423361.json, 视频生成/文生视频/9图3视频3音频全能多参音视频生成开源加速版｜海螺H3文生图生视频工作流_2088148034331963394.json, 音频生成/音频生成/MiniMax H3 TTS文生音频音频克隆SeedAudio开源版_2088194262323253249.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_148

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/H3双人对话 文生音频图生图处理生成工具_2100316663001477121.json、视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094250837928407041.json、视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094271866994257922.json、视频生成/图生视频/导演台双采样全能工作流｜MiniMax H3图生视频_2092388355215552514.json、视频生成/图生视频/高质量加速图生视频 Minimax H3 画质与速度兼顾快速出片_2094180356353249281.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `PathchSageAttentionKJ` —— 8/11 个有
- `MiniMaxH3ImageToVideo` —— 7/11 个有
- `ResolutionSelector` —— 6/11 个有
- `CreateVideo` —— 5/11 个有
- `ImageResizeKJv2` —— 5/11 个有
- `LoadAudio` —— 5/11 个有
- `MiniMaxH3ReferenceToVideo` —— 5/11 个有
- `SaveVideo` —— 5/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/11 个有
- `VHS_VideoCombine` —— 4/11 个有
- `EasyCache` —— 3/11 个有
- `MiniMaxH3BlockCacheT8` —— 3/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `PrimitiveInt` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `MiniMaxH3AudioConditioningT8` —— 2/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/11 个有
- `SaveAudioAdvanced` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `easy ifElse` —— 2/11 个有
- `easy isNone` —— 2/11 个有
- `easy seed` —— 2/11 个有
- `LazySwitchKJ` —— 1/11 个有
- `PrimitiveBoolean` —— 1/11 个有
- `SolAttnPatch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足

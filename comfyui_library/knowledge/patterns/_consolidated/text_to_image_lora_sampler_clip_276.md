---
name: text_to_image_lora_sampler_clip_276
type: Text To Image
frequency: 8
level: strong
coverage: 0.890375
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3文生视频8步工作流 高效视频生成工具_2100289449610534913.json, 视频生成/文生视频/H3文生视频加速版 官方Turbo加速出片_2099594371384561665.json, 视频生成/文生视频/H3最优官流｜文生图生视频高质量一键生成_2092047166419324930.json, 视频生成/文生视频/H3最优官流｜文生视频图生视频双模式官方_2089391709946994690.json, 视频生成/文生视频/H3高动态打斗场景武术动作二采修复 提示词增强工作流_2099919995085086722.json, 视频生成/文生视频/LightX2V Turbo加速｜MiniMax H3文生图生视频生视频工作流_2087187099337445378.json, 视频生成/文生视频/MINIMAX-H3文生视频工作流｜图生视频双模式｜短视频创作提效_2101872099584466946.json, 视频生成/文生视频/MiniMax H3多合一Turbo4 Sage T8 Stable-R2V Turbo6 EXP二_2087347142024327170.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_276

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/H3文生视频8步工作流 高效视频生成工具_2100289449610534913.json、视频生成/文生视频/H3文生视频加速版 官方Turbo加速出片_2099594371384561665.json、视频生成/文生视频/H3最优官流｜文生图生视频高质量一键生成_2092047166419324930.json、视频生成/文生视频/H3最优官流｜文生视频图生视频双模式官方_2089391709946994690.json、视频生成/文生视频/H3高动态打斗场景武术动作二采修复 提示词增强工作流_2099919995085086722.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `LoadImage` —— 5/8 个有
- `MiniMaxH3ImageToVideo` —— 5/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `MiniMaxH3ReferenceToVideo` —— 4/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `ManualSigmas` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `SolAttnPatch` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `DisableNoise` —— 1/8 个有
- `GetVideoComponents` —— 1/8 个有
- `LoadVideo` —— 1/8 个有
- `LoraLoaderBypassModelOnly` —— 1/8 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/8 个有
- `PT_H3ConcatAVLatent` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `SplitSigmas` —— 1/8 个有
- `VAEEncode` —— 1/8 个有
- `VAEEncodeAudio` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足

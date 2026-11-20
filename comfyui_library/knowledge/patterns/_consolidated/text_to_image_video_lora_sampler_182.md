---
name: text_to_image_video_lora_sampler_182
type: Text To Image
frequency: 4
level: strong
coverage: 0.6555
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/minimax_h3_i2vw4a8-0810超低显存ENGENG_2087115217783316482.json, 视频生成/文生视频/minimax阿里8步加速三合一｜文生视频图生视频全能参考_2095568310212587522.json, 视频生成/文生视频/图MiniMax文生视频视频生视频图生视频_2085849570684260354.json, 视频生成/文生视频/多参考生成视频｜MiniMax H3官方工作流一键直出_2090147863308357634.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_182

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/minimax_h3_i2vw4a8-0810超低显存ENGENG_2087115217783316482.json、视频生成/文生视频/minimax阿里8步加速三合一｜文生视频图生视频全能参考_2095568310212587522.json、视频生成/文生视频/图MiniMax文生视频视频生视频图生视频_2085849570684260354.json、视频生成/文生视频/多参考生成视频｜MiniMax H3官方工作流一键直出_2090147863308357634.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
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
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `VAEDecodeAudio` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `Text` —— 2/4 个有
- `Display Any (rgthree)` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `LoraLoaderBypassModelOnly` —— 1/4 个有
- `MiniMaxH3AVDecodeT8` —— 1/4 个有
- `MiniMaxH3BlockCacheT8` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SolAttnPatch` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

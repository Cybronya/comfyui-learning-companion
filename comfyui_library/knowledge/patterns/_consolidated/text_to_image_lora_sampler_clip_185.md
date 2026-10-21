---
name: text_to_image_lora_sampler_clip_185
type: Text To Image
frequency: 7
level: strong
coverage: 0.896714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3动作迁移图生视频 二采放大高清视频输出工作流_2094358912484073473.json, 视频生成/图生视频/ref turbo加速图生视频动作模仿｜MiniMax-H3动作迁移视频生视频_2088380985703485441.json, 视频生成/图生视频/动作模仿ref turbo加速MiniMax H3图生视频动作迁移工作流_2088402060675997697.json, 视频生成/图生视频/单模型二采无编解码放大｜MiniMax-H3 ref2va超分_2093849774721167362.json, 视频生成/图生视频/多参图生视频双采Latent放大｜Minimax-H3一键直出_2091672749377941505.json, 视频生成/文生视频/两步生成768P视频｜Minimax H3 多参数加速LoRA_2096256232272257025.json, 视频生成/文生视频/多参数视频生成768p｜Minimax H3加速LoRA两步_2095964673219846146.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_185

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3动作迁移图生视频 二采放大高清视频输出工作流_2094358912484073473.json、视频生成/图生视频/ref turbo加速图生视频动作模仿｜MiniMax-H3动作迁移视频生视频_2088380985703485441.json、视频生成/图生视频/动作模仿ref turbo加速MiniMax H3图生视频动作迁移工作流_2088402060675997697.json、视频生成/图生视频/单模型二采无编解码放大｜MiniMax-H3 ref2va超分_2093849774721167362.json、视频生成/图生视频/多参图生视频双采Latent放大｜Minimax-H3一键直出_2091672749377941505.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 5/7 个有
- `LTXVConcatAVLatent` —— 5/7 个有
- `LTXVSeparateAVLatent` —— 5/7 个有
- `LoadVideo` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `MinimaxH3LatentUpscaler3D` —— 5/7 个有
- `ModelPreviewOverrideKJ` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `ComfyMathExpression` —— 4/7 个有
- `MiniMaxH3SigmaShift` —— 4/7 个有
- `ModelAttentionBackend` —— 4/7 个有
- `PixaromaDuration` —— 4/7 个有
- `PixaromaSizes` —— 4/7 个有
- `ResolutionSelector` —— 4/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `LoadAudio` —— 3/7 个有
- `ManualSigmas` —— 3/7 个有
- `MiniMaxH3BlockCacheT8` —— 3/7 个有
- `TrimAudioDuration` —— 3/7 个有
- `VRAM_Debug` —— 3/7 个有
- `Video Slice` —— 3/7 个有
- `SplitSigmas` —— 2/7 个有
- `VHS_VideoCombine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足

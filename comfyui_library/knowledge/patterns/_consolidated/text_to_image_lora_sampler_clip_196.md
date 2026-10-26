---
name: text_to_image_lora_sampler_clip_196
type: Text To Image
frequency: 10
level: strong
coverage: 0.8664
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/minimax_h3_i2vw4a8-0810超低显存ENGENG_2087115217783316482.json, 视频生成/文生视频/minimax阿里8步加速三合一｜文生视频图生视频全能参考_2095568310212587522.json, 视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json, 视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json, 视频生成/文生视频/图文生视频直出｜MiniMax H3多模态视频生成_2093141446219091969.json, 视频生成/文生视频/多参考全模态视频生成｜MiniMax H3文图视频生_2092207503110135809.json, 视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速_2089249506813636609.json, 视频生成/文生视频/文生视频｜MiniMax H3 SageAttention+LoRA 双重加速刘神_2094117560072626177.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频生成_2094051162357063682.json, 视频生成/文生视频/真实电影质感｜MiniMax H3文生图生视频直出_2093845276451753986.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_196

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/minimax_h3_i2vw4a8-0810超低显存ENGENG_2087115217783316482.json、视频生成/文生视频/minimax阿里8步加速三合一｜文生视频图生视频全能参考_2095568310212587522.json、视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json、视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json、视频生成/文生视频/图文生视频直出｜MiniMax H3多模态视频生成_2093141446219091969.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
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
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/10 个有
- `MiniMaxH3ImageToVideo` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `LoadImage` —— 7/10 个有
- `LoraLoaderBypassModelOnly` —— 5/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `MiniMaxH3ReferenceToVideo` —— 5/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `LoadAudio` —— 3/10 个有
- `MiniMaxH3BlockCacheT8` —— 3/10 个有
- `DisableNoise` —— 2/10 个有
- `H3SigmaRefiner` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `SplitSigmas` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `easy anythingIndexSwitch` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `Display Any (rgthree)` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有
- `Text` —— 1/10 个有

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

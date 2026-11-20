---
name: text_to_image_lora_sampler_clip_233
type: Text To Image
frequency: 9
level: strong
coverage: 0.880444
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax H3多图参考加速文生视频图生视频工作流_2088178522983587841.json, 视频生成/文生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086200437891485697.json, 视频生成/文生视频/Ref2VA剧本直出六段式自动生成校验9图参考成片｜H3原生音画同步文生图生视频_2088323034326331393.json, 视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json, 视频生成/文生视频/SageAttention+LoRA双重加速｜MiniMax H3文生视频_2089404463130963970.json, 视频生成/文生视频/T2V文生视频直出｜MiniMax H3高清视频一键生成_2089822887556509698.json, 视频生成/文生视频/多参考图+视频参考｜minimax_h3 sage加速图生视频_2090199253544165378.json, 视频生成/文生视频/新4步LoRa参考图｜MiniMax H3角色一致图生视频_2092736016280023041.json, 视频生成/文生视频/量化加速参考生视频｜MiniMaxH3 文本图像音视频全参考_2089345982659121153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_233

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/Minimax H3多图参考加速文生视频图生视频工作流_2088178522983587841.json、视频生成/文生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086200437891485697.json、视频生成/文生视频/Ref2VA剧本直出六段式自动生成校验9图参考成片｜H3原生音画同步文生图生视频_2088323034326331393.json、视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json、视频生成/文生视频/SageAttention+LoRA双重加速｜MiniMax H3文生视频_2089404463130963970.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
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
- `BasicGuider` —— 8/9 个有
- `BasicScheduler` —— 8/9 个有
- `KSamplerSelect` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `CreateVideo` —— 7/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `SaveVideo` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `MiniMaxH3ReferenceToVideo` —— 6/9 个有
- `LoadAudio` —— 4/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/9 个有
- `VHS_LoadVideo` —— 4/9 个有
- `MiniMaxH3ImageToVideo` —— 3/9 个有
- `PathchSageAttentionKJ` —— 3/9 个有
- `LoraLoaderBypassModelOnly` —— 2/9 个有
- `VHS_VideoCombine` —— 2/9 个有
- `CFGGuider` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `DiffusionModelLoaderKJ` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `MiniMaxH3BlockCacheT8` —— 1/9 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/9 个有
- `PainterVRAM` —— 1/9 个有
- `RHLLMChatNode` —— 1/9 个有
- `VideoInfoLoaded` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足

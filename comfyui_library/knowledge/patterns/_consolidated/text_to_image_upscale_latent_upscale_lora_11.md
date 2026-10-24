---
name: text_to_image_upscale_latent_upscale_lora_11
type: Text To Image
frequency: 6
level: strong
coverage: 0.574333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax-H3疯狂测试工作流｜文生视频视频生视频_2095216174060630017.json, 视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json, 视频生成/文生视频/文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298.json, 视频生成/文生视频/疯狂测试全通过｜MiniMax H3三模输入全能出片_2096527562737541121.json, 视频生成/文生视频/疯狂测试工作流｜Aiden MiniMax-H3文生视频视频生视频_2095553065045807106.json, 视频生成/文生视频/疯狂测试工作流｜MiniMax H3文生视频图生视频多模式_2096295220886466562.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax-H3疯狂测试工作流｜文生视频视频生视频_2095216174060630017.json、视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json、视频生成/文生视频/文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298.json、视频生成/文生视频/疯狂测试全通过｜MiniMax H3三模输入全能出片_2096527562737541121.json、视频生成/文生视频/疯狂测试工作流｜Aiden MiniMax-H3文生视频视频生视频_2095553065045807106.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 5/6 个有
- `easy boolean` —— 5/6 个有
- `忽略多组孤海` —— 5/6 个有
- `AudioCrop` —— 4/6 个有
- `ComfySwitchNode` —— 4/6 个有
- `CreateVideo` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `easy positive` —— 4/6 个有
- `Any Switch (rgthree)` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `H3AudioRefineSampler` —— 2/6 个有
- `H3FrozenVideoCache` —— 2/6 个有
- `Int` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `ManualSigmas` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `SolAttnPatch` —— 2/6 个有
- `SplitSigmas` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/6 个有
- `easy ifElse` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足

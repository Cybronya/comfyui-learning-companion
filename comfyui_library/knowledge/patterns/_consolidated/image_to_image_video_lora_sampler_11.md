---
name: image_to_image_video_lora_sampler_11
type: Image To Image
frequency: 3
level: strong
coverage: 0.598
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, FloatToSigmas, GetNode, INTConstant, ImageResizeKJv2, ImageScaleBy, KSampler, KSamplerSelect, LTXVConditioning, LTXVLatentUpsampler, LTXVLatentUpsamplerModelLoader, LTXVLoopingSampler, LTXVTiledVAEDecode, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MultiPromptProvider, PathchSageAttentionKJ, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, SetNode, StringToFloatList, UNETLoader, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/ltxv-13b-i2v高速生成+独家放大工作流_1947851096858472450.json, 视频生成/图生视频/ltxv-13b-i2v高速生成+独家放大工作流_1950513192411844609.json, 视频生成/图生视频/ltxv图生视频+wan2.1视频放大_1948658851380887554.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/ltxv-13b-i2v高速生成+独家放大工作流_1947851096858472450.json、视频生成/图生视频/ltxv-13b-i2v高速生成+独家放大工作流_1950513192411844609.json、视频生成/图生视频/ltxv图生视频+wan2.1视频放大_1948658851380887554.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `FloatToSigmas`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSampler`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVLatentUpsamplerModelLoader`
- `LTXVLoopingSampler`
- `LTXVTiledVAEDecode`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MultiPromptProvider`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `SetNode`
- `StringToFloatList`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | lcm | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode

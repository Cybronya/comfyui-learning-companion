---
name: text_to_image_upscale_sampler_clip_41
type: Text To Image
frequency: 2
level: weak
coverage: 0.9715
common_nodes: [CLIPLoader, CLIPLoaderGGUF, CLIPTextEncode, CR Text, ConditioningZeroOut, DisTorchPurgeVRAMV2, EmptyLatentImage, KSampler, PurgeVRAM_UTK, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy int]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/Krea2(raw+turbo)+Zimage三重采样-+seedVR2超清放大_2074538764248109058.json, 图片生成/文生图/Krea2迭代采样三次-极致细节--直出4K_2075890836566528002.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2(raw+turbo)+Zimage三重采样-+seedVR2超清放大_2074538764248109058.json、图片生成/文生图/Krea2迭代采样三次-极致细节--直出4K_2075890836566528002.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DisTorchPurgeVRAMV2`
- `EmptyLatentImage`
- `KSampler`
- `PurgeVRAM_UTK`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `TTResolutionSelector` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | - | 2 | 97% |
| 高度 | 1472 | - | 2 | 70% |
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 6.5 | - | 2 | 15% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler_ancestral | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1472，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 6.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 15%
- 调度器 最常用 euler_ancestral，2 个样本，一致性 50%
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 高发问题（1/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

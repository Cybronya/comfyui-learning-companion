---
name: image_to_image_lora_sampler_clip_170
type: Image To Image
frequency: 2
level: weak
coverage: 0.6425
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetNode, ImageSmartSharpen+, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RebatchLatents, RepeatLatentBatch, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/造相 Z-image 图生图重绘_洗图_1994091834760691713.json, 图片生成/图生图/🈚️QWEN + z-image 基础 图生图_洗图 +反推+图生图重绘_1955619987023171585.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_170

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/造相 Z-image 图生图重绘_洗图_1994091834760691713.json、图片生成/图生图/🈚️QWEN + z-image 基础 图生图_洗图 +反推+图生图重绘_1955619987023171585.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetNode`
- `ImageSmartSharpen+`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RebatchLatents`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `CFGZeroStar` —— 1/2 个有
- `DetailDaemonSamplerNode` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SamplerCustom` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.565 | - | 2 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.565，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: image_to_image_lora_sampler_unet_212
type: Image To Image
frequency: 2
level: weak
coverage: 0.826
common_nodes: [CLIPLoader, ConditioningZeroOut, ImpactSwitch, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, Text, TextCombinerTwo, TextEncodeQwenImageEditPlus, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ComfyUI短发焕新：多款男女发型随心所“发”工作流_1991833569553174530.json, 图片生成/图生图/男女发型设计 发型变换 脸型配发型 一键换发型_2018850790487625729.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_212

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ComfyUI短发焕新：多款男女发型随心所“发”工作流_1991833569553174530.json、图片生成/图生图/男女发型设计 发型变换 脸型配发型 一键换发型_2018850790487625729.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text`
- `TextCombinerTwo`
- `TextEncodeQwenImageEditPlus`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 6.5 | - | 2 | 15% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 6.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 15%
- 调度器 最常用 euler，2 个样本，一致性 50%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

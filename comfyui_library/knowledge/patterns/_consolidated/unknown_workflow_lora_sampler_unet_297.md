---
name: unknown_workflow_lora_sampler_unet_297
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9545
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UnetLoaderGGUF, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问像素不偏移-换装版-qwen image edit_1979100026792218626.json, 图片生成/图生图/图像镜头转换角度-预设功能版-qwen edit-2509_1987417210643787778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_297

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/千问像素不偏移-换装版-qwen image edit_1979100026792218626.json、图片生成/图生图/图像镜头转换角度-预设功能版-qwen edit-2509_1987417210643787778.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LazySwitch1way` —— 1/2 个有
- `Text to String` —— 1/2 个有
- `Upscale Model Loader` —— 1/2 个有
- `easy boolean` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

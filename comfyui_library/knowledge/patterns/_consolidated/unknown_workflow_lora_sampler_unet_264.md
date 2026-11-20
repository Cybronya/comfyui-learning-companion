---
name: unknown_workflow_lora_sampler_unet_264
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.969667
common_nodes: [CFGNorm, CLIPLoader, CR Text, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Edit-指定区域编辑-qwen image Edit_1983058606935420929.json, 图片生成/图生图/千问像素不偏移-换装版-qwen image edit_1979100026792218626.json, 图片生成/图生图/图像镜头转换角度-预设功能版-qwen edit-2509_1987417210643787778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_264

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问Edit-指定区域编辑-qwen image Edit_1983058606935420929.json、图片生成/图生图/千问像素不偏移-换装版-qwen image edit_1979100026792218626.json、图片生成/图生图/图像镜头转换角度-预设功能版-qwen edit-2509_1987417210643787778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `LazySwitch1way` —— 1/3 个有
- `Text to String` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `Upscale Model Loader` —— 1/3 个有
- `easy boolean` —— 1/3 个有
- `easy float` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）

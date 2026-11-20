---
name: unknown_workflow_controlnet_lora_sampler_23
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.816
common_nodes: [AIO_Preprocessor, Anything Everywhere, CFGNorm, CLIPLoader, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Controlnet （姿势，深度，线稿可选）_1961346295246032898.json, 图片生成/图生图/Qwen 重绘 洗图 CN可控 自动化提示词（可选）_1978104373295374337.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Controlnet （姿势，深度，线稿可选）_1961346295246032898.json、图片生成/图生图/Qwen 重绘 洗图 CN可控 自动化提示词（可选）_1978104373295374337.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

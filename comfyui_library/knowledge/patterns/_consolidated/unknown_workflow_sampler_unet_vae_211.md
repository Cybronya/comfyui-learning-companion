---
name: unknown_workflow_sampler_unet_vae_211
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.960286
common_nodes: [DifferentialDiffusion, DualCLIPLoader, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/flux-icedit用提示词来改图像_1930516395245867010.json, 平台全量/【新】flux fill ACE++  example_1890025037695688706.json, 平台全量/【新】flux fill inpaint example_1859948635189374977.json, 平台全量/【模特换装 】Flux Fill 局部重绘 实用好用 简洁新民版_1964516891400224769.json, 平台全量/【阡陌】Flux fill OneReward 无痕去水印工作流_1970758194148614146.json, 平台全量/【阡陌】Flux fill OneReward 物体移除工作流_1970482876372447233.json, 平台全量/最强擦除工作流_objectRemovalv1-lora_1930168135654215682.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_211

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/flux-icedit用提示词来改图像_1930516395245867010.json、平台全量/【新】flux fill ACE++  example_1890025037695688706.json、平台全量/【新】flux fill inpaint example_1859948635189374977.json、平台全量/【模特换装 】Flux Fill 局部重绘 实用好用 简洁新民版_1964516891400224769.json、平台全量/【阡陌】Flux fill OneReward 无痕去水印工作流_1970758194148614146.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintModelConditioning` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `CLIPTextEncode` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `ArgosTranslateCLIPTextEncodeNode` —— 2/7 个有
- `EasyCache` —— 2/7 个有
- `LayerMask: MaskGrow` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `DiptychCreate` —— 1/7 个有
- `ICEFConditioning` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `easy makeImageForICLora` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 28 | 7 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 57% |
| 重绘幅度 | 1 | 0.15 - 1 | 7 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 28，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，7 个样本

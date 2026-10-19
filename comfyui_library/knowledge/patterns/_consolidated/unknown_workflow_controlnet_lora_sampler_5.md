---
name: unknown_workflow_controlnet_lora_sampler_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7145
common_nodes: [BNK_CLIPTextEncodeAdvanced, CLIPSetLastLayer, CR SDXL Aspect Ratio, CheckpointLoaderSimple, ControlNetLoader, GetNode, HyperLoRAApplyLoRA, HyperLoRAConfig, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, HyperLoRAIDCond, HyperLoRALoader, ImpactMakeImageBatch, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LoadImage, PreviewImage, RH_Captioner, SaveImage, SetNode, Text Concatenate, Text Multiline, TextPreview, VAEDecode]
problems: []
missing: [LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, Text Concatenate, Text Multiline, CR SDXL Aspect Ratio, WD14Tagger|pysssss]
members: [图片生成/文生图/1916087629534924802.json, 图片生成/文生图/1916097178987859970.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1916087629534924802.json、图片生成/文生图/1916097178987859970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `CLIPSetLastLayer`
- `CR SDXL Aspect Ratio`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `GetNode`
- `HyperLoRAApplyLoRA`
- `HyperLoRAConfig`
- `HyperLoRAFaceAttr`
- `HyperLoRAGenerateIDLoRA`
- `HyperLoRAIDCond`
- `HyperLoRALoader`
- `ImpactMakeImageBatch`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `SetNode`
- `Text Concatenate`
- `Text Multiline`
- `TextPreview`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ApplyInstantIDAdvanced` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `FaceDetailer` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `InstantIDFaceAnalysis` —— 1/2 个有
- `InstantIDModelLoader` —— 1/2 个有
- `SDXLPromptStyler` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 1 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 75% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: PersonMaskUltra V2、LayerUtility: CropByMask V2、Text Concatenate、Text Multiline、CR SDXL Aspect Ratio
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

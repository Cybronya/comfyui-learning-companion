---
name: unknown_workflow_lora_sampler_clip_263
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.852
common_nodes: [BasicScheduler, CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, DeepTranslatorTextNode, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RH_Captioner, SamplerCustom, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2人像洗图反推_1953312130965622786.json, 图片生成/图生图/【洗图反推】Wan2.2 洗图 超级修复 Wan2.2人像全图修复_1982282591334211586.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_263

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Wan2.2人像洗图反推_1953312130965622786.json、图片生成/图生图/【洗图反推】Wan2.2 洗图 超级修复 Wan2.2人像全图修复_1982282591334211586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `DeepTranslatorTextNode`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_Captioner`
- `SamplerCustom`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.7 | - | 2 | 100% |
| LoRA 文本强度 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

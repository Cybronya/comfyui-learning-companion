---
name: unknown_workflow_lora_sampler_unet_275
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.892
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, Fast Groups Muter (rgthree), GetImageSize, ImageFromBatch, ImageScaleToTotalPixels, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3UnifiedToVideo, PreviewImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy imageConcat, easy imageInsetCrop]
problems: []
missing: []
members: [图片生成/图生图/人物迁移-minimax图像编辑（API版）_2102450365731008514.json, 图片生成/图生图/人物迁移-minimax图像编辑（免费版）_2104550573549903874.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_275

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物迁移-minimax图像编辑（API版）_2102450365731008514.json、图片生成/图生图/人物迁移-minimax图像编辑（免费版）_2104550573549903874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `Fast Groups Muter (rgthree)`
- `GetImageSize`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3UnifiedToVideo`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageConcat`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `Qwen3VL_Chat` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

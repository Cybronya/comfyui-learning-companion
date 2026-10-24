---
name: unknown_workflow_sampler_unet_vae_296
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.755
common_nodes: [CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, ModelAttentionBackend, PreviewAny, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, QwenImage21Cache, QwenImage21ConfigPreparer_EditUtils, QwenImage21ModelConfig_EditUtils, RepeatLatentBatch, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy ifElse, easy imageSizeByLongerSide, easy indexAnything, easy lengthAnything, easy makeImageList, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 图片编辑（提示词反推）2609_2106049358109167617.json, 图片生成/文生图/Qwen Image 2.1 图片编辑（一流通吃）_2101867655480307714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_296

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 图片编辑（提示词反推）2609_2106049358109167617.json、图片生成/文生图/Qwen Image 2.1 图片编辑（一流通吃）_2101867655480307714.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ModelAttentionBackend`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `QwenImage21ConfigPreparer_EditUtils`
- `QwenImage21ModelConfig_EditUtils`
- `RepeatLatentBatch`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy imageSizeByLongerSide`
- `easy indexAnything`
- `easy lengthAnything`
- `easy makeImageList`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_lora_unet_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [Anything Everywhere3, CFGNorm, CLIPLoader, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RHHiddenNodes, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/迄今超强Qwen image-edit2511版工业外观风格迁移神器白底白膜线框一键上色在线运行_1914154624285376513.json, 图片生成/图生图/迄今超强Qwen image-edit2511版（更强一致性）支持单图双图多图编辑在线运行+可选4K高清放大V2_1958410274757885953.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_unet_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/迄今超强Qwen image-edit2511版工业外观风格迁移神器白底白膜线框一键上色在线运行_1914154624285376513.json、图片生成/图生图/迄今超强Qwen image-edit2511版（更强一致性）支持单图双图多图编辑在线运行+可选4K高清放大V2_1958410274757885953.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `FluxResolutionNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSampler (Efficient)` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 824 | - | 2 | 100% |
| 高度 | 1376 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 824，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1376，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

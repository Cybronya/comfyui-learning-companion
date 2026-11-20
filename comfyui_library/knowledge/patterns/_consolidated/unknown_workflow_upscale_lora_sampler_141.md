---
name: unknown_workflow_upscale_lora_sampler_141
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.456
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelPreviewOverrideKJ, PathchSageAttentionKJ, PlaySound|pysssss, PrimitiveString, ProcessString, QwenImage21Cache, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, StringConcatenate, TextEncodeQwenImage21, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy int, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/④「写真V0」Z+Qwen2.1 写真分镜「10.9」_2108558851799867393.json, 视频生成/图生视频/❹「写真V0」Z+Qwen2.1_写真分镜「10.9」_2115979956839862273.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_141

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/④「写真V0」Z+Qwen2.1 写真分镜「10.9」_2108558851799867393.json、视频生成/图生视频/❹「写真V0」Z+Qwen2.1_写真分镜「10.9」_2115979956839862273.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelPreviewOverrideKJ`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PrimitiveString`
- `ProcessString`
- `QwenImage21Cache`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SomethingToString`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy promptLine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

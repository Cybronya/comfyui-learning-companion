---
name: text_to_image_lora_sampler_clip_376
type: Text To Image
frequency: 2
level: weak
coverage: 0.615
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, INTConstant, Image Comparer (rgthree), KSampler, KSamplerAdvanced, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, PathchSageAttentionKJ, ResolutionSelector, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SetNode, ShowText|pysssss, String, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 多风格LORA工作流_2083014218642706434.json, 图片生成/文生图/Krea2 高质量动漫工作流_2083760574575497217.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_376

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2 多风格LORA工作流_2083014218642706434.json、图片生成/文生图/Krea2 高质量动漫工作流_2083760574575497217.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SetNode`
- `ShowText|pysssss`
- `String`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `String Literal` —— 1/2 个有
- `Switch` —— 1/2 个有
- `easy int` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | res_2s | - | 2 | 50% |
| 重绘幅度 | linear_quadratic | - | 2 | 50% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2s，2 个样本，一致性 50%
- 重绘幅度 最常用 linear_quadratic，2 个样本，一致性 50%
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

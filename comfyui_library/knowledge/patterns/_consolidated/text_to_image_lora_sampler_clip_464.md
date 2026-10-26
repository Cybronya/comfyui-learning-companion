---
name: text_to_image_lora_sampler_clip_464
type: Text To Image
frequency: 4
level: strong
coverage: 0.851
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ColorMatchV2, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleBy, KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(Krea2+Klein)双K风格化细节增强_2073293647621222402.json, 图片生成/文生图/krea2+klein双采多风格通用工作流_2072555688601153538.json, 图片生成/文生图/krea2+klein双采多风格通用工作流_2073783289609023490.json, 图片生成/文生图/文生图-krea2+klein双采多风格通用工作流_2089927009278447618.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_464

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/(Krea2+Klein)双K风格化细节增强_2073293647621222402.json、图片生成/文生图/krea2+klein双采多风格通用工作流_2072555688601153538.json、图片生成/文生图/krea2+klein双采多风格通用工作流_2073783289609023490.json、图片生成/文生图/文生图-krea2+klein双采多风格通用工作流_2089927009278447618.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorMatchV2`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `llama_cpp_parameters` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `OpenAI_Chat_API` —— 1/4 个有
- `QZ_ResolutionPreset` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `SimpleMathDual+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2m | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足

---
name: text_to_image_lora_sampler_clip_85
type: Text To Image
frequency: 11
level: moderate
coverage: 0.868182
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/(Krea2+Klein)双K风格化细节增强_2073293647621222402.json, 图片生成/文生图/krea2+klein双采多风格通用工作流_2072555688601153538.json, 图片生成/文生图/krea2+klein双采多风格通用工作流_2073783289609023490.json, 图片生成/文生图/krea2上传剧本自动提取生成角色资产_2081945873101185026.json, 图片生成/文生图/krea2上传剧本自动提取生成角色资产_2082631048692846594.json, 图片生成/文生图/krea2影视资产生成_2080971161210544130.json, 图片生成/文生图/krea2角色资产生成-有剧本即可自动化生成_2081247228685017089.json, 图片生成/文生图/krea2角色资产生成_2081907438109941762.json, 图片生成/文生图/minimax h3-krea2角色资产生成-剧本自动化生成_2094446589719957506.json, 图片生成/文生图/剧本自动提取角色资产｜krea2文生图反推提示词生成_2092597301486379010.json, 图片生成/文生图/文生图-krea2+klein双采多风格通用工作流_2089927009278447618.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/(Krea2+Klein)双K风格化细节增强_2073293647621222402.json、图片生成/文生图/krea2+klein双采多风格通用工作流_2072555688601153538.json、图片生成/文生图/krea2+klein双采多风格通用工作流_2073783289609023490.json、图片生成/文生图/krea2上传剧本自动提取生成角色资产_2081945873101185026.json、图片生成/文生图/krea2上传剧本自动提取生成角色资产_2082631048692846594.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `easy showAnything` —— 10/11 个有
- `Fast Groups Bypasser (rgthree)` —— 9/11 个有
- `ColorMatch` —— 7/11 个有
- `EmptyFlux2LatentImage` —— 7/11 个有
- `ImageScaleToTotalPixels` —— 7/11 个有
- `TTResolutionSelector` —— 7/11 个有
- `RH_LLMAPI_Pro_Node` —— 6/11 个有
- `ColorMatchV2` —— 4/11 个有
- `ImageScaleBy` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `llama_cpp_instruct_adv` —— 4/11 个有
- `llama_cpp_model_loader` —— 4/11 个有
- `Any Switch (rgthree)` —— 3/11 个有
- `LoadImage` —— 3/11 个有
- `ResolutionSelector` —— 3/11 个有
- `llama_cpp_parameters` —— 3/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `OpenAI_Chat_API` —— 1/11 个有
- `QZ_ResolutionPreset` —— 1/11 个有
- `Seed (rgthree)` —— 1/11 个有
- `SimpleMathDual+` —— 1/11 个有
- `solarL_SaveImagesToZip` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 11 | 57% |
| 高度 | 1024 | 80 - 1024 | 11 | 57% |
| 采样步数 | 8 | 4 - 8 | 11 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 11 | 24% |
| 采样算法 | euler | - | 11 | 55% |
| 调度器 | simple | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，11 个样本
- 高度 中位数 1024，观测区间 80 - 1024，11 个样本
- 采样步数 中位数 8，观测区间 4 - 8，11 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，11 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，11 个样本，一致性 55%
- 调度器 最常用 simple，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足

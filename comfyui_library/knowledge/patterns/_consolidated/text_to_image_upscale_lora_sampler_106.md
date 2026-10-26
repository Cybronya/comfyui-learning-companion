---
name: text_to_image_upscale_lora_sampler_106
type: Text To Image
frequency: 3
level: moderate
coverage: 0.824667
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/影视级场景资产工作流（开源版）_2048266987880587265.json, 图片生成/文生图/影视级角色资产工作流（开源版）_2047695377284993025.json, 图片生成/文生图/影视级道具资产工作流（开源版）_2049490901575143425.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/影视级场景资产工作流（开源版）_2048266987880587265.json、图片生成/文生图/影视级角色资产工作流（开源版）_2047695377284993025.json、图片生成/文生图/影视级道具资产工作流（开源版）_2049490901575143425.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `AdaptiveLongestEdge_EditUtils` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `CropWithPadInfo_EditUtils` —— 1/3 个有
- `EditTextEncode_EditUtils` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Resize Factor (mtb)` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `QwenConfigPreparer_EditUtils` —— 1/3 个有
- `QwenEditOutputExtractor_EditUtils` —— 1/3 个有
- `QwenModelConfig_EditUtils` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 3 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 3 | 65% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1920 | 1080 - 1920 | 3 | 76% |
| 高度 | 1080 | 1080 - 1920 | 3 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，3 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1080 - 1920，3 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足

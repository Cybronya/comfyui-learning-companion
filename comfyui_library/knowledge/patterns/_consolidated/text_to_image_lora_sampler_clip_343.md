---
name: text_to_image_lora_sampler_clip_343
type: Text To Image
frequency: 6
level: moderate
coverage: 0.931333
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, ImageConcatMulti, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 4模型贞贞对比_2013662502973874178.json, 图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 5模型贞贞对比_2016756560374013954.json, 图片生成/文生图/Qwen2512 Vs Qwen Old Vs Z-image Turbo智能扩写对比工作流_2006323246228054018.json, 图片生成/文生图/Qwen2512 Vs Z-image Turbo 智能扩写对比工作流 浮云 1.3_2007011244896690178.json, 图片生成/文生图/Qwen2512⚡️Qwen Old⚡️Z-image Turbo 图像质量对比工作流_2006405378501779458.json, 图片生成/文生图/Qwen_2512_Qwen_Old _Z-image Turbo对比工作流_2006543899233357826.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_343

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 4模型贞贞对比_2013662502973874178.json、图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 5模型贞贞对比_2016756560374013954.json、图片生成/文生图/Qwen2512 Vs Qwen Old Vs Z-image Turbo智能扩写对比工作流_2006323246228054018.json、图片生成/文生图/Qwen2512 Vs Z-image Turbo 智能扩写对比工作流 浮云 1.3_2007011244896690178.json、图片生成/文生图/Qwen2512⚡️Qwen Old⚡️Z-image Turbo 图像质量对比工作流_2006405378501779458.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `ImageConcatMulti`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 5/6 个有
- `UnetLoaderGGUF` —— 5/6 个有
- `CFGNorm` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `easy promptLine` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `EmptyFlux2LatentImage` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `PDIMAGE_LongerSize` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `AspectRatio` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 904 | 720 - 1080 | 6 | 84% |
| 高度 | 1600 | 1280 - 1920 | 6 | 84% |
| 采样步数 | 9 | 8 - 50 | 6 | 12% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | res_2s | - | 6 | 50% |
| 调度器 | beta57 | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 904，观测区间 720 - 1080，6 个样本，取值集中（一致性 84%）
- 高度 中位数 1600，观测区间 1280 - 1920，6 个样本，取值集中（一致性 84%）
- 采样步数 中位数 9，观测区间 8 - 50，6 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 res_2s，6 个样本，一致性 50%
- 调度器 最常用 beta57，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足

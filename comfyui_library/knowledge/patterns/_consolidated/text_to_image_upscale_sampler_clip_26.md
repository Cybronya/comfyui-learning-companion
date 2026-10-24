---
name: text_to_image_upscale_sampler_clip_26
type: Text To Image
frequency: 3
level: moderate
coverage: 0.849333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, INTConstant, ImageScaleToTotalPixels, KSampler, PreviewAny, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2  3.8反推_2092915740558053377.json, 图片生成/图生图/实用工具-Qwen3.8图片反推+洗图_2090832571054772226.json, 图片生成/文生图/啊癫 krea2 人物多角度4视图_2091908917856129025.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Krea2  3.8反推_2092915740558053377.json、图片生成/图生图/实用工具-Qwen3.8图片反推+洗图_2090832571054772226.json、图片生成/文生图/啊癫 krea2 人物多角度4视图_2091908917856129025.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `KSampler`
- `PreviewAny`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `Text` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `WujiCleaner` —— 1/3 个有
- `easy saveText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1560 | 3 | 59% |
| 高度 | 1536 | 512 - 2440 | 3 | 47% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1560，3 个样本
- 高度 中位数 1536，观测区间 512 - 2440，3 个样本，取值分散，一致性仅 47%
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

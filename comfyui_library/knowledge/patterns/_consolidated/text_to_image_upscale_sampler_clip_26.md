---
name: text_to_image_upscale_sampler_clip_26
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8512
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 MIX融合版 东方审美 高清直出工作流_2070837337231282177.json, 图片生成/文生图/Krea2-真人角色4K文生图_2095131210359074818.json, 图片生成/文生图/Krea2文生图-天宫中式巨构_2097024511869804546.json, 图片生成/文生图/影视级场景资产工作流（开源版）_2048266987880587265.json, 图片生成/文生图/影视级道具资产工作流（开源版）_2049490901575143425.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Krea 2 MIX融合版 东方审美 高清直出工作流_2070837337231282177.json、图片生成/文生图/Krea2-真人角色4K文生图_2095131210359074818.json、图片生成/文生图/Krea2文生图-天宫中式巨构_2097024511869804546.json、图片生成/文生图/影视级场景资产工作流（开源版）_2048266987880587265.json、图片生成/文生图/影视级道具资产工作流（开源版）_2049490901575143425.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `llama_cpp_instruct_adv` —— 3/5 个有
- `llama_cpp_model_loader` —— 3/5 个有
- `AddLabel` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `QZ_ResolutionPreset` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `DuckDecodeNode` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1920 | 5 | 52% |
| 高度 | 1080 | 512 - 1280 | 5 | 74% |
| 采样步数 | 9 | 8 - 25 | 5 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 5 | 69% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1920，5 个样本
- 高度 中位数 1080，观测区间 512 - 1280，5 个样本
- 采样步数 中位数 9，观测区间 8 - 25，5 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足

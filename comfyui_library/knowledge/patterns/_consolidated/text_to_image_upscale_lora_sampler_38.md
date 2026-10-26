---
name: text_to_image_upscale_lora_sampler_38
type: Text To Image
frequency: 7
level: moderate
coverage: 0.932429
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-双采样latent放大直出4K超清-自动扩写提示词_2075861775614038018.json, 图片生成/文生图/Krea2-双采样latent放大直出4K超清_2075937369521475586.json, 图片生成/文生图/Krea2-手动提示词+seedVr2超清8K放大_2071971991279718401.json, 图片生成/文生图/Krea2-提示词自动扩写（汉服电影）+seedVr2超清8K放大_2072005157788930050.json, 图片生成/文生图/Krea2-提示词自动扩写（通用）+seedVr2超清8K放大_2071983007401074690.json, 图片生成/文生图/Krea2-深度控制洗图+二次采样极致细节-controlnet图生图-二采直出4K_2075582967837192194.json, 图片生成/文生图/krea2-深度控制洗图-图生图-动作迁移-controlnet-画风互转_2075498402560954369.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Krea2-双采样latent放大直出4K超清-自动扩写提示词_2075861775614038018.json、图片生成/文生图/Krea2-双采样latent放大直出4K超清_2075937369521475586.json、图片生成/文生图/Krea2-手动提示词+seedVr2超清8K放大_2071971991279718401.json、图片生成/文生图/Krea2-提示词自动扩写（汉服电影）+seedVr2超清8K放大_2072005157788930050.json、图片生成/文生图/Krea2-提示词自动扩写（通用）+seedVr2超清8K放大_2071983007401074690.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `ConditioningKrea2Rebalance` —— 3/7 个有
- `DisTorchPurgeVRAMV2` —— 3/7 个有
- `LatentUpscaleBy` —— 3/7 个有
- `RHLLMChatNode` —— 3/7 个有
- `TTResolutionSelector` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `DepthAnythingV2Preprocessor` —— 2/7 个有
- `Krea2ControlApply` —— 2/7 个有
- `Krea2ControlImageEncode` —— 2/7 个有
- `Krea2ControlLoRALoader` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `Qwen3_VQA` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 7 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.4 - 1 | 7 | 77% |
| 宽度 | 1024 | 512 - 1080 | 7 | 67% |
| 高度 | 1536 | 512 - 1920 | 7 | 49% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，7 个样本
- 宽度 中位数 1024，观测区间 512 - 1080，7 个样本
- 高度 中位数 1536，观测区间 512 - 1920，7 个样本，取值分散，一致性仅 49%
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足

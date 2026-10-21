---
name: text_to_image_lora_sampler_clip_102
type: Text To Image
frequency: 10
level: weak
coverage: 0.8745
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-双采样latent放大直出4K超清-自动扩写提示词_2075861775614038018.json, 图片生成/文生图/Krea2-双采样latent放大直出4K超清_2075937369521475586.json, 图片生成/文生图/Krea2-手动提示词+seedVr2超清8K放大_2071971991279718401.json, 图片生成/文生图/Krea2-提示词自动扩写（汉服电影）+seedVr2超清8K放大_2072005157788930050.json, 图片生成/文生图/Krea2-提示词自动扩写（通用）+seedVr2超清8K放大_2071983007401074690.json, 图片生成/文生图/Krea2-深度控制洗图+二次采样极致细节-controlnet图生图-二采直出4K_2075582967837192194.json, 图片生成/文生图/Krea2深度控制+双重调节细节加强文生图2K版V2_2074865088221237249.json, 图片生成/文生图/Krea2深度控制人物+节点51和70自定义人物lora+全节点注释_2082965427004723202.json, 图片生成/文生图/krea2-深度控制洗图-图生图-动作迁移-controlnet-画风互转_2075498402560954369.json, 图片生成/文生图/（贞贞版）Krea2深度控制+双重调节细节加强文生图2K版V2_2074766270821654529.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Krea2-双采样latent放大直出4K超清-自动扩写提示词_2075861775614038018.json、图片生成/文生图/Krea2-双采样latent放大直出4K超清_2075937369521475586.json、图片生成/文生图/Krea2-手动提示词+seedVr2超清8K放大_2071971991279718401.json、图片生成/文生图/Krea2-提示词自动扩写（汉服电影）+seedVr2超清8K放大_2072005157788930050.json、图片生成/文生图/Krea2-提示词自动扩写（通用）+seedVr2超清8K放大_2071983007401074690.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 8/10 个有
- `SeedVR2LoadDiTModel` —— 7/10 个有
- `SeedVR2LoadVAEModel` —— 7/10 个有
- `SeedVR2VideoUpscaler` —— 7/10 个有
- `easy int` —— 7/10 个有
- `CR Text` —— 6/10 个有
- `ConditioningKrea2Rebalance` —— 6/10 个有
- `LatentUpscaleBy` —— 6/10 个有
- `CR Prompt Text` —— 5/10 个有
- `Krea2ControlApply` —— 5/10 个有
- `Krea2ControlImageEncode` —— 5/10 个有
- `Krea2ControlLoRALoader` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `LoadImage` —— 5/10 个有
- `PreviewImage` —— 5/10 个有
- `Qwen3_VQA` —— 5/10 个有
- `AIO_Preprocessor` —— 3/10 个有
- `DisTorchPurgeVRAMV2` —— 3/10 个有
- `Float` —— 3/10 个有
- `ImageConcanate` —— 3/10 个有
- `RHLLMChatNode` —— 3/10 个有
- `TTResolutionSelector` —— 3/10 个有
- `TextConcat` —— 3/10 个有
- `DepthAnythingV2Preprocessor` —— 2/10 个有
- `DuckHideNode` —— 2/10 个有
- `JjkText` —— 1/10 个有
- `solarL_SaveImagesToZip` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 10 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 10 | 22% |
| 采样算法 | er_sde | - | 10 | 70% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 0.3 - 1 | 10 | 62% |
| 宽度 | 1024 | 80 - 1080 | 10 | 57% |
| 高度 | 1536 | 80 - 1920 | 10 | 44% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，10 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，10 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 er_sde，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，10 个样本
- 宽度 中位数 1024，观测区间 80 - 1080，10 个样本
- 高度 中位数 1536，观测区间 80 - 1920，10 个样本，取值分散，一致性仅 44%
- 高发问题（17/10 个样本）：Steps较低可能导致细节不足

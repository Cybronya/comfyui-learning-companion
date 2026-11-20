---
name: text_to_image_lora_sampler_clip_236
type: Text To Image
frequency: 8
level: strong
coverage: 0.898375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea2局部重绘PS版本，风格化反推提示词图生图精准区域编辑工具_2103567391509794817.json, 图片生成/反推提示词/Moss Image SFT重绘洗图 自动反推提示词图生图处理工具_2113317132820901889.json, 图片生成/反推提示词/Moss Image SFT重绘洗图三合一，文生图自动反推提示词省心_2114502604238704642.json, 图片生成/反推提示词/Moss Image SFT重绘洗图｜文生图自动反推提示词图生图三合一_2114272477919666178.json, 图片生成/图生图/Flux2 Klein服装精修 去褶皱版型3D立体质感处理工具_2113369997715263489.json, 图片生成/图生图/Moss Image SFT重绘洗图 自动反推提示词处理工具_2113784055333474306.json, 图片生成/图生图/Moss_Image_SFT重绘洗图三合一，文生图自动反推提示词省心_2115964223204450305.json, 图片生成/图生图/Moss_Image_SFT重绘洗图三合一，文生图自动反推提示词省心_2116016308050546690.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_236

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Krea2局部重绘PS版本，风格化反推提示词图生图精准区域编辑工具_2103567391509794817.json、图片生成/反推提示词/Moss Image SFT重绘洗图 自动反推提示词图生图处理工具_2113317132820901889.json、图片生成/反推提示词/Moss Image SFT重绘洗图三合一，文生图自动反推提示词省心_2114502604238704642.json、图片生成/反推提示词/Moss Image SFT重绘洗图｜文生图自动反推提示词图生图三合一_2114272477919666178.json、图片生成/图生图/Flux2 Klein服装精修 去褶皱版型3D立体质感处理工具_2113369997715263489.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 7/8 个有
- `Float` —— 7/8 个有
- `Int` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `llama_cpp_instruct_adv` —— 6/8 个有
- `llama_cpp_model_loader` —— 6/8 个有
- `孤海注释` —— 6/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `KSamplerAdvanced` —— 1/8 个有
- `LayerMask: BiRefNetUltraV2` —— 1/8 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/8 个有
- `ReferenceLatent` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足

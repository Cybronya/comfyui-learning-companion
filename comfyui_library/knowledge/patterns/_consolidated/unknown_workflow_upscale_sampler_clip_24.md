---
name: unknown_workflow_upscale_sampler_clip_24
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.91175
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人像高清【supir+脸部模型+增加纹理】_1938506337967865858.json, 图片生成/图生图/皮肤细节优化_1978758438199119874.json, 图片生成/图生图/皮肤质感丨皮肤纹理丨皮肤细节丨高清还原！！！_1983089936633110530.json, 图片生成/图生图/皮肤质感还原-高清修复_1978639859789221889.json, 图片生成/图生图/真人皮肤质感生成工作流_1928828118797074433.json, 平台全量/AI增加肤质-发布_1945745982913126401.json, 平台全量/人像双重放大增加质感不变形_1921829923848388609.json, 平台全量/皮肤质感极致增强_1985999449459761154.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/人像高清【supir+脸部模型+增加纹理】_1938506337967865858.json、图片生成/图生图/皮肤细节优化_1978758438199119874.json、图片生成/图生图/皮肤质感丨皮肤纹理丨皮肤细节丨高清还原！！！_1983089936633110530.json、图片生成/图生图/皮肤质感还原-高清修复_1978639859789221889.json、图片生成/图生图/真人皮肤质感生成工作流_1928828118797074433.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `easy int` —— 7/8 个有
- `PreviewImage` —— 6/8 个有
- `ColorAdjust(FaceParsing)` —— 5/8 个有
- `ReActorRestoreFace` —— 5/8 个有
- `DualCLIPLoader` —— 4/8 个有
- `VAELoader` —— 4/8 个有
- `ModelSamplingFlux` —— 3/8 个有
- `UNETLoader` —— 3/8 个有
- `UltimateSDUpscale` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageSharpen` —— 1/8 个有
- `Int` —— 1/8 个有
- `UltimateSDUpscaleNoUpscale` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `easy imageColorMatch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 8 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 8 | 71% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | kl_optimal | - | 8 | 88% |
| 重绘幅度 | 0.3 | 0.25 - 0.4 | 8 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 8/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，8 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 kl_optimal，8 个样本，一致性 88%
- 重绘幅度 中位数 0.3，观测区间 0.25 - 0.4，8 个样本，取值集中（一致性 83%）
- 高发问题（8/8 个样本）：发现KSampler但没有VAEDecode
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足

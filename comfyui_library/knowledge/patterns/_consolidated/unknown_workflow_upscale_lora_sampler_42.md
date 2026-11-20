---
name: unknown_workflow_upscale_lora_sampler_42
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9292
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled, easy int]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/人像高清【supir+脸部模型+增加纹理】_1938506337967865858.json, 图片生成/图生图/皮肤细节优化_1978758438199119874.json, 图片生成/图生图/皮肤质感丨皮肤纹理丨皮肤细节丨高清还原！！！_1983089936633110530.json, 图片生成/图生图/皮肤质感还原-高清修复_1978639859789221889.json, 图片生成/图生图/真人皮肤质感生成工作流_1928828118797074433.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人像高清【supir+脸部模型+增加纹理】_1938506337967865858.json、图片生成/图生图/皮肤细节优化_1978758438199119874.json、图片生成/图生图/皮肤质感丨皮肤纹理丨皮肤细节丨高清还原！！！_1983089936633110530.json、图片生成/图生图/皮肤质感还原-高清修复_1978639859789221889.json、图片生成/图生图/真人皮肤质感生成工作流_1928828118797074433.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `VAELoader` —— 4/5 个有
- `ModelSamplingFlux` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `UltimateSDUpscale` —— 3/5 个有
- `ColorAdjust(FaceParsing)` —— 2/5 个有
- `ReActorRestoreFace` —— 2/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | kl_optimal | - | 5 | 100% |
| 重绘幅度 | 0.4 | 0.3 - 0.4 | 5 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 kl_optimal，5 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.3 - 0.4，5 个样本，取值集中（一致性 86%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode

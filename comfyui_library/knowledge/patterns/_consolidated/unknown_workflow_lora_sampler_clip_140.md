---
name: unknown_workflow_lora_sampler_clip_140
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83425
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, CheckpointLoaderSimple, DualCLIPLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/去AI感图像质感优化 加强脸部纹理_1954441094429863937.json, 图片生成/图生图/增加人物皮肤细节去AI感｜Flux krea_1986777700302057473.json, 图片生成/图生图/提升皮肤质感（精修人物皮肤去除AI味）_1990766340678033410.json, 图片生成/图生图/消除 AI 感人像皮肤 细腻皮肤｜一键生成_1933848354814087170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_140

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/去AI感图像质感优化 加强脸部纹理_1954441094429863937.json、图片生成/图生图/增加人物皮肤细节去AI感｜Flux krea_1986777700302057473.json、图片生成/图生图/提升皮肤质感（精修人物皮肤去除AI味）_1990766340678033410.json、图片生成/图生图/消除 AI 感人像皮肤 细腻皮肤｜一键生成_1933848354814087170.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UpscaleModelLoader` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `UltimateSDUpscale` —— 2/4 个有
- `GetNode` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `SUPIR_tiles` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

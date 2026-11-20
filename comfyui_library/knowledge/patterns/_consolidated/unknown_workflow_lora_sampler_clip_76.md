---
name: unknown_workflow_lora_sampler_clip_76
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.861667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, CheckpointLoaderSimple, DualCLIPLoader, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/27removealimage_2049447688550223873.json, 图片生成/图生图/去AI感-增加皮肤质感_1956564091567525890.json, 图片生成/图生图/去AI感图像质感优化 加强脸部纹理_1954441094429863937.json, 图片生成/图生图/增加人物皮肤细节去AI感｜Flux krea_1986777700302057473.json, 图片生成/图生图/提升皮肤质感（精修人物皮肤去除AI味）_1990766340678033410.json, 图片生成/图生图/消除 AI 感人像皮肤 细腻皮肤｜一键生成_1933848354814087170.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/27removealimage_2049447688550223873.json、图片生成/图生图/去AI感-增加皮肤质感_1956564091567525890.json、图片生成/图生图/去AI感图像质感优化 加强脸部纹理_1954441094429863937.json、图片生成/图生图/增加人物皮肤细节去AI感｜Flux krea_1986777700302057473.json、图片生成/图生图/提升皮肤质感（精修人物皮肤去除AI味）_1990766340678033410.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
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
- `Image Comparer (rgthree)` —— 5/6 个有
- `UpscaleModelLoader` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `UltimateSDUpscale` —— 3/6 个有
- `ImageResize+` —— 2/6 个有
- `ImpactInt` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `SUPIR_tiles` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 0.8 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）

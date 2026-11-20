---
name: unknown_workflow_controlnet_upscale_lora_4
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8768
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, Image Comparer (rgthree), ImageBlend, ImageResize+, ImpactInt, LoadImage, LoraLoader, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, Seed_, UltimateSDUpscale, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/人像高清放大高分辨率_2062014292223942658.json, 平台全量/一键高清放大_1915215634114740226.json, 平台全量/人像高清放大高分辨率_2058514632129732609.json, 平台全量/人像高清放大（高分辨率）_2049514936056942593.json, 平台全量/完美SUPIR高清放大_1977309423263731713.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人像高清放大高分辨率_2062014292223942658.json、平台全量/一键高清放大_1915215634114740226.json、平台全量/人像高清放大高分辨率_2058514632129732609.json、平台全量/人像高清放大（高分辨率）_2049514936056942593.json、平台全量/完美SUPIR高清放大_1977309423263731713.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `ImageResize+`
- `ImpactInt`
- `LoadImage`
- `LoraLoader`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `Seed_`
- `UltimateSDUpscale`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.35 | 0.35 - 0.35 | 5 | 100% |
| LoRA 模型强度 | 0.2 | 0.2 - 0.3 | 5 | 82% |
| LoRA 文本强度 | 0 | 0 - 0 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.35，观测区间 0.35 - 0.35，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.2，观测区间 0.2 - 0.3，5 个样本，取值集中（一致性 82%）
- LoRA 文本强度 中位数 0，观测区间 0 - 0，5 个样本，取值集中（一致性 100%）

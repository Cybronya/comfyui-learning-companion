---
name: unknown_workflow_upscale_clip_checkpoint_2
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.868
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), ImageResize+, ImageUpscaleWithModel, LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.Krea半身模糊变清晰_1937332253624049665.json, 图片生成/图生图/高清放大_修复_2038651650352619521.json, 图片生成/图生图/🦁【实用工具】人像皮肤4K超清放大流🦁_1944938430025617409.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX.Krea半身模糊变清晰_1937332253624049665.json、图片生成/图生图/高清放大_修复_2038651650352619521.json、图片生成/图生图/🦁【实用工具】人像皮肤4K超清放大流🦁_1944938430025617409.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `LoadImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `UltimateSDUpscaleNoUpscale` —— 2/3 个有
- `easy int` —— 2/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `ColorMatch` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImitationHueNode` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuTextEncoderLoaderV2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SUPIR_Upscale` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_upscale_vae_65
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5605
common_nodes: [Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, MuyeTextEditOutput, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/全能图片G--image-2.0 RH平台廉价版api调用  0.1_次_2047868011910012930.json, 图片生成/文生图/全能图片G--image-2.0 官方稳定版 api 调用_2048948080573161474.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_65

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/全能图片G--image-2.0 RH平台廉价版api调用  0.1_次_2047868011910012930.json、图片生成/文生图/全能图片G--image-2.0 官方稳定版 api 调用_2048948080573161474.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `MuyeTextEditOutput`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text`
- `easy int`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/2 个有
- `RH_RhartImageG2OfficialTextToImage` —— 1/2 个有
- `RH_RhartImageG2TextToImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

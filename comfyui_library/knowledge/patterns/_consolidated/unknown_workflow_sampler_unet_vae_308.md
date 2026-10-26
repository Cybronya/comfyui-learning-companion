---
name: unknown_workflow_sampler_unet_vae_308
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPLoader, ConstrainImage|pysssss, ImpactInt, KSamplerSelect, LayerUtility: ExtendCanvasV2, LoadImage, ManualSigmas, SamplerCustom, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein_亚秒级自然无缝扩图_2087363520521396225.json, 图片生成/图生图/qwen_image_2.1自然无缝扩图_2087728590073978882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_308

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Klein_亚秒级自然无缝扩图_2087363520521396225.json、图片生成/图生图/qwen_image_2.1自然无缝扩图_2087728590073978882.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConstrainImage|pysssss`
- `ImpactInt`
- `KSamplerSelect`
- `LayerUtility: ExtendCanvasV2`
- `LoadImage`
- `ManualSigmas`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

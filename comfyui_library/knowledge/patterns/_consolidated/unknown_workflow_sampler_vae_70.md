---
name: unknown_workflow_sampler_vae_70
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.951667
common_nodes: [BasicGuider, BasicScheduler, DisableNoise, FlipSigmas, FluxForwardODESampler, FluxReverseODESampler, Image Comparer (rgthree), InFluxModelSamplingPred, LoadImage, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/flux万物精修_1911956945350160385.json, 平台全量/最快nunchaku-flux万物精修，重塑_1938586397664333825.json, 平台全量/熨烫工作流（逆采样技术）_1995695007761829890.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_70

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/flux万物精修_1911956945350160385.json、平台全量/最快nunchaku-flux万物精修，重塑_1938586397664333825.json、平台全量/熨烫工作流（逆采样技术）_1995695007761829890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DisableNoise`
- `FlipSigmas`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `Image Comparer (rgthree)`
- `InFluxModelSamplingPred`
- `LoadImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `NunchakuFluxDiTLoader` —— 2/3 个有
- `OutFluxModelSamplingPred` —— 2/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `FluxDeGuidance` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `Int` —— 1/3 个有
- `Joy_caption_two` —— 1/3 个有
- `Joy_caption_two_load` —— 1/3 个有
- `NunchakuTextEncoderLoader` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

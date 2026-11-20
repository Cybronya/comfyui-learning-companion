---
name: unknown_workflow_sampler_clip_vae_60
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84625
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, GetImageSize+, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/🥎Kontext 局部重绘+万物消除【题词优化】🤹_1938850655211544577.json, 图片生成/图生图/🥎Kontext 老照片一键修复+上色🤹_1939498210631270401.json, 图片生成/图生图/🥎kontext多图组合优化方案🤹_1939865850146889730.json, 平台全量/图像编辑 _ Kontext局部重绘_1951636255434027009.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/🥎Kontext 局部重绘+万物消除【题词优化】🤹_1938850655211544577.json、图片生成/图生图/🥎Kontext 老照片一键修复+上色🤹_1939498210631270401.json、图片生成/图生图/🥎kontext多图组合优化方案🤹_1939865850146889730.json、平台全量/图像编辑 _ Kontext局部重绘_1951636255434027009.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `Convert Masks to Images` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Image To Mask` —— 2/4 个有
- `ImageAndMaskPreview` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `easy imageSize` —— 2/4 个有
- `Compositor3` —— 1/4 个有
- `CompositorConfig3` —— 1/4 个有
- `CompositorTools3` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `Get resolution [Crystools]` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `NunchakuFluxDiTLoader` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

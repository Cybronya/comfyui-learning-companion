---
name: unknown_workflow_lora_sampler_clip_133
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.761
common_nodes: [BasicGuider, BasicScheduler, Bounded Image Blend with Mask, Bounded Image Crop with Mask, CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize, Image Comparer (rgthree), Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LayerUtility: BooleanOperatorV2, LayerUtility: If , LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RH_Translator, RandomNoise, ResizeImageMixlab, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/FLUX - 局部重绘 - Webui复刻版_1946901695579189250.json, 图片生成/图生图/FLUX - 局部重绘 - Webui复刻版_1953822021987782658.json, 图片生成/图生图/图片-FLUX - 局部重绘_1960282002446561281.json, 图片生成/图生图/局部重绘（新版优化加强）_1989221305629151234.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_133

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX - 局部重绘 - Webui复刻版_1946901695579189250.json、图片生成/图生图/FLUX - 局部重绘 - Webui复刻版_1953822021987782658.json、图片生成/图生图/图片-FLUX - 局部重绘_1960282002446561281.json、图片生成/图生图/局部重绘（新版优化加强）_1989221305629151234.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `Bounded Image Blend with Mask`
- `Bounded Image Crop with Mask`
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: If `
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Translator`
- `RandomNoise`
- `ResizeImageMixlab`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `Display Int (rgthree)` —— 3/4 个有
- `MaskPreview+` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `easy showAnything` —— 3/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

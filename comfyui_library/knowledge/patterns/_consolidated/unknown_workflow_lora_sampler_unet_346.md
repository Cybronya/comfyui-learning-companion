---
name: unknown_workflow_lora_sampler_unet_346
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.839
common_nodes: [CFGGuider, CLIPLoader, ColorMatch, DrawMaskOnImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImagePadForOutpaint, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MuyeSizeSelector, PainterFluxImageEdit, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/产品换背景+老照片修复+扩图_2112089424862466049.json, 图片生成/图生图/产品换背景+老照片修复+扩图_2116378471340535809.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_346

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品换背景+老照片修复+扩图_2112089424862466049.json、图片生成/图生图/产品换背景+老照片修复+扩图_2116378471340535809.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ColorMatch`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeSizeSelector`
- `PainterFluxImageEdit`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

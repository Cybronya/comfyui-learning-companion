---
name: unknown_workflow_sampler_clip_unet_238
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [AILab_QwenVL, CFGOverride, CLIPLoader, CLIPTextEncode, ComfyNumberConvert, DualModelGuider, Ideogram4OptimizationsKJ, Ideogram4Scheduler, ImageScaleToTotalPixelsX, JsonExtractString, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SplitSigmas, StringReplace, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/ideogram4-文生图-高清画质-400万像素直出_2064169225039728641.json, 图片生成/文生图/ideogram4-文生图-高清画质-400万像素直出_2074309690607095810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_238

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/ideogram4-文生图-高清画质-400万像素直出_2064169225039728641.json、图片生成/文生图/ideogram4-文生图-高清画质-400万像素直出_2074309690607095810.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyNumberConvert`
- `DualModelGuider`
- `Ideogram4OptimizationsKJ`
- `Ideogram4Scheduler`
- `ImageScaleToTotalPixelsX`
- `JsonExtractString`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewAny`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SplitSigmas`
- `StringReplace`
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

---
name: unknown_workflow_sampler_clip_unet_136
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.925556
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570.json, 图片生成/图生图/千府AI-FluxKlein室内风格迁移工作流_2031990406266753026.json, 图片生成/图生图/千府AI-FluxKlein效果图风格转换工作流_2013475853849595906.json, 图片生成/图生图/千府AI-FluxKlein立面风格迁移工作流_2031957779518332929.json, 图片生成/图生图/漫画转欧美美女（解禁模型）：Flux2 Klein 9B_2055197694913720322.json, 图片生成/图生图/老照片修复 -｜Flux-Klein｜底模_2054444918260682753.json, 图片生成/图生图/老照片修复 -｜Flux-Klein｜底模_2069231901122056194.json, 图片生成/图生图/脱衣服穿衣服_2080345607318884353.json, 图片生成/图生图/高清放大_2072576146432159746.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_136

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570.json、图片生成/图生图/千府AI-FluxKlein室内风格迁移工作流_2031990406266753026.json、图片生成/图生图/千府AI-FluxKlein效果图风格转换工作流_2013475853849595906.json、图片生成/图生图/千府AI-FluxKlein立面风格迁移工作流_2031957779518332929.json、图片生成/图生图/漫画转欧美美女（解禁模型）：Flux2 Klein 9B_2055197694913720322.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `GetImageSize` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `ConditioningZeroOut` —— 5/9 个有
- `Anything Everywhere` —— 4/9 个有
- `ModelPatchTorchSettings` —— 4/9 个有
- `ImitationHueNode` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `ImageBlend` —— 1/9 个有
- `ImageColorMatch+` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `JsonPromptNode` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

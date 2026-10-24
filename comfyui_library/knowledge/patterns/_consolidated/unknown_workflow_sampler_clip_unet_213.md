---
name: unknown_workflow_sampler_clip_unet_213
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9335
common_nodes: [CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux2.0图生图_1994969105419657218.json, 图片生成/图生图/flux2_klein双图编辑_2038872372450697217.json, 图片生成/图生图/千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570.json, 图片生成/图生图/千府AI-FluxKlein室内风格迁移工作流_2031990406266753026.json, 图片生成/图生图/千府AI-FluxKlein效果图风格转换工作流_2013475853849595906.json, 图片生成/图生图/千府AI-FluxKlein立面风格迁移工作流_2031957779518332929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_213

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/flux2.0图生图_1994969105419657218.json、图片生成/图生图/flux2_klein双图编辑_2038872372450697217.json、图片生成/图生图/千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570.json、图片生成/图生图/千府AI-FluxKlein室内风格迁移工作流_2031990406266753026.json、图片生成/图生图/千府AI-FluxKlein效果图风格转换工作流_2013475853849595906.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CFGGuider` —— 5/6 个有
- `EmptyFlux2LatentImage` —— 5/6 个有
- `Anything Everywhere` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `ModelPatchTorchSettings` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `ImitationHueNode` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `BasicGuider` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `ImageBlend` —— 1/6 个有
- `JsonPromptNode` —— 1/6 个有
- `Width/Height Literal` —— 1/6 个有
- `Width/Height Literal (Image Saver)` —— 1/6 个有
- `easy imageScaleDown` —— 1/6 个有
- `孤海图像缩放按像素` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

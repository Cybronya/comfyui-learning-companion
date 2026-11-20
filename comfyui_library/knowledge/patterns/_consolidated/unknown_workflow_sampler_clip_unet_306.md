---
name: unknown_workflow_sampler_clip_unet_306
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.996
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/材质迁移工作流：两次同时（目前最强）_2106755242196037633.json, 图片生成/图生图/炉石卡通转换_2093517690102181890.json, 图片生成/图生图/预测女儿长相_2046549583253213186.json, 图片生成/图生图/👾怪獸-Flux2Klein 去水印马赛克👾_2047809913426022401.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_306

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/材质迁移工作流：两次同时（目前最强）_2106755242196037633.json、图片生成/图生图/炉石卡通转换_2093517690102181890.json、图片生成/图生图/预测女儿长相_2046549583253213186.json、图片生成/图生图/👾怪獸-Flux2Klein 去水印马赛克👾_2047809913426022401.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
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
- `LoraLoaderModelOnly` —— 2/4 个有
- `FancyNoteNode` —— 1/4 个有
- `ImageBatch` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `ImageGrid` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `ttN text` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

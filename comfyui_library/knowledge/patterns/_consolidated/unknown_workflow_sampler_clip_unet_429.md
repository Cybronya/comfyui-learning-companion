---
name: unknown_workflow_sampler_clip_unet_429
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.992
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/材质迁移工作流：两次同时（目前最强）_2106755242196037633.json, 图片生成/图生图/预测女儿长相_2046549583253213186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_429

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/材质迁移工作流：两次同时（目前最强）_2106755242196037633.json、图片生成/图生图/预测女儿长相_2046549583253213186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 2 个 workflow 都包含：
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
- `FancyNoteNode` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `ImageGrid` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `ttN text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

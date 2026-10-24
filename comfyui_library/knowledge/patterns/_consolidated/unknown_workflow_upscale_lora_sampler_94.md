---
name: unknown_workflow_upscale_lora_sampler_94
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9025
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ImageResize+, KSamplerSelect, LatentPixelScale, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, Qwen2.5VL, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/z_image_x2放大生产力_2006714840588492802.json, 图片生成/图生图/z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_94

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/z_image_x2放大生产力_2006714840588492802.json、图片生成/图生图/z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResize+`
- `KSamplerSelect`
- `LatentPixelScale`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `Qwen2.5VL`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

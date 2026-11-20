---
name: unknown_workflow_upscale_lora_sampler_78
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.909333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ImageResize+, KSamplerSelect, LatentPixelScale, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, Qwen2.5VL, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/z_image_x2放大生产力_2006714840588492802.json, 图片生成/图生图/z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994.json, 平台全量/z_image_x2放大生产力_2002999205956337666.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/z_image_x2放大生产力_2006714840588492802.json、图片生成/图生图/z_image_x4放大   Novel Board AI API调用专用工作流_2002993912438484994.json、平台全量/z_image_x2放大生产力_2002999205956337666.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `SeedVR2ExtraArgs` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_sampler_unet_vae_255
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.914667
common_nodes: [BasicScheduler, CLIPLoader, EmptySD3LatentImage, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/OmniGen2图像编辑_Comfy官方流_1938893412261093377.json, 图片生成/图生图/image_omnigen2_图片编辑工作流_1939951595721560065.json, 图片生成/图生图/【老金驿站】Qwen双图溶图4步极速工作流_1958780124068016129.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_255

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/OmniGen2图像编辑_Comfy官方流_1938893412261093377.json、图片生成/图生图/image_omnigen2_图片编辑工作流_1939951595721560065.json、图片生成/图生图/【老金驿站】Qwen双图溶图4步极速工作流_1958780124068016129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `EmptySD3LatentImage`
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
- `CFGGuider` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `DualCFGGuider` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

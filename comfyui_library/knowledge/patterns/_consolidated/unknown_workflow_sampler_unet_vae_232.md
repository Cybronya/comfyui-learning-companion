---
name: unknown_workflow_sampler_unet_vae_232
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92525
common_nodes: [BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/OmniGen2图像编辑_Comfy官方流_1938893412261093377.json, 图片生成/图生图/image_omnigen2_图片编辑工作流_1939951595721560065.json, 图片生成/图生图/【老金驿站】Qwen双图溶图4步极速工作流_1958780124068016129.json, 图片生成/图生图/角色正视图和三视图_2100255300451397633.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_232

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/OmniGen2图像编辑_Comfy官方流_1938893412261093377.json、图片生成/图生图/image_omnigen2_图片编辑工作流_1939951595721560065.json、图片生成/图生图/【老金驿站】Qwen双图溶图4步极速工作流_1958780124068016129.json、图片生成/图生图/角色正视图和三视图_2100255300451397633.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
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
- `CFGGuider` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `EmptySD3LatentImage` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `DualCFGGuider` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `JWImageResizeByLongerSide` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

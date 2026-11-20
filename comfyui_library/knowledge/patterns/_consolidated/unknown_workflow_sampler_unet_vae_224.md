---
name: unknown_workflow_sampler_unet_vae_224
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9095
common_nodes: [BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/OmniGen2图像编辑_Comfy官方流_1938893412261093377.json, 图片生成/图生图/image_omnigen2_图片编辑工作流_1939951595721560065.json, 图片生成/图生图/【老金驿站】Qwen双图溶图4步极速工作流_1958780124068016129.json, 图片生成/图生图/角色正视图和三视图_2100255300451397633.json, 平台全量/Y-omnigen2_image_edit_1947465783519629313.json, 平台全量/涂抹图1 指定区域位置大小，放置图2 中的产品_2044033238884163585.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_224

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/OmniGen2图像编辑_Comfy官方流_1938893412261093377.json、图片生成/图生图/image_omnigen2_图片编辑工作流_1939951595721560065.json、图片生成/图生图/【老金驿站】Qwen双图溶图4步极速工作流_1958780124068016129.json、图片生成/图生图/角色正视图和三视图_2100255300451397633.json、平台全量/Y-omnigen2_image_edit_1947465783519629313.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CLIPTextEncode` —— 5/6 个有
- `GetImageSize` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `CFGGuider` —— 4/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `DualCFGGuider` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `EmptyFlux2LatentImage` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `ImageStitch` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `CR SDXL Aspect Ratio` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `PainterNode` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `TextEncodeQwenImageEdit` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

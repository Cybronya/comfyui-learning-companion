---
name: unknown_workflow_sampler_clip_unet_194
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.855429
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSamplerSelect, LoadImage, RFInversion, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UnofficialExtensions, UntwistingRoPE, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein-9b-最强风格迁移_2064327792870907906.json, 图片生成/图生图/z-image-turbo-参考风格生成_2062502317689233409.json, 图片生成/文生图/Untwisting-RoPE：免训练高级图像风格转绘（文生图）_2070058042036670466.json, 图片生成/文生图/flux2_klein_9b ROPE 风格变换 工作流_2062039782582210561.json, 图片生成/文生图/qwen_image_edit_2511 ROPE 风格变换 工作流_2062044303366647809.json, 图片生成/文生图/z_image_turbo-UntwistingROPE 风格变换 工作流_2062027500867383297.json, 图片生成/文生图/【万物皆可转绘】Untwisting RoPE 免训练任意风格迁移_2069064857554604034.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_194

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/klein-9b-最强风格迁移_2064327792870907906.json、图片生成/图生图/z-image-turbo-参考风格生成_2062502317689233409.json、图片生成/文生图/Untwisting-RoPE：免训练高级图像风格转绘（文生图）_2070058042036670466.json、图片生成/文生图/flux2_klein_9b ROPE 风格变换 工作流_2062039782582210561.json、图片生成/文生图/qwen_image_edit_2511 ROPE 风格变换 工作流_2062044303366647809.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `LoadImage`
- `RFInversion`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UnofficialExtensions`
- `UntwistingRoPE`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `ReferenceLatent` —— 3/7 个有
- `ConditioningAddImageReference` —— 2/7 个有
- `ImageScaleBy` —— 2/7 个有
- `Int` —— 2/7 个有
- `GetImageSize` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageScaleToTotalPixelsX` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `TextConcatenate` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

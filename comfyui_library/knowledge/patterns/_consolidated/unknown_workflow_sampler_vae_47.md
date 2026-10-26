---
name: unknown_workflow_sampler_vae_47
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8574
common_nodes: [JoyAI_Image_ENCODER, JoyAI_Image_LATENTS, JoyAI_Image_SM_Clip, JoyAI_Image_SM_KSampler, JoyAI_Image_SM_Model, JoyAI_Image_SM_VAE, JoyAI_Vae_Decoder, LoadImage, PreviewAny, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/JoyAI_Image图像编辑_2042043063824031746.json, 图片生成/图生图/京东编辑模型_2079972499621761026.json, 图片生成/文生图/JoyAI-Image单图编辑_2043308514138918913.json, 图片生成/文生图/JoyAI_Image 图像编辑_2043146539337519106.json, 数字人/数字人/JoyAI_Image图像编辑_2042125972094328834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_47

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/JoyAI_Image图像编辑_2042043063824031746.json、图片生成/图生图/京东编辑模型_2079972499621761026.json、图片生成/文生图/JoyAI-Image单图编辑_2043308514138918913.json、图片生成/文生图/JoyAI_Image 图像编辑_2043146539337519106.json、数字人/数字人/JoyAI_Image图像编辑_2042125972094328834.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `JoyAI_Image_ENCODER`
- `JoyAI_Image_LATENTS`
- `JoyAI_Image_SM_Clip`
- `JoyAI_Image_SM_KSampler`
- `JoyAI_Image_SM_Model`
- `JoyAI_Image_SM_VAE`
- `JoyAI_Vae_Decoder`
- `LoadImage`
- `PreviewAny`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 3/5 个有
- `CR Prompt Text` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `KepStringLiteral` —— 2/5 个有
- `image_scale_pixel_v2` —— 2/5 个有
- `MuyeSizeSelector` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

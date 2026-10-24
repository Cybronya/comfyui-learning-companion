---
name: unknown_workflow_upscale_vae_36
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.628667
common_nodes: [Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/Running-角色定妆设计_2042131439310872578.json, 图片生成/图生图/SeedVR2 高清放大（B站：带你吃火锅）_2065898772965711874.json, 图片生成/图生图/图像放大工作流（SeedVR2.5.1）_2110631951051874305.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_36

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Running-角色定妆设计_2042131439310872578.json、图片生成/图生图/SeedVR2 高清放大（B站：带你吃火锅）_2065898772965711874.json、图片生成/图生图/图像放大工作流（SeedVR2.5.1）_2110631951051874305.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/3 个有
- `LayerUtility: TextJoinV2` —— 1/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `VRAM_Debug` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

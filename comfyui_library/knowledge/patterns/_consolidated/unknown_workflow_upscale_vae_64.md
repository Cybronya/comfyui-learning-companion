---
name: unknown_workflow_upscale_vae_64
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7385
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy forLoopEnd, easy forLoopStart, easy imageScaleDownToSize, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/image-2(多图生成)3.0_2065236904529981441.json, 图片生成/文生图/全能图片G-image2;图像工作流（需接API）_2052969404006187010.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_64

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/image-2(多图生成)3.0_2065236904529981441.json、图片生成/文生图/全能图片G-image2;图像工作流（需接API）_2052969404006187010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageScaleDownToSize`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Comfly_gpt_image_2` —— 1/2 个有
- `ComfyUI_Image_Round__ImageCropAdvanced` —— 1/2 个有
- `ComfyuiZhangyuAPIImage2Node` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `String` —— 1/2 个有
- `easy imageSplitGrid` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

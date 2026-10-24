---
name: unknown_workflow_upscale_vae_60
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8405
common_nodes: [ImageFromBatch+, ImageScaleToTotalPixels, ImageTile+, JoinImageWithAlpha, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy cleanGpuUsed, easy clearCacheAll, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/文生图/AI动画 IMAGE - Workflow V1.0_2027604910757388289.json, 视频生成/文生视频/5.1 工具：拆图+放大_2031785449819217921.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_60

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/AI动画 IMAGE - Workflow V1.0_2027604910757388289.json、视频生成/文生视频/5.1 工具：拆图+放大_2031785449819217921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageFromBatch+`
- `ImageScaleToTotalPixels`
- `ImageTile+`
- `JoinImageWithAlpha`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy imageInsetCrop` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_upscale_vae_34
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8495
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2简单放大_2101433189830057985.json, 图片生成/图生图/Seedvr2高清工作流_2055454834110812162.json, 图片生成/图生图/seedVR2图片高清放大_2032355636960305154.json, 图片生成/图生图/seedvr2 放大_2074418010059788289.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_34

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/SeedVR2简单放大_2101433189830057985.json、图片生成/图生图/Seedvr2高清工作流_2055454834110812162.json、图片生成/图生图/seedVR2图片高清放大_2032355636960305154.json、图片生成/图生图/seedvr2 放大_2074418010059788289.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/4 个有
- `ZML_DualInteger` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

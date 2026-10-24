---
name: unknown_workflow_upscale_vae_35
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.847
common_nodes: [LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/FlashVSR+SeedVR2双重放大_2031676606560870401.json, 图片生成/图生图/SEEDVR2.5 基础放大工作流_2006571587549536258.json, 图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FlashVSR+SeedVR2双重放大_2031676606560870401.json、图片生成/图生图/SEEDVR2.5 基础放大工作流_2006571587549536258.json、图片生成/图生图/SEEDVR2放大 图像放大到2K  接入SD-PPP实现 SEEDVR2.5放大_2073377648025358338.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

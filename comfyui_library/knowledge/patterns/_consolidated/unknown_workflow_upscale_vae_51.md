---
name: unknown_workflow_upscale_vae_51
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.454
common_nodes: [Image Comparer (rgthree), LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode]
problems: []
missing: []
members: [图片生成/图生图/短剧人物转三视图（基于你的参考图生成「正面 _ 侧面 _ 背面」三视角色设定图）_2087107240661708802.json, 平台全量/要发布的10--三视_2089170369595924481.json, 平台全量/高清修复V2加强版（完美还原原始图片的细节）_2005532213741584385.json, 平台全量/高清修复_2006323404256845826.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_51

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/短剧人物转三视图（基于你的参考图生成「正面 _ 侧面 _ 背面」三视角色设定图）_2087107240661708802.json、平台全量/要发布的10--三视_2089170369595924481.json、平台全量/高清修复V2加强版（完美还原原始图片的细节）_2005532213741584385.json、平台全量/高清修复_2006323404256845826.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 4 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `RH_RhartImageG2ImageToImage` —— 2/4 个有
- `easy imageSizeBySide` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

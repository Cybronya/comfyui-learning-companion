---
name: unknown_workflow_controlnet
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7575
common_nodes: [ControlNetLoader, LoadImage, PreviewImage, SaveImage, workflow/CLIP Text Encode (Prompt), workflow/face, workflow/instantID, workflow/instantID FACE, workflow/mask, workflow/sam, workflow/采样]
problems: []
missing: []
members: [图片生成/图生图/一键极速无损换脸_1889248467305357313.json, 平台全量/哪吒2一键换脸熬闰_1888138718698430466.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键极速无损换脸_1889248467305357313.json、平台全量/哪吒2一键换脸熬闰_1888138718698430466.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `ControlNetLoader`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `workflow/CLIP Text Encode (Prompt)`
- `workflow/face`
- `workflow/instantID`
- `workflow/instantID FACE`
- `workflow/mask`
- `workflow/sam`
- `workflow/采样`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `workflow/模型组` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

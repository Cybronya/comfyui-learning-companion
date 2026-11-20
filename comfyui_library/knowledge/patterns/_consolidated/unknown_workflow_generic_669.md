---
name: unknown_workflow_generic_669
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88125
common_nodes: [ImageStitch, LoadImage, SaveImage]
problems: []
missing: []
members: [comfyui-workflow-templates-json/api_bfl_flux_1_kontext_max_image.json, comfyui-workflow-templates-json/utility_image_stitch.json, 图片生成/文生图/三图缝合（2个参考图）一个分镜图_2005203215652188161.json, 图片生成/文生图/双图拼接缝合_2001537601662271489.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_669

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/api_bfl_flux_1_kontext_max_image.json、comfyui-workflow-templates-json/utility_image_stitch.json、图片生成/文生图/三图缝合（2个参考图）一个分镜图_2005203215652188161.json、图片生成/文生图/双图拼接缝合_2001537601662271489.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageStitch`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMaxImageNode` —— 1/4 个有
- `ResizeImageMaskNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

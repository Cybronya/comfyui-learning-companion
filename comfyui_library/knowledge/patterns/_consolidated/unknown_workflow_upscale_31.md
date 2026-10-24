---
name: unknown_workflow_upscale_31
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.944333
common_nodes: [ImageUpscaleWithModel, LoadImage, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/普通放大--不透明1011_2109121126667476994.json, 图片生成/图生图/超分+加噪声增加真实度_1981305628402638849.json, 图片生成/图生图/高清放大_基础版_2068227997240479746.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_31

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/普通放大--不透明1011_2109121126667476994.json、图片生成/图生图/超分+加噪声增加真实度_1981305628402638849.json、图片生成/图生图/高清放大_基础版_2068227997240479746.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `LayerFilter: AddGrain` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

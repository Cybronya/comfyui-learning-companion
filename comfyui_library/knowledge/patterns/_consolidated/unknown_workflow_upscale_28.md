---
name: unknown_workflow_upscale_28
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7278
common_nodes: [ImageUpscaleWithModel, LoadImage, PreviewImage, UpscaleModelLoader]
problems: []
missing: []
members: [平台全量/4xNomos調度器放大_1822622656821923842.json, 平台全量/ComfyUI官方示例5：Upscale工作流详解 _ ComfyUI从入门到精通_1931676914157858817.json, 平台全量/SUPIR高清放大_2005576164875923457.json, 平台全量/reactor换脸_1978365341933920258.json, 平台全量/基础超分算法（模型放大）工作流_2057721244753154050.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/4xNomos調度器放大_1822622656821923842.json、平台全量/ComfyUI官方示例5：Upscale工作流详解 _ ComfyUI从入门到精通_1931676914157858817.json、平台全量/SUPIR高清放大_2005576164875923457.json、平台全量/reactor换脸_1978365341933920258.json、平台全量/基础超分算法（模型放大）工作流_2057721244753154050.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `PreviewImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ReActorFaceSwap` —— 1/5 个有
- `SUPIR_Upscale` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

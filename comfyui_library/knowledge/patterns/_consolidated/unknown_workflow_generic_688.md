---
name: unknown_workflow_generic_688
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.677
common_nodes: [HAIGC_LoadImagesFromZip, HAIGC_SaveImagesToZip, ImageScaleToTotalPixels, PreviewImage, easy forLoopEnd, easy forLoopStart, easy imageCount, easy saveText]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3.5_图片批量打标_2037249054605844482.json, 图片生成/反推提示词/qwen3.5批量快速批量打标_2042200295891017730.json, 图片生成/反推提示词/图片批量打标_2041441041722646530.json, 图片生成/文生图/图片批量打标_2034228470494011393.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_688

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/Qwen3.5_图片批量打标_2037249054605844482.json、图片生成/反推提示词/qwen3.5批量快速批量打标_2042200295891017730.json、图片生成/反推提示词/图片批量打标_2041441041722646530.json、图片生成/文生图/图片批量打标_2034228470494011393.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `HAIGC_LoadImagesFromZip`
- `HAIGC_SaveImagesToZip`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 3/4 个有
- `RH_BatchImages` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `llama_cpp_parameters` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `RHBatchImages:` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

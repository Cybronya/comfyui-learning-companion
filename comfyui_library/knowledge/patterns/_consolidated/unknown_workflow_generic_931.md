---
name: unknown_workflow_generic_931
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.827
common_nodes: [LoadImage, PreviewAny, SaveImage, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/反推提示词/反推提示词再生成新的_2048962009487646721.json, 图片生成/文生图/G2+ Gemma 4 替你写生图提示词！_2048327820568432642.json, 视频生成/文生视频/反推重绘_2047964125099204609.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_931

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/反推提示词再生成新的_2048962009487646721.json、图片生成/文生图/G2+ Gemma 4 替你写生图提示词！_2048327820568432642.json、视频生成/文生视频/反推重绘_2047964125099204609.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2TextToImage` —— 2/3 个有
- `easy saveText` —— 2/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

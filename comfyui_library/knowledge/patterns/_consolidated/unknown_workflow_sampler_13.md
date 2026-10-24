---
name: unknown_workflow_sampler_13
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.856
common_nodes: [EligenArgsConcat, LoadImage, LoadQwenImageDiffSynthiPipe, MaskToImage, PreviewImage, PrimitiveStringMultiline, QwenImageDiffSynthSampler, SaveImage, SetEligenArgs]
problems: []
missing: []
members: [图片生成/文生图/Eligen自由画布工作流48GB显存版要点“运行Plus”_1953929861947805698.json, 图片生成/文生图/Eligen自由画布工作流_1955090857663893506.json, 图片生成/文生图/Qwen-Image-EliGen 日拱一卒 封面生成_1958077760537317377.json, 图片生成/文生图/Qwen-Image-EliGen自由画布工作流V1_1954036823100313601.json, 图片生成/文生图/Qwen-Image-EliGen自由画布工作流V2（贞贞lora版）_1954578900275884034.json, 图片生成/文生图/Qwen千问Eligen自由设计画布_1954024086618066945.json, 图片生成/文生图/指哪画哪！Qwen-Image自由画布eligen_1955738055426674689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_13

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Eligen自由画布工作流48GB显存版要点“运行Plus”_1953929861947805698.json、图片生成/文生图/Eligen自由画布工作流_1955090857663893506.json、图片生成/文生图/Qwen-Image-EliGen 日拱一卒 封面生成_1958077760537317377.json、图片生成/文生图/Qwen-Image-EliGen自由画布工作流V1_1954036823100313601.json、图片生成/文生图/Qwen-Image-EliGen自由画布工作流V2（贞贞lora版）_1954578900275884034.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `EligenArgsConcat`
- `LoadImage`
- `LoadQwenImageDiffSynthiPipe`
- `MaskToImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImageDiffSynthSampler`
- `SaveImage`
- `SetEligenArgs`

**可变部分**（部分 workflow 才有）：
- `QwenImageRatio2Size` —— 6/7 个有
- `LoadQwenImageDiffSynthLora` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `CR Text` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `SetMultiEligenArgs` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

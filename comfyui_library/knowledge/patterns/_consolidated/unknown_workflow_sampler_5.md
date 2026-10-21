---
name: unknown_workflow_sampler_5
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.750571
common_nodes: [EligenArgsConcat, LoadImage, LoadQwenImageDiffSynthiPipe, MaskToImage, PreviewImage, PrimitiveStringMultiline, QwenImageDiffSynthSampler, SaveImage, SetEligenArgs]
problems: []
missing: [CR Text, easy cleanGpuUsed, CR Prompt Text]
members: [图片生成/文生图/1953929861947805698.json, 图片生成/文生图/1954024086618066945.json, 图片生成/文生图/1954036823100313601.json, 图片生成/文生图/1954578900275884034.json, 图片生成/文生图/1955090857663893506.json, 图片生成/文生图/1955738055426674689.json, 图片生成/文生图/1958077760537317377.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_5

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1953929861947805698.json、图片生成/文生图/1954024086618066945.json、图片生成/文生图/1954036823100313601.json、图片生成/文生图/1954578900275884034.json、图片生成/文生图/1955090857663893506.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：75%

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

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy cleanGpuUsed、CR Prompt Text

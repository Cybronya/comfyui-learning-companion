---
name: unknown_workflow_generic_429
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.794
common_nodes: [Qwen3_VQA, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3 VQA图片反推视频提示词V1_1999477689276825601.json, 图片生成/反推提示词/Qwen3 VQA首尾帧图片反推提示词_1999645493368156162.json, 图片生成/反推提示词/Qwen3+VQA图片反推JSON格式提示词_1999643010478600193.json, 图片生成/反推提示词/千问图片反推_1986006571178176514.json, 图片生成/反推提示词/图像提示词反推（超详细版）QWEN3 VL_2015765733640249346.json, 图片生成/反推提示词/视频反推提示词_2000036361459691521.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_429

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/Qwen3 VQA图片反推视频提示词V1_1999477689276825601.json、图片生成/反推提示词/Qwen3 VQA首尾帧图片反推提示词_1999645493368156162.json、图片生成/反推提示词/Qwen3+VQA图片反推JSON格式提示词_1999643010478600193.json、图片生成/反推提示词/千问图片反推_1986006571178176514.json、图片生成/反推提示词/图像提示词反推（超详细版）QWEN3 VL_2015765733640249346.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `Qwen3_VQA`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageLoader` —— 5/6 个有
- `MultiplePathsInput` —— 3/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `LoadImage` —— 1/6 个有
- `VideoLoader` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

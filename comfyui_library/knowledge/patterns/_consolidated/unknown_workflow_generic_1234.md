---
name: unknown_workflow_generic_1234
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.743
common_nodes: [GetImageRangeFromBatch, SaveImage, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/图生图/首尾帧提取_2087401134448271361.json, 平台全量/提取视频中的帧_1953832159515693057.json, 平台全量/视频首帧图片提取（视频涂抹消除水印）_1917499330985394177.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1234

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/首尾帧提取_2087401134448271361.json、平台全量/提取视频中的帧_1953832159515693057.json、平台全量/视频首帧图片提取（视频涂抹消除水印）_1917499330985394177.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `SaveImage`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

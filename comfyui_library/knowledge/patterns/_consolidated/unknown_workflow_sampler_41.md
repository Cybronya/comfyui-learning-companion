---
name: unknown_workflow_sampler_41
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92475
common_nodes: [ImageConcatMulti, LoadImage, RunningHub XVerse Pipeline Loader, RunningHub XVerse Sampler, SaveImage, Text Multiline, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/任意男女合影_字节XVerse多主题一致性_1944543533074141186.json, 图片生成/图生图/单物一致性_字节XVerse多主题一致性_1943974592962527233.json, 图片生成/图生图/多人物一致性_字节XVerse多主题一致性_1943729955022966786.json, 图片生成/图生图/服装一致性_字节XVerse多人物一致性_1943740467731369986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_41

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/任意男女合影_字节XVerse多主题一致性_1944543533074141186.json、图片生成/图生图/单物一致性_字节XVerse多主题一致性_1943974592962527233.json、图片生成/图生图/多人物一致性_字节XVerse多主题一致性_1943729955022966786.json、图片生成/图生图/服装一致性_字节XVerse多人物一致性_1943740467731369986.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageConcatMulti`
- `LoadImage`
- `RunningHub XVerse Pipeline Loader`
- `RunningHub XVerse Sampler`
- `SaveImage`
- `Text Multiline`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CropFace` —— 3/4 个有
- `LayerMask: PersonMaskUltra V2` —— 3/4 个有
- `LayerUtility: CropByMask V2` —— 3/4 个有
- `PreviewImage` —— 3/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_upscale_43
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.73
common_nodes: [Image Comparer (rgthree), LoadImage, SUPIR_Upscale, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Supir高清放大_1914192946978091010.json, 平台全量/SUPIR-高度还原高清放大-在线生图V2.0_1902001768077926402.json, 平台全量/无损抠图1103_2117462772194832386.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_43

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Supir高清放大_1914192946978091010.json、平台全量/SUPIR-高度还原高清放大-在线生图V2.0_1902001768077926402.json、平台全量/无损抠图1103_2117462772194832386.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SUPIR_Upscale`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 2/3 个有
- `BiRefNet_Hugo` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `SaveImageAdvanced` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

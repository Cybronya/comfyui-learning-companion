---
name: unknown_workflow_upscale_26
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6892
common_nodes: [DF_Image_scale_to_side, LoadImage, SUPIR_Upscale, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/快速换脸 InfiniteYou_1923673512211304450.json, 图片生成/文生图/SUPIR-8K图片放大+高清放大+4K+8K+大分辨率+全节点注释_2057704104763412482.json, 图片生成/文生图/SUPIR-壁纸级放大+全节点注释_2056290929077743618.json, 平台全量/SUPIR-8K放大（微修复+放大）_1950130109950943233.json, 平台全量/SUPIR高清放大_图像修复_1973978788310683650.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_26

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/快速换脸 InfiniteYou_1923673512211304450.json、图片生成/文生图/SUPIR-8K图片放大+高清放大+4K+8K+大分辨率+全节点注释_2057704104763412482.json、图片生成/文生图/SUPIR-壁纸级放大+全节点注释_2056290929077743618.json、平台全量/SUPIR-8K放大（微修复+放大）_1950130109950943233.json、平台全量/SUPIR高清放大_图像修复_1973978788310683650.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `DF_Image_scale_to_side`
- `LoadImage`
- `SUPIR_Upscale`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `ReActorFaceSwap` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

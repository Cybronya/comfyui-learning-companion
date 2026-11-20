---
name: unknown_workflow_generic_473
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.730143
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, SeedVR2, SeedVR2BlockSwap]
problems: []
missing: []
members: [图片生成/图生图/高清放大工作流_2086423456144519169.json, 图片生成/图生图/高清放大（SeedVR2）_2014775599767752705.json, 图片生成/图生图/黑鹤-SeedVR2高清放大_2095521993763418113.json, 图片生成/图生图/黑鹤-SeedVR2高清放大_2100474974531309570.json, 平台全量/SeedVR2-图像无损高清放大_1960604630856196098.json, 平台全量/SeedVR2图片高清修复_1984865201658937345.json, 平台全量/SeedVR2无损高清放大_2021088886927138818.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_473

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/高清放大工作流_2086423456144519169.json、图片生成/图生图/高清放大（SeedVR2）_2014775599767752705.json、图片生成/图生图/黑鹤-SeedVR2高清放大_2095521993763418113.json、图片生成/图生图/黑鹤-SeedVR2高清放大_2100474974531309570.json、平台全量/SeedVR2-图像无损高清放大_1960604630856196098.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`

**可变部分**（部分 workflow 才有）：
- `SeedVR2ExtraArgs` —— 3/7 个有
- `easy int` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `easy imageScaleDownToSize` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

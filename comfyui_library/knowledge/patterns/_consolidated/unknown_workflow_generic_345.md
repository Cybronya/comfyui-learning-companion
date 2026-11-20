---
name: unknown_workflow_generic_345
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.83775
common_nodes: [BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/RMBG一键抠图_2057714410445164545.json, 图片生成/图生图/RMBG一键抠图_2079022658536173569.json, 图片生成/图生图/RMBG一键抠图_2079402674667216898.json, 图片生成/图生图/RMBG抠图_2108788082693730305.json, 平台全量/RMBG-背景分割_1795328706277888001.json, 平台全量/remove background_1869314887879921666.json, 平台全量/一键抠图遮罩_1896442512528048129.json, 平台全量/人像&产品自动扣除背景工作流_1940024100658253825.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_345

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/RMBG一键抠图_2057714410445164545.json、图片生成/图生图/RMBG一键抠图_2079022658536173569.json、图片生成/图生图/RMBG一键抠图_2079402674667216898.json、图片生成/图生图/RMBG抠图_2108788082693730305.json、平台全量/RMBG-背景分割_1795328706277888001.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/8 个有
- `preview_mask` —— 5/8 个有
- `MaskToImage` —— 2/8 个有
- `InspyrenetRembg` —— 1/8 个有
- `LayerMask: RmBgUltra V2` —— 1/8 个有
- `easy imageRemBg` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

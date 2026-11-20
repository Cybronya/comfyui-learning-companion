---
name: unknown_workflow_upscale_20
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.828
common_nodes: [AddBackgroundNode, HivisionLayOutNode, HivisionNode, LaterProcessNode, LoadImage, SaveImage, ZHHivisionParamsNode]
problems: []
missing: []
members: [平台全量/证件照 - 极速排版_1897243263475372034.json, 平台全量/证件照(寸照)生成器(排版)_1926630769081618434.json, 平台全量/证件照制作+自动裁切+自动抠图换底色+自动排版，识别人脸，倾斜自动校正_2011733057136500738.json, 平台全量/证件照片制作+自动裁切_1977939529594273794.json, 平台全量/证件照生成器，生成各种规格的证件照，直接拿去打印_1833431631565905921.json, 平台全量/陆老师_证件照生成器，生成各种规格的证件照，直接拿去打印_1970463220291018754.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_20

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/证件照 - 极速排版_1897243263475372034.json、平台全量/证件照(寸照)生成器(排版)_1926630769081618434.json、平台全量/证件照制作+自动裁切+自动抠图换底色+自动排版，识别人脸，倾斜自动校正_2011733057136500738.json、平台全量/证件照片制作+自动裁切_1977939529594273794.json、平台全量/证件照生成器，生成各种规格的证件照，直接拿去打印_1833431631565905921.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `AddBackgroundNode`
- `HivisionLayOutNode`
- `HivisionNode`
- `LaterProcessNode`
- `LoadImage`
- `SaveImage`
- `ZHHivisionParamsNode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/6 个有
- `AddWaterMarkNode` —— 3/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_upscale_7
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.818556
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [图片生成/图生图/VOSR2-文字放大_2108182051798208513.json, 图片生成/图生图/VOSR2文字海报放大_2100133119436349442.json, 图片生成/图生图/VOSR2文字海报放大_2101483417417371649.json, 图片生成/图生图/VOSR2文字海报放大_2102213109866909697.json, 图片生成/图生图/Vosr 2.0_极速高清修复_文本修复_一键4K图像_2097239382121078785.json, 图片生成/图生图/Vosr 2图像高清放大_2097142921681264641.json, 图片生成/图生图/Vosr_2.0_极速高清修复_文本修复_一键4K图像_2102323097541107714.json, 平台全量/VOSR 2.0 放大_2103391638453317633.json, 平台全量/VOSR2-高清放大（支持文字放大）_2096859197026684929.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_7

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/VOSR2-文字放大_2108182051798208513.json、图片生成/图生图/VOSR2文字海报放大_2100133119436349442.json、图片生成/图生图/VOSR2文字海报放大_2101483417417371649.json、图片生成/图生图/VOSR2文字海报放大_2102213109866909697.json、图片生成/图生图/Vosr 2.0_极速高清修复_文本修复_一键4K图像_2097239382121078785.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `Int` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `CM_FloatToInt` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

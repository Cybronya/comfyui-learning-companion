---
name: unknown_workflow_generic_106
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.910429
common_nodes: [Get Image Size, Image Comparer (rgthree), ImageResize+, ImpactMinMax, LoadImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch]
problems: []
missing: []
members: [图片生成/图生图/seedVR2图片高清放大_1977995529814769665.json, 图片生成/图生图/seedVR2放大修复（按目标分辨率K数同比例放大）_1980684915954110466.json, 图片生成/图生图/万物图片高清放大（分块）seedVR2_1956177364311048194.json, 图片生成/图生图/万物高清_2086061742978846722.json, 图片生成/图生图/万物高清放大_1985667227728916481.json, 图片生成/图生图/人像、文字、万物皆可高清放大8K（不变形）_2112521603924971521.json, 图片生成/图生图/图像分块极速放大 SeedVR2 【快速、好用】_1977525512761417729.json, 图片生成/图生图/图片清晰放大优化精修模糊变清晰seedVR2 万物高清放大（分块）_2074670337190621185.json, 图片生成/图生图/老孙AI 万物高清放大（分块）_2085590392736673793.json, 图片生成/图生图/高清8K放大新版_1984920818033573890.json, 图片生成/图生图/高清放大 seedVR2 TTP_1972557496084852737.json, 图片生成/图生图/高清放大 seedVR2 TTP_2098713428201402370.json, 图片生成/图生图/高清放大_seedVR2_TTP_2089687383133474818.json, 视频生成/图生视频/seedVR2 TTP 高清修复放大_2066714614678773761.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_106

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/seedVR2图片高清放大_1977995529814769665.json、图片生成/图生图/seedVR2放大修复（按目标分辨率K数同比例放大）_1980684915954110466.json、图片生成/图生图/万物图片高清放大（分块）seedVR2_1956177364311048194.json、图片生成/图生图/万物高清_2086061742978846722.json、图片生成/图生图/万物高清放大_1985667227728916481.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImpactMinMax`
- `LoadImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 13/14 个有
- `SimpleMath+` —— 13/14 个有
- `SaveImage` —— 11/14 个有
- `ImageCASharpening+` —— 9/14 个有
- `easy cleanGpuUsed` —— 9/14 个有
- `SeedVR2BlockSwap` —— 6/14 个有
- `ImageColorMatchAdobe+` —— 5/14 个有
- `KOOK_SaveJPGImage` —— 3/14 个有
- `ColorMatch` —— 1/14 个有
- `Fast Groups Muter (rgthree)` —— 1/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `TT_img_enc` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

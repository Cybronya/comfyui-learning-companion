---
name: unknown_workflow_generic_712
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.64225
common_nodes: [Get Image Size, Image Crop Location, Image Scale by Shortside (WLSH), ImageBatch, ImageConcanateOfUtils, ImpactMinMax, ImpactSwitch, Int, JWImageResizeByLongerSide, LoadImage, PreviewImage, RH_Nano_Banana_Image2Image, Resolutions by Ratio (WLSH), SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/柜机柜贴全流程_1993887255498522626.json, 图片生成/图生图/海报机器合成_1985965796599967746.json, 图片生成/图生图/海报机器合成url_1991417885222522881.json, 图片生成/图生图/海报机器合成本地_1991791658786451458.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_712

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/柜机柜贴全流程_1993887255498522626.json、图片生成/图生图/海报机器合成_1985965796599967746.json、图片生成/图生图/海报机器合成url_1991417885222522881.json、图片生成/图生图/海报机器合成本地_1991791658786451458.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 4 个 workflow 都包含：
- `Get Image Size`
- `Image Crop Location`
- `Image Scale by Shortside (WLSH)`
- `ImageBatch`
- `ImageConcanateOfUtils`
- `ImpactMinMax`
- `ImpactSwitch`
- `Int`
- `JWImageResizeByLongerSide`
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `Resolutions by Ratio (WLSH)`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImagesFromURL` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `Mix Color By Mask` —— 1/4 个有
- `RH_Nano_Banana2_Image2Image` —— 1/4 个有
- `TopazImageEnhance` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

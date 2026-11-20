---
name: unknown_workflow_video_inpaint_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [Color (hexadecimal), Get Image Size, HfImageToRGBA, INPAINT_MaskedFill, ImageCompositeMasked, ImageConstant, InvertMask, LayerUtility: RGB Value, MathExpression|pysssss, PlaySound|pysssss, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/视频抠像，添加绿幕_1893503148189761538.json, 平台全量/🦖视频抠像_2015612207131795457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频抠像，添加绿幕_1893503148189761538.json、平台全量/🦖视频抠像_2015612207131795457.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `Color (hexadecimal)`
- `Get Image Size`
- `HfImageToRGBA`
- `INPAINT_MaskedFill`
- `ImageCompositeMasked`
- `ImageConstant`
- `InvertMask`
- `LayerUtility: RGB Value`
- `MathExpression|pysssss`
- `PlaySound|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `InspyrenetRembgAdvanced` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

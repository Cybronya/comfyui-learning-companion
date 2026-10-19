---
name: unknown_workflow_video_5
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.988556
common_nodes: [GrowMask, INTConstant, ImageBatch, ImageCompositeMasked, ImageResizeKJv2, ImageToMask, InvertMask, LayerColor: BrightnessContrastV2, LoadAudio, LoadImage, LoadImageMask, MaskBlur+, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: [LayerColor: BrightnessContrastV2, MaskBlur+]
members: [视频生成/图生视频/2013490499956514818.json, 视频生成/图生视频/1959597724477894657.json, 视频生成/图生视频/2011235737471029250.json, 视频生成/图生视频/2031202509624184834.json, 视频生成/图生视频/2039877279874031617.json, 视频生成/图生视频/2050882588805480449.json, 视频生成/图生视频/2057267742750892033.json, 视频生成/图生视频/2059150379807494146.json, 视频生成/文生视频/1961976286589730817.json]
source: knowledge_consolidation
---

# unknown_workflow_video_5

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2013490499956514818.json、视频生成/图生视频/1959597724477894657.json、视频生成/图生视频/2011235737471029250.json、视频生成/图生视频/2031202509624184834.json、视频生成/图生视频/2039877279874031617.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 9 个 workflow 都包含：
- `GrowMask`
- `INTConstant`
- `ImageBatch`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `ImageToMask`
- `InvertMask`
- `LayerColor: BrightnessContrastV2`
- `LoadAudio`
- `LoadImage`
- `LoadImageMask`
- `MaskBlur+`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerColor: BrightnessContrastV2、MaskBlur+

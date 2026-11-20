---
name: unknown_workflow_video_inpaint_sampler_3
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.846286
common_nodes: [GrowMaskWithBlur, ImageResizeKJ, InpaintPreprocessor, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/电商视频换产品(Wan2.1Vace视频遮罩重绘）_2011157655569567746.json, 平台全量/直播定制动物跳舞 视频遮罩重绘_1928045787630944257.json, 平台全量/直播电影换主角_1928075988117110786.json, 视频生成/图生视频/VACE 14B注意力蒙版视频生视频V2_1922710502047367170.json, 视频生成/图生视频/普通版VACE注意力蒙版视频生视频_1907808853109387266.json, 视频生成/图生视频/电商视频扩图（遮罩重绘）_1927919884900909058.json, 视频生成/图生视频/电商视频换产品（视频遮罩重绘）_1927712380627599361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_3

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/电商视频换产品(Wan2.1Vace视频遮罩重绘）_2011157655569567746.json、平台全量/直播定制动物跳舞 视频遮罩重绘_1928045787630944257.json、平台全量/直播电影换主角_1928075988117110786.json、视频生成/图生视频/VACE 14B注意力蒙版视频生视频V2_1922710502047367170.json、视频生成/图生视频/普通版VACE注意力蒙版视频生视频_1907808853109387266.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `GrowMaskWithBlur`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `WanVideoBlockSwap` —— 6/7 个有
- `WanVideoVACEModelSelect` —— 6/7 个有
- `JjkText` —— 5/7 个有
- `LayerMask: LoadSegmentAnythingModels` —— 5/7 个有
- `LayerMask: SegmentAnythingUltra V3` —— 5/7 个有
- `ImagePadForOutpaint` —— 3/7 个有
- `JWInteger` —— 3/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `PDIMAGE_LongerSize` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有
- `easy compare` —— 1/7 个有
- `easy ifElse` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

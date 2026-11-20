---
name: unknown_workflow_video_inpaint_sampler_8
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.889667
common_nodes: [ImageResize+, InpaintPreprocessor, LayerMask: SegmentAnythingUltra V2, LoadImage, LoadWanVideoT5TextEncoder, MaskFix+, MaskToImage, PreviewImage, PrimitiveString, RMBG, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/VACE14B替换视频中物体 换服装 换模特 换产品 换背景_1925931113640841217.json, 平台全量/VACE14B替换视频中物体 换服装 换模特 换产品 换背景_1926621852884475905.json, 平台全量/VACE14B视频主体替换_1923478006843830274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VACE14B替换视频中物体 换服装 换模特 换产品 换背景_1925931113640841217.json、平台全量/VACE14B替换视频中物体 换服装 换模特 换产品 换背景_1926621852884475905.json、平台全量/VACE14B视频主体替换_1923478006843830274.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResize+`
- `InpaintPreprocessor`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskFix+`
- `MaskToImage`
- `PreviewImage`
- `PrimitiveString`
- `RMBG`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Mute / Bypass Relay (rgthree)` —— 1/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/3 个有
- `Note _O` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

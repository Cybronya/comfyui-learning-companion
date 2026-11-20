---
name: unknown_workflow_video_sampler_vae_48
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.804
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJ, LoadWanVideoT5TextEncoder, MaskPreview+, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/WAN VACE 14B首尾帧图生视频_1925906203904266242.json, 平台全量/视频换背景v1-zlink_1874288833763086338.json, 视频生成/图生视频/FusionX+LightX2V首尾帧特效版_1948561964491517953.json, 视频生成/图生视频/LightX2V人物变装视频首尾帧特效版V1_1945679647550132225.json, 视频生成/图生视频/LightX2V首尾帧特效版_1945794498888658946.json, 视频生成/图生视频/VACE 14B-首尾帧图生视频_1925111334327754753.json, 视频生成/图生视频/VACE-14B首尾视频生成_1922637708198559745.json, 视频生成/图生视频/VACE-14B首尾视频生成_1922829567898304514.json, 视频生成/图生视频/最新Wan2.1+Vace首尾帧  极速运行 中文注释_1912169450282647553.json, 视频生成/图生视频/贞贞换发型首尾帧特效版（T8自用）_1945694756720582658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_48

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/WAN VACE 14B首尾帧图生视频_1925906203904266242.json、平台全量/视频换背景v1-zlink_1874288833763086338.json、视频生成/图生视频/FusionX+LightX2V首尾帧特效版_1948561964491517953.json、视频生成/图生视频/LightX2V人物变装视频首尾帧特效版V1_1945679647550132225.json、视频生成/图生视频/LightX2V首尾帧特效版_1945794498888658946.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview+`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `WanVideoVACEStartToEndFrame` —— 9/10 个有
- `GetNode` —— 5/10 个有
- `SetNode` —— 5/10 个有
- `WanVideoLoraSelect` —— 4/10 个有
- `WanVideoTorchCompileSettings` —— 4/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `INPAINT_MaskedFill` —— 1/10 个有
- `InvertMask` —— 1/10 个有
- `LayerMask: BiRefNetUltra` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `Note _O` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

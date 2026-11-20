---
name: unknown_workflow_video_sampler_vae_80
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.972
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, TextInput_, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/VACE  视频换人--参考图局部重绘_1907391023100620801.json, 平台全量/VACE  视频换人--参考图局部重绘_1967883750451326978.json, 平台全量/VACE视频编辑之【动作迁移】 美女跳舞？_1907321135112052738.json, 平台全量/🦖VACE 14B 视频重绘_1923281980199530497.json, 视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1922660439551873025.json, 视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1934429538858266626.json, 视频生成/图生视频/【抖音爆款国风古画健身视频】VACE-CausVid加速版_1925071264359378946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_80

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/VACE  视频换人--参考图局部重绘_1907391023100620801.json、平台全量/VACE  视频换人--参考图局部重绘_1967883750451326978.json、平台全量/VACE视频编辑之【动作迁移】 美女跳舞？_1907321135112052738.json、平台全量/🦖VACE 14B 视频重绘_1923281980199530497.json、视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1922660439551873025.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `TextInput_`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/7 个有
- `WanVideoBlockSwap` —— 4/7 个有
- `WanVideoVACEModelSelect` —— 4/7 个有
- `GrowMaskWithBlur` —— 3/7 个有
- `InpaintPreprocessor` —— 3/7 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/7 个有
- `WanVideoEnhanceAVideo` —— 3/7 个有
- `WanVideoExperimentalArgs` —— 3/7 个有
- `WanVideoSLG` —— 3/7 个有
- `DWPreprocessor` —— 1/7 个有
- `ImageBlend` —— 1/7 个有
- `Int` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `ResizeLongestToNode` —— 1/7 个有
- `Text` —— 1/7 个有
- `VHS_VideoInfoSource` —— 1/7 个有
- `WanVideoLoraSelect` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

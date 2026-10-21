---
name: unknown_workflow_video_sampler_vae_38
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.929909
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1923668312054484994.json, 视频生成/图生视频/1923687527591366658.json, 视频生成/图生视频/1923364827979239425.json, 视频生成/图生视频/1923428731015393281.json, 视频生成/图生视频/1927548581379465217.json, 视频生成/图生视频/1925380470958399490.json, 视频生成/图生视频/1925071264359378946.json, 视频生成/图生视频/1969653436927143937.json, 视频生成/图生视频/1968167021571616770.json, 视频生成/图生视频/2000276235513196545.json, 视频生成/图生视频/1968700709732589569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1923668312054484994.json、视频生成/图生视频/1923687527591366658.json、视频生成/图生视频/1923364827979239425.json、视频生成/图生视频/1923428731015393281.json、视频生成/图生视频/1927548581379465217.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/11 个有
- `WanVideoEnhanceAVideo` —— 9/11 个有
- `WanVideoExperimentalArgs` —— 9/11 个有
- `WanVideoSLG` —— 9/11 个有
- `AIO_Preprocessor` —— 8/11 个有
- `VHS_LoadVideo` —— 8/11 个有
- `WanVideoTeaCache` —— 8/11 个有
- `ColorMatch` —— 7/11 个有
- `TextInput_` —— 7/11 个有
- `JWInteger` —— 6/11 个有
- `WanVideoVACEStartToEndFrame` —— 6/11 个有
- `DWPreprocessor` —— 5/11 个有
- `ImageBlend` —— 5/11 个有
- `ImageResizeKJ` —— 5/11 个有
- `WanVideoTorchCompileSettings` —— 5/11 个有
- `EmptyImage` —— 4/11 个有
- `GetImageSizeAndCount` —— 4/11 个有
- `ImageConcatMulti` —— 4/11 个有
- `ImagePadKJ` —— 4/11 个有
- `LayerUtility: PurgeVRAM V2` —— 4/11 个有
- `ShowText|pysssss` —— 4/11 个有
- `ImpactSwitch` —— 3/11 个有
- `Int` —— 3/11 个有
- `Primitive integer [Crystools]` —— 3/11 个有
- `SimpleMath+` —— 3/11 个有
- `Text Concatenate` —— 3/11 个有
- `Text Multiline` —— 3/11 个有
- `easy int` —— 3/11 个有
- `ImageRepeat` —— 2/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `RH_Captioner` —— 1/11 个有
- `VHS_VideoInfoSource` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

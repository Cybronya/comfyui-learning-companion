---
name: unknown_workflow_video_sampler_vae_36
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.928
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1922660439551873025.json, 视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1934429538858266626.json, 视频生成/图生视频/VACE双图参考，教程请看b站八月饺子_1926978789408952322.json, 视频生成/图生视频/VACE视频转绘美女跳舞_1909879938038624257.json, 视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json, 视频生成/图生视频/【抖音爆款国风古画健身视频】VACE-CausVid加速版_1925071264359378946.json, 视频生成/图生视频/人物动作迁移_图生视频_wan2.2_1969653436927143937.json, 视频生成/图生视频/动作迁移_人物跳舞图生视频_加速版_支持15S_1968167021571616770.json, 视频生成/图生视频/动作迁移_人物跳舞图生视频_加速版_支持15S_2000276235513196545.json, 视频生成/图生视频/舞蹈迁移-FusionX-VACE大师级视频ott_1940038425300860930.json, 视频生成/图生视频/视频动作迁移_wan2.2_15秒版_1968700709732589569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_36

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1922660439551873025.json、视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1934429538858266626.json、视频生成/图生视频/VACE双图参考，教程请看b站八月饺子_1926978789408952322.json、视频生成/图生视频/VACE视频转绘美女跳舞_1909879938038624257.json、视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 10/11 个有
- `VHS_LoadVideo` —— 10/11 个有
- `WanVideoBlockSwap` —— 10/11 个有
- `WanVideoExperimentalArgs` —— 10/11 个有
- `WanVideoTeaCache` —— 10/11 个有
- `WanVideoTorchCompileSettings` —— 10/11 个有
- `WanVideoEnhanceAVideo` —— 9/11 个有
- `WanVideoSLG` —— 9/11 个有
- `WanVideoVACEModelSelect` —— 9/11 个有
- `DWPreprocessor` —— 6/11 个有
- `GetImageSizeAndCount` —— 6/11 个有
- `ImageBlend` —— 6/11 个有
- `WanVideoLoraSelect` —— 6/11 个有
- `ColorMatch` —— 5/11 个有
- `EmptyImage` —— 5/11 个有
- `ImageConcatMulti` —— 5/11 个有
- `ImagePadKJ` —— 5/11 个有
- `ShowText|pysssss` —— 5/11 个有
- `LayerUtility: PurgeVRAM V2` —— 4/11 个有
- `Primitive integer [Crystools]` —— 4/11 个有
- `Text Concatenate` —— 4/11 个有
- `Text Multiline` —— 4/11 个有
- `TextInput_` —— 4/11 个有
- `ImpactSwitch` —— 3/11 个有
- `Int` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `SimpleMath+` —— 3/11 个有
- `easy int` —— 3/11 个有
- `AddLabel` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `RH_Captioner` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `VHS_VideoInfoSource` —— 1/11 个有
- `easy imageRemBg` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

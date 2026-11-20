---
name: unknown_workflow_video_sampler_vae_43
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8894
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1922660439551873025.json, 视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1934429538858266626.json, 视频生成/图生视频/VACE双图参考，教程请看b站八月饺子_1926978789408952322.json, 视频生成/图生视频/VACE视频转绘美女跳舞_1909879938038624257.json, 视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json, 视频生成/图生视频/【抖音爆款国风古画健身视频】VACE-CausVid加速版_1925071264359378946.json, 视频生成/图生视频/人物动作迁移_图生视频_wan2.2_1969653436927143937.json, 视频生成/图生视频/舞蹈迁移-FusionX-VACE大师级视频ott_1940038425300860930.json, 视频生成/图生视频/通义万相统一模型FusionX-LORA版本美女跳舞转绘工作流_1935676000963321857.json, 视频生成/文生视频/160帧-舞蹈-超高拟态-直出1920高清_1949732964007059457.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_43

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1922660439551873025.json、视频生成/图生视频/VACE14B正式版【动作迁移&图片跳舞】-有参考图_1934429538858266626.json、视频生成/图生视频/VACE双图参考，教程请看b站八月饺子_1926978789408952322.json、视频生成/图生视频/VACE视频转绘美女跳舞_1909879938038624257.json、视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 9/10 个有
- `VHS_LoadVideo` —— 9/10 个有
- `WanVideoModelLoader` —— 9/10 个有
- `WanVideoBlockSwap` —— 8/10 个有
- `WanVideoExperimentalArgs` —— 8/10 个有
- `WanVideoTeaCache` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `WanVideoSLG` —— 7/10 个有
- `WanVideoVACEModelSelect` —— 7/10 个有
- `WanVideoEnhanceAVideo` —— 6/10 个有
- `GetImageSizeAndCount` —— 5/10 个有
- `ImageBlend` —— 5/10 个有
- `AddLabel` —— 4/10 个有
- `ColorMatch` —— 4/10 个有
- `DWPreprocessor` —— 4/10 个有
- `EmptyImage` —— 4/10 个有
- `ImageConcatMulti` —— 4/10 个有
- `RH_Captioner` —— 4/10 个有
- `ShowText|pysssss` —— 4/10 个有
- `TextInput_` —— 4/10 个有
- `WanVideoLoraSelect` —— 4/10 个有
- `GetNode` —— 3/10 个有
- `ImagePadKJ` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `Primitive integer [Crystools]` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `Text Concatenate` —— 3/10 个有
- `Text Multiline` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `RHHiddenNodes` —— 2/10 个有
- `ImageConcanate` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `VHS_VideoInfoSource` —— 1/10 个有
- `Zoe-DepthMapPreprocessor` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy imageRemBg` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

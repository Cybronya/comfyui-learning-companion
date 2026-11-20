---
name: unknown_workflow_video_sampler_vae_7
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.743192
common_nodes: [EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, ImpactSwitch, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/Wan VACE CausVid三倍加速 参考图动作迁移 视频转绘编辑 智能提示词 工作流-Star_1924946957419094018.json, 视频生成/图生视频/150帧-跳舞-动作迁移-直出1920P高清-V1版本_1933077979956215810.json, 视频生成/图生视频/150帧-跳舞-动作迁移-直出1920P高清-V1版本_1986080138964205570.json, 视频生成/图生视频/150帧-跳舞-动作迁移-直出1920P高清-V1版本_1989255304942596097.json, 视频生成/图生视频/Radial Attention提速20%-FusionX-舞蹈动作迁移v2_1943365680282693633.json, 视频生成/图生视频/Radial提速20%_FusionX_舞蹈动作迁移V3_1950083383838818305.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移-直出1920P高清_2051825815473668098.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移-直出1920P高清_2051912300868710402.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移-直出1920P高清_2052572511736479746.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移-直出1920P高清_2052924055216504834.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移_2052197097281208321.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移_2054011411742896129.json, 视频生成/图生视频/图生跳舞视频-跳舞-动作迁移-出1920P高清_1996616325067849729.json, 视频生成/图生视频/舞蹈-超高拟态_1945365424944947201.json, 视频生成/图生视频/舞蹈-超高拟态_1946130631811055617.json, 视频生成/图生视频/视频「背景」替换-V2版本_1965213821134622721.json, 视频生成/图生视频/视频人物换背景_1964883443333087234.json, 视频生成/图生视频/视频替换背景-V2版本_1989248787958870017.json, 视频生成/图生视频/视频替换背景-V2版本_2115273278456680449.json, 视频生成/图生视频/视频替换背景_2017131658423570434.json, 视频生成/图生视频/视频替换背景_2038239610723115009.json, 视频生成/图生视频/超高拟态-直出1920高清-V2版本-循环版_1964248565730131970.json, 视频生成/图生视频/跳舞-动作迁移-直出高清_1971021623618899970.json, 视频生成/文生视频/160帧-舞蹈-超高拟态-直出1920高清_1949732964007059457.json, 视频生成/文生视频/视频替换背景-V2版本_1959794144917008385.json, 视频生成/视频生视频/视频替换背景-V2版本_1959794144917008385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_7

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（平台全量/Wan VACE CausVid三倍加速 参考图动作迁移 视频转绘编辑 智能提示词 工作流-Star_1924946957419094018.json、视频生成/图生视频/150帧-跳舞-动作迁移-直出1920P高清-V1版本_1933077979956215810.json、视频生成/图生视频/150帧-跳舞-动作迁移-直出1920P高清-V1版本_1986080138964205570.json、视频生成/图生视频/150帧-跳舞-动作迁移-直出1920P高清-V1版本_1989255304942596097.json、视频生成/图生视频/Radial Attention提速20%-FusionX-舞蹈动作迁移v2_1943365680282693633.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 26 个 workflow 都包含：
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `ImpactSwitch`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 25/26 个有
- `PreviewImage` —— 25/26 个有
- `RH_Captioner` —— 25/26 个有
- `SimpleMath+` —— 25/26 个有
- `Text Concatenate` —— 25/26 个有
- `Text Multiline` —— 25/26 个有
- `RHHiddenNodes` —— 24/26 个有
- `WanVideoExperimentalArgs` —— 24/26 个有
- `AIO_Preprocessor` —— 18/26 个有
- `AddLabel` —— 18/26 个有
- `WanVideoTeaCache` —— 16/26 个有
- `ShowText|pysssss` —— 14/26 个有
- `WanVideoBlockSwap` —— 14/26 个有
- `WanVideoLoraSelect` —— 14/26 个有
- `WanVideoModelLoader` —— 14/26 个有
- `WanVideoTorchCompileSettings` —— 14/26 个有
- `WanVideoVACEModelSelect` —— 12/26 个有
- `WanVideoEnhanceAVideo` —— 9/26 个有
- `ImageFromBatch` —— 8/26 个有
- `LayerUtility: ImageBlend` —— 8/26 个有
- `ImageBlend` —— 5/26 个有
- `WanVideoEasyCache` —— 2/26 个有
- `WanVideoSetRadialAttention` —— 2/26 个有
- `CR Text` —— 1/26 个有
- `InspyrenetRembg` —— 1/26 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/26 个有
- `Note Plus (mtb)` —— 1/26 个有
- `easy imageSize` —— 1/26 个有
- `easy seed` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

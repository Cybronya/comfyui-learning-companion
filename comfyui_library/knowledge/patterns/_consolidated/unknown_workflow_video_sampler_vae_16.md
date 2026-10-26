---
name: unknown_workflow_video_sampler_vae_16
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.711125
common_nodes: [GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【丝滑】Wan2.1-VACE-14B首尾帧动画（超详细讲解）_1923066679113543681.json, 视频生成/图生视频/Aniwan+百变星君（原59美元LORA）丝滑变装首尾帧_1951187088609882114.json, 视频生成/图生视频/CausVid仅需3-9步极速VACE首尾帧视频加速版_1923973452506853378.json, 视频生成/图生视频/FusionX+LightX2V首尾帧特效版_1948561964491517953.json, 视频生成/图生视频/FusionX_图生视频动作迁移_1947326478251872258.json, 视频生成/图生视频/wan2.1 万相 Q版卡通动漫角色跳舞视频动画_1936291028129206274.json, 视频生成/图生视频/wan2.1fun超强控制视频人物动作迁移丝滑不崩脸_1934538219805417473.json, 视频生成/图生视频/【直出高清】人物跳舞动作迁移_1934767007986294786.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移-直出1920P高清_2051825815473668098.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移-直出1920P高清_2051912300868710402.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移-直出1920P高清_2052572511736479746.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移-直出1920P高清_2052924055216504834.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移_2052197097281208321.json, 视频生成/图生视频/图生视频---150帧-跳舞-动作迁移_2054011411742896129.json, 视频生成/图生视频/图生跳舞视频-跳舞-动作迁移-出1920P高清_1996616325067849729.json, 视频生成/图生视频/跳舞-动作迁移-直出高清_1971021623618899970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_16

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/【丝滑】Wan2.1-VACE-14B首尾帧动画（超详细讲解）_1923066679113543681.json、视频生成/图生视频/Aniwan+百变星君（原59美元LORA）丝滑变装首尾帧_1951187088609882114.json、视频生成/图生视频/CausVid仅需3-9步极速VACE首尾帧视频加速版_1923973452506853378.json、视频生成/图生视频/FusionX+LightX2V首尾帧特效版_1948561964491517953.json、视频生成/图生视频/FusionX_图生视频动作迁移_1947326478251872258.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 16 个 workflow 都包含：
- `GetImageSizeAndCount`
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
- `AddLabel` —— 15/16 个有
- `EmptyImage` —— 15/16 个有
- `GetNode` —— 15/16 个有
- `ImageConcatMulti` —— 15/16 个有
- `SetNode` —— 15/16 个有
- `WanVideoLoraSelect` —— 15/16 个有
- `WanVideoSLG` —— 15/16 个有
- `WanVideoTeaCache` —— 15/16 个有
- `ImageResizeKJ` —— 14/16 个有
- `WanVideoExperimentalArgs` —— 14/16 个有
- `WanVideoTorchCompileSettings` —— 13/16 个有
- `ColorMatch` —— 12/16 个有
- `PreviewImage` —— 12/16 个有
- `Primitive integer [Crystools]` —— 12/16 个有
- `Text Multiline` —— 12/16 个有
- `VHS_LoadVideo` —— 12/16 个有
- `AIO_Preprocessor` —— 11/16 个有
- `Text Concatenate` —— 11/16 个有
- `easy cleanGpuUsed` —— 11/16 个有
- `RH_Captioner` —— 9/16 个有
- `ImpactSwitch` —— 8/16 个有
- `RHHiddenNodes` —— 8/16 个有
- `SimpleMath+` —— 8/16 个有
- `WanVideoVACEStartToEndFrame` —— 5/16 个有
- `MaskPreview+` —— 3/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `ImageResize+` —— 2/16 个有
- `Anything Everywhere` —— 1/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `Int` —— 1/16 个有
- `Joy_caption_two` —— 1/16 个有
- `Joy_caption_two_load` —— 1/16 个有
- `VHS_VideoInfo` —— 1/16 个有
- `WD14Tagger|pysssss` —— 1/16 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

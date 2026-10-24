---
name: unknown_workflow_video_lora_sampler_140
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.739
common_nodes: [AIO_Preprocessor, AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoSampler, WanVideoTextEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE14b-美女疯狂跳舞机V1_1923648831874134018.json, 视频生成/图生视频/wan2.1fun超强控制视频人物动作迁移丝滑不崩脸_1934538219805417473.json, 视频生成/图生视频/【直出高清】人物跳舞动作迁移_1934767007986294786.json, 视频生成/图生视频/加快兼质量参考视频姿势跳舞_1924138217270857730.json, 视频生成/图生视频/动作Pose迁移_1948594124155944961.json, 视频生成/图生视频/图转视频0701_1939830629229830146.json, 视频生成/图生视频/新150帧高清美女跳舞机 （任何动作均可迁移）_1934886185854509058.json, 视频生成/图生视频/新Wan2.1卡通人物跳舞机V3.0_1932026704078766082.json, 视频生成/图生视频/新Wan2.2 至高160帧超级动作迁移美女跳舞_1955521868151361537.json, 视频生成/图生视频/最新美女跳舞机2K高清视频直接160帧V3_1930203972051832833.json, 视频生成/图生视频/视频动作迁移｜上传视频和图片｜_1962127053556531202.json, 视频生成/文生视频/【闪电极速】Wan2.1 WanVACE动作迁移视频动画生成_1924702934460715010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_140

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/VACE14b-美女疯狂跳舞机V1_1923648831874134018.json、视频生成/图生视频/wan2.1fun超强控制视频人物动作迁移丝滑不崩脸_1934538219805417473.json、视频生成/图生视频/【直出高清】人物跳舞动作迁移_1934767007986294786.json、视频生成/图生视频/加快兼质量参考视频姿势跳舞_1924138217270857730.json、视频生成/图生视频/动作Pose迁移_1948594124155944961.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 12 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `Primitive integer [Crystools]` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `WanVideoVACEEncode` —— 11/12 个有
- `WanVideoModelLoader` —— 10/12 个有
- `WanVideoSLG` —— 9/12 个有
- `ColorMatch` —— 8/12 个有
- `WanVideoExperimentalArgs` —— 8/12 个有
- `WanVideoTorchCompileSettings` —— 8/12 个有
- `Text Concatenate` —— 7/12 个有
- `Text Multiline` —— 7/12 个有
- `ImageUpscaleWithModel` —— 6/12 个有
- `RHHiddenNodes` —— 6/12 个有
- `UpscaleModelLoader` —— 6/12 个有
- `WanVideoTeaCache` —— 5/12 个有
- `Bjornulf_ShowJson` —— 4/12 个有
- `LayerUtility: PurgeVRAM` —— 4/12 个有
- `RH_Translator` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `ImagePadKJ` —— 3/12 个有
- `Note Plus (mtb)` —— 3/12 个有
- `RH_Captioner` —— 3/12 个有
- `ShowText|pysssss` —— 3/12 个有
- `WD14Tagger|pysssss` —— 3/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `easy int` —— 2/12 个有
- `FILM VFI` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

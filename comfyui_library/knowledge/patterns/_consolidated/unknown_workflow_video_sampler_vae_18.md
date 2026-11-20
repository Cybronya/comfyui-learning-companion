---
name: unknown_workflow_video_sampler_vae_18
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.674733
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/首尾帧参考转视频，视频风格转绘参考，非常滴稳定_1915808034642132993.json, 视频生成/图生视频/Aniwan+百变星君（原59美元LORA）丝滑变装首尾帧_1951187088609882114.json, 视频生成/图生视频/CausVid仅需3-9步极速VACE首尾帧视频加速版_1923973452506853378.json, 视频生成/图生视频/FusionX_图生视频动作迁移_1947326478251872258.json, 视频生成/图生视频/VACE14B-极致完美动作姿势迁移_1922696527037480962.json, 视频生成/图生视频/VACE14B-极致完美动作姿势迁移_1932273644485902337.json, 视频生成/图生视频/VACE14B-首尾帧视频生成_1922723230275223554.json, 视频生成/图生视频/VACE14B万相吉卜力风格转绘_1923032081754935297.json, 视频生成/图生视频/VACE14B手绘线稿风格转绘_1923004449781182465.json, 视频生成/图生视频/VACE视频编辑（图片参考视频一致性跳舞视频转绘）工作流_1922996913308954625.json, 视频生成/图生视频/wan2.1fun超强控制视频人物动作迁移丝滑不崩脸_1934538219805417473.json, 视频生成/图生视频/【直出高清】人物跳舞动作迁移_1934767007986294786.json, 视频生成/图生视频/仅需3-9步极速WanVACE动作Pose迁移(CausVid)_1923678505442136066.json, 视频生成/图生视频/加快兼质量参考视频姿势跳舞_1924138217270857730.json, 视频生成/图生视频/动作Pose迁移_1948594124155944961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_18

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（平台全量/首尾帧参考转视频，视频风格转绘参考，非常滴稳定_1915808034642132993.json、视频生成/图生视频/Aniwan+百变星君（原59美元LORA）丝滑变装首尾帧_1951187088609882114.json、视频生成/图生视频/CausVid仅需3-9步极速VACE首尾帧视频加速版_1923973452506853378.json、视频生成/图生视频/FusionX_图生视频动作迁移_1947326478251872258.json、视频生成/图生视频/VACE14B-极致完美动作姿势迁移_1922696527037480962.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 15 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 14/15 个有
- `WanVideoVACEModelSelect` —— 14/15 个有
- `Primitive integer [Crystools]` —— 13/15 个有
- `Text Multiline` —— 13/15 个有
- `WanVideoTorchCompileSettings` —— 13/15 个有
- `VHS_LoadVideo` —— 12/15 个有
- `AIO_Preprocessor` —— 11/15 个有
- `Text Concatenate` —— 11/15 个有
- `WanVideoSLG` —— 11/15 个有
- `WanVideoTeaCache` —— 11/15 个有
- `WanVideoExperimentalArgs` —— 10/15 个有
- `Fast Groups Bypasser (rgthree)` —— 9/15 个有
- `ImagePadKJ` —— 9/15 个有
- `RH_Captioner` —— 9/15 个有
- `ShowText|pysssss` —— 8/15 个有
- `WanVideoLoraSelect` —— 8/15 个有
- `ColorMatch` —— 7/15 个有
- `DepthAnything_V2` —— 6/15 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 6/15 个有
- `GetImageRangeFromBatch` —— 5/15 个有
- `MaskPreview+` —— 4/15 个有
- `PreviewImage` —— 4/15 个有
- `WanVideoVACEStartToEndFrame` —— 4/15 个有
- `easy cleanGpuUsed` —— 4/15 个有
- `easy imageRemBg` —— 2/15 个有
- `Joy_caption_two` —— 1/15 个有
- `Joy_caption_two_load` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `WD14Tagger|pysssss` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

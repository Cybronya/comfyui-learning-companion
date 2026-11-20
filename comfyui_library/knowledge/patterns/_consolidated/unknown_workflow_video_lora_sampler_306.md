---
name: unknown_workflow_video_lora_sampler_306
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.731
common_nodes: [AIO_Preprocessor, AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE14b-美女疯狂跳舞机V1_1923648831874134018.json, 视频生成/图生视频/图转视频0701_1939830629229830146.json, 视频生成/图生视频/新150帧高清美女跳舞机 （任何动作均可迁移）_1934886185854509058.json, 视频生成/图生视频/新Wan2.1卡通人物跳舞机V3.0_1932026704078766082.json, 视频生成/图生视频/新Wan2.2 至高160帧超级动作迁移美女跳舞_1955521868151361537.json, 视频生成/图生视频/最新美女跳舞机2K高清视频直接160帧V3_1930203972051832833.json, 视频生成/图生视频/视频动作迁移｜上传视频和图片｜_1962127053556531202.json, 视频生成/图生视频/视频动作迁移｜上传视频和图片｜深度+open pose 控制_1937838882719469569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_306

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/VACE14b-美女疯狂跳舞机V1_1923648831874134018.json、视频生成/图生视频/图转视频0701_1939830629229830146.json、视频生成/图生视频/新150帧高清美女跳舞机 （任何动作均可迁移）_1934886185854509058.json、视频生成/图生视频/新Wan2.1卡通人物跳舞机V3.0_1932026704078766082.json、视频生成/图生视频/新Wan2.2 至高160帧超级动作迁移美女跳舞_1955521868151361537.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 7/8 个有
- `WanVideoExperimentalArgs` —— 7/8 个有
- `WanVideoVACEEncode` —— 7/8 个有
- `ImageUpscaleWithModel` —— 6/8 个有
- `RHHiddenNodes` —— 6/8 个有
- `UpscaleModelLoader` —— 6/8 个有
- `WanVideoModelLoader` —— 6/8 个有
- `Bjornulf_ShowJson` —— 4/8 个有
- `ColorMatch` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `RH_Translator` —— 4/8 个有
- `WanVideoTeaCache` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `Note Plus (mtb)` —— 3/8 个有
- `Text Concatenate` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `FILM VFI` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `WD14Tagger|pysssss` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

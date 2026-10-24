---
name: unknown_workflow_video_lora_sampler_190
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8266
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json, 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版V2（大幅度增加时长）_1936304565509607426.json, 视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版（UNI3C运镜版）_1936341490123837441.json, 视频生成/图生视频/MultiTalk对口型（万相实现）+uni3C运镜控制_1937801479434735618.json, 视频生成/图生视频/MultiTalk数字人口播单人版_1940606353897402370.json, 视频生成/图生视频/MultiTalk最强数字人插件16G可玩，音频+图片=王炸数字人_1937864518498455553.json, 视频生成/图生视频/MultiTalk：超6倍加速，超逼真顶流K歌数字人_1936605606658625537.json, 视频生成/图生视频/Multitalk--唱歌数字人_1936361924722593793.json, 视频生成/图生视频/Multitalk数字人（极速版）_1937674986381295618.json, 视频生成/图生视频/💂‍【大炮数字人】音乐自动生成+数字人对口型💂‍_1937733481621557249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_190

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版(无clipvision版)_1936345879362310145.json、视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版V2（大幅度增加时长）_1936304565509607426.json、视频生成/图生视频/MultiTalk单人KJ高质量加速稳定版（UNI3C运镜版）_1936341490123837441.json、视频生成/图生视频/MultiTalk对口型（万相实现）+uni3C运镜控制_1937801479434735618.json、视频生成/图生视频/MultiTalk数字人口播单人版_1940606353897402370.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 9/10 个有
- `WanVideoBlockSwap` —— 9/10 个有
- `WanVideoClipVisionEncode` —— 9/10 个有
- `JWIntegerToString` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `PrimitiveInt` —— 7/10 个有
- `easy cleanGpuUsed` —— 7/10 个有
- `Audio Duration (mtb)` —— 6/10 个有
- `PrimitiveFloat` —— 6/10 个有
- `TextInput_` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `JWInteger` —— 5/10 个有
- `LayerUtility: PurgeVRAM` —— 5/10 个有
- `VHS_LoadVideo` —— 5/10 个有
- `WanVideoEncode` —— 5/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 5/10 个有
- `WanVideoUni3C_embeds` —— 5/10 个有
- `ImageResizeKJ` —— 4/10 个有
- `WanVideoContextOptions` —— 4/10 个有
- `WanVideoTorchCompileSettings` —— 4/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `CreateCFGScheduleFloatList` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `INTConstant` —— 2/10 个有
- `CR Text Concatenate` —— 1/10 个有
- `DF_Integer` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `RH_Captioner` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `SongGeneration_Sampler` —— 1/10 个有
- `SongGeneration_Stage1` —— 1/10 个有
- `SongGeneration_Stage2` —— 1/10 个有
- `Text` —— 1/10 个有
- `VHS_DuplicateImages` —— 1/10 个有
- `easy anythingIndexSwitch` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

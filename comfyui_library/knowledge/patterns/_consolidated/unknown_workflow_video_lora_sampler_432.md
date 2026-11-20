---
name: unknown_workflow_video_lora_sampler_432
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.765143
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/04-07-01-WAN2.2-数字人-InfiniteTalk-单人_1990969342198226945.json, 数字人/数字人/04-07-02-WAN2.2-数字人-InfiniteiTalk+UNI3C_1990969387870003201.json, 数字人/数字人/最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161.json, 视频生成/图生视频/Multitalk-图片+音频=MV_1936408506675154946.json, 视频生成/图生视频/Multitalk-音乐生成+图片=MV_1941728602893479937.json, 视频生成/图生视频/Multitalk（图片+音频）生成数字人视频_1937081431380119554.json, 视频生成/图生视频/最新数字人Multitalk-图片+音频=高质量数字人，支持唱歌唇形同步_1936210894722355202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_432

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/04-07-01-WAN2.2-数字人-InfiniteTalk-单人_1990969342198226945.json、数字人/数字人/04-07-02-WAN2.2-数字人-InfiniteiTalk+UNI3C_1990969387870003201.json、数字人/数字人/最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161.json、视频生成/图生视频/Multitalk-图片+音频=MV_1936408506675154946.json、视频生成/图生视频/Multitalk-音乐生成+图片=MV_1941728602893479937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanVideoEncode` —— 6/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/7 个有
- `WanVideoUni3C_embeds` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `ImpactSwitch` —— 5/7 个有
- `JWInteger` —— 5/7 个有
- `RHHiddenNodes` —— 5/7 个有
- `RH_LLMAPI_NODE` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `VHS_DuplicateImages` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `easy compare` —— 5/7 个有
- `easy ifElse` —— 5/7 个有
- `easy imageScaleDownToSize` —— 5/7 个有
- `easy imageSize` —— 5/7 个有
- `WanVideoApplyNAG` —— 4/7 个有
- `WanVideoEnhanceAVideo` —— 4/7 个有
- `WanVideoSLG` —— 4/7 个有
- `WanVideoTextEncodeSingle` —— 4/7 个有
- `CreateCFGScheduleFloatList` —— 3/7 个有
- `WanVideoSetBlockSwap` —— 3/7 个有
- `WanVideoSetLoRAs` —— 3/7 个有
- `WanVideoTextEncode` —— 3/7 个有
- `Anything Everywhere` —— 2/7 个有
- `FloatConstant` —— 2/7 个有
- `INTConstant` —— 2/7 个有
- `ImageUpscaleWithModel` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `Primitive string [Crystools]` —— 2/7 个有
- `RIFE VFI` —— 2/7 个有
- `UpscaleModelLoader` —— 2/7 个有
- `WanVideoContextOptions` —— 2/7 个有
- `WanVideoExperimentalArgs` —— 2/7 个有
- `ACEStepGen` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GenerationParameters` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `MultiLineLyrics` —— 1/7 个有
- `MultiLinePromptACES` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

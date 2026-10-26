---
name: unknown_workflow_video_lora_sampler_240
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.799222
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, ImageFromBatch+, ImpactSwitch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_LLMAPI_NODE, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/双人版-数字人InfiniteTalk -图片+音频=高质量数字人（支持超长时间）_1963963504116027393.json, 数字人/数字人/数字人infinitetalk（视频+音频驱动）_1958735631235067905.json, 数字人/数字人/数字人带货最强数字人infinitetalk（视频+音频驱动）支持长视频_1958311795096240130.json, 数字人/数字人/最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161.json, 数字人/数字人/最新数字人InfiniteTalk -图片+音频=高质量数字人（支持超长时间）_1957814463565066242.json, 视频生成/图生视频/Multitalk-图片+音频=MV_1936408506675154946.json, 视频生成/图生视频/Multitalk-音乐生成+图片=MV_1941728602893479937.json, 视频生成/图生视频/Multitalk（图片+音频）生成数字人视频_1937081431380119554.json, 视频生成/图生视频/最新数字人Multitalk-图片+音频=高质量数字人，支持唱歌唇形同步_1936210894722355202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_240

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/双人版-数字人InfiniteTalk -图片+音频=高质量数字人（支持超长时间）_1963963504116027393.json、数字人/数字人/数字人infinitetalk（视频+音频驱动）_1958735631235067905.json、数字人/数字人/数字人带货最强数字人infinitetalk（视频+音频驱动）支持长视频_1958311795096240130.json、数字人/数字人/最新Wan2.2 Multitalk数字人单人版-图片+音频=高质量数字人_1955987498365276161.json、数字人/数字人/最新数字人InfiniteTalk -图片+音频=高质量数字人（支持超长时间）_1957814463565066242.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `ImageFromBatch+`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_LLMAPI_NODE`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 8/9 个有
- `AudioCrop` —— 8/9 个有
- `easy compare` —— 8/9 个有
- `easy ifElse` —— 8/9 个有
- `easy imageScaleDownToSize` —— 8/9 个有
- `easy imageSize` —— 8/9 个有
- `GetNode` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `SetNode` —— 7/9 个有
- `RHHiddenNodes` —— 5/9 个有
- `VHS_DuplicateImages` —— 5/9 个有
- `WanVideoEncode` —— 5/9 个有
- `WanVideoImageToVideoEncode` —— 5/9 个有
- `WanVideoTextEncode` —— 5/9 个有
- `WanVideoUni3C_ControlnetLoader` —— 5/9 个有
- `WanVideoUni3C_embeds` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `PreviewAudio` —— 4/9 个有
- `WanVideoApplyNAG` —— 4/9 个有
- `WanVideoEnhanceAVideo` —— 4/9 个有
- `WanVideoImageToVideoMultiTalk` —— 4/9 个有
- `WanVideoTextEncodeSingle` —— 4/9 个有
- `JWIntegerToString` —— 3/9 个有
- `GetImagesFromBatchIndexed` —— 2/9 个有
- `ImageUpscaleWithModel` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `RIFE VFI` —— 2/9 个有
- `UpscaleModelLoader` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `WanVideoContextOptions` —— 2/9 个有
- `WanVideoExperimentalArgs` —— 2/9 个有
- `WanVideoSLG` —— 2/9 个有
- `ACEStepGen` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `CreateCFGScheduleFloatList` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GenerationParameters` —— 1/9 个有
- `MaskPreview+` —— 1/9 个有
- `MultiLineLyrics` —— 1/9 个有
- `MultiLinePromptACES` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `SaveAudio` —— 1/9 个有
- `SeparateMasks` —— 1/9 个有
- `WanVideoSetBlockSwap` —— 1/9 个有
- `WanVideoSetLoRAs` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

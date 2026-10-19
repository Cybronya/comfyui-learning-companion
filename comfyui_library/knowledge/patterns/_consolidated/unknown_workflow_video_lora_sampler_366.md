---
name: unknown_workflow_video_lora_sampler_366
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.942333
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1936361924722593793.json, 视频生成/图生视频/1958373813031485441.json, 视频生成/图生视频/1936354882708475905.json, 视频生成/图生视频/1936629963053256706.json, 视频生成/图生视频/1936154909266055170.json, 视频生成/图生视频/1936293743358038017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_366

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1936361924722593793.json、视频生成/图生视频/1958373813031485441.json、视频生成/图生视频/1936354882708475905.json、视频生成/图生视频/1936629963053256706.json、视频生成/图生视频/1936154909266055170.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 5/6 个有
- `WanVideoImageToVideoEncode` —— 5/6 个有
- `CreateCFGScheduleFloatList` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `WanVideoContextOptions` —— 4/6 个有
- `WanVideoEncode` —— 4/6 个有
- `WanVideoUni3C_ControlnetLoader` —— 4/6 个有
- `WanVideoUni3C_embeds` —— 4/6 个有
- `VHS_DuplicateImages` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `Audio Duration (mtb)` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `JWIntegerToString` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `WanVideoImageToVideoMultiTalk` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

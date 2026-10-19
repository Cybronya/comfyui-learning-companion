---
name: unknown_workflow_video_lora_sampler_52
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.82885
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1958425733460815874.json, 视频生成/图生视频/1995765952610447361.json, 视频生成/图生视频/1981723961920757761.json, 视频生成/图生视频/1960989551487594497.json, 视频生成/图生视频/1958729195713097730.json, 视频生成/图生视频/2016014882017120257.json, 视频生成/图生视频/1983918698648010754.json, 视频生成/图生视频/2026172210423013377.json, 视频生成/图生视频/2017268323733479425.json, 视频生成/图生视频/1981983249872371714.json, 视频生成/图生视频/1998792511760031746.json, 视频生成/图生视频/1999018182650290177.json, 视频生成/图生视频/2005664941799600130.json, 视频生成/图生视频/1980212523465084929.json, 视频生成/图生视频/2015232276317081602.json, 视频生成/图生视频/1981699993402785793.json, 视频生成/图生视频/2036305163903836161.json, 视频生成/图生视频/2046423290310303746.json, 视频生成/图生视频/2016403173090533378.json, 视频生成/图生视频/1995303342127689730.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_52

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/1958425733460815874.json、视频生成/图生视频/1995765952610447361.json、视频生成/图生视频/1981723961920757761.json、视频生成/图生视频/1960989551487594497.json、视频生成/图生视频/1958729195713097730.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 20 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 19/20 个有
- `GetImageSizeAndCount` —— 19/20 个有
- `JWInteger` —— 19/20 个有
- `PreviewAny` —— 19/20 个有
- `CR Prompt Text` —— 18/20 个有
- `LoadAudio` —— 18/20 个有
- `WanVideoBlockSwap` —— 18/20 个有
- `JWFloat` —— 13/20 个有
- `PreviewImage` —— 3/20 个有
- `ImageResize+` —— 2/20 个有
- `IndexTTS2Run` —— 2/20 个有
- `RH_Nano_Banana_Image2Image` —— 2/20 个有
- `RH_Translator` —— 2/20 个有
- `VHS_LoadVideoFFmpeg` —— 2/20 个有
- `VHS_VideoInfoLoaded` —— 2/20 个有
- `GetAudioDurationFromAudio` —— 1/20 个有
- `Label (rgthree)` —— 1/20 个有
- `PrimitiveString` —— 1/20 个有
- `SaveAudio` —— 1/20 个有
- `SimpleMath+` —— 1/20 个有
- `Text Multiline` —— 1/20 个有
- `VHS_LoadVideo` —— 1/20 个有
- `WanVideoTorchCompileSettings` —— 1/20 个有
- `easy showAnything` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

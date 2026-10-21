---
name: unknown_workflow_video_lora_sampler_40
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.845087
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1995765952610447361.json, 视频生成/图生视频/1981723961920757761.json, 视频生成/图生视频/2073246385209700353.json, 视频生成/图生视频/2073246674415349762.json, 视频生成/图生视频/1960989551487594497.json, 视频生成/图生视频/1958729195713097730.json, 视频生成/图生视频/2016014882017120257.json, 视频生成/图生视频/1983918698648010754.json, 视频生成/图生视频/2026172210423013377.json, 视频生成/图生视频/2017268323733479425.json, 视频生成/图生视频/1997484530254680066.json, 视频生成/图生视频/1981983249872371714.json, 视频生成/图生视频/2015681612746330114.json, 视频生成/图生视频/1998792511760031746.json, 视频生成/图生视频/1999018182650290177.json, 视频生成/图生视频/2005664941799600130.json, 视频生成/图生视频/1980212523465084929.json, 视频生成/图生视频/2015232276317081602.json, 视频生成/图生视频/1981699993402785793.json, 视频生成/图生视频/2036305163903836161.json, 视频生成/图生视频/2046423290310303746.json, 视频生成/图生视频/2016403173090533378.json, 视频生成/图生视频/1995303342127689730.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/1995765952610447361.json、视频生成/图生视频/1981723961920757761.json、视频生成/图生视频/2073246385209700353.json、视频生成/图生视频/2073246674415349762.json、视频生成/图生视频/1960989551487594497.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 23 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 22/23 个有
- `JWInteger` —— 22/23 个有
- `LoadAudio` —— 21/23 个有
- `WanVideoBlockSwap` —— 21/23 个有
- `CR Prompt Text` —— 20/23 个有
- `GetImageSizeAndCount` —— 20/23 个有
- `LoadWanVideoT5TextEncoder` —— 20/23 个有
- `PreviewAny` —— 20/23 个有
- `WanVideoTextEncode` —— 20/23 个有
- `JWFloat` —— 14/23 个有
- `PreviewImage` —— 4/23 个有
- `WanVideoTextEncodeCached` —— 3/23 个有
- `ImageResize+` —— 2/23 个有
- `RH_Nano_Banana_Image2Image` —— 2/23 个有
- `RH_Translator` —— 2/23 个有
- `VHS_LoadVideoFFmpeg` —— 2/23 个有
- `VHS_VideoInfoLoaded` —— 2/23 个有
- `WanVideoTorchCompileSettings` —— 2/23 个有
- `Anything Everywhere` —— 1/23 个有
- `Audio Duration (mtb)` —— 1/23 个有
- `IndexTTS2Run` —— 1/23 个有
- `JjkText` —— 1/23 个有
- `MathExpression|pysssss` —— 1/23 个有
- `PreviewAudio` —— 1/23 个有
- `Text Multiline` —— 1/23 个有
- `VHS_LoadVideo` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

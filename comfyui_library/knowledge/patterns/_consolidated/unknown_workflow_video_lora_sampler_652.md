---
name: unknown_workflow_video_lora_sampler_652
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.56875
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [图片生成/文生图/文字转音频+对口型+图生视频+标准1080P_1970453209825374209.json, 数字人/数字人/infiniteTalk单人v2v_2005939130049724418.json, 数字人/数字人/infiniteTalk多人图单人说话_2008829722586783746.json, 数字人/数字人/一键数字人对口型 Multitalk all for free V1.0_1979010362202820609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_652

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/文字转音频+对口型+图生视频+标准1080P_1970453209825374209.json、数字人/数字人/infiniteTalk单人v2v_2005939130049724418.json、数字人/数字人/infiniteTalk多人图单人说话_2008829722586783746.json、数字人/数字人/一键数字人对口型 Multitalk all for free V1.0_1979010362202820609.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadWav2VecModel` —— 3/4 个有
- `GetImageRangeFromBatch` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `MelBandRoFormerModelLoader` —— 2/4 个有
- `MelBandRoFormerSampler` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `IndexTTS2Run` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `MaskPreview` —— 1/4 个有
- `Sa2VANodeTpl` —— 1/4 个有
- `SaveAudio` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `ZML_TextInput` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

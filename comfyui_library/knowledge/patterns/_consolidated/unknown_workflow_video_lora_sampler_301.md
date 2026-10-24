---
name: unknown_workflow_video_lora_sampler_301
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.721571
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk数字人-基础视频生成_1975057390238306306.json, 视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json, 视频生成/图生视频/Wan2.1对口型数字人_2054610077646114818.json, 视频生成/图生视频/Wan21Animate高质量丝滑单人数字人_1993501240730599426.json, 视频生成/图生视频/数字人 InfiniTetalk 音频+图片GGUF_2012499953494528001.json, 视频生成/图生视频/无限时长多人数字人-InfiniteTalkd多人图生视频_1958125817404542978.json, 视频生成/图生视频/无限时长音乐数字人-InfiniteTalk单人图生视频_1958125770365423618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_301

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk数字人-基础视频生成_1975057390238306306.json、视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json、视频生成/图生视频/Wan2.1对口型数字人_2054610077646114818.json、视频生成/图生视频/Wan21Animate高质量丝滑单人数字人_1993501240730599426.json、视频生成/图生视频/数字人 InfiniTetalk 音频+图片GGUF_2012499953494528001.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 6/7 个有
- `GetImageSizeAndCount` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `WanVideoTextEncodeCached` —— 5/7 个有
- `INTConstant` —— 3/7 个有
- `JWInteger` —— 3/7 个有
- `LoadWanVideoT5TextEncoder` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `WanVideoTextEncode` —— 2/7 个有
- `Audio Duration (mtb)` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `DF_Int_to_Float` —— 1/7 个有
- `IndexTTSNode` —— 1/7 个有
- `JWIntegerToString` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PixaromaLabel` —— 1/7 个有
- `PixaromaResolution` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `RH_Translator` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

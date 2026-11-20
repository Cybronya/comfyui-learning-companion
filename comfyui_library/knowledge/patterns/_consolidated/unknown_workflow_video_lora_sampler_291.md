---
name: unknown_workflow_video_lora_sampler_291
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9746
common_nodes: [DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/infinite+wan2.1多人对口型_1960541577531842561.json, 视频生成/图生视频/双人对话对口型_1994221474806513665.json, 视频生成/图生视频/口播唱歌数字人InfiniteTalk 对口型_1970330754632851457.json, 视频生成/图生视频/图生视频-基于InfiniteTalk_2005465061298761730.json, 视频生成/图生视频/对嘴型·数字人·影视·唱歌·讲话对口型·超自然现实有喘息细节_2015414691312443393.json, 视频生成/图生视频/情歌对唱妹妹坐船头_1989787883399729154.json, 视频生成/图生视频/打大富翁_1990048687038623745.json, 视频生成/图生视频/数字人_Aiwood-infinitetalk双人对话_1978726455507095554.json, 视频生成/图生视频/数字人_Aiwood-infinitetalk双人对话_2009633003546353665.json, 视频生成/文生视频/数字人对口型深情歌唱_1989702067088486402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_291

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/infinite+wan2.1多人对口型_1960541577531842561.json、视频生成/图生视频/双人对话对口型_1994221474806513665.json、视频生成/图生视频/口播唱歌数字人InfiniteTalk 对口型_1970330754632851457.json、视频生成/图生视频/图生视频-基于InfiniteTalk_2005465061298761730.json、视频生成/图生视频/对嘴型·数字人·影视·唱歌·讲话对口型·超自然现实有喘息细节_2015414691312443393.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 9/10 个有
- `CLIPVisionLoader` —— 9/10 个有
- `WanVideoClipVisionEncode` —— 9/10 个有
- `AudioSeparation` —— 7/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `INTConstant` —— 5/10 个有
- `SeparateMasks` —— 5/10 个有
- `PreviewAudio` —— 4/10 个有
- `Anything Everywhere` —— 3/10 个有
- `MaskPreview+` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `AudioPlay` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `孤海图像缩放按像素` —— 2/10 个有
- `GetImageSize` —— 1/10 个有
- `ImageScaleToMegapixels` —— 1/10 个有
- `MaskPreview` —— 1/10 个有
- `UpscaleModelLoader` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

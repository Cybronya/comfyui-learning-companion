---
name: unknown_workflow_video_sampler_vae_56
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.958
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/情歌对唱妹妹坐船头_1989787883399729154.json, 视频生成/图生视频/打大富翁_1990048687038623745.json, 视频生成/图生视频/数字人-InfiniteTalk-单人对口型工作流_2051262997816983554.json, 视频生成/图生视频/数字人_Aiwood-infinitetalk双人对话_1978726455507095554.json, 视频生成/图生视频/数字人_Aiwood-infinitetalk双人对话_2009633003546353665.json, 视频生成/文生视频/InfiniteTalk对口型_1963933041288728578.json, 视频生成/文生视频/数字人对口型深情歌唱_1989702067088486402.json, 视频生成/文生视频/最强数字人infinitetalk（图片唱歌图片说话）_1957952304787898369.json, 音频生成/音频生成/标准版图生单多人讲话工作流_2030914032869318658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_56

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/情歌对唱妹妹坐船头_1989787883399729154.json、视频生成/图生视频/打大富翁_1990048687038623745.json、视频生成/图生视频/数字人-InfiniteTalk-单人对口型工作流_2051262997816983554.json、视频生成/图生视频/数字人_Aiwood-infinitetalk双人对话_1978726455507095554.json、视频生成/图生视频/数字人_Aiwood-infinitetalk双人对话_2009633003546353665.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 8/9 个有
- `WanVideoLoraSelect` —— 8/9 个有
- `AudioSeparation` —— 6/9 个有
- `INTConstant` —— 4/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `PreviewAudio` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `Anything Everywhere` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `SeparateMasks` —— 3/9 个有
- `AudioPlay` —— 2/9 个有
- `MaskPreview+` —— 2/9 个有
- `孤海图像缩放按像素` —— 2/9 个有
- `MaskPreview` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

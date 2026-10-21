---
name: unknown_workflow_video_sampler_vae_54
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.948333
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1989787883399729154.json, 视频生成/图生视频/1990048687038623745.json, 视频生成/图生视频/2051262997816983554.json, 视频生成/图生视频/2051497728395489282.json, 视频生成/文生视频/图生视频 数字人 InfiniteTalk 多人对口型 动作模仿_2044640516272295938.json, 视频生成/文生视频/数字人对口型深情歌唱_1989702067088486402.json, 音频生成/音频生成/数字人-InfiniteTalk-视频对口型工作流_2051512102539538434.json, 音频生成/音频生成/标准版图生单多人讲话工作流_2030914032869318658.json, 音频生成/音频生成/视频单人对口型_2029818322556035074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_54

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1989787883399729154.json、视频生成/图生视频/1990048687038623745.json、视频生成/图生视频/2051262997816983554.json、视频生成/图生视频/2051497728395489282.json、视频生成/文生视频/图生视频 数字人 InfiniteTalk 多人对口型 动作模仿_2044640516272295938.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `AudioSeparation` —— 6/9 个有
- `PreviewAudio` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `WanVideoLoraSelect` —— 5/9 个有
- `WanVideoLoraSelectMulti` —— 4/9 个有
- `Anything Everywhere` —— 3/9 个有
- `SeparateMasks` —— 3/9 个有
- `AudioPlay` —— 2/9 个有
- `ImageConcanate` —— 2/9 个有
- `LayerMask: MaskPreview` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `WanVideoEncode` —— 2/9 个有
- `孤海图像缩放按像素` —— 2/9 个有
- `MaskPreview` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

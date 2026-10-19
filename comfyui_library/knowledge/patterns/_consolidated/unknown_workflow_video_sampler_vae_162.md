---
name: unknown_workflow_video_sampler_vae_162
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.971
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2065613874346418178.json, 视频生成/文生视频/1958330393214783490.json, 视频生成/文生视频/数字人对口型深情歌唱_1989702067088486402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_162

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2065613874346418178.json、视频生成/文生视频/1958330393214783490.json、视频生成/文生视频/数字人对口型深情歌唱_1989702067088486402.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `ImageResizeKJv2` —— 2/3 个有
- `MultiTalkModelLoader` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `AudioCrop` —— 1/3 个有
- `AudioCropProcessUTK` —— 1/3 个有
- `AudioPlay` —— 1/3 个有
- `MelBandRoFormerModelLoader` —— 1/3 个有
- `MelBandRoFormerSampler` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `孤海图像缩放按像素` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

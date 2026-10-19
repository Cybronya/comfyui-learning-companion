---
name: unknown_workflow_video_lora_sampler_202
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7321
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1989787883399729154.json, 视频生成/图生视频/1990048687038623745.json, 视频生成/图生视频/2051262997816983554.json, 视频生成/图生视频/数字人口播_2106320471296925698.json, 视频生成/文生视频/【语言切换】数字人口型驱动自然增强版_2072520224041168898.json, 视频生成/文生视频/声音克隆数字人对口型单人图像驱动_可编辑_精简稳定版_稍快版_2076654319981654018.json, 视频生成/文生视频/我的数字人口播3_2095509150016040961.json, 视频生成/文生视频/我的数字人口播_2076595656273260545.json, 视频生成/文生视频/数字人口播_2106320471296925698.json, 音频生成/音频生成/3秒声音克隆+超自然数字人对口型_2037720604018741250.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_202

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1989787883399729154.json、视频生成/图生视频/1990048687038623745.json、视频生成/图生视频/2051262997816983554.json、视频生成/图生视频/数字人口播_2106320471296925698.json、视频生成/文生视频/【语言切换】数字人口型驱动自然增强版_2072520224041168898.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 10 个 workflow 都包含：
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `AudioSeparation` —— 8/10 个有
- `PreviewAudio` —— 8/10 个有
- `Anything Everywhere` —— 7/10 个有
- `Audio Duration (mtb)` —— 7/10 个有
- `GetImageRangeFromBatch` —— 7/10 个有
- `MathExpression|pysssss` —— 7/10 个有
- `easy int` —— 7/10 个有
- `IndexTTS2Run` —— 6/10 个有
- `PlaySound|pysssss` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `GetNode` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `LogicUtil_SleepNodeAny` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `AudioPlay` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `LatentUpscale` —— 1/10 个有
- `MaskPreview` —— 1/10 个有
- `SeparateMasks` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `孤海图像缩放按像素` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

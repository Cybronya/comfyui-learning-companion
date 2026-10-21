---
name: unknown_workflow_video_sampler_vae_23
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.878077
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1987166609188040706.json, 视频生成/图生视频/1958063092703907841.json, 视频生成/图生视频/2014497648656523265.json, 视频生成/图生视频/1988439303661469698.json, 视频生成/图生视频/2003092894418370562.json, 视频生成/图生视频/2018702863702167554.json, 视频生成/图生视频/2018674445128310785.json, 视频生成/图生视频/1985744717117890562.json, 视频生成/图生视频/2014949900475174914.json, 视频生成/图生视频/2061786776032866305.json, 视频生成/图生视频/2081267787426787330.json, 视频生成/图生视频/Infinite数字人对口型（音频驱动 表情自然 可编辑动作）_2110374253521625090.json, 视频生成/图生视频/2011801795986722818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1987166609188040706.json、视频生成/图生视频/1958063092703907841.json、视频生成/图生视频/2014497648656523265.json、视频生成/图生视频/1988439303661469698.json、视频生成/图生视频/2003092894418370562.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 12/13 个有
- `LoadWanVideoT5TextEncoder` —— 12/13 个有
- `WanVideoLoraSelect` —— 12/13 个有
- `WanVideoTextEncode` —— 12/13 个有
- `AudioSeparation` —— 11/13 个有
- `GetImageSizeAndCount` —— 11/13 个有
- `JWInteger` —— 11/13 个有
- `PreviewAny` —— 11/13 个有
- `CR Prompt Text` —— 10/13 个有
- `JWFloat` —— 9/13 个有
- `easy showAnything` —— 5/13 个有
- `AudioToFPS` —— 4/13 个有
- `LayerUtility: PurgeVRAM V2` —— 4/13 个有
- `SimpleMath+` —— 3/13 个有
- `INTConstant` —— 2/13 个有
- `Audio Duration (mtb)` —— 1/13 个有
- `Float` —— 1/13 个有
- `GrowMaskWithBlur` —— 1/13 个有
- `MaskPreview+` —— 1/13 个有
- `PrimitiveFloat` —— 1/13 个有
- `RH_GetAudioDuration` —— 1/13 个有
- `Sa2VANodeTpl` —— 1/13 个有
- `ToInt` —— 1/13 个有
- `WanVideoLoraSelectMulti` —— 1/13 个有
- `WanVideoTextEncodeCached` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

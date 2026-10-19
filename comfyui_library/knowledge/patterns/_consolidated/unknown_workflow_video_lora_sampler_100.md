---
name: unknown_workflow_video_lora_sampler_100
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.8598
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1988439303661469698.json, 视频生成/图生视频/2003092894418370562.json, 视频生成/图生视频/1969944110868164610.json, 视频生成/图生视频/2018702863702167554.json, 视频生成/图生视频/2018674445128310785.json, 视频生成/图生视频/1985744717117890562.json, 视频生成/图生视频/2061786776032866305.json, 视频生成/图生视频/2081267787426787330.json, 视频生成/图生视频/Infinite数字人对口型（音频驱动 表情自然 可编辑动作）_2110374253521625090.json, 视频生成/图生视频/2011699798700728322.json, 视频生成/图生视频/2011801795986722818.json, 视频生成/图生视频/乔帮主-对口型数字人 最强音色克隆带语气情感 音频生成 数字人 声音克隆  情绪参考   Infinite+_2086424507589423105.json, 视频生成/图生视频/2016109597077020673.json, 视频生成/图生视频/2082392926398799873.json, 视频生成/图生视频/1996720816832270337.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_100

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/1988439303661469698.json、视频生成/图生视频/2003092894418370562.json、视频生成/图生视频/1969944110868164610.json、视频生成/图生视频/2018702863702167554.json、视频生成/图生视频/2018674445128310785.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `AudioCrop` —— 13/15 个有
- `AudioSeparation` —— 13/15 个有
- `CR Prompt Text` —— 13/15 个有
- `JWInteger` —— 13/15 个有
- `PreviewAny` —— 13/15 个有
- `JWFloat` —— 12/15 个有
- `easy showAnything` —— 6/15 个有
- `AudioToFPS` —— 5/15 个有
- `LayerUtility: PurgeVRAM V2` —— 5/15 个有
- `PrimitiveFloat` —— 2/15 个有
- `GrowMaskWithBlur` —— 1/15 个有
- `INTConstant` —— 1/15 个有
- `MaskPreview+` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有
- `RH_GetAudioDuration` —— 1/15 个有
- `Sa2VANodeTpl` —— 1/15 个有
- `SimpleMath+` —— 1/15 个有
- `ToInt` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

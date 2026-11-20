---
name: unknown_workflow_video_lora_vae_3
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9655
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Aiwood-首发Multitalk多人对话_1940854355119730690.json, 数字人/数字人/Multitalk多人对话（超级版）_1941152199026307073.json, 数字人/数字人/数字人图片对口型_2027596633734647810.json, 数字人/数字人/最强数字人InfiniteTalk_1981009825838546946.json, 数字人/数字人/超逼真多人对话数字人-KJ-MultiTalk_1940916699317354497.json, 视频生成/图生视频/Aiwood-infinitetalk双人对话_1957826997610446849.json, 视频生成/图生视频/INF双人对话_1971453748994359297.json, 视频生成/图生视频/InfiniteTalk-wan-双人-index tts_1958085210749415426.json, 视频生成/图生视频/Multitalk三人多人对话+Radial Attention加速_1948369611300438017.json, 视频生成/图生视频/Multitalk双人对唱数字人_1941678134205038593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_3

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/Aiwood-首发Multitalk多人对话_1940854355119730690.json、数字人/数字人/Multitalk多人对话（超级版）_1941152199026307073.json、数字人/数字人/数字人图片对口型_2027596633734647810.json、数字人/数字人/最强数字人InfiniteTalk_1981009825838546946.json、数字人/数字人/超逼真多人对话数字人-KJ-MultiTalk_1940916699317354497.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiTalkWav2VecEmbeds` —— 9/10 个有
- `WanVideoImageToVideoMultiTalk` —— 9/10 个有
- `WanVideoSampler` —— 9/10 个有
- `SeparateMasks` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `AudioCrop` —— 6/10 个有
- `AudioSeparation` —— 6/10 个有
- `MaskPreview+` —— 6/10 个有
- `WanVideoTextEncode` —— 6/10 个有
- `PreviewAudio` —— 4/10 个有
- `SaveAudioMP3` —— 4/10 个有
- `WanVideoApplyNAG` —— 4/10 个有
- `WanVideoTextEncodeSingle` —— 4/10 个有
- `EsesImageEffectBloom` —— 3/10 个有
- `INTConstant` —— 2/10 个有
- `MaskPreview` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `IndexTTSNode` —— 1/10 个有
- `Primitive integer [Crystools]` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `StringToInt` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `WanVideoSetRadialAttention` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

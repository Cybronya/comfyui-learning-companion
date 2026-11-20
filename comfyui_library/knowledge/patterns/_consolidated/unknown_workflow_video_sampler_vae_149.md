---
name: unknown_workflow_video_sampler_vae_149
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.749333
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/人物对口型_2035299713183916034.json, 数字人/数字人/03-09-01-WAN2.1-数字人-MultiTalk-单人-kijai_1989933367212822530.json, 数字人/数字人/03-09-03-WAN2.1-数字人-MultiTalk+indextts-双人-kijai_1989933411018133506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_149

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/人物对口型_2035299713183916034.json、数字人/数字人/03-09-01-WAN2.1-数字人-MultiTalk-单人-kijai_1989933367212822530.json、数字人/数字人/03-09-03-WAN2.1-数字人-MultiTalk+indextts-双人-kijai_1989933411018133506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `JWIntegerToString` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `MegaTTS3Run` —— 1/3 个有
- `MultiLinePromptMG` —— 1/3 个有
- `SaveAudioMP3` —— 1/3 个有
- `SeparateMasks` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

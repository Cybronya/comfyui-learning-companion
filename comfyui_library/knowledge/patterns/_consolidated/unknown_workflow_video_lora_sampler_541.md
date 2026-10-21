---
name: unknown_workflow_video_lora_sampler_541
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.81675
common_nodes: [CLIPVisionLoader, CR Prompt Text, GetImageSizeAndCount, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkSilentEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1970454402555408386.json, 视频生成/图生视频/1965504800706187266.json, 视频生成/图生视频/2005591443018317826.json, 音频生成/音频生成/数字人对口型Wan+Inifinte Talk无限时长_1967102112964468737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_541

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1970454402555408386.json、视频生成/图生视频/1965504800706187266.json、视频生成/图生视频/2005591443018317826.json、音频生成/音频生成/数字人对口型Wan+Inifinte Talk无限时长_1967102112964468737.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `GetImageSizeAndCount`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkSilentEmbeds`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `DF_Int_to_Float` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

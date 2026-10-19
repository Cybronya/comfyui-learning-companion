---
name: unknown_workflow_video_lora_sampler_611
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.942667
common_nodes: [ComfyNumberConvert, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LongCatAvatarWhisperEmbeds, TrimAudioDuration, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLongCatAvatarExtendEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2059078929838854146.json, 视频生成/图生视频/2059921141237641218.json, 视频生成/图生视频/longcatAvatar1.5 图片数字人v1_2106246745930944513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_611

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2059078929838854146.json、视频生成/图生视频/2059921141237641218.json、视频生成/图生视频/longcatAvatar1.5 图片数字人v1_2106246745930944513.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ComfyNumberConvert`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LongCatAvatarWhisperEmbeds`
- `TrimAudioDuration`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLongCatAvatarExtendEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `Int` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `Text` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

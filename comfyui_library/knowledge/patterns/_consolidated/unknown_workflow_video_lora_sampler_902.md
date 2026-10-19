---
name: unknown_workflow_video_lora_sampler_902
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.963
common_nodes: [CLIPVisionLoader, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/2011076540066439169.json, 视频生成/文生视频/卡通数字人_2086779135497687042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_902

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2011076540066439169.json、视频生成/文生视频/卡通数字人_2086779135497687042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadAudio`
- `LoadImage`
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LogicUtil_CeilNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

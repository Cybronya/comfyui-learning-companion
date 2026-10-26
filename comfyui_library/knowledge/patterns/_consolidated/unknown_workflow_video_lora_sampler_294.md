---
name: unknown_workflow_video_lora_sampler_294
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.99075
common_nodes: [CLIPVisionLoader, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/AI数字人-动物_2084929827878031362.json, 视频生成/图生视频/Unipus-AI数字人_2071856835908427777.json, 视频生成/图生视频/Unipus-AI数字人_2072507975016738818.json, 视频生成/图生视频/Unipus-AI数字人_2072619753109278721.json, 视频生成/图生视频/Unipus-AI数字人_2074016139532918786.json, 视频生成/图生视频/写实数字人_2073956730425401346.json, 视频生成/图生视频/数字人音频驱动模型 Inifinte Talk  Wan 2.1 i2v 480p Worfklow_2011076540066439169.json, 视频生成/文生视频/卡通数字人_2086779135497687042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_294

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/AI数字人-动物_2084929827878031362.json、视频生成/图生视频/Unipus-AI数字人_2071856835908427777.json、视频生成/图生视频/Unipus-AI数字人_2072507975016738818.json、视频生成/图生视频/Unipus-AI数字人_2072619753109278721.json、视频生成/图生视频/Unipus-AI数字人_2074016139532918786.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
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
- `Audio Duration` —— 7/8 个有
- `ComfyMathExpression` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `LogicUtil_CeilNode` —— 5/8 个有
- `GetImageSize` —— 1/8 个有
- `ImageScale` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

---
name: unknown_workflow_video_lora_sampler_555
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6975
common_nodes: [LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [Image Crop Face, CR Text, CR Text Concatenate, MathExpression|pysssss, easy int]
members: [视频生成/文生视频/1976007633784147970.json, 视频生成/文生视频/1976487534681300993.json, 视频生成/文生视频/2073283173435588608.json, 视频生成/文生视频/lynx基础流程ID一致性文生视频_2072999523280265216.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_555

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1976007633784147970.json、视频生成/文生视频/1976487534681300993.json、视频生成/文生视频/2073283173435588608.json、视频生成/文生视频/lynx基础流程ID一致性文生视频_2072999523280265216.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Crop Face` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `RMBG` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Image Crop Face、CR Text、CR Text Concatenate、MathExpression|pysssss、easy int

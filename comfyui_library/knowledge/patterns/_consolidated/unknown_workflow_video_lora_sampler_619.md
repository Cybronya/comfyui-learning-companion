---
name: unknown_workflow_video_lora_sampler_619
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.66125
common_nodes: [LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, PreviewImage, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/lynx基础流程ID一致性文生视频_1975835025436487681.json, 视频生成/文生视频/lynx标准工作流_1975939269380452353.json, 视频生成/文生视频/人脸一致-文生视频-lynx_1976487534681300993.json, 视频生成/文生视频/文生图角色一致性——Lynx_1977745156428496897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_619

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/lynx基础流程ID一致性文生视频_1975835025436487681.json、视频生成/文生视频/lynx标准工作流_1975939269380452353.json、视频生成/文生视频/人脸一致-文生视频-lynx_1976487534681300993.json、视频生成/文生视频/文生图角色一致性——Lynx_1977745156428496897.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：66%

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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SetNode` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `RMBG` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

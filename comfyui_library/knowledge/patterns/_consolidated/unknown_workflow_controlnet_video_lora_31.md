---
name: unknown_workflow_controlnet_video_lora_31
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93675
common_nodes: [CR String To Combo, GetImagesFromBatchIndexed, ImageConcanate, ImageResizeKJ, ImageResizeKJv2, Int2String, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Primitive integer [Crystools], RH_Captioner, RunningHub OmniConsistency LoraLoader, RunningHub OmniConsistency Sampler, SaveImage, Text Concatenate, TextSwitchCase, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/视频风格转绘2.0-22种风格--Uni3C+OmniConsistency+FusionX_1929065895359057921.json, 平台全量/视频风格转绘2.0-22种风格_1971860768574664705.json, 平台全量/视频风格转绘5.0-24种风格_1996835691264974849.json, 平台全量/金_2037905340401983490.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_31

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频风格转绘2.0-22种风格--Uni3C+OmniConsistency+FusionX_1929065895359057921.json、平台全量/视频风格转绘2.0-22种风格_1971860768574664705.json、平台全量/视频风格转绘5.0-24种风格_1996835691264974849.json、平台全量/金_2037905340401983490.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CR String To Combo`
- `GetImagesFromBatchIndexed`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `Int2String`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `RunningHub OmniConsistency LoraLoader`
- `RunningHub OmniConsistency Sampler`
- `SaveImage`
- `Text Concatenate`
- `TextSwitchCase`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraModelLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

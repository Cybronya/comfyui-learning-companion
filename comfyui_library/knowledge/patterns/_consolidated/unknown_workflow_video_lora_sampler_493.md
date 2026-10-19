---
name: unknown_workflow_video_lora_sampler_493
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.49025
common_nodes: [FloatConstant, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchExtendWithOverlap, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1986678094163542018.json, 视频生成/图生视频/1985530198026297346.json, 视频生成/图生视频/1988142072014266369.json, 视频生成/文生视频/LongCat_T2V_full_automatic_1985535936635224065.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_493

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1986678094163542018.json、视频生成/图生视频/1985530198026297346.json、视频生成/图生视频/1988142072014266369.json、视频生成/文生视频/LongCat_T2V_full_automatic_1985535936635224065.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 4 个 workflow 都包含：
- `FloatConstant`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `easy forLoopEnd` —— 3/4 个有
- `easy forLoopStart` —— 3/4 个有
- `easy promptLine` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text Replace` —— 1/4 个有
- `Int` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `ToString` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

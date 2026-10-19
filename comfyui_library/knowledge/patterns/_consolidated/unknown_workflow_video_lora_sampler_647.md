---
name: unknown_workflow_video_lora_sampler_647
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.932
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1951139393090334722.json, 视频生成/图生视频/2056763668582461441.json, 视频生成/图生视频/1955612950611443714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_647

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1951139393090334722.json、视频生成/图生视频/2056763668582461441.json、视频生成/图生视频/1955612950611443714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `WanVideoSetBlockSwap` —— 2/3 个有
- `WanVideoSetLoRAs` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Wan22PromptSelector` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

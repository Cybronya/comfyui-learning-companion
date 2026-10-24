---
name: unknown_workflow_video_lora_sampler_810
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, SimpleMath+, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频-自动生成动态提示词_1951139393090334722.json, 视频生成/图生视频/smooth-kj_2056763668582461441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_810

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频-自动生成动态提示词_1951139393090334722.json、视频生成/图生视频/smooth-kj_2056763668582461441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
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
- `RH_Captioner` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `Wan22PromptSelector` —— 1/2 个有
- `WanVideoSetBlockSwap` —— 1/2 个有
- `WanVideoSetLoRAs` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

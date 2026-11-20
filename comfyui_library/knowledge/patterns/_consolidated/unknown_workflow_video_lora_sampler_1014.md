---
name: unknown_workflow_video_lora_sampler_1014
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.949
common_nodes: [Int, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/QwenVL图片反推提示词-图生视频KJ工作流_1983484440976531458.json, 视频生成/文生视频/Wan2.2文生视频-Kijai优化版_1950891815438327809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1014

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/QwenVL图片反推提示词-图生视频KJ工作流_1983484440976531458.json、视频生成/文生视频/Wan2.2文生视频-Kijai优化版_1950891815438327809.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `Int`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiplePathsInput` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `VideoLoader` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

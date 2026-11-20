---
name: unknown_workflow_video_upscale_lora_44
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [LoadWanVideoT5TextEncoder, RIFE VFI, VHS_VideoCombine, Video_Upscale_With_Model, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoVRAMManagement]
problems: []
missing: []
members: [视频生成/文生视频/kijai_wanvideo_T2V_selfforcing5_14b 文生视频_1934871279478448130.json, 视频生成/文生视频/【阿辉聊AI】Self Forcing极速文生视频工作流_1935156530729951234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_44

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/kijai_wanvideo_T2V_selfforcing5_14b 文生视频_1934871279478448130.json、视频生成/文生视频/【阿辉聊AI】Self Forcing极速文生视频工作流_1935156530729951234.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
- `VHS_VideoCombine`
- `Video_Upscale_With_Model`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

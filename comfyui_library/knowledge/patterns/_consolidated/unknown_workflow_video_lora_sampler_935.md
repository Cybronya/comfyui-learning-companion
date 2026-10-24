---
name: unknown_workflow_video_lora_sampler_935
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [INTConstant, LoadWanVideoT5TextEncoder, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/WAN2.2-AllInOne文生视频_1963909620598394882.json, 视频生成/文生视频/WAN2.2-AllInOne首尾帧_1963907661271224322.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_935

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/WAN2.2-AllInOne文生视频_1963909620598394882.json、视频生成/文生视频/WAN2.2-AllInOne首尾帧_1963907661271224322.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

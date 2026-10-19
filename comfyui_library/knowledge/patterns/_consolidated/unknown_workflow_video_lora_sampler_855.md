---
name: unknown_workflow_video_lora_sampler_855
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6415
common_nodes: [Anything Everywhere, Divide [DVB], GetNode, LoadWanVideoT5TextEncoder, SetNode, Textbox, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, mxSlider]
problems: []
missing: []
members: [视频生成/图生视频/1957436481176530945.json, 视频生成/文生视频/1955628048441905154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_855

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1957436481176530945.json、视频生成/文生视频/1955628048441905154.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Divide [DVB]`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `Textbox`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `mxSlider`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

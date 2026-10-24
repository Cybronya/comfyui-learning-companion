---
name: unknown_workflow_video_lora_sampler_945
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.866
common_nodes: [CR Text Replace, Int, PrimitiveBoolean, SimpleMath+, TextBox, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy ifElse]
problems: []
missing: []
members: [视频生成/文生视频/wan2_2_fun_vace+MiniCPM_视频反推_文生视频-KJ_1970315752047865858.json, 视频生成/文生视频/wan2_2_fun_vace_文生视频-自动提示词-KJ_1971918446537666562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_945

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/wan2_2_fun_vace+MiniCPM_视频反推_文生视频-KJ_1970315752047865858.json、视频生成/文生视频/wan2_2_fun_vace_文生视频-自动提示词-KJ_1971918446537666562.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text Replace`
- `Int`
- `PrimitiveBoolean`
- `SimpleMath+`
- `TextBox`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V_Advanced` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

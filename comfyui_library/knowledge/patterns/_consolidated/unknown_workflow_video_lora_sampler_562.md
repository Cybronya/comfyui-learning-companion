---
name: unknown_workflow_video_lora_sampler_562
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90125
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1956922387473076226.json, 视频生成/文生视频/1957002960897236994.json, 视频生成/文生视频/StandIn人物一致性_2072999632508329984.json, 视频生成/文生视频/1956683255350005762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_562

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1956922387473076226.json、视频生成/文生视频/1957002960897236994.json、视频生成/文生视频/StandIn人物一致性_2072999632508329984.json、视频生成/文生视频/1956683255350005762.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/4 个有
- `CR Text Replace` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `RH_Prompter` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `TextBox` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

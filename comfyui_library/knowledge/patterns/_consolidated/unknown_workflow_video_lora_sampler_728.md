---
name: unknown_workflow_video_lora_sampler_728
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9705
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, EmptyHunyuanLatentVideo, FSampler, KSamplerSelect, Label (rgthree), LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SamplerCustom, SplitSigmas, TorchCompileModelWanVideoV2, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: [Label (rgthree)]
members: [视频生成/图生视频/1977282385228242946.json, 视频生成/文生视频/1977282385228242946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_728

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1977282385228242946.json、视频生成/文生视频/1977282385228242946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `EmptyHunyuanLatentVideo`
- `FSampler`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SplitSigmas`
- `TorchCompileModelWanVideoV2`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

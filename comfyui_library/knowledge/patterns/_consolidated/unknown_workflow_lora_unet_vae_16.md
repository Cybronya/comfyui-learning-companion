---
name: unknown_workflow_lora_unet_vae_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6095
common_nodes: [BlockSparseAttention, CLIPLoader, H3LongVideo, H3VideoPromptPlan, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelAttentionBackend, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [平台全量/H3 长视频API_2117442471532781570.json, 平台全量/H3-长视频_2117786837837242369.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/H3 长视频API_2117442471532781570.json、平台全量/H3-长视频_2117786837837242369.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockSparseAttention`
- `CLIPLoader`
- `H3LongVideo`
- `H3VideoPromptPlan`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelAttentionBackend`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

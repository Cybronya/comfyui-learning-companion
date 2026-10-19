---
name: unknown_workflow_lora_sampler_unet_56
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.986
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax+H3_Native_vs_DMAD文生视频_2106242276044394498.json, 视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json, 视频生成/文生视频/Minimax+H3_Native_vs_DMAD文生视频_2106242276044394498.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_56

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Minimax+H3_Native_vs_DMAD文生视频_2106242276044394498.json、视频生成/图生视频/四步极速文生视频stableyogi-h3-pdmd-4step_2108569415804608514.json、视频生成/文生视频/Minimax+H3_Native_vs_DMAD文生视频_2106242276044394498.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `Int` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

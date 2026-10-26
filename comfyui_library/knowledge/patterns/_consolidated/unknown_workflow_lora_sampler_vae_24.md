---
name: unknown_workflow_lora_sampler_vae_24
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.904
common_nodes: [BasicGuider, BasicScheduler, DeepTranslatorTextNode, DetailDaemonSamplerNode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/JoyCaption3超强反推+双截棍快速出图_1922580731393097729.json, 图片生成/文生图/Nunchaku速度提升3倍工作流_1910162390728568834.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/JoyCaption3超强反推+双截棍快速出图_1922580731393097729.json、图片生成/文生图/Nunchaku速度提升3倍工作流_1910162390728568834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DeepTranslatorTextNode`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `CLIPTextEncodeFlux` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `JJC_JoyCaption` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SDXLAspectRatioSelector` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 1024 | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 1024，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

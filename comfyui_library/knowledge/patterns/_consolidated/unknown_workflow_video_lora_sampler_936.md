---
name: unknown_workflow_video_lora_sampler_936
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9155
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, SimpleMath+, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy int]
problems: []
missing: []
members: [视频生成/文生视频/WAN22运动性3xKsampler高速工作流_1959177557772021762.json, 视频生成/文生视频/【老金驿站】提升WAN22运动性3xKsampler高速工作流_1965219730770546689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_936

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/WAN22运动性3xKsampler高速工作流_1959177557772021762.json、视频生成/文生视频/【老金驿站】提升WAN22运动性3xKsampler高速工作流_1965219730770546689.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SimpleMath+`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CLIPLoaderGGUF` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | 2.25 | - | 2 | 44% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

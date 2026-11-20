---
name: unknown_workflow_video_lora_sampler_895
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.902
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, SimpleMath+, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频超级加速_1955793674186604546.json, 视频生成/文生视频/WAN22运动性3xKsampler高速工作流_1959177557772021762.json, 视频生成/文生视频/【老金驿站】提升WAN22运动性3xKsampler高速工作流_1965219730770546689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_895

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频超级加速_1955793674186604546.json、视频生成/文生视频/WAN22运动性3xKsampler高速工作流_1959177557772021762.json、视频生成/文生视频/【老金驿站】提升WAN22运动性3xKsampler高速工作流_1965219730770546689.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `SimpleMath+`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 2/3 个有
- `easy int` —— 2/3 个有
- `CLIPLoaderGGUF` —— 1/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `WanVideoVACEStartToEndFrame` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 7 | 6 - 7 | 3 | 93% |
| 采样算法 | 1 | 1 - 3.5 | 3 | 36% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 7，3 个样本，取值集中（一致性 93%）
- 采样算法 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%

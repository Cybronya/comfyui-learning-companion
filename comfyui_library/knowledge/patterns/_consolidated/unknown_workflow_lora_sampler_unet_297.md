---
name: unknown_workflow_lora_sampler_unet_297
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.963333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy float]
problems: []
missing: []
members: [视频生成/图生视频/余温MINIMAX H3多参生视频工作流_2110183533531713537.json, 视频生成/图生视频/余温MINIMAX H3多参生视频工作流_2110342441948766210.json, 视频生成/文生视频/余温MINIMAX H3多参生视频工作流_2107841554848247809.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_297

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/余温MINIMAX H3多参生视频工作流_2110183533531713537.json、视频生成/图生视频/余温MINIMAX H3多参生视频工作流_2110342441948766210.json、视频生成/文生视频/余温MINIMAX H3多参生视频工作流_2107841554848247809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `RH_Astra` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论

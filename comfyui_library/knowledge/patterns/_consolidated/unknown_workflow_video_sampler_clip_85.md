---
name: unknown_workflow_video_sampler_clip_85
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.47125
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Float, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression_UTK, ModelSamplingSD3, Text, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy clearCacheAll, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/动漫图生视频：DasiwaV10+Qwen3.5_2021958481347088386.json, 视频生成/图生视频/动漫图生视频：DasiwaV10+Qwen3.5_2046470504948703234.json, 视频生成/图生视频/动漫图生视频：DasiwaV10+Qwen3.5_2054012165388021762.json, 视频生成/图生视频/动漫视频 图生视频：DasiwaV10&Qwen3.5_2046953828343353345.json, 视频生成/图生视频/动漫首尾帧生视频：DasiwaV10+Qwen3.5_2022333235971235842.json, 视频生成/图生视频/最强动漫首尾帧生视频_2034099796876726273.json, 视频生成/图生视频/超强质感，动漫视频生成（自动提示词）DasiwaV10_2043578904195108866.json, 视频生成/图生视频/首尾帧生视频DasiwaV10+Qwen3.5（动漫优化）_2046075077883600898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/动漫图生视频：DasiwaV10+Qwen3.5_2021958481347088386.json、视频生成/图生视频/动漫图生视频：DasiwaV10+Qwen3.5_2046470504948703234.json、视频生成/图生视频/动漫图生视频：DasiwaV10+Qwen3.5_2054012165388021762.json、视频生成/图生视频/动漫视频 图生视频：DasiwaV10&Qwen3.5_2046953828343353345.json、视频生成/图生视频/动漫首尾帧生视频：DasiwaV10+Qwen3.5_2022333235971235842.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Float`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression_UTK`
- `ModelSamplingSD3`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `llama_cpp_instruct_adv` —— 7/8 个有
- `llama_cpp_model_loader` —— 7/8 个有
- `llama_cpp_parameters` —— 7/8 个有
- `PainterI2V` —— 5/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `WanFirstLastFrameToVideo` —— 3/8 个有
- `Qwen3_VQA_Plus` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%

---
name: unknown_workflow_video_lora_sampler_160
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.800182
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, GetNode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2019039231745728514.json, 视频生成/图生视频/1991284667739648001.json, 视频生成/图生视频/2004740865878884354.json, 视频生成/图生视频/1989222645507952641.json, 视频生成/图生视频/2049774509045104642.json, 视频生成/图生视频/2051900032323989506.json, 视频生成/图生视频/2059887838782648321.json, 视频生成/图生视频/2059921253905027073.json, 视频生成/图生视频/2062774735607525377.json, 视频生成/图生视频/2066800648426975233.json, 视频生成/图生视频/1988864272392400898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_160

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2019039231745728514.json、视频生成/图生视频/1991284667739648001.json、视频生成/图生视频/2004740865878884354.json、视频生成/图生视频/1989222645507952641.json、视频生成/图生视频/2049774509045104642.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `GetNode`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Muter (rgthree)` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `Mute / Bypass Repeater (rgthree)` —— 10/11 个有
- `RIFE VFI` —— 10/11 个有
- `easy getNode` —— 10/11 个有
- `easy setNode` —— 10/11 个有
- `Float` —— 7/11 个有
- `easy seed` —— 7/11 个有
- `CompressImages` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `RHBatchImages:` —— 1/11 个有
- `RHExtractImage` —— 1/11 个有
- `RHUploadZip` —— 1/11 个有
- `VHS_SelectFilename` —— 1/11 个有
- `easy forLoopEnd` —— 1/11 个有
- `easy forLoopStart` —— 1/11 个有
- `easy imageCount` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 11 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 11 | 100% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | 1 | 1 - 1 | 11 | 100% |
| 重绘幅度 | euler_ancestral | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，11 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，11 个样本，一致性 100%

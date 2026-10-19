---
name: unknown_workflow_video_lora_sampler_371
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.941
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2056552561905332226.json, 视频生成/图生视频/1996104036933910529.json, 视频生成/图生视频/1996401587960561665.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json, 视频生成/图生视频/1950344638181892097.json, 视频生成/图生视频/1982023168992919554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_371

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2056552561905332226.json、视频生成/图生视频/1996104036933910529.json、视频生成/图生视频/1996401587960561665.json、视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json、视频生成/图生视频/1950344638181892097.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 4/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `ComfyMathExpression` —— 1/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `Int` —— 1/6 个有
- `LoadImagesFromURL` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 6 | 88% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | lcm | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，6 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%

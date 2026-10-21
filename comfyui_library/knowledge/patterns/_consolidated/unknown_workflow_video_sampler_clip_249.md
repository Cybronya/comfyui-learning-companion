---
name: unknown_workflow_video_sampler_clip_249
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8485
common_nodes: [Any To Any, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, Qwen3_VQA, Seed (rgthree), Text Concatenate, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1999314736896503810.json, 视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_249

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1999314736896503810.json、视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Any To Any`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `Qwen3_VQA`
- `Seed (rgthree)`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy int` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

---
name: unknown_workflow_video_sampler_clip_26
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.889929
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1978096633571368961.json, 视频生成/图生视频/1978140653064445953.json, 视频生成/图生视频/1978111164158763009.json, 视频生成/图生视频/1976190699999756289.json, 视频生成/图生视频/1978095349178982402.json, 视频生成/图生视频/1972554470959869953.json, 视频生成/图生视频/1972558560423047170.json, 视频生成/图生视频/1986706185669832705.json, 视频生成/图生视频/2029757199156776962.json, 视频生成/图生视频/1978387992047931393.json, 视频生成/图生视频/1978282591151349762.json, 视频生成/图生视频/2033413176150204417.json, 视频生成/图生视频/1958522667143950337.json, 视频生成/图生视频/1958523149342162945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1978096633571368961.json、视频生成/图生视频/1978140653064445953.json、视频生成/图生视频/1978111164158763009.json、视频生成/图生视频/1976190699999756289.json、视频生成/图生视频/1978095349178982402.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 12/14 个有
- `CLIPVisionLoader` —— 12/14 个有
- `JWInteger` —— 12/14 个有
- `LoraLoaderModelOnly` —— 12/14 个有
- `WanImageToVideo` —— 12/14 个有
- `CR Prompt Text` —— 10/14 个有
- `ImageFromBatch+` —— 9/14 个有
- `TorchCompileModel` —— 9/14 个有
- `ModelPatchTorchSettings` —— 5/14 个有
- `RIFE VFI` —— 3/14 个有
- `UnetLoaderGGUF` —— 3/14 个有
- `easy cleanGpuUsed` —— 3/14 个有
- `Int` —— 2/14 个有
- `JWFloat` —— 2/14 个有
- `PrimitiveInt` —— 2/14 个有
- `WanFirstLastFrameToVideo` —— 2/14 个有
- `FSampler` —— 1/14 个有
- `FSamplerAdvanced` —— 1/14 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/14 个有
- `Seed (rgthree)` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 57% |
| Prompt 约束强度(CFG) | 6 | 4 - 14 | 14 | 55% |
| 采样算法 | 1 | 0 - 3.5 | 14 | 25% |
| 调度器 | euler | - | 14 | 93% |
| 重绘幅度 | simple | - | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 14，14 个样本
- 采样算法 中位数 1，观测区间 0 - 3.5，14 个样本，取值分散，一致性仅 25%
- 调度器 最常用 euler，14 个样本，一致性 93%
- 重绘幅度 最常用 simple，14 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

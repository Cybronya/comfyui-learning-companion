---
name: unknown_workflow_video_clip_unet_14
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.975857
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Bypasser (rgthree), ImageResizeKJv2, ImpactInt, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1987894798759735297.json, 视频生成/图生视频/1981343312810598402.json, 视频生成/图生视频/1981307265980555265.json, 视频生成/图生视频/2004053514764599297.json, 视频生成/图生视频/1988425926365110274.json, 视频生成/图生视频/2009284920207745026.json, 视频生成/图生视频/2017792462663716865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1987894798759735297.json、视频生成/图生视频/1981343312810598402.json、视频生成/图生视频/1981307265980555265.json、视频生成/图生视频/2004053514764599297.json、视频生成/图生视频/1988425926365110274.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Fast Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImpactInt`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 6/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `ImageFromBatch` —— 4/7 个有
- `MathExpression|pysssss` —— 4/7 个有
- `String Literal` —— 4/7 个有
- `Text Load Line From File` —— 4/7 个有
- `WanImageToVideo` —— 4/7 个有
- `WanMoeKSampler` —— 4/7 个有
- `KSamplerAdvanced` —— 3/7 个有
- `WanFirstLastFrameToVideo` —— 3/7 个有
- `ImageScaleBy` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `easy anythingIndexSwitch` —— 2/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `easy imageIndexSwitch` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 86% |
| Prompt 约束强度(CFG) | 6 | 6 - 16 | 7 | 49% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | 1 | 1 - 1 | 4 | 100% |
| 重绘幅度 | euler_ancestral | - | 7 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 16，7 个样本，取值分散，一致性仅 49%
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，7 个样本，一致性 57%
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

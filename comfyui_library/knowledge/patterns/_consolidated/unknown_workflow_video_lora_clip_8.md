---
name: unknown_workflow_video_lora_clip_8
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.88625
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, ImpactInt, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, Qwen3_VQA, RIFE VFI, Seed (rgthree), SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy clearCacheAll, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2_图生视频_1993607152562536450.json, 视频生成/图生视频/wan2.2_首中尾帧_1993672653156401154.json, 视频生成/图生视频/wan2.2_首尾帧_1993648600257413122.json, 视频生成/文生视频/wan2.2_文生视频_1993592376180539394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.2_图生视频_1993607152562536450.json、视频生成/图生视频/wan2.2_首中尾帧_1993672653156401154.json、视频生成/图生视频/wan2.2_首尾帧_1993648600257413122.json、视频生成/文生视频/wan2.2_文生视频_1993592376180539394.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `ImpactInt`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `RIFE VFI`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy clearCacheAll`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ImageLoader` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `MultiplePathsInput` —— 3/4 个有
- `SeedVR2LoadDiTModel` —— 3/4 个有
- `SeedVR2LoadVAEModel` —— 3/4 个有
- `SeedVR2VideoUpscaler` —— 3/4 个有
- `WanMoeKSampler` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `CR Text Replace` —— 1/4 个有
- `EmptyHunyuanLatentVideo` —— 1/4 个有
- `ImageBatchMulti` —— 1/4 个有
- `KSamplerAdvanced` —— 1/4 个有
- `ShowAnything|Mie` —— 1/4 个有
- `WanFirstLastFrameToVideo` —— 1/4 个有
- `WanImageToVideo` —— 1/4 个有
- `WanMultiFrameRefToVideo` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy imageSize` —— 1/4 个有
- `easy mathInt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | euler | - | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，4 个样本，一致性 75%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

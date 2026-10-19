---
name: unknown_workflow_video_lora_sampler_630
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.951667
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, INTConstant, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PatchModelPatcherOrder, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1928043329005436930.json, 视频生成/图生视频/1928040420029120514.json, 视频生成/图生视频/1926519641286320129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_630

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1928043329005436930.json、视频生成/图生视频/1928040420029120514.json、视频生成/图生视频/1926519641286320129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `TorchCompileModelWanVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `String Literal` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `JWImageExtractFromBatch` —— 1/3 个有
- `KepStringLiteral` —— 1/3 个有
- `LoadImagesFromDir //Inspire` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `Text Load Line From File` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 3 - 10 | 3 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 3 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足

---
name: unknown_workflow_video_lora_sampler_183
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9133
common_nodes: [Any To Any, CLIPLoader, CLIPTextEncode, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, MultiplePathsInput, PathchSageAttentionKJ, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1985339190529376257.json, 视频生成/图生视频/1995446964584165378.json, 视频生成/图生视频/1983126528336797697.json, 视频生成/图生视频/1985878683623796737.json, 视频生成/图生视频/1990766383455744002.json, 视频生成/图生视频/2026240892415250433.json, 视频生成/图生视频/1987740278771658754.json, 视频生成/图生视频/1987576515279958018.json, 视频生成/图生视频/1987598878985883650.json, 视频生成/图生视频/1987598888204963842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_183

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1985339190529376257.json、视频生成/图生视频/1995446964584165378.json、视频生成/图生视频/1983126528336797697.json、视频生成/图生视频/1985878683623796737.json、视频生成/图生视频/1990766383455744002.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `Any To Any`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `MultiplePathsInput`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 9/10 个有
- `ImageConcatMulti` —— 9/10 个有
- `ImageScaleBy` —— 9/10 个有
- `Float` —— 8/10 个有
- `GetImageRangeFromBatch` —— 6/10 个有
- `LayerUtility: PurgeVRAM` —— 6/10 个有
- `easy batchAnything` —— 6/10 个有
- `RunningHub Deepcleaner` —— 4/10 个有
- `ImageConcanate` —— 3/10 个有
- `ImageFromBatch+` —— 3/10 个有
- `MathExpression|pysssss` —— 3/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有
- `easy int` —— 1/10 个有
- `easy positive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 90% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 90%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%

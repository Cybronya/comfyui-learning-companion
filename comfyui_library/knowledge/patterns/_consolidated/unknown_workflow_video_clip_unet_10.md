---
name: unknown_workflow_video_clip_unet_10
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.659333
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageLoader, ImageResizeKJ, ImpactFloat, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MemoryCleaner, ModelBlockSwap, MultiplePathsInput, PathchSageAttentionKJ, PreviewImage, PrimitiveFloat, Qwen3_VQA, SetNode, StringFunction|pysssss, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanVideoNAG, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/视频-首尾帧中间帧视频扩写-wan2.2-smoothMix-官方_1985386184434196481.json, 视频生成/图生视频/视频-首尾帧视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008209726496051201.json, 视频生成/图生视频/视频-首尾帧视频扩写(动漫-真人)_2091124043847127042.json, 视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-Remix-官方_1986618366645465090.json, 视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-smoothMix-官方_1983005590224011265.json, 视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-官方_1973043040770199553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/视频-首尾帧中间帧视频扩写-wan2.2-smoothMix-官方_1985386184434196481.json、视频生成/图生视频/视频-首尾帧视频扩写(动漫)-wan2.2-DasiwaV10-官方_2008209726496051201.json、视频生成/图生视频/视频-首尾帧视频扩写(动漫-真人)_2091124043847127042.json、视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-Remix-官方_1986618366645465090.json、视频生成/图生视频/视频-首尾帧视频扩写-wan2.2-smoothMix-官方_1983005590224011265.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageLoader`
- `ImageResizeKJ`
- `ImpactFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `ModelBlockSwap`
- `MultiplePathsInput`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `SetNode`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`
- `easy anythingIndexSwitch`
- `easy imageSize`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WanFirstLastFrameToVideo` —— 5/6 个有
- `WanMoeKSampler` —— 5/6 个有
- `ImageConcanate` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `CLIPVisionEncode` —— 1/6 个有
- `CLIPVisionLoader` —— 1/6 个有
- `ColorMatch` —— 1/6 个有
- `Florence2ModelLoader` —— 1/6 个有
- `Florence2Run` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `ImageFromBatch+` —— 1/6 个有
- `JoinStrings` —— 1/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/6 个有
- `easy string` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 83% |
| Prompt 约束强度(CFG) | 20 | 8 - 20 | 6 | 75% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | 1 | 1 - 1 | 5 | 100% |
| 重绘幅度 | sa_solver | - | 6 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 20，观测区间 8 - 20，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 sa_solver，6 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））

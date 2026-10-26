---
name: unknown_workflow_video_lora_sampler_635
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.799
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, INTConstant, ImageLoader, ImageResizeKJv2, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ModelSamplingSD3, MultiplePathsInput, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, YC_textReplaceNode, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [图片生成/图生图/片场探班首尾帧驱动一镜到底运镜Smooth Mix Wan 2.2 I2V High_2004828661687742466.json, 视频生成/图生视频/明星合影相遇图生视频首尾帧V3_2003113307240374273.json, 视频生成/图生视频/电影片场转场合影图生视频（首尾帧）_2003436959081111553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_635

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/片场探班首尾帧驱动一镜到底运镜Smooth Mix Wan 2.2 I2V High_2004828661687742466.json、视频生成/图生视频/明星合影相遇图生视频首尾帧V3_2003113307240374273.json、视频生成/图生视频/电影片场转场合影图生视频（首尾帧）_2003436959081111553.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `INTConstant`
- `ImageLoader`
- `ImageResizeKJv2`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `MultiplePathsInput`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `YC_textReplaceNode`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Any To Any` —— 2/3 个有
- `HunyuanVideoFoley` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SaveLatent` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `VHS_SelectFilename` —— 2/3 个有
- `CR Integer To String` —— 1/3 个有
- `Float` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | normal | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 normal，3 个样本，一致性 100%

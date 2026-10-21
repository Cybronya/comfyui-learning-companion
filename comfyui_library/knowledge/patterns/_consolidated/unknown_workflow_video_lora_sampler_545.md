---
name: unknown_workflow_video_lora_sampler_545
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.849
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageLoader, ImageResizeKJv2, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ModelSamplingSD3, MultiplePathsInput, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2003113307240374273.json, 视频生成/图生视频/2009656283015684097.json, 视频生成/图生视频/2003436959081111553.json, 视频生成/图生视频/2003358593732771842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_545

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2003113307240374273.json、视频生成/图生视频/2009656283015684097.json、视频生成/图生视频/2003436959081111553.json、视频生成/图生视频/2003358593732771842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Any To Any` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `CR Text Replace` —— 2/4 个有
- `HunyuanVideoFoley` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `Pick From Batch (mtb)` —— 2/4 个有
- `RH_Nano_Banana2_Image2Image` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `SaveLatent` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `VHS_SelectFilename` —— 2/4 个有
- `YC_textReplaceNode` —— 2/4 个有
- `LoadVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | normal | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 normal，4 个样本，一致性 100%

---
name: unknown_workflow_video_lora_sampler_515
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.784
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, INTConstant, ImageScaleBy, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2046147525731688449.json, 视频生成/图生视频/2047589071815446530.json, 视频生成/图生视频/2064427317950246914.json, 视频生成/图生视频/2065831471654457346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_515

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2046147525731688449.json、视频生成/图生视频/2047589071815446530.json、视频生成/图生视频/2064427317950246914.json、视频生成/图生视频/2065831471654457346.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 3/4 个有
- `llama_cpp_model_loader` —— 3/4 个有
- `llama_cpp_parameters` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `GetImageRangeFromBatch` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `ImageBatchMulti` —— 2/4 个有
- `ModelPatchTorchSettings` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `Wan22PromptSelector` —— 2/4 个有
- `easy clearCacheAll` —— 2/4 个有
- `easy saveText` —— 2/4 个有
- `DuckHideNode` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | beta | - | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 beta，4 个样本，一致性 75%

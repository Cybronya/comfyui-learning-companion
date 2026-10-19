---
name: unknown_workflow_video_sampler_clip_33
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.870462
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2080624345147334658.json, 视频生成/图生视频/2082282165500469249.json, 视频生成/图生视频/Wan2.2双模型首尾帧视频_2083014224594427906.json, 视频生成/图生视频/Wan2.2双模型首尾帧视频_2083105850020950017.json, 视频生成/图生视频/2009700904043286530.json, 视频生成/图生视频/2013871524415016962.json, 视频生成/图生视频/1987524619294978050.json, 视频生成/图生视频/1978796084820611074.json, 视频生成/图生视频/2008498194912649217.json, 视频生成/图生视频/2065475173511417857.json, 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834.json, 视频生成/文生视频/Wan2.2双模型首尾帧视频_2061638984954105858.json, 视频生成/文生视频/Wan2.2双模型首尾帧视频_2064706031250395137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2080624345147334658.json、视频生成/图生视频/2082282165500469249.json、视频生成/图生视频/Wan2.2双模型首尾帧视频_2083014224594427906.json、视频生成/图生视频/Wan2.2双模型首尾帧视频_2083105850020950017.json、视频生成/图生视频/2009700904043286530.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 12/13 个有
- `ImageResizeKJ` —— 12/13 个有
- `easy textSwitch` —— 10/13 个有
- `GetNode` —— 7/13 个有
- `Images to RGB` —— 7/13 个有
- `Qwen3_VQA` —— 7/13 个有
- `RH_LLMAPI_NODE` —— 7/13 个有
- `SetNode` —— 7/13 个有
- `Fast Groups Bypasser (rgthree)` —— 6/13 个有
- `RIFE VFI` —— 6/13 个有
- `SeedVR2BlockSwap` —— 6/13 个有
- `SeedVR2ExtraArgs` —— 6/13 个有
- `SeedVR2GGUF` —— 6/13 个有
- `intToFloat _O` —— 6/13 个有
- `ImpactSwitch` —— 3/13 个有
- `Int` —— 2/13 个有
- `ImageConcatMulti` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有
- `Maoyu_ListToString` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `YC_SingleTextNode` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 13 | 92% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 13 | 100% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | euler | - | 13 | 69% |
| 重绘幅度 | simple | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，13 个样本，一致性 92%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，13 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，13 个样本，一致性 69%
- 重绘幅度 最常用 simple，13 个样本，一致性 100%

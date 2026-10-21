---
name: unknown_workflow_video_lora_sampler_724
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6825
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DeepTranslatorTextNode, EmptyHunyuanLatentVideo, Fast Groups Bypasser (rgthree), GetNode, ImageBatch, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, PrimitiveInt, RIFE VFI, SaveImage, Seed Everywhere, SetNode, ShowText|pysssss, SimpleMath+, StringLength, TextInput_, TorchCompileModel, TorchCompileModelWanVideoV2, VAEDecode, VAEDecodeTiled, VHS_GetImageCount, VHS_LoadVideoPath, VHS_PruneOutputs, VHS_SelectFilename, VHS_SplitImages, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, workflow>Clip Text, workflow>加速节点]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss, RIFE VFI, SimpleMath+, workflow>加速节点, Seed Everywhere, workflow>Clip Text]
members: [视频生成/图生视频/1959961684356050946.json, 视频生成/文生视频/1959961684356050946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_724

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1959961684356050946.json、视频生成/文生视频/1959961684356050946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DeepTranslatorTextNode`
- `EmptyHunyuanLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageBatch`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveInt`
- `RIFE VFI`
- `SaveImage`
- `Seed Everywhere`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `StringLength`
- `TextInput_`
- `TorchCompileModel`
- `TorchCompileModelWanVideoV2`
- `VAEDecode`
- `VAEDecodeTiled`
- `VHS_GetImageCount`
- `VHS_LoadVideoPath`
- `VHS_PruneOutputs`
- `VHS_SelectFilename`
- `VHS_SplitImages`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `workflow>Clip Text`
- `workflow>加速节点`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，2 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、PlaySound|pysssss、RIFE VFI、SimpleMath+、workflow>加速节点
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参

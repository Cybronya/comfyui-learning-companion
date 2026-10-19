---
name: unknown_workflow_video_sampler_clip_17
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.8015
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, GetNode, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1987535452620173313.json, 视频生成/图生视频/1988081469920882689.json, 视频生成/图生视频/1988165926900121601.json, 视频生成/图生视频/1982410881613078529.json, 视频生成/图生视频/1980829288985444354.json, 视频生成/图生视频/1982062028078620674.json, 视频生成/图生视频/1980947136646959105.json, 视频生成/图生视频/1986648481861431297.json, 视频生成/图生视频/1979748549997006850.json, 视频生成/图生视频/1979541039348355074.json, 视频生成/图生视频/1979545928719831042.json, 视频生成/图生视频/2017190232734568450.json, 视频生成/图生视频/2010927245770100738.json, 视频生成/图生视频/1990436662905901058.json, 视频生成/图生视频/1987522876448419841.json, 视频生成/图生视频/2025865580863037441.json, 视频生成/图生视频/2050780959615791106.json, 视频生成/图生视频/2054015321224302593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1987535452620173313.json、视频生成/图生视频/1988081469920882689.json、视频生成/图生视频/1988165926900121601.json、视频生成/图生视频/1982410881613078529.json、视频生成/图生视频/1980829288985444354.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `RIFE VFI`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 17/18 个有
- `easy showAnything` —— 17/18 个有
- `LoraLoaderModelOnly` —— 13/18 个有
- `ImpactSwitch` —— 11/18 个有
- `WanImageToVideo` —— 10/18 个有
- `ImageConcanate` —— 9/18 个有
- `WanFirstLastFrameToVideo` —— 8/18 个有
- `ImageResizeKJ` —— 7/18 个有
- `LayerUtility: PurgeVRAM V2` —— 7/18 个有
- `AILab_QwenVL` —— 5/18 个有
- `CR Text Input Switch (4 way)` —— 5/18 个有
- `CombinationText` —— 5/18 个有
- `Text Concatenate` —— 5/18 个有
- `Wan22PromptSelector` —— 5/18 个有
- `easy cleanGpuUsed` —— 5/18 个有
- `ShowText|pysssss` —— 4/18 个有
- `Text Multiline` —— 2/18 个有
- `easy textSwitch` —— 2/18 个有
- `AddLabel` —— 1/18 个有
- `CompressImages` —— 1/18 个有
- `ImageConcatMulti` —— 1/18 个有
- `ImageStitch` —— 1/18 个有
- `PDIMAGE_LongerSize` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `RunningHub Deepcleaner` —— 1/18 个有
- `VHS_LoadVideo` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 18 | 56% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 18 | 93% |
| 采样算法 | 1 | 1 - 1 | 18 | 100% |
| 调度器 | euler_ancestral | - | 18 | 94% |
| 重绘幅度 | simple | - | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，18 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，18 个样本，取值集中（一致性 93%）
- 采样算法 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，18 个样本，一致性 94%
- 重绘幅度 最常用 simple，18 个样本，一致性 100%

---
name: unknown_workflow_video_sampler_clip_83
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.81975
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, Fast Groups Bypasser (rgthree), GetNode, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json, 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧视频_1988612935910121474.json, 视频生成/图生视频/嘟嘟-Wan_2.2_FMLF多帧首尾帧_1988086364040310785.json, 视频生成/图生视频/图生视频 Wan2.2 Remix 高画质高动态_1987454672774565889.json, 视频生成/图生视频/图生视频工作流_2050780959615791106.json, 视频生成/图生视频/图生视频工作流_2054015321224302593.json, 视频生成/图生视频/最强Wan2.2动漫模型DaSiWa-首尾帧视频_2008457370875207681.json, 视频生成/图生视频/最强Wan2.2模型DaSiWa-首尾帧视频_2009267956248748034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json、视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧视频_1988612935910121474.json、视频生成/图生视频/嘟嘟-Wan_2.2_FMLF多帧首尾帧_1988086364040310785.json、视频生成/图生视频/图生视频 Wan2.2 Remix 高画质高动态_1987454672774565889.json、视频生成/图生视频/图生视频工作流_2050780959615791106.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/8 个有
- `RH_LLMAPI_NODE` —— 6/8 个有
- `CLIPVisionEncode` —— 5/8 个有
- `CLIPVisionLoader` —— 5/8 个有
- `ImageConcanate` —— 5/8 个有
- `ImageResizeKJ` —— 5/8 个有
- `ImpactSwitch` —— 5/8 个有
- `ImageBatchMulti` —— 3/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/8 个有
- `WanImageToVideo` —— 3/8 个有
- `WanMultiFrameRefToVideo` —— 3/8 个有
- `AILab_QwenVL` —— 2/8 个有
- `CR Text Input Switch (4 way)` —— 2/8 个有
- `CombinationText` —— 2/8 个有
- `RHHiddenNodes` —— 2/8 个有
- `WanFirstLastFrameToVideo` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `easy textSwitch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 62% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler_ancestral | - | 8 | 75% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，8 个样本，一致性 75%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%

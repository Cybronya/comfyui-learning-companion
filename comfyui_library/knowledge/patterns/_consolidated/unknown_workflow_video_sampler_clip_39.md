---
name: unknown_workflow_video_sampler_clip_39
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.798
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, Fast Groups Bypasser (rgthree), JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1988124359338389506.json, 视频生成/图生视频/2013598944579821569.json, 视频生成/图生视频/2076910094813589506.json, 视频生成/图生视频/2067206177418727425.json, 视频生成/图生视频/1988612935910121474.json, 视频生成/图生视频/1979745226703147009.json, 视频生成/图生视频/2013169073936408577.json, 视频生成/图生视频/1988086364040310785.json, 视频生成/图生视频/2008457370875207681.json, 视频生成/图生视频/2009267956248748034.json, 视频生成/图生视频/1980857970835804161.json, 视频生成/图生视频/1980631743067803649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1988124359338389506.json、视频生成/图生视频/2013598944579821569.json、视频生成/图生视频/2076910094813589506.json、视频生成/图生视频/2067206177418727425.json、视频生成/图生视频/1988612935910121474.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
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

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `ImageConcanate` —— 11/12 个有
- `ImageResizeKJ` —— 11/12 个有
- `wanBlockSwap` —— 11/12 个有
- `CLIPVisionEncode` —— 9/12 个有
- `CLIPVisionLoader` —— 9/12 个有
- `RH_LLMAPI_NODE` —— 9/12 个有
- `WanFirstLastFrameToVideo` —— 9/12 个有
- `ImpactSwitch` —— 8/12 个有
- `ImageConcatMulti` —— 4/12 个有
- `LoraLoaderModelOnly` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `easy textSwitch` —— 4/12 个有
- `ImageBatchMulti` —— 3/12 个有
- `ImageScaleToTotalPixels` —— 3/12 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/12 个有
- `WanMultiFrameRefToVideo` —— 3/12 个有
- `PromptTemplateSelector` —— 2/12 个有
- `RHHiddenNodes` —— 2/12 个有
- `RH_Nano_Banana_Image2Image` —— 2/12 个有
- `SaveImage` —— 2/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `Int` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `Make Image Grid JK` —— 1/12 个有
- `Qwen3_VQA_Plus` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 92% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 12 | 100% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler_ancestral | - | 12 | 58% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 92%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，12 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，12 个样本，一致性 58%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%

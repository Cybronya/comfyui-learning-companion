---
name: unknown_workflow_video_sampler_clip_53
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.810455
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, Fast Groups Bypasser (rgthree), JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json, 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧视频_1988612935910121474.json, 视频生成/图生视频/嘟嘟-Wan_2.2_FMLF多帧首尾帧_1988086364040310785.json, 视频生成/图生视频/图生视频，Wan2.2高动态，超强语义遵循_1981008328186806273.json, 视频生成/图生视频/最强Wan2.2动漫模型DaSiWa-首尾帧视频_2008457370875207681.json, 视频生成/图生视频/最强Wan2.2模型DaSiWa-首尾帧视频_2009267956248748034.json, 视频生成/图生视频/首尾帧 图生视频 高动态 Wan2.2 Smooth Mix_1978796084820611074.json, 视频生成/图生视频/首尾帧视频-最强Wan2.2动漫模型DaSiWa_2008498194912649217.json, 视频生成/图生视频/首尾帧视频-最强Wan2.2动漫模型DaSiWa_2065475173511417857.json, 视频生成/图生视频/高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json, 视频生成/文生视频/Wan2.2 Smooth Mix首尾帧视频（高动态+自动提示词）_1986071453768568834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2067206177418727425.json、视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧视频_1988612935910121474.json、视频生成/图生视频/嘟嘟-Wan_2.2_FMLF多帧首尾帧_1988086364040310785.json、视频生成/图生视频/图生视频，Wan2.2高动态，超强语义遵循_1981008328186806273.json、视频生成/图生视频/最强Wan2.2动漫模型DaSiWa-首尾帧视频_2008457370875207681.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `ImageConcanate` —— 9/11 个有
- `ImageResizeKJ` —— 9/11 个有
- `RH_LLMAPI_NODE` —— 9/11 个有
- `CLIPVisionEncode` —— 8/11 个有
- `CLIPVisionLoader` —— 8/11 个有
- `ImpactSwitch` —— 8/11 个有
- `WanFirstLastFrameToVideo` —— 6/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `ImageBatchMulti` —— 3/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `ImageScaleToTotalPixels` —— 3/11 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/11 个有
- `WanMultiFrameRefToVideo` —— 3/11 个有
- `CR Text Input Switch` —— 2/11 个有
- `Int` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `WanImageToVideo` —— 2/11 个有
- `easy textSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 11 | 91% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 11 | 100% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler_ancestral | - | 11 | 64% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，11 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，11 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，11 个样本，一致性 64%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%

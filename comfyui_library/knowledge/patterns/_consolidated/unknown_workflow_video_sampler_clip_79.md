---
name: unknown_workflow_video_sampler_clip_79
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.650429
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, Fast Groups Bypasser (rgthree), GetNode, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, Qwen3_VQA, RIFE VFI, SetNode, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2055728891322486786.json, 视频生成/图生视频/2056085171165769729.json, 视频生成/图生视频/2010940564040060929.json, 视频生成/图生视频/2048449800865058818.json, 视频生成/图生视频/2008384521632227329.json, 视频生成/图生视频/2059769555181985793.json, 视频生成/图生视频/2064594591789174785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_79

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2055728891322486786.json、视频生成/图生视频/2056085171165769729.json、视频生成/图生视频/2010940564040060929.json、视频生成/图生视频/2048449800865058818.json、视频生成/图生视频/2008384521632227329.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
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
- `Qwen3_VQA`
- `RIFE VFI`
- `SetNode`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/7 个有
- `PainterI2V` —— 5/7 个有
- `Text Concatenate` —— 5/7 个有
- `CheckpointLoaderSimple` —— 4/7 个有
- `ImageScaleToTotalPixels` —— 4/7 个有
- `Int` —— 4/7 个有
- `MathExpression_UTK` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `SeedVR2` —— 4/7 个有
- `SeedVR2BlockSwap` —— 4/7 个有
- `SeedVR2ExtraArgs` —— 4/7 个有
- `Text` —— 4/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `VHS_VideoInfoSource` —— 4/7 个有
- `FlashVSRNode` —— 3/7 个有
- `ImpactSwitch` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `Wan22PromptSelector` —— 3/7 个有
- `Fast Bypasser (rgthree)` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `ImageResizeKJ` —— 2/7 个有
- `Images to RGB` —— 2/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/7 个有
- `WanFirstLastFrameToVideo` —— 2/7 个有
- `easy textSwitch` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `LoadVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 71% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | 1 | 1 - 1.6 | 7 | 81% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.6，7 个样本，取值集中（一致性 81%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%

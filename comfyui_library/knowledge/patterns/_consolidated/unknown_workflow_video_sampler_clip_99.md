---
name: unknown_workflow_video_sampler_clip_99
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.84
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, JWInteger, KSamplerAdvanced, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RH_LLMAPI_NODE, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/文生视频+高动态++Remix+Wan2.2 (2)_2054361569718489089.json, 视频生成/图生视频/文生视频+高动态++Smooth+Mix+Wan2.2 (1)_2052573232586346497.json, 视频生成/图生视频/文生视频+高动态+高遵循_2053725147890241538.json, 视频生成/图生视频/高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json, 视频生成/图生视频/（lora版）WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980995649351061505.json, 视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979519177214038018.json, 视频生成/文生视频/Wan2.2 文生视频 Smooth Mix 动态丝滑_1979834834325508097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/文生视频+高动态++Remix+Wan2.2 (2)_2054361569718489089.json、视频生成/图生视频/文生视频+高动态++Smooth+Mix+Wan2.2 (1)_2052573232586346497.json、视频生成/图生视频/文生视频+高动态+高遵循_2053725147890241538.json、视频生成/图生视频/高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json、视频生成/图生视频/（lora版）WAN2.2-LightX2V-I2V图生视频最强动态搭配_1980995649351061505.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `JWInteger`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `RIFE VFI`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `Text Concatenate` —— 6/7 个有
- `Wan22PromptSelector` —— 6/7 个有
- `CR Text Input Switch (4 way)` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `ImpactSwitch` —— 3/7 个有
- `CLIPVisionEncode` —— 2/7 个有
- `CLIPVisionLoader` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `LoadImage` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `CR Text Input Switch` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 71% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler_ancestral | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
